# Unit 16: JDBC Part 2

## Unit Overview
This unit covers ResultSet interface (types, concurrency, holdability, navigation methods), JDBC Transactions (ACID, isolation levels, savepoints), concurrency issues (dirty read, non-repeatable read, phantom read), batch processing, RowSet interface, metadata, CallableStatement for stored procedures, and important exam questions from PYQ analysis.

# Unit 16: JDBC Part 2

## Unit Overview
This unit covers ResultSet interface (types, concurrency, holdability, navigation methods), JDBC Transactions (ACID, isolation levels, savepoints), concurrency issues (dirty read, non-repeatable read, phantom read), batch processing, RowSet interface, metadata, CallableStatement for stored procedures, and important exam questions from PYQ analysis.

> **Prerequisite**: Review Unit 15 for JDBC Architecture, Driver Types, Connection Steps, Statement types, and DriverManager.

---

## 16.1 ResultSet Interface

### Definition
> **ResultSet** represents a table of data returned by a query. It maintains a cursor pointing to the current row. Think of it as an iterator over the result set that allows you to traverse and manipulate data retrieved from the database.

### ResultSet Types (Scrollability)

| Type | Constant | Description |
|------|----------|-------------|
| **Forward Only** | `TYPE_FORWARD_ONLY` | Default; cursor moves only forward, like an iterator |
| **Scroll Insensitive** | `TYPE_SCROLL_INSENSITIVE` | Scrollable; not affected by database changes during its existence |
| **Scroll Sensitive** | `TYPE_SCROLL_SENSITIVE` | Scrollable; reflects database changes made by others after ResultSet was created |

### ResultSet Concurrency

| Concurrency | Constant | Description |
|-------------|----------|-------------|
| **Read Only** | `CONCUR_READ_ONLY` | Default; cannot update |
| **Updatable** | `CONCUR_UPDATABLE` | Can update rows via ResultSet |

### ResultSet Holdability

| Holdability | Constant | Description |
|-------------|----------|-------------|
| **Keep Open** | `HOLD_CURSORS_OVER_COMMIT` | Cursors remain open after transaction commit |
| **Close on Commit** | `CLOSE_CURSORS_AT_COMMIT` | Cursors close automatically after transaction commit (default for most databases) |

> **Exam Tip**: Holdability determines cursor behavior during transaction commit. Use `conn.getHoldability()` to check current setting.

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

> **Important**: All navigation methods (except `next()`) throw `SQLException` if the ResultSet type is `TYPE_FORWARD_ONLY`.

```java
// Moving through the result set
rs.next();           // Next row (forward only, works for all types)
rs.previous();       // Previous row (TYPE_SCROLL_INSENSITIVE/SENSITIVE only)
rs.first();          // First row
rs.last();           // Last row
rs.absolute(5);      // Row 5 (1-based), negative means from end
rs.relative(2);      // 2 rows forward from current
rs.relative(-1);     // 1 row back from current
rs.beforeFirst();    // Position before first row
rs.afterLast();      // Position after last row

// Position checks
rs.isFirst();        // true if on first row
rs.isLast();         // true if on last row
rs.isBeforeFirst();  // true if before first row
rs.isAfterLast();    // true if after last row
rs.isClosed();       // true if ResultSet is closed
rs.getRow();         // Current row number (1-based), returns 0 if before first/after last

// Fetch size (performance optimization)
conn.setStatementTimeout(30);  // Set timeout
rs.setFetchSize(100);          // Fetch 100 rows at a time
```

### Updating Rows (Updatable ResultSet)

```java
// Update current row
rs.updateDouble("gpa", 3.8);
rs.updateString("name", "Updated Name");
rs.updateRow();           // Commit changes to database

// Update by index
rs.updateString(3, "New Email");  // Update column 3
rs.updateRow();

// Insert new row into ResultSet (then into database)
rs.moveToInsertRow();
rs.updateString("name", "New Student");
rs.updateInt("age", 20);
rs.insertRow();           // Adds row to database
rs.moveToCurrentRow();    // Return to original position

// Delete current row from database
rs.deleteRow();

// Refresh row from database
rs.refreshRow();
```

### Getter Methods

> **Common Mistakes**: `rs.getString("id")` returns String, not int. Always use appropriate getXXX method.

```java
// By column name (recommended - more readable)
rs.getInt("id");
rs.getString("name");
rs.getDouble("gpa");
rs.getDate("dob");
rs.getBoolean("active");
rs.getTimestamp("created_at");
rs.getLong("phone");
rs.getBytes("data");      // For BLOB data
rs.getClob("document");     // For CLOB data

// By column index (1-based - faster but less readable)
rs.getInt(1);
rs.getString(2);

// Handling NULL values
int id = rs.getInt("id");
if (rs.wasNull()) { /* column was NULL */ }

// Alternative NULL handling (pre-JDBC 2.0 compatible)
Object obj = rs.getObject("age");
if (obj == null) { /* was NULL */ }

// Date/Time handling with java.time (JDBC 4.2+)
LocalDate date = rs.getObject("dob", LocalDate.class);
LocalDateTime timestamp = rs.getObject("created_at", LocalDateTime.class);

// getTime() for millisecond precision
java.sql.Timestamp ts = rs.getTimestamp("created_at");
java.util.Date utilDate = new java.util.Date(ts.getTime());
```

### ResultSet Navigation Details

| Method | Description | ResultSet Type Required |
|--------|-------------|------------------------|
| `next()` | Move to next row | All types |
| `previous()` | Move to previous row | SCROLL_INSENSITIVE/SENSITIVE |
| `first()` | Move to first row | SCROLL_INSENSITIVE/SENSITIVE |
| `last()` | Move to last row | SCROLL_INSENSITIVE/SENSITIVE |
| `absolute(n)` | Move to row n | SCROLL_INSENSITIVE/SENSITIVE |
| `relative(n)` | Move n rows from current | SCROLL_INSENSITIVE/SENSITIVE |
| `beforeFirst()` | Position before first row | SCROLL_INSENSITIVE/SENSITIVE |
| `afterLast()` | Position after last row | SCROLL_INSENSITIVE/SENSITIVE |

---

## 16.2 JDBC Transactions

### ACID Properties

| Property | Description | Example |
|----------|-------------|---------|
| **Atomicity** | All or nothing - transaction completes fully or rolls back completely | Transfer between accounts: if debit succeeds but credit fails, both must roll back |
| **Consistency** | Database moves from one valid state to another | Money total must remain same before and after transfer |
| **Isolation** | Concurrent transactions don't interfere | User doesn't see partial updates from other transactions |
| **Durability** | Committed changes survive failures | After commit, data persists even if server crashes |

> **Exam Tip**: ACID is fundamental for banking, e-commerce, and any system requiring data integrity.

### Transaction Management

**Best Practice**: Use try-with-resources for automatic resource cleanup.

```java
Connection conn = null;
try {
    // 1. Get connection
    conn = DriverManager.getConnection(url, user, pass);
    
    // 2. Disable auto-commit to start transaction
    conn.setAutoCommit(false);
    
    // 3. Execute multiple operations
    PreparedStatement pstmt1 = conn.prepareStatement(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?");
    pstmt1.setDouble(1, 100.0);
    pstmt1.setInt(2, 1);
    pstmt1.executeUpdate();
    pstmt1.close();
    
    PreparedStatement pstmt2 = conn.prepareStatement(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?");
    pstmt2.setDouble(1, 100.0);
    pstmt2.setInt(2, 2);
    pstmt2.executeUpdate();
    pstmt2.close();
    
    // 4. Commit if all successful
    conn.commit();
    System.out.println("Transaction committed successfully");
    
} catch (SQLException e) {
    // Rollback on any error
    if (conn != null) {
        try {
            conn.rollback();  // Undo all changes
            System.out.println("Transaction rolled back");
        } catch (SQLException rollbackEx) {
            rollbackEx.printStackTrace();
        }
    }
    e.printStackTrace();
} finally {
    // 5. Restore auto-commit and close connection
    if (conn != null) {
        try {
            conn.setAutoCommit(true);  // Restore default
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

### Complete Transaction Example with Transfer

```java
public void transferMoney(Connection conn, int fromAccount, int toAccount, double amount) 
        throws SQLException {
    // Validate
    if (amount <= 0) throw new SQLException("Invalid amount");
    
    // Check balance
    PreparedStatement checkStmt = conn.prepareStatement(
        "SELECT balance FROM accounts WHERE id = ?");
    checkStmt.setInt(1, fromAccount);
    ResultSet rs = checkStmt.executeQuery();
    
    if (rs.next()) {
        double balance = rs.getDouble("balance");
        if (balance < amount) {
            rs.close();
            checkStmt.close();
            throw new SQLException("Insufficient balance");
        }
    }
    rs.close();
    checkStmt.close();
    
    // Perform transfer
    PreparedStatement debitStmt = conn.prepareStatement(
        "UPDATE accounts SET balance = balance - ? WHERE id = ?");
    debitStmt.setDouble(1, amount);
    debitStmt.setInt(2, fromAccount);
    debitStmt.executeUpdate();
    debitStmt.close();
    
    PreparedStatement creditStmt = conn.prepareStatement(
        "UPDATE accounts SET balance = balance + ? WHERE id = ?");
    creditStmt.setDouble(1, amount);
    creditStmt.setInt(2, toAccount);
    creditStmt.executeUpdate();
    creditStmt.close();
}

// Usage:
// conn.setAutoCommit(false);
// transferMoney(conn, 1, 2, 500.0);
// conn.commit();
```

### Savepoints (Partial Rollback)

**Use Case**: When a transaction has multiple stages and you want to retry or undo only part of it.

```java
conn.setAutoCommit(false);

try {
    // Operation 1: Deduct from account 1
    try (PreparedStatement stmt = conn.prepareStatement(
            "UPDATE accounts SET balance = balance - 100 WHERE id = 1")) {
        stmt.executeUpdate();
    }
    
    // Create savepoint after first operation
    Savepoint sp1 = conn.setSavepoint("AfterFirstTransfer");
    
    // Operation 2: Add to account 2
    try (PreparedStatement stmt = conn.prepareStatement(
            "UPDATE accounts SET balance = balance + 100 WHERE id = 2")) {
        stmt.executeUpdate();
    }
    
    // Operation 3: Add bonus to account 3
    Savepoint sp2 = conn.setSavepoint("AfterSecondTransfer");
    
    try (PreparedStatement stmt = conn.prepareStatement(
            "UPDATE accounts SET balance = balance + 50 WHERE id = 3")) {
        stmt.executeUpdate();
    }
    
    // Operation 4 may fail
    // stmt.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE id = 999");
    
    conn.commit();
    System.out.println("All operations committed");
    
} catch (SQLException e) {
    // Option 1: Rollback to last savepoint (retry operation 4)
    conn.rollback(sp2);  // Undo only operation 4
    System.out.println("Rolled back to: " + sp2.getSavepointName());
    
    // Option 2: Rollback to before any operations
    // conn.rollback(sp1);  // Undo operations 3 and 4
    // conn.commit();  // Commit operations 1 and 2
    
    // Option 3: Full rollback (default)
    // conn.rollback();  // Undo all operations
    
    e.printStackTrace();
} finally {
    conn.setAutoCommit(true);
}
```

### Savepoint Methods

```java
// Create named savepoint
Savepoint sp = conn.setSavepoint("BeforeTransfer");

// Create unnamed savepoint
Savepoint sp = conn.setSavepoint();

// Rollback to savepoint
conn.rollback(sp);

// Get savepoint name
String name = sp.getSavepointName();

// Get savepoint ID (for unnamed savepoints)
int id = sp.getSavepointId();

// Release savepoint (optional, allows partial rollback in some databases)
conn.releaseSavepoint(sp);
```

### Transaction Isolation Levels

| Level | Constant | Dirty Read | Non-Repeatable Read | Phantom Read | Performance |
|-------|----------|------------|---------------------|--------------|-------------|
| **Read Uncommitted** | `TRANSACTION_READ_UNCOMMITTED` | ✅ Possible | ✅ Possible | ✅ Possible | Highest |
| **Read Committed** | `TRANSACTION_READ_COMMITTED` | ❌ Prevented | ✅ Possible | ✅ Possible | High |
| **Repeatable Read** | `TRANSACTION_REPEATABLE_READ` | ❌ Prevented | ❌ Prevented | ✅ Possible | Medium |
| **Serializable** | `TRANSACTION_SERIALIZABLE` | ❌ Prevented | ❌ Prevented | ❌ Prevented | Lowest |

> **Real-world Examples**:
> - **Read Uncommitted**: Never used in practice (dirty reads are dangerous)
> - **Read Committed**: Default for PostgreSQL, Oracle - good for most applications
> - **Repeatable Read**: Default for MySQL - good for reports, inventory checks
> - **Serializable**: Highest safety - equivalent to running transactions sequentially

### Setting and Checking Isolation Level

```java
// Get current isolation level
int currentLevel = conn.getTransactionIsolation();
System.out.println("Current level: " + isolationLevelToString(currentLevel));

// Set isolation level (MUST be called before starting transaction!)
conn.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);

// Helper method to print level
public String isolationLevelToString(int level) {
    return switch (level) {
        case Connection.TRANSACTION_READ_UNCOMMITTED -> "Read Uncommitted";
        case Connection.TRANSACTION_READ_COMMITTED -> "Read Committed";
        case Connection.TRANSACTION_REPEATABLE_READ -> "Repeatable Read";
        case Connection.TRANSACTION_SERIALIZABLE -> "Serializable";
        case Connection.TRANSACTION_NONE -> "None";
        default -> "Unknown";
    };
}

// Isolation level constants
Connection.TRANSACTION_READ_UNCOMMITTED   // 0 - Lowest
Connection.TRANSACTION_READ_COMMITTED     // 2 - Default for most DBs
Connection.TRANSACTION_REPEATABLE_READ    // 4 - Good balance
Connection.TRANSACTION_SERIALIZABLE     // 8 - Highest isolation
Connection.TRANSACTION_NONE               // For read-only scenarios
```

### Database-Specific Isolation Levels

| Database | Default | Supported Levels |
|----------|---------|------------------|
| MySQL | Repeatable Read | READ_UNCOMMITTED, READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE |
| PostgreSQL | Read Committed | READ_UNCOMMITTED, READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE |
| Oracle | Read Committed | READ_COMMITTED, SERIALIZABLE |
| SQL Server | Read Committed | READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE |
| SQLite | Serializable | SERIALIZABLE |

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

> **Exam Tip**: Batch processing appeared 2021, 2023, 2025. Use PreparedStatement for batch operations.

### Purpose
Execute multiple SQL statements as a batch for better performance. Reduces network round-trips by sending multiple statements in one request.

### How Batch Processing Works

```java
// Traditional approach (single statement, multiple trips):
for (int i = 0; i < 1000; i++) {
    stmt.executeUpdate("INSERT INTO students VALUES(" + i + ", 'Student" + i + "')");
    // 1000 network round-trips!
}

// Batch approach (multiple statements, one trip):
for (int i = 0; i < 1000; i++) {
    stmt.addBatch("INSERT INTO students VALUES(" + i + ", 'Student" + i + "')");
}
int[] results = stmt.executeBatch();  // Single network trip
```

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

**Best Practice**: Always use try-with-resources and handle BatchUpdateException properly.

```java
try (PreparedStatement pstmt = conn.prepareStatement(
        "INSERT INTO students(id, name, age) VALUES(?, ?, ?)")) {
    
    for (int i = 1; i <= 100; i++) {
        pstmt.setInt(1, i);
        pstmt.setString(2, "Student" + i);
        pstmt.setInt(3, 18 + i);
        pstmt.addBatch();
    }
    
    int[] results = pstmt.executeBatch();
    
    // Verify all inserts succeeded
    for (int i = 0; i < results.length; i++) {
        if (results[i] == Statement.EXECUTE_FAILED) {
            System.out.println("Batch statement " + i + " failed");
        } else {
            System.out.println("Batch statement " + i + ": inserted " + results[i] + " row(s)");
        }
    }
    
} catch (BatchUpdateException e) {
    // Database-specific error handling
    System.err.println("Batch failed with error: " + e.getMessage());
    System.err.println("SQL State: " + e.getSQLState());
    System.err.println("Error Code: " + e.getErrorCode());
    
    // Get update counts for successful statements before failure
    int[] updateCounts = e.getUpdateCounts();
    System.out.println("Successful statements before failure: " + updateCounts.length);
}

// Connection-wide batch execution with success/failure tracking
try {
    conn.setAutoCommit(false);
    Statement stmt = conn.createStatement();
    
    stmt.addBatch("INSERT INTO products VALUES(1, 'Laptop', 50000)");
    stmt.addBatch("INSERT INTO products VALUES(2, 'Mouse', 500)");  
    stmt.addBatch("INVALID SQL STATEMENT");  // This will fail
    stmt.addBatch("INSERT INTO products VALUES(3, 'Keyboard', 800)");
    
    int[] counts = stmt.executeBatch();
    
    System.out.println("Batch results: " + java.util.Arrays.toString(counts));
    conn.commit();
    
} catch (BatchUpdateException e) {
    conn.rollback();
    System.out.println("Rolled back due to batch error");
}
```

### Batch Processing with Different Statement Types

| Statement Type | Use Case | Performance |
|----------------|----------|-------------|
| `Statement` | DDL, simple static SQL | Slower (no parameter caching) |
| `PreparedStatement` | Insert/update with parameters | Faster (compiled once) |
| `CallableStatement` | Stored procedure calls | Depends on procedure |

---

## 16.5 CallableStatement (Stored Procedures)

> **Important**: CallableStatement is CRITICAL for exams (appeared 2023, 2025).

### What is a Stored Procedure?
A pre-compiled program stored in the database that can be called from Java. Benefits include:
- Pre-compiled (better performance)
- Centralized business logic
- Security (SQL injection prevention)
- Reduced network traffic

### Creating a Stored Procedure (MySQL Example)
```sql
-- Procedure with IN, OUT, and INOUT parameters
DELIMITER //
CREATE PROCEDURE calculateBonus(
    IN emp_id INT,
    IN bonus_percent DECIMAL(5,2),
    OUT new_salary DECIMAL(10,2)
)
BEGIN
    DECLARE current_salary DECIMAL(10,2);
    
    SELECT salary INTO current_salary FROM employees WHERE id = emp_id;
    SET new_salary = current_salary * (1 + bonus_percent/100);
    
    UPDATE employees SET salary = new_salary WHERE id = emp_id;
END //
DELIMITER ;

-- Procedure with no parameters
DELIMITER //
CREATE PROCEDURE getAllEmployees()
BEGIN
    SELECT id, name, salary FROM employees;
END //
DELIMITER ;

-- Function
DELIMITER //
CREATE FUNCTION getEmployeeCount() RETURNS INT
READS SQL DATA
BEGIN
    DECLARE count INT;
    SELECT COUNT(*) INTO count FROM employees;
    RETURN count;
END //
DELIMITER ;
```

### Calling Stored Procedures from Java

```java
// 1. Procedure with IN, OUT parameters
String call = "{call calculateBonus(?, ?, ?)}";
try (CallableStatement cstmt = conn.prepareCall(call)) {
    
    // Set IN parameters
    cstmt.setInt(1, 101);           // emp_id
    cstmt.setDouble(2, 10.0);       // bonus_percent
    
    // Register OUT parameter
    cstmt.registerOutParameter(3, Types.DECIMAL);  // new_salary
    
    // Execute the procedure
    boolean hasResults = cstmt.execute();
    
    // Get OUT parameter value
    double newSalary = cstmt.getDouble(3);
    System.out.println("New salary: " + newSalary);
}

// 2. Procedure with no parameters
String call = "{call getAllEmployees()}";
try (CallableStatement cstmt = conn.prepareCall(call)) {
    boolean hasResults = cstmt.execute();
    
    if (hasResults) {
        try (ResultSet rs = cstmt.getResultSet()) {
            while (rs.next()) {
                System.out.println("Employee: " + rs.getString("name"));
            }
        }
    }
}

// 3. Function call (returns value)
String call = "{? = call getEmployeeCount()}";
try (CallableStatement cstmt = conn.prepareCall(call)) {
    // Register return parameter
    cstmt.registerOutParameter(1, Types.INTEGER);
    cstmt.execute();
    
    int count = cstmt.getInt(1);
    System.out.println("Total employees: " + count);
}
```

### CallableStatement Methods

| Method | Description |
|--------|-------------|
| `registerOutParameter(int paramIndex, int sqlType)` | Register OUT parameter type |
| `registerOutParameter(int paramIndex, int sqlType, int scale)` | Register DECIMAL NUMERIC with scale |
| `wasNull()` | Check if last OUT parameter was NULL |
| `getString(), getInt(), getDouble(), ...` | Get OUT parameter values |

---

## 16.6 RowSet Interface (Extended ResultSet)

### Definition
> **RowSet** extends ResultSet interface and adds JavaBeans properties, making it serializable. It provides enhanced functionality like disconnected operation and event handling.

### RowSet Characteristics
- **JavaBeans Compliant**: Has properties, events, and serialization support
- **Scrollable & Updatable**: Default behavior
- **Connected vs Disconnected**: Can work with or without continuous database connection
- **Event-driven**: Supports PropertyChangeListener, RowSetListener

### RowSet Types

| Type | Description | Connected? | Use Case |
|------|-------------|------------|----------|
| **JdbcRowSet** | Wrapper around a ResultSet | Yes | Simple connected operations |
| **CachedRowSet** | Catches ResultSet data into memory | No | Offline work, disconnected scenario |
| **WebRowSet** | CachedRowSet with XML support | No | Data export/import via XML |
| **JoinRowSet** | Join multiple CachedRowSets | No | Relational joins without DB |
| **FilteredRowSet** | Filtered view of RowSet | No | Conditional data view |
| **FreeableRowSet** | Can free resources before close | No | Memory optimization |

### JdbcRowSet (Connected)

**Use Case**: Simple wrapper around ResultSet with JDBC-like interface.

```java
import javax.sql.rowset.JdbcRowSet;
import javax.sql.rowset.RowSetProvider;

// Modern way (JDBC 4.0+)
JdbcRowSet jrs = RowSetProvider.newFactory().createJdbcRowSet();
jrs.setUrl("jdbc:mysql://localhost:3306/school");
jrs.setUsername("root");
jrs.setPassword("password");
jrs.setCommand("SELECT * FROM students WHERE age > ?");
jrs.setInt(1, 18);

jrs.execute();  // Connects and executes

try {
    while (jrs.next()) {
        System.out.println(jrs.getString("name") + " - " + jrs.getInt("age"));
    }
} finally {
    if (jrs != null) jrs.close();
}

// Event handling with JdbcRowSet
jrs.addRowSetListener(new RowSetListener() {
    @Override public void rowChanged(RowSetEvent event) {}
    @Override public void cursorMoved(RowSetEvent event) {}
    @Override public void lifeCycleChanged(RowSetEvent event) {}
});
```

### CachedRowSet (Disconnected)

**Use Case**: Work with data offline, useful for distributed applications.

```java
import javax.sql.rowset.CachedRowSet;
import javax.sql.rowset.RowSetProvider;

CachedRowSet crs = RowSetProvider.newFactory().createCachedRowSet();
crs.setUrl("jdbc:mysql://localhost:3306/school");
crs.setUsername("root");
crs.setPassword("password");
crs.setCommand("SELECT * FROM students ORDER BY id");
crs.execute();  // Connects, fetches all, disconnects

// Work completely offline
System.out.println("Total rows: " + crs.size());

while (crs.next()) {
    String name = crs.getString("name");
    if (name.startsWith("A")) {
        crs.updateString("name", name.toUpperCase());
        crs.updateRow();
    }
}

// Modify without database access
crs.moveToInsertRow();
crs.updateInt("id", 100);
crs.updateString("name", "New Student");
crs.insertRow();
crs.moveToCurrentRow();

// Reconnect and sync changes
try {
    crs.acceptChanges();  // Reconnects and writes changes
} catch (SQLException e) {
    System.err.println("Sync failed: " + e.getMessage());
    // Handle conflict resolution
}

// Population property for security
crs.setKeyColumns(new int[]{1});  // Set primary key column(s)
crs.populate(resultSet);  // Populate from existing ResultSet
```

### CachedRowSet Properties and Methods

```java
// Properties
crs.setDataSourceName("jdbcDS");           // JNDI DataSource
crs.setCatalog("mydb");                    // Catalog name
crs.setEscapeProcessing(true);             // Enable escape processing
crs.setMaxRows(1000);                      // Limit rows
crs.setOriginalRow();                      // Reset to original position
crs.restoreOriginal();                     // Restore original data
crs.deleteRow();                           // Delete current row

// Navigation
crs.next();
crs.previous();
crs.absolute(5);
crs.beforeFirst();
crs.afterLast();
crs.relative(2);

// Position checking
crs.isFirst();
crs.isLast();
crs.isBeforeFirst();
crs.isAfterLast();
crs.getRow();    // Current row number
crs.getPageSize(); // Rows per page
crs.setPageSize(50);
```

### RowSet vs ResultSet Comparison

| Feature | ResultSet | RowSet |
|---------|-----------|--------|
| Interface | Direct JDBC | Extends ResultSet |
| Disconnected | No | Yes (CachedRowSet) |
| Serialization | No | Yes |
| Events | No | Yes (RowSetListener) |
| Bean Properties | No | Yes |
| Lazy fetching | Only with TYPE_FORWARD_ONLY | Configurable |

---

## 16.7 DatabaseMetaData and ResultSetMetaData

### DatabaseMetaData (Database Information)

Provides comprehensive information about the database and driver.

```java
DatabaseMetaData meta = conn.getMetaData();

// Database identification
System.out.println("Database: " + meta.getDatabaseProductName() + " " + 
                   meta.getDatabaseProductVersion());
System.out.println("Driver: " + meta.getDriverName() + " " + 
                   meta.getDriverVersion());
System.out.println("URL: " + meta.getURL());
System.out.println("User: " + meta.getUserName());
System.out.println("Schema: " + meta.getSchemaName());

// Capabilities
System.out.println("Supports Transactions: " + meta.supportsTransactions());
System.out.println("Supports Savepoints: " + meta.supportsSavepoints());
System.out.println("Supports Batch Updates: " + meta.supportsBatchUpdates());
System.out.println("Maximum Columns: " + meta.getMaxColumnsInTable());
System.out.println("Maximum Tables: " + meta.getMaxTableNameLength());

// Catalog and Schema operations
DatabaseMetaData meta = conn.getMetaData();

// Get all tables
try (ResultSet tables = meta.getTables(null, "schema_name", "%", 
        new String[]{"TABLE", "VIEW"})) {
    while (tables.next()) {
        String tableName = tables.getString("TABLE_NAME");
        String tableType = tables.getString("TABLE_TYPE");
        System.out.println("Table: " + tableName + " (" + tableType + ")");
    }
}

// Get all columns for a table
try (ResultSet columns = meta.getColumns(null, null, "students", "%")) {
    while (columns.next()) {
        System.out.println(columns.getString("COLUMN_NAME") + " - " +
            columns.getString("TYPE_NAME") + " (" +
            columns.getInt("COLUMN_SIZE") + ")");
    }
}

// Get primary keys
try (ResultSet pk = meta.getPrimaryKeys(null, null, "students")) {
    while (pk.next()) {
        System.out.println("PK Column: " + pk.getString("COLUMN_NAME"));
    }
}

// Get foreign keys
try (ResultSet fk = meta.getImportedKeys(null, null, "orders")) {
    while (fk.next()) {
        System.out.println("FK: " + fk.getString("FK_COLUMN_NAME") + 
            " -> " + fk.getString("PK_COLUMN_NAME") +
            " in table " + fk.getString("PK_TABLE_NAME"));
    }
}

// Get functions/procedures (for stored procedures)
try (ResultSet procs = meta.getProcedures(null, null, "%")) {
    while (procs.next()) {
        System.out.println("Procedure: " + procs.getString("PROCEDURE_NAME"));
    }
}
```

### ResultSetMetaData (ResultSet Structure)

Provides information about columns in a ResultSet.

```java
ResultSet rs = stmt.executeQuery("SELECT id, name, salary FROM employees");
ResultSetMetaData rsMeta = rs.getMetaData();

int columnCount = rsMeta.getColumnCount();
for (int i = 1; i <= columnCount; i++) {
    System.out.println("Column " + i + ":");
    System.out.println("  Label: " + rsMeta.getColumnLabel(i));
    System.out.println("  Name: " + rsMeta.getColumnName(i));
    System.out.println("  Type Name: " + rsMeta.getColumnTypeName(i));
    System.out.println("  SQL Type: " + rsMeta.getParameterType(i));
    System.out.println("  Precision: " + rsMeta.getPrecision(i));
    System.out.println("  Scale: " + rsMeta.getScale(i));
    System.out.println("  Nullable: " + (rsMeta.isNullable(i) == ResultSetMetaData.columnNoNulls ? 
                       "NO" : rsMeta.isNullable(i) == ResultSetMetaData.columnNullable ? 
                       "YES" : "UNKNOWN"));
    System.out.println("  Signed: " + rsMeta.isSigned(i));
    System.out.println("  Auto Increment: " + rsMeta.isAutoIncrement(i));
    System.out.println("  Case Sensitive: " + rsMeta.isCaseSensitive(i));
}
```

### ParameterMetaData (PreparedStatement Parameters)

Provides information about parameters in a PreparedStatement.

```java
PreparedStatement pstmt = conn.prepareStatement(
    "SELECT * FROM employees WHERE dept_id = ? AND salary > ? AND name LIKE ?");

ParameterMetaData pMeta = pstmt.getParameterMetaData();

System.out.println("Parameter count: " + pMeta.getParameterCount());

for (int i = 1; i <= pMeta.getParameterCount(); i++) {
    System.out.println("Param " + i + ":");
    System.out.println("  Type: " + pMeta.getParameterTypeName(i));
    System.out.println("  SQL Type: " + pMeta.getParameterType(i));  // java.sql.Types
    System.out.println("  Precision: " + pMeta.getPrecision(i));
    System.out.println("  Scale: " + pMeta.getScale(i));
    System.out.println("  Signed: " + pMeta.isSigned(i));
}

// Getting underlying JDBC type constant
int sqlType = pMeta.getParameterType(2);  // Returns Types.DECIMAL
if (sqlType == Types.VARCHAR) {
    System.out.println("Parameter 3 is a string");
}
```

**Note**: ParameterMetaData may return approximate values for some databases.

---

## 16.8 Important Exam Questions (from PYQ Analysis)

Based on analysis of Dec 2021 - June 2026 question papers.

### High Priority - 2 Mark Questions

1. **ResultSet types**: `TYPE_FORWARD_ONLY`, `TYPE_SCROLL_INSENSITIVE`, `TYPE_SCROLL_SENSITIVE`
2. **ResultSet concurrency**: `CONCUR_READ_ONLY`, `CONCUR_UPDATABLE`
3. **What is ResultSet holdability?** Explain `HOLD_CURSORS_OVER_COMMIT` and `CLOSE_CURSORS_AT_COMMIT`
4. **Difference between ResultSet and RowSet** (appeared 2023, 2026)
5. **What is JDBC batch processing?** Explain `addBatch()` and `executeBatch()` methods
6. **ABCD properties of transactions** with brief explanation
7. **Four JDBC transaction isolation levels** with their constants
8. **Explain three concurrency problems**: Dirty Read, Non-Repeatable Read, Phantom Read
9. **What is a savepoint?** Explain `setSavepoint()` and `rollback(Savepoint)`
10. **JdbcRowSet vs CachedRowSet**: Compare connectivity and use cases
11. **What is CallableStatement?** Difference from PreparedStatement
12. **RowSet types**: JdbcRowSet, CachedRowSet, WebRowSet, JoinRowSet, FilteredRowSet

### High Priority - 5 Mark Questions

1. **Explain ResultSet types, concurrency, and holdability** with practical example
2. **Explain updatable ResultSet** with insert, update, delete operations
3. **Explain batch processing with PreparedStatement** including error handling
4. **Explain JDBC transactions** with ACID properties and commit/rollback mechanism
5. **Explain isolation levels** with demonstration of dirty/non-repeatable/phantom reads
6. **Explain RowSet types** (JdbcRowSet, CachedRowSet) with practical use cases
7. **Explain DatabaseMetaData and ResultSetMetaData** with example code
8. **Explain CallableStatement for stored procedures** with IN/OUT parameters
9. **RowSet vs ResultSet**: Explain differences and use cases

### High Priority - 10 Mark Questions

1. **ResultSet (types, concurrency, holdability), Transactions (ACID, isolation, savepoints), Batch Processing, RowSet, Metadata.** (Appeared 2022, 2023, 2024, 2025)
2. **Complete JDBC program** demonstrating: connection, transaction with savepoint, batch insert, ResultSet navigation
3. **CallableStatement for stored procedures** with parameter handling and result set retrieval
4. **CachedRowSet offline operations** with sync back to database

### Programs to Practice

| # | Program | Years Appeared | Marks |
|---|---------|----------------|-------|
| 1 | ✅ **Scrollable ResultSet navigation** (next, previous, absolute) | 2022, 2023, 2024 | 5-10 |
| 2 | ✅ **Updatable ResultSet** (updateRow, insertRow, deleteRow) | 2022, 2023, 2024 | 10 |
| 3 | ✅ **Batch processing with PreparedStatement** | 2021, 2023, 2025 | 10 |
| 4 | ✅ **Transaction with savepoint** | 2023, 2024, 2025 | 10 |
| 5 | ✅ **Isolation level demonstration** | 2023 | 10 |
| 6 | ✅ **CachedRowSet offline editing** | 2023, 2026 | 5-10 |
| 7 | ✅ **CallableStatement stored procedure** | 2023, 2025 | 5-10 |
| 8 | ✅ **Metadata retrieval program** | 2024, 2025 | 10 |

---

## 16.9 Summary of Unit 16

| Topic | Key Points | Exam Year(s) |
|-------|------------|--------------|
| **ResultSet Types** | FORWARD_ONLY (default), SCROLL_INSENSITIVE, SCROLL_SENSITIVE | 2022×2, 2023, 2024 |
| **ResultSet Concurrency** | READ_ONLY (default), UPDATABLE | 2022, 2024 |
| **ResultSet Holdability** | HOLD_CURSORS_OVER_COMMIT, CLOSE_CURSORS_AT_COMMIT | 2024 |
| **ResultSet Navigation** | next, previous, first, last, absolute, relative, getRow | 2022, 2023, 2024 |
| **Updatable ResultSet** | updateXxx(), updateRow(), insertRow(), deleteRow(), moveToInsertRow() | 2022×2, 2023 |
| **Transactions** | ACID; setAutoCommit(false); commit(); rollback(); try-with-resources | 2023, 2024, 2025 |
| **Savepoints** | setSavepoint(), rollback(sp), releaseSavepoint() | 2023, 2024, 2025 |
| **Isolation Levels** | READ_UNCOMMITTED, READ_COMMITTED, REPEATABLE_READ, SERIALIZABLE | 2023 |
| **Concurrency Issues** | Dirty Read, Non-Repeatable Read, Phantom Read (explained with T1/T2 examples) | 2023 |
| **Batch Processing** | addBatch(), executeBatch(), BatchUpdateException, PreparedStatement preferred | 2021, 2023×2, 2025 |
| **CallableStatement** | Stored procedures, IN/OUT parameters, registerOutParameter(), execute() | 2023, 2025 |
| **JdbcRowSet** | Connected, wrapper around ResultSet, setCommand(), execute(), close() | 2023, 2026 |
| **CachedRowSet** | Disconnected, caches in memory, acceptChanges(), populate() | 2023, 2026 |
| **Metadata** | DatabaseMetaData (products, tables, columns), ResultSetMetaData (columns), ParameterMetaData (Pstmt params) | 2024, 2025 |

---

## 16.10 Best Practices Checklist

- [ ] Use **try-with-resources** for automatic resource cleanup
- [ ] Use **PreparedStatement** instead of Statement for parameters
- [ ] Always **close resources** in finally block or try-with-resources
- [ ] Use **savepoints** for partial rollback in complex transactions
- [ ] Choose **appropriate isolation level** based on requirements
- [ ] Use **batch processing** for bulk operations
- [ ] Handle **BatchUpdateException** for batch errors
- [ ] Use **metadata** for database-independent code
- [ ] Consider **CachedRowSet** for disconnected/offline scenarios
- [ ] Call **setAutoCommit(false)** before starting any transaction work

---

## 16.11 Quick Reference: Transaction Template

```java
Connection conn = null;
try {
    conn = DriverManager.getConnection(url, user, pass);
    conn.setAutoCommit(false);
    
    Savepoint sp = conn.setSavepoint("Start");
    
    try (PreparedStatement ps1 = conn.prepareStatement("UPDATE accounts SET balance = balance - ? WHERE id = ?")) {
        ps1.setDouble(1, 100.0);
        ps1.setInt(2, 1);
        ps1.executeUpdate();
    }
    
    try (PreparedStatement ps2 = conn.prepareStatement("UPDATE accounts SET balance = balance + ? WHERE id = ?")) {
        ps2.setDouble(1, 100.0);
        ps2.setInt(2, 2);
        ps2.executeUpdate();
    }
    
    conn.commit();
    System.out.println("Transaction committed successfully");
    
} catch (SQLException e) {
    if (conn != null) {
        try {
            conn.rollback();  // Full rollback
            System.out.println("Transaction rolled back");
        } catch (SQLException rollbackEx) {
            rollbackEx.printStackTrace();
        }
    }
    e.printStackTrace();
} finally {
    if (conn != null) {
        try { 
            conn.setAutoCommit(true);  // Restore default
            conn.close(); 
        } catch (SQLException ignored) {}
    }
}
```

## 16.12 RowSet vs ResultSet Code Comparison

| Operation | ResultSet | RowSet |
|-----------|-----------|--------|
| Create | `stmt.executeQuery(sql)` | `RowSetProvider.newFactory().createCachedRowSet()` |
| Navigate | `rs.next()`, `rs.previous()` | Same methods |
| Update | `rs.updateString(...)` + `rs.updateRow()` | `crs.updateString(...)` + `crs.updateRow()` |
| Insert | `rs.moveToInsertRow()` + `rs.insertRow()` | `crs.moveToInsertRow()` + `crs.insertRow()` |
| Close | `rs.close()` | `crs.close()` |
| Offline | Not possible | `crs.execute()` fetchs and disconnects, `crs.acceptChanges()` syncs |
| Events | No | `crs.addRowSetListener(listener)` |