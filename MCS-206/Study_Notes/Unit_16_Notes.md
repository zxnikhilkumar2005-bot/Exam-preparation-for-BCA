# Unit 16: JDBC Part 2

## Unit Overview
This unit covers ResultSet interface (types, concurrency, holdability), JDBC Transactions (ACID, isolation levels, savepoints), concurrency issues (dirty read, non-repeatable read, phantom read), batch processing, RowSet interface, and metadata.

---

## 16.1 ResultSet Interface

### Definition
> **ResultSet** represents a table of data returned by a query. It maintains a cursor pointing to the current row.

### ResultSet Types (Scrollability)

| Type | Constant | Description |
|------|----------|-------------|
| **Forward Only** | `TYPE_FORWARD_ONLY` | Default; cursor moves only forward |
| **Scroll Insensitive** | `TYPE_SCROLL_INSENSITIVE` | Scrollable; not affected by DB changes |
| **Scroll Sensitive** | `TYPE_SCROLL_SENSITIVE` | Scrollable; reflects DB changes |

### ResultSet Concurrency

| Concurrency | Constant | Description |
|-------------|----------|-------------|
| **Read Only** | `CONCUR_READ_ONLY` | Default; cannot update |
| **Updatable** | `CONCUR_UPDATABLE` | Can update rows via ResultSet |

### ResultSet Holdability

| Holdability | Constant | Description |
|-------------|----------|-------------|
| **Close on Commit** | `HOLD_CURSORS_OVER_COMMIT` | Keep open after commit |
| **Close on Commit** | `CLOSE_CURSORS_AT_COMMIT` | Close after commit (default) |

### Creating Scrollable/Updatable ResultSet
```java
// Statement with scrollable, updatable ResultSet
Statement stmt = conn.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE,
    ResultSet.CONCUR_UPDATABLE
);

ResultSet rs = stmt.executeQuery("SELECT * FROM students");
```

### Navigation Methods (Scrollable)
```java
rs.next();           // Next row
rs.previous();       // Previous row
rs.first();          // First row
rs.last();           // Last row
rs.absolute(5);      // Row 5 (1-based)
rs.relative(2);      // 2 rows from current
rs.beforeFirst();    // Before first row
rs.afterLast();      // After last row

// Position checks
rs.isFirst();
rs.isLast();
rs.isBeforeFirst();
rs.isAfterLast();
rs.getRow();         // Current row number (1-based)
```

### Updating Rows (Updatable ResultSet)
```java
// Update current row
rs.updateString("name", "New Name");
rs.updateInt("age", 25);
rs.updateRow();  // Commit to database

// Insert new row
rs.moveToInsertRow();
rs.updateString("name", "New Student");
rs.updateInt("age", 20);
rs.insertRow();  // Insert into database
rs.moveToCurrentRow();  // Back to current row

// Delete current row
rs.deleteRow();
```

### Getter Methods
```java
// By column name (recommended)
rs.getInt("id");
rs.getString("name");
rs.getDouble("gpa");
rs.getDate("dob");
rs.getBoolean("active");
rs.getTimestamp("created_at");

// By column index (1-based)
rs.getInt(1);
rs.getString(2);

// Handling NULL
int id = rs.getInt("id");
if (rs.wasNull()) { /* was NULL */ }

// Better: use getObject
Object obj = rs.getObject("age");
if (obj == null) { /* was NULL */ }
```

---

## 16.2 JDBC Transactions

### ACID Properties
| Property | Description |
|----------|-------------|
| **Atomicity** | All or nothing - transaction completes fully or rolls back completely |
| **Consistency** | Database moves from one valid state to another |
| **Isolation** | Concurrent transactions don't interfere |
| **Durability** | Committed changes survive failures |

### Transaction Management
```java
Connection conn = DriverManager.getConnection(url, user, pass);

// Disable auto-commit
conn.setAutoCommit(false);

try {
    // Multiple operations
    PreparedStatement pstmt1 = conn.prepareStatement(
        "UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    pstmt1.executeUpdate();
    
    PreparedStatement pstmt2 = conn.prepareStatement(
        "UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    pstmt2.executeUpdate();
    
    // Commit if all successful
    conn.commit();
    
} catch (SQLException e) {
    // Rollback on any error
    conn.rollback();
    e.printStackTrace();
} finally {
    conn.setAutoCommit(true);  // Restore default
}
```

### Savepoints (Partial Rollback)
```java
conn.setAutoCommit(false);

Savepoint sp1 = conn.setSavepoint("BeforeTransfer");

try {
    // Operation 1
    stmt.executeUpdate("UPDATE accounts SET balance = balance - 100 WHERE id = 1");
    
    Savepoint sp2 = conn.setSavepoint("AfterFirstTransfer");
    
    // Operation 2
    stmt.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE id = 2");
    
    // Operation 3 fails
    stmt.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE id = 999");
    
    conn.commit();
    
} catch (SQLException e) {
    // Rollback to specific savepoint
    conn.rollback(sp2);  // Undo only operation 3
    // Or rollback(sp1) to undo everything
    conn.commit();  // Commit operations 1-2
}
```

### Transaction Isolation Levels

| Level | Constant | Dirty Read | Non-Repeatable Read | Phantom Read |
|-------|----------|------------|---------------------|--------------|
| **Read Uncommitted** | `TRANSACTION_READ_UNCOMMITTED` | Possible | Possible | Possible |
| **Read Committed** | `TRANSACTION_READ_COMMITTED` | Prevented | Possible | Possible |
| **Repeatable Read** | `TRANSACTION_REPEATABLE_READ` | Prevented | Prevented | Possible |
| **Serializable** | `TRANSACTION_SERIALIZABLE` | Prevented | Prevented | Prevented |

### Setting Isolation Level
```java
// Get current level
int level = conn.getTransactionIsolation();

// Set level (before transaction starts)
conn.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);

// Constants in Connection interface
Connection.TRANSACTION_READ_UNCOMMITTED
Connection.TRANSACTION_READ_COMMITTED
Connection.TRANSACTION_REPEATABLE_READ
Connection.TRANSACTION_SERIALIZABLE
Connection.TRANSACTION_NONE  // No transactions
```

---

## 16.3 Concurrency Problems

### 1. Dirty Read
> Reading **uncommitted** data from another transaction.

```
T1: UPDATE accounts SET balance = 500 WHERE id = 1  (not committed)
T2: SELECT balance FROM accounts WHERE id = 1  → Reads 500 (DIRTY!)
T1: ROLLBACK  (balance back to 100)
T2: Now has incorrect data!
```

### 2. Non-Repeatable Read
> Reading same row twice, getting **different** values (due to UPDATE/DELETE by another transaction).

```
T1: SELECT balance FROM accounts WHERE id = 1  → 100
T2: UPDATE accounts SET balance = 200 WHERE id = 1; COMMIT
T1: SELECT balance FROM accounts WHERE id = 1  → 200 (CHANGED!)
```

### 3. Phantom Read
> Re-executing query returns **different set of rows** (due to INSERT/DELETE by another transaction).

```
T1: SELECT * FROM accounts WHERE balance > 100  → 5 rows
T2: INSERT INTO accounts (balance) VALUES (200); COMMIT
T1: SELECT * FROM accounts WHERE balance > 100  → 6 rows (PHANTOM!)
```

### Isolation Level Protection

| Problem | Read Uncommitted | Read Committed | Repeatable Read | Serializable |
|---------|------------------|----------------|-----------------|--------------|
| Dirty Read | ✅ Occurs | ❌ Prevented | ❌ Prevented | ❌ Prevented |
| Non-Repeatable Read | ✅ Occurs | ✅ Occurs | ❌ Prevented | ❌ Prevented |
| Phantom Read | ✅ Occurs | ✅ Occurs | ✅ Occurs | ❌ Prevented |

---

## 16.4 JDBC Batch Processing

### Purpose
Execute multiple SQL statements as a batch for better performance.

### Using Statement
```java
Statement stmt = conn.createStatement();

stmt.addBatch("INSERT INTO students(name) VALUES('Alice')");
stmt.addBatch("INSERT INTO students(name) VALUES('Bob')");
stmt.addBatch("INSERT INTO students(name) VALUES('Charlie')");

int[] results = stmt.executeBatch();  // Returns update counts
// results = [1, 1, 1]
```

### Using PreparedStatement (Preferred)
```java
String sql = "INSERT INTO students(name, age, email) VALUES(?, ?, ?)";
PreparedStatement pstmt = conn.prepareStatement(sql);

for (int i = 1; i <= 100; i++) {
    pstmt.setString(1, "Student" + i);
    pstmt.setInt(2, 18 + i);
    pstmt.setString(3, "student" + i + "@example.com");
    pstmt.addBatch();
}

int[] results = pstmt.executeBatch();
// results = [1, 1, 1, ...] (100 elements)

conn.commit();  // If auto-commit false
```

### Batch Error Handling
```java
try {
    int[] results = pstmt.executeBatch();
} catch (BatchUpdateException e) {
    int[] updateCounts = e.getUpdateCounts();
    // Process partial results
    for (int i = 0; i < updateCounts.length; i++) {
        if (updateCounts[i] == Statement.EXECUTE_FAILED) {
            System.out.println("Batch " + i + " failed");
        }
    }
}
```

---

## 16.5 RowSet Interface

### Definition
> **RowSet** extends ResultSet, adds JavaBeans properties, scrollable/updatable by default, can be disconnected (serializable).

### RowSet Types

| Type | Description | Connected? |
|------|-------------|------------|
| **JdbcRowSet** | Wrapper around ResultSet; connected | Yes |
| **CachedRowSet** | Disconnected; caches data in memory | No |
| **WebRowSet** | CachedRowSet + XML read/write | No |
| **JoinRowSet** | Join multiple RowSets | No |
| **FilteredRowSet** | Filtered view of RowSet | No |

### JdbcRowSet (Connected)
```java
import javax.sql.rowset.JdbcRowSet;
import com.sun.rowset.JdbcRowSetImpl;

JdbcRowSet jrs = new JdbcRowSetImpl();
jrs.setUrl("jdbc:mysql://localhost:3306/school");
jrs.setUsername("root");
jrs.setPassword("password");
jrs.setCommand("SELECT * FROM students");
jrs.execute();  // Connects and executes

while (jrs.next()) {
    System.out.println(jrs.getString("name"));
}
jrs.close();
```

### CachedRowSet (Disconnected)
```java
import javax.sql.rowset.CachedRowSet;
import com.sun.rowset.CachedRowSetImpl;

CachedRowSet crs = new CachedRowSetImpl();
crs.setUrl("jdbc:mysql://localhost:3306/school");
crs.setUsername("root");
crs.setPassword("password");
crs.setCommand("SELECT * FROM students");
crs.execute();  // Connects, fetches, disconnects

// Work offline
while (crs.next()) {
    System.out.println(crs.getString("name"));
}

// Modify offline
crs.updateString("name", "Updated");
crs.updateRow();

// Reconnect to sync
crs.acceptChanges();  // Reconnects and applies changes
```

---

## 16.6 Metadata

### DatabaseMetaData (Database Info)
```java
DatabaseMetaData meta = conn.getMetaData();

System.out.println("DB Product: " + meta.getDatabaseProductName());
System.out.println("DB Version: " + meta.getDatabaseProductVersion());
System.out.println("Driver: " + meta.getDriverName());
System.out.println("Driver Version: " + meta.getDriverVersion());
System.out.println("URL: " + meta.getURL());
System.out.println("User: " + meta.getUserName());

// Table info
ResultSet tables = meta.getTables(null, null, "%", new String[]{"TABLE"});
while (tables.next()) {
    System.out.println("Table: " + tables.getString("TABLE_NAME"));
}

// Column info
ResultSet cols = meta.getColumns(null, null, "students", "%");
while (cols.next()) {
    System.out.println(cols.getString("COLUMN_NAME") + " " + 
                       cols.getString("TYPE_NAME"));
}
```

### ResultSetMetaData (ResultSet Info)
```java
ResultSet rs = stmt.executeQuery("SELECT * FROM students");
ResultSetMetaData rsMeta = rs.getMetaData();

int columnCount = rsMeta.getColumnCount();
for (int i = 1; i <= columnCount; i++) {
    System.out.println("Column " + i + ":");
    System.out.println("  Name: " + rsMeta.getColumnName(i));
    System.out.println("  Type: " + rsMeta.getColumnTypeName(i));
    System.out.println("  Precision: " + rsMeta.getPrecision(i));
    System.out.println("  Nullable: " + rsMeta.isNullable(i));
}
```

### ParameterMetaData (PreparedStatement Parameters)
```java
PreparedStatement pstmt = conn.prepareStatement(
    "INSERT INTO students(name, age) VALUES(?, ?)");
ParameterMetaData pMeta = pstmt.getParameterMetaData();

int paramCount = pMeta.getParameterCount();
for (int i = 1; i <= paramCount; i++) {
    System.out.println("Param " + i + ": " + pMeta.getParameterTypeName(i));
}
```

---

## 16.7 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. ResultSet types: TYPE_FORWARD_ONLY, TYPE_SCROLL_INSENSITIVE, TYPE_SCROLL_SENSITIVE.
2. ResultSet concurrency: CONCUR_READ_ONLY, CONCUR_UPDATABLE.
3. What is holdability?
4. Difference between ResultSet and RowSet.
5. What is batch processing? addBatch(), executeBatch().
6. Transaction ACID properties.
7. Four isolation levels.
8. Dirty read, Non-repeatable read, Phantom read.
9. What is a savepoint?
10. JdbcRowSet vs CachedRowSet.

**5-Mark Questions:**
1. Explain ResultSet types, concurrency, and holdability.
2. Explain updatable ResultSet with example.
3. Explain batch processing with PreparedStatement.
4. Explain JDBC transactions with commit/rollback.
5. Explain isolation levels with dirty/non-repeatable/phantom reads.
6. Explain RowSet types (JdbcRowSet, CachedRowSet).
7. Explain DatabaseMetaData and ResultSetMetaData.

**10-Mark Questions:**
1. **ResultSet (scrollable/updatable), Transactions (ACID, isolation, savepoints), Batch Processing, RowSet, Metadata.** (Appeared 2022, 2023, 2024, 2025)
2. Complete program: Transaction with savepoint, batch insert, ResultSet navigation.

### Programs to Practice
1. ✅ **Scrollable ResultSet navigation** - appeared 2022, 2023, 2024
2. ✅ **Updatable ResultSet (update/insert/delete row)** - appeared 2022, 2023, 2024
3. ✅ **Batch processing with PreparedStatement** - appeared 2021, 2023, 2025
4. ✅ **Transaction with savepoint** - appeared 2023, 2024, 2025
5. ✅ **Isolation level demonstration** - appeared 2023
6. ✅ **CachedRowSet offline editing** - appeared 2023, 2026

---

## 16.8 Summary of Unit 16

| Topic | Key Points |
|-------|------------|
| **ResultSet Types** | FORWARD_ONLY (default), SCROLL_INSENSITIVE, SCROLL_SENSITIVE |
| **Concurrency** | READ_ONLY (default), UPDATABLE |
| **Holdability** | HOLD_CURSORS_OVER_COMMIT, CLOSE_CURSORS_AT_COMMIT |
| **Navigation** | next, previous, first, last, absolute, relative |
| **Updatable** | updateXxx(), updateRow(), insertRow(), deleteRow() |
| **Transactions** | ACID; setAutoCommit(false); commit(); rollback() |
| **Savepoints** | setSavepoint(), rollback(sp), releaseSavepoint() |
| **Isolation Levels** | READ_UNCOMMITTED, READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE |
| **Concurrency Issues** | Dirty Read, Non-Repeatable Read, Phantom Read |
| **Batch Processing** | addBatch(), executeBatch(); better performance |
| **RowSet** | JdbcRowSet (connected), CachedRowSet (disconnected) |
| **Metadata** | DatabaseMetaData, ResultSetMetaData, ParameterMetaData |

---

## 16.9 Quick Reference: Transaction Template

```java
Connection conn = null;
try {
    conn = DriverManager.getConnection(url, user, pass);
    conn.setAutoCommit(false);
    
    Savepoint sp = conn.setSavepoint();
    
    // Operation 1
    // Operation 2
    
    conn.commit();
} catch (SQLException e) {
    if (conn != null) conn.rollback();
    e.printStackTrace();
} finally {
    if (conn != null) {
        try { conn.setAutoCommit(true); } catch (SQLException ignored) {}
        try { conn.close(); } catch (SQLException ignored) {}
    }
}
```