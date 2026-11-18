# Unit 15: JDBC Part 1

## Unit Overview
This unit covers **JDBC Architecture** (2-tier vs 3-tier), **JDBC Driver Types** (I-IV), **JDBC Core Components**, database connection steps, **DriverManager** class, **Connection** interface, **Statement types** (Statement, PreparedStatement, CallableStatement), basic **JDBC programming** (CRUD), and **Transaction Management** basics.

> **Exam Priority (PYQ Analysis 2021-2026):** 🔴 **CRITICAL** — JDBC appears 8/10 years. 10-mark questions combining Architecture + Drivers + Connection Steps + Statement Types + Transactions appeared in **2021, 2022, 2023, 2024, 2025**. Driver Types (10m): 2022, 2023, 2024, 2025. Architecture (10m): 2022, 2023, 2024, 2025. Connection Steps + Code: every year.

---

## 15.1 Introduction to JDBC

### Definition
> **JDBC (Java Database Connectivity)** is a Java API for connecting to and executing queries on relational databases. It provides a **standard interface** for **database-independent connectivity**.

### Why JDBC?
- **Database-independent code** — write once, run on any RDBMS
- **Standard API** across all RDBMS (MySQL, Oracle, PostgreSQL, SQL Server, etc.)
- **Part of Java SE** (`java.sql`, `javax.sql` packages)
- **Vendor-neutral** — switch databases by changing driver/URL only

### JDBC Packages

| Package | Description |
|---------|-------------|
| `java.sql` | **Core JDBC API** — DriverManager, Connection, Statement, PreparedStatement, CallableStatement, ResultSet, SQLException, DatabaseMetaData, ResultSetMetaData |
| `javax.sql` | **Extended JDBC API** — DataSource, ConnectionPoolDataSource, PooledConnection, RowSet (JdbcRowSet, CachedRowSet, WebRowSet) |

> **Note**: `java.sql` is the primary package for all basic JDBC operations. `javax.sql` adds enterprise features (connection pooling, DataSource, RowSet).

---

## 15.2 JDBC Architecture

### Two-Tier Architecture (Client-Server)
```
┌─────────────────┐         JDBC          ┌─────────────────┐
│   Java App      │  ◄─────────────────►  │   Database      │
│   (Client)      │    SQL + Results      │   (Server)      │
└─────────────────┘                       └─────────────────┘
```
- **Client**: Java application with JDBC driver
- **Server**: Database engine
- **Communication**: Direct via JDBC driver
- **Use Case**: Simple applications, desktop apps, tools

### Three-Tier Architecture
```
┌─────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Client     │     │  Middle Tier    │     │  Database       │
│  (Browser/  │◄───►│  (App Server/   │◄───►│  (Data Source)  │
│   GUI)      │     │   Business Logic)     │                 │
└─────────────┘     └─────────────────┘     └─────────────────┘
```
- **Client**: Presentation layer (HTML, JavaFX, Swing, mobile)
- **Middle Tier**: Business logic, **connection pooling**, transaction management, security
- **Database**: Data storage only
- **Use Case**: Enterprise applications, web apps, scalable systems

### JDBC Architecture Components (Core Components)
```
Java Application
       │
       ▼
┌──────────────────┐
│   JDBC API       │  ← java.sql.* interfaces (DriverManager, Connection, 
│  (Core Components)    Statement, PreparedStatement, CallableStatement,
│                  │     ResultSet, SQLException, DatabaseMetaData)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  JDBC Driver     │  ← Vendor-specific implementation (Type I-IV)
│  (Driver class)  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Database        │  ← MySQL, Oracle, PostgreSQL, SQL Server, etc.
└──────────────────┘
```

> **Exam Key Point (2025 Q4(a) 10m)**: "JDBC Core Components" = **DriverManager, Driver, Connection, Statement, PreparedStatement, CallableStatement, ResultSet, SQLException**. Draw this diagram with labels.

### JDBC Core Components — Detailed

| Component | Interface/Class | Purpose |
|-----------|-----------------|---------|
| **DriverManager** | `java.sql.DriverManager` | Loads drivers, manages connections |
| **Driver** | `java.sql.Driver` | Vendor-specific; implements protocol |
| **Connection** | `java.sql.Connection` | Session with DB; creates statements; transactions |
| **Statement** | `java.sql.Statement` | Executes static SQL queries |
| **PreparedStatement** | `java.sql.PreparedStatement` | Executes parameterized SQL (pre-compiled) |
| **CallableStatement** | `java.sql.CallableStatement` | Calls stored procedures/functions |
| **ResultSet** | `java.sql.ResultSet` | Cursor over query results; read/update data |
| **SQLException** | `java.sql.SQLException` | Checked exception for DB errors |
| **DatabaseMetaData** | `java.sql.DatabaseMetaData` | DB info (tables, columns, version, capabilities) |
| **ResultSetMetaData** | `java.sql.ResultSetMetaData` | ResultSet structure (column count, types, names) |

---

## 15.3 JDBC Driver Types

### Type 1: JDBC-ODBC Bridge Driver
- **Mechanism**: JDBC → ODBC → Database
- **Pros**: Works with any ODBC-compliant database
- **Cons**: Requires ODBC driver; not portable; **deprecated (removed in Java 8)**
- **Example**: `sun.jdbc.odbc.JdbcOdbcDriver`
- **Status**: **Obsolete** — do not use in modern applications

### Type 2: Native-API Driver (Partial Java)
- **Mechanism**: JDBC → Native Client Library → Database
- **Pros**: Better performance than Type 1
- **Cons**: Requires native library on client; not fully portable; platform-dependent
- **Example**: Oracle OCI Driver (`oracle.jdbc.driver.OracleDriver` — older)
- **Use Case**: Legacy Oracle installations

### Type 3: Network Protocol Driver (Middleware / Pure Java)
- **Mechanism**: JDBC → Middleware Server → Database
- **Pros**: Pure Java; database-independent middleware; flexible (single middleware → multiple DBs)
- **Cons**: Extra network hop; middleware complexity; middleware becomes bottleneck
- **Example**: IDS Server, DataDirect SequeLink
- **Use Case**: Application servers, multi-database environments

### Type 4: Thin Driver (Pure Java) — **RECOMMENDED & STANDARD**
- **Mechanism**: JDBC → Direct Database Protocol (TCP/IP)
- **Pros**: **Pure Java**; **no client installation**; **best performance**; **fully portable**; direct socket connection
- **Cons**: Database-specific protocol (one driver per database)
- **Examples**:
  - MySQL: `com.mysql.cj.jdbc.Driver` (MySQL Connector/J 8.0+)
  - PostgreSQL: `org.postgresql.Driver`
  - Oracle: `oracle.jdbc.OracleDriver` (ojdbc8.jar+)
  - SQL Server: `com.microsoft.sqlserver.jdbc.SQLServerDriver`
  - H2: `org.h2.Driver`
  - Derby: `org.apache.derby.jdbc.ClientDriver`

### Driver Comparison Table

| Type | Portability | Performance | Installation | Use Case | Status |
|------|-------------|-------------|--------------|----------|--------|
| Type 1 | Low | Low | ODBC needed | Legacy only | **Removed (Java 8+)** |
| Type 2 | Medium | Medium | Native lib | Legacy Oracle | **Avoid** |
| Type 3 | High | Medium | Middleware | App servers | Niche |
| **Type 4** | **High** | **High** | **None** | **Modern apps** | **Standard** |

> **Exam Tip (2022, 2023, 2024, 2025 — 10 marks each)**: Always draw comparison table. **Type 4 is the answer for "which driver is preferred and why?"** — Pure Java, no client install, best performance, portable.

### Driver Loading — JDBC 4.0+ (Java 6+) Auto-Loading
```java
// OLD WAY (pre-JDBC 4.0 / Java 6) — still works but not needed
Class.forName("com.mysql.cj.jdbc.Driver");

// NEW WAY (JDBC 4.0+ / Java 6+) — AUTOMATIC via SPI (Service Provider Interface)
// Driver JAR must contain META-INF/services/java.sql.Driver with driver class name
// Just ensure driver JAR is in classpath — DriverManager auto-discovers it
Connection conn = DriverManager.getConnection(url, user, pass);
```

> **Exam Note**: Mention **"JDBC 4.0 introduced auto-loading via SPI; Class.forName() optional since Java 6"** — shows depth.

---

## 15.4 JDBC Connection Steps (6 Standard Steps)

```java
// 1. Load Driver (Optional since JDBC 4.0 / Java 6 — auto-loaded via SPI)
Class.forName("com.mysql.cj.jdbc.Driver");  // Only needed for older drivers / explicit loading

// 2. Establish Connection
Connection conn = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/mydb", "username", "password");

// 3. Create Statement
Statement stmt = conn.createStatement();
// OR PreparedStatement pstmt = conn.prepareStatement(sql);
// OR CallableStatement cstmt = conn.prepareCall(sql);

// 4. Execute Query
ResultSet rs = stmt.executeQuery("SELECT * FROM students");
// OR int rows = stmt.executeUpdate("INSERT ...");

// 5. Process Results
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
}

// 6. Close Resources (in REVERSE order: ResultSet → Statement → Connection)
rs.close();
stmt.close();
conn.close();
```

### Connection URL Formats (Memorize for Exams)

| Database | URL Format | Default Port |
|----------|------------|--------------|
| **MySQL** | `jdbc:mysql://host:port/dbname?useSSL=false&serverTimezone=UTC` | 3306 |
| **PostgreSQL** | `jdbc:postgresql://host:port/dbname` | 5432 |
| **Oracle (Thin)** | `jdbc:oracle:thin:@host:port:sid` or `jdbc:oracle:thin:@//host:port/service` | 1521 |
| **SQL Server** | `jdbc:sqlserver://host:port;databaseName=dbname` | 1433 |
| **H2 (Embedded)** | `jdbc:h2:~/test` or `jdbc:h2:mem:test` | N/A |
| **Derby (Embedded)** | `jdbc:derby:dbname;create=true` | N/A |

> **Exam Tip**: MySQL URL **must** include `useSSL=false&serverTimezone=UTC` (or `serverTimezone=IST`) for production to avoid warnings/errors.

### Connection via Properties Object (Best Practice for Config)
```java
Properties props = new Properties();
props.setProperty("user", "root");
props.setProperty("password", "password");
props.setProperty("useSSL", "false");
props.setProperty("serverTimezone", "UTC");
props.setProperty("autoReconnect", "true");
props.setProperty("characterEncoding", "UTF-8");
props.setProperty("connectionTimeout", "30000");  // 30 seconds

Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", props);
```

---

## 15.5 DriverManager Class

### Purpose
Manages loaded JDBC drivers and establishes database connections. **Factory for Connection objects.**

### Key Methods
```java
// Register driver (automatic in JDBC 4.0+ via SPI)
DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());

// Get connection — 3 overloaded versions
Connection getConnection(String url)
Connection getConnection(String url, String user, String password)
Connection getConnection(String url, Properties info)

// Driver management
Enumeration<Driver> getDrivers()           // List all loaded drivers
Driver getDriver(String url)               // Find driver for URL
void deregisterDriver(Driver driver)       // Remove driver (rarely used)
```

### DriverManager Internals
- Maintains a `Vector<Driver>` of registered drivers
- On `getConnection()`, iterates drivers calling `driver.connect(url, info)`
- First driver returning non-null Connection wins
- **Thread-safe**

---

## 15.6 Connection Interface

### Key Methods
```java
// Create statements
Statement createStatement()
PreparedStatement prepareStatement(String sql)
CallableStatement prepareCall(String sql)

// Transaction management
void setAutoCommit(boolean autoCommit)     // Default: true
void commit()
void rollback()
void rollback(Savepoint savepoint)         // Partial rollback
Savepoint setSavepoint()                   // Unnamed savepoint
Savepoint setSavepoint(String name)        // Named savepoint
void releaseSavepoint(Savepoint savepoint) // Release savepoint

// Metadata
DatabaseMetaData getMetaData()

// Connection properties
boolean isClosed()
void close()
String getCatalog() / void setCatalog(String catalog)
int getTransactionIsolation() / void setTransactionIsolation(int level)
boolean isReadOnly() / void setReadOnly(boolean readOnly)
```

### Auto-Commit Mode & Transaction Management (HIGH Priority — 2023, 2024, 2025)

```java
Connection conn = DriverManager.getConnection(url, user, pass);

// Default: autoCommit = true (each statement committed individually)
conn.setAutoCommit(false);  // START TRANSACTION — disable auto-commit

try {
    // Multiple operations as single atomic unit
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

    // COMMIT — make all changes permanent
    conn.commit();
    System.out.println("Transaction committed successfully");

} catch (SQLException e) {
    // ROLLBACK — undo ALL changes in this transaction
    conn.rollback();
    System.out.println("Transaction rolled back: " + e.getMessage());

} finally {
    // ALWAYS restore auto-commit and close
    conn.setAutoCommit(true);  // Restore default
    conn.close();
}
```

### Savepoints (Partial Rollback) — Unit 16 covers in detail, but basics here
```java
conn.setAutoCommit(false);
Savepoint sp1 = conn.setSavepoint("AfterStep1");  // Named savepoint

// ... perform operations ...
// If needed: conn.rollback(sp1);  // Undo only to this savepoint
// conn.releaseSavepoint(sp1);     // Release when done
```

> **Exam Tip (2024 Q4(a) 10m)**: "JDBC connection steps + commit vs rollback" — **Must show**: `setAutoCommit(false)`, try block with operations, `commit()` in try, `rollback()` in catch, `setAutoCommit(true)` in finally.

---

## 15.7 Statement Types — Detailed Comparison

### 1. Statement (Static SQL)
```java
Statement stmt = conn.createStatement();

// Execute queries (returns ResultSet)
ResultSet rs = stmt.executeQuery("SELECT * FROM students");

// Execute updates — INSERT, UPDATE, DELETE, DDL (returns int: row count)
int rows = stmt.executeUpdate("INSERT INTO students(name) VALUES('John')");
int rows = stmt.executeUpdate("UPDATE students SET age=21 WHERE id=1");
int rows = stmt.executeUpdate("DELETE FROM students WHERE id=2");
int rows = stmt.executeUpdate("CREATE TABLE test (id INT)");  // DDL

// Execute any SQL (returns boolean: true if ResultSet, false if update count)
boolean hasResults = stmt.execute("SELECT * FROM students");
if (hasResults) {
    ResultSet rs = stmt.getResultSet();
} else {
    int count = stmt.getUpdateCount();
}
```

### 2. PreparedStatement (Parameterized SQL) — **PREFERRED FOR ALL DML**
```java
String sql = "INSERT INTO students(name, age, email) VALUES(?, ?, ?)";
PreparedStatement pstmt = conn.prepareStatement(sql);

// Set parameters (1-based index)
pstmt.setString(1, "Alice");
pstmt.setInt(2, 20);
pstmt.setString(3, "alice@example.com");

// Execute
int rows = pstmt.executeUpdate();

// For SELECT
PreparedStatement pstmt2 = conn.prepareStatement("SELECT * FROM students WHERE age > ?");
pstmt2.setInt(1, 18);
ResultSet rs = pstmt2.executeQuery();
```

#### Advantages of PreparedStatement (MEMORIZE for Exams)

| Advantage | Description |
|-----------|-------------|
| **SQL Injection Prevention** | Parameters escaped automatically; user input never concatenated into SQL |
| **Performance** | SQL parsed, compiled, optimized **once**; execution plan cached; reused for multiple executions |
| **Readability** | Clean separation of SQL logic and data |
| **Type Safety** | `setXxx()` methods enforce correct Java-to-SQL type mapping |
| **Batch Processing** | `addBatch()` / `executeBatch()` for bulk operations |

#### Parameter Setter Methods (Common)
```java
pstmt.setString(1, "text");
pstmt.setInt(2, 42);
pstmt.setLong(3, 123L);
pstmt.setDouble(4, 3.14);
pstmt.setBoolean(5, true);
pstmt.setDate(6, java.sql.Date.valueOf("2024-01-15"));
pstmt.setTimestamp(7, java.sql.Timestamp.valueOf("2024-01-15 10:30:00"));
pstmt.setNull(8, Types.VARCHAR);
pstmt.setObject(9, someObject);  // Generic (JDBC 2.0+)
pstmt.setBigDecimal(10, new BigDecimal("123.45"));
pstmt.setBytes(11, byteArray);   // For BLOB
```

### 3. CallableStatement (Stored Procedures & Functions) — **CRITICAL (2023, 2025 Q5(a) 5m)**

```java
// Stored procedure: CREATE PROCEDURE getStudentCount(OUT count INT)
String sql = "{call getStudentCount(?)}";
CallableStatement cstmt = conn.prepareCall(sql);

// Register OUT parameter BEFORE execute
cstmt.registerOutParameter(1, Types.INTEGER);

// Execute
cstmt.execute();

// Get OUT parameter value
int count = cstmt.getInt(1);

// With IN/OUT parameters
// Procedure: CREATE PROCEDURE updateSalary(IN id INT, INOUT salary DECIMAL(10,2))
String sql2 = "{call updateSalary(?, ?)}";
CallableStatement cstmt2 = conn.prepareCall(sql2);
cstmt2.setInt(1, 101);                    // IN parameter
cstmt2.setDouble(2, 50000.0);             // INOUT: set initial value
cstmt2.registerOutParameter(2, Types.DECIMAL);  // Register as OUT
cstmt2.execute();
double newSalary = cstmt2.getDouble(2);   // Get updated value

// Function returning value: {? = call functionName(?)}
String sql3 = "{? = call getEmployeeCount()}";
CallableStatement cstmt3 = conn.prepareCall(sql3);
cstmt3.registerOutParameter(1, Types.INTEGER);  // Return value
cstmt3.execute();
int count = cstmt3.getInt(1);
```

#### CallableStatement Syntax Rules
| Syntax | Meaning |
|--------|---------|
| `{call procedureName(?)}` | Procedure with no return |
| `{call procedureName(?, ?)}` | Procedure with parameters |
| `{? = call functionName(?)}` | Function with return value |

#### CallableStatement Methods (Key)
| Method | Purpose |
|--------|---------|
| `registerOutParameter(int index, int sqlType)` | Register OUT/INOUT parameter type |
| `registerOutParameter(int index, int sqlType, int scale)` | For DECIMAL/NUMERIC with scale |
| `wasNull()` | Check if last OUT parameter was SQL NULL |
| `getString(), getInt(), getDouble(), ...` | Retrieve OUT/INOUT values |

---

## 15.8 ResultSet Interface — Basic Overview (Used throughout, detailed in Unit 16)

> **Note**: ResultSet is covered in depth in **Unit 16**. Here are the basics used in Unit 15 examples.

```java
// Execute query
ResultSet rs = stmt.executeQuery("SELECT id, name, age FROM students");

// Cursor starts BEFORE first row — call next() to move to first row
while (rs.next()) {
    // Getter methods — by column name (recommended) or index (1-based, faster)
    int id = rs.getInt("id");           // or rs.getInt(1)
    String name = rs.getString("name"); // or rs.getString(2)
    int age = rs.getInt("age");         // or rs.getInt(3)
}

// Handle NULL values
int age = rs.getInt("age");
if (rs.wasNull()) {
    // Column was NULL in database
}

// Close
rs.close();
```

### ResultSet Navigation (Forward-Only Default)
| Method | Description |
|--------|-------------|
| `next()` | Move to next row (returns false if no more rows) |
| `close()` | Release resources immediately |
| `wasNull()` | Check if last getXXX returned SQL NULL |

> **Scrollable/Updatable ResultSet** (`TYPE_SCROLL_INSENSITIVE`, `CONCUR_UPDATABLE`) — **Unit 16**

---

## 15.9 Complete JDBC CRUD Program (EXAM STANDARD — Appeared 2021, 2022, 2023, 2024, 2025)

```java
import java.sql.*;

public class StudentCRUD {
    // Database configuration
    private static final String URL = "jdbc:mysql://localhost:3306/school?useSSL=false&serverTimezone=UTC";
    private static final String USER = "root";
    private static final String PASS = "password";

    public static void main(String[] args) {
        // Try-with-resources: auto-closes Connection (and nested resources)
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            
            // Ensure table exists (DDL via Statement)
            createTable(conn);
            
            // CREATE
            createStudent(conn, "Alice", 20, "alice@email.com");
            createStudent(conn, "Bob", 22, "bob@email.com");
            
            // READ
            readAllStudents(conn);
            
            // UPDATE
            updateStudent(conn, 1, "Alice Smith");
            
            // READ after update
            readAllStudents(conn);
            
            // DELETE
            deleteStudent(conn, 2);
            
            // Final READ
            readAllStudents(conn);

        } catch (SQLException e) {
            // Proper exception handling
            System.err.println("SQL State: " + e.getSQLState());
            System.err.println("Error Code: " + e.getErrorCode());
            System.err.println("Message: " + e.getMessage());
            e.printStackTrace();
        }
    }

    // DDL — Create table (run once)
    static void createTable(Connection conn) throws SQLException {
        String sql = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                age INT,
                email VARCHAR(100)
            )
            """;
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
            System.out.println("Table 'students' ready.");
        }
    }

    // CREATE — PreparedStatement with parameters
    static void createStudent(Connection conn, String name, int age, String email) throws SQLException {
        String sql = "INSERT INTO students(name, age, email) VALUES(?, ?, ?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setString(3, email);
            int rows = pstmt.executeUpdate();
            
            // Get auto-generated ID
            try (ResultSet keys = pstmt.getGeneratedKeys()) {
                if (keys.next()) {
                    System.out.println("Inserted student ID: " + keys.getInt(1));
                }
            }
            System.out.println(rows + " student(s) inserted.");
        }
    }

    // READ — Statement for simple query, PreparedStatement if parameterized
    static void readAllStudents(Connection conn) throws SQLException {
        String sql = "SELECT id, name, age, email FROM students";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            System.out.println("\n--- Students ---");
            boolean hasRows = false;
            while (rs.next()) {
                hasRows = true;
                System.out.printf("ID: %d, Name: %s, Age: %d, Email: %s%n",
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getInt("age"),
                    rs.getString("email"));
            }
            if (!hasRows) {
                System.out.println("(no records)");
            }
        }
    }

    // UPDATE — PreparedStatement
    static void updateStudent(Connection conn, int id, String newName) throws SQLException {
        String sql = "UPDATE students SET name = ? WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, newName);
            pstmt.setInt(2, id);
            int rows = pstmt.executeUpdate();
            System.out.println(rows + " student(s) updated.");
        }
    }

    // DELETE — PreparedStatement
    static void deleteStudent(Connection conn, int id) throws SQLException {
        String sql = "DELETE FROM students WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int rows = pstmt.executeUpdate();
            System.out.println(rows + " student(s) deleted.");
        }
    }
}
```

---

## 15.10 Transaction Management Example (EXAM STANDARD — 2023, 2024, 2025)

```java
import java.sql.*;

public class TransactionDemo {
    private static final String URL = "jdbc:mysql://localhost:3306/bank?useSSL=false&serverTimezone=UTC";
    private static final String USER = "root";
    private static final String PASS = "password";

    public static void main(String[] args) {
        Connection conn = null;
        try {
            // 1. Get connection
            conn = DriverManager.getConnection(URL, USER, PASS);
            
            // 2. Disable auto-commit = START TRANSACTION
            conn.setAutoCommit(false);
            
            // 3. Perform multiple operations
            transferMoney(conn, 1, 2, 500.0);  // Debit from 1, credit to 2
            
            // 4. Commit if all successful
            conn.commit();
            System.out.println("Transaction committed successfully!");
            
        } catch (SQLException e) {
            // 5. Rollback on ANY error
            if (conn != null) {
                try {
                    conn.rollback();
                    System.out.println("Transaction rolled back due to: " + e.getMessage());
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        } finally {
            // 6. ALWAYS restore auto-commit and close
            if (conn != null) {
                try {
                    conn.setAutoCommit(true);  // Restore default
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    static void transferMoney(Connection conn, int fromAcc, int toAcc, double amount) throws SQLException {
        if (amount <= 0) throw new SQLException("Invalid amount: " + amount);
        
        // Check balance
        String checkSql = "SELECT balance FROM accounts WHERE id = ?";
        try (PreparedStatement checkStmt = conn.prepareStatement(checkSql)) {
            checkStmt.setInt(1, fromAcc);
            try (ResultSet rs = checkStmt.executeQuery()) {
                if (!rs.next()) throw new SQLException("Account " + fromAcc + " not found");
                double balance = rs.getDouble("balance");
                if (balance < amount) throw new SQLException("Insufficient balance: " + balance);
            }
        }
        
        // Debit
        String debitSql = "UPDATE accounts SET balance = balance - ? WHERE id = ?";
        try (PreparedStatement debitStmt = conn.prepareStatement(debitSql)) {
            debitStmt.setDouble(1, amount);
            debitStmt.setInt(2, fromAcc);
            debitStmt.executeUpdate();
        }
        
        // Credit
        String creditSql = "UPDATE accounts SET balance = balance + ? WHERE id = ?";
        try (PreparedStatement creditStmt = conn.prepareStatement(creditSql)) {
            creditStmt.setDouble(1, amount);
            creditStmt.setInt(2, toAcc);
            creditStmt.executeUpdate();
        }
        
        System.out.println("Transferred " + amount + " from account " + fromAcc + " to " + toAcc);
    }
}
```

---

## 15.11 Exception Handling in JDBC

```java
try (Connection conn = DriverManager.getConnection(url, user, pass);
     PreparedStatement pstmt = conn.prepareStatement(sql)) {
     
    pstmt.setString(1, value);
    pstmt.executeUpdate();
    
} catch (SQLException e) {
    // SQLException provides detailed error info
    System.err.println("SQL State: " + e.getSQLState());    // XOPEN/SQL standard code
    System.err.println("Error Code: " + e.getErrorCode());  // Vendor-specific code
    System.err.println("Message: " + e.getMessage());       // Human-readable
    
    // Print chained exceptions (multiple causes)
    while (e != null) {
        e.printStackTrace();
        e = e.getNextException();
    }
    
    // Common SQL States:
    // 08001 - Connection refused / cannot connect
    // 08003 - Connection does not exist
    // 08006 - Connection failure
    // 23000 - Integrity constraint violation (PK, FK, unique)
    // 28000 - Invalid authorization (wrong user/pass)
    // 42000 - Syntax error / access violation
} catch (Exception e) {
    // Other exceptions (ClassNotFoundException, etc.)
    e.printStackTrace();
}
```

---

## 15.12 Important Exam Questions (from PYQ Analysis 2021-2026)

### High Priority — 2-Mark Questions
1. **What is JDBC? Why is it used?** — Standard API, database-independent, part of Java SE
2. **JDBC Architecture: 2-tier vs 3-tier** — Draw diagrams; Client-Server vs Client-Middle-DB
3. **Four types of JDBC drivers** — Type I (JDBC-ODBC), II (Native-API), III (Middleware), IV (Thin/Pure Java)
4. **Why Type 4 driver is preferred?** — Pure Java, no client install, best performance, portable
5. **Steps to connect to database using JDBC** — 6 steps: Load Driver → Connection → Statement → Execute → Process → Close
6. **Difference between Statement, PreparedStatement, CallableStatement** — Static vs Parameterized vs Stored Proc
7. **What is auto-commit? How to manage transactions?** — Default true; setAutoCommit(false); commit()/rollback()
8. **What is DriverManager?** — Manages drivers; factory for Connections
9. **Connection URL for MySQL/PostgreSQL/Oracle** — Memorize formats
10. **JDBC Core Components** — DriverManager, Driver, Connection, Statement, PreparedStatement, CallableStatement, ResultSet, SQLException (2025 Q4(a))
11. **What is PreparedStatement? Advantages?** — Pre-compiled, SQL injection prevention, performance, type safety
12. **What is CallableStatement?** — For stored procedures/functions; supports IN/OUT/INOUT params

### 5-Mark Questions (Short Notes / Explain with Example)
1. **Explain JDBC Architecture with diagram (2-tier and 3-tier)** — 2022, 2023, 2024, 2025
2. **Explain four types of JDBC drivers with comparison table** — 2022, 2023, 2024, 2025 (10m also)
3. **Explain database connection steps with example code** — Every year
4. **Explain PreparedStatement advantages with example** — 2025 Q5(b) — 5 marks!
5. **Explain CallableStatement for stored procedures with syntax** — 2025 Q5(a) — 5 marks!
6. **Explain JDBC Transaction Management (commit/rollback/savepoint)** — 2024 Q4(a)
7. **Explain DriverManager class and its methods** — 2021 Q1(f)
8. **Explain Connection interface methods** — commit, rollback, setAutoCommit, prepareStatement

### 10-Mark Questions (Detailed Theory + Complete Program)
1. **JDBC Architecture (2/3 tier), Driver Types, Connection Steps, Statement Types, Transaction Management** — **Appeared 2021, 2022, 2023, 2024, 2025** — **MUST MASTER**
2. **Complete JDBC program: Connection, CRUD operations, Exception handling, Transaction demo**
3. **JDBC Core Components + Architecture diagram + Driver comparison + Transaction example** — 2025 Q4(a)

### Programs to Practice (High Yield — Appeared Repeatedly)
1. ✅ **JDBC Connection + CRUD** — 2021, 2022, 2023, 2024, 2025
2. ✅ **PreparedStatement demo (parameterized INSERT/SELECT)** — 2022, 2023, 2024, 2025
3. ✅ **Transaction management (commit/rollback with try-catch-finally)** — 2023, 2024
4. ✅ **Driver types comparison table** — 2022, 2023, 2024, 2025
5. ✅ **CallableStatement (stored procedure with IN/OUT params)** — 2023, 2025
6. ✅ **Connection via Properties object** — Configuration best practice

---

## 15.13 Quick Comparison: Statement vs PreparedStatement vs CallableStatement

| Feature | Statement | PreparedStatement | CallableStatement |
|---------|-----------|-------------------|-------------------|
| **SQL Type** | Static | Parameterized | Stored Procedure/Function |
| **Compilation** | Every execution | Once (pre-compiled) | Pre-compiled in DB |
| **Parameters** | Not supported | `setXxx(index, value)` | `setXxx()` + `registerOutParameter()` |
| **IN Params** | ❌ | ✅ | ✅ |
| **OUT Params** | ❌ | ❌ | ✅ |
| **INOUT Params** | ❌ | ❌ | ✅ |
| **SQL Injection** | Vulnerable | **Prevented** | **Prevented** |
| **Performance** | Low | **High** | **High** |
| **Batch Support** | `addBatch(sql)` | `addBatch()` (params) | `addBatch()` |
| **Use Case** | DDL, simple static queries | **All DML (INSERT/UPDATE/DELETE/SELECT)** | Stored procedures, functions |
| **Syntax** | `stmt.executeQuery(sql)` | `pstmt.executeQuery()` | `cstmt.execute()` + `getResultSet()` |
| **Create via** | `conn.createStatement()` | `conn.prepareStatement(sql)` | `conn.prepareCall("{call proc(?)}")` |

---

## 15.14 Summary of Unit 15

| Topic | Key Points |
|-------|------------|
| **JDBC** | Java API for database connectivity; database-independent; `java.sql`, `javax.sql` |
| **Architecture** | 2-tier (Client-Server) vs 3-tier (Client-Middle-DB); **Core Components**: DriverManager, Driver, Connection, Statement, PreparedStatement, CallableStatement, ResultSet, SQLException |
| **Driver Types** | Type 1: JDBC-ODBC (removed); Type 2: Native-API; Type 3: Middleware; **Type 4: Pure Java (Best)** |
| **Connection Steps** | 1. Load Driver (auto since JDBC 4.0), 2. Get Connection, 3. Create Statement, 4. Execute, 5. Process, 6. Close |
| **DriverManager** | Manages drivers; `getConnection()` overloads; `getDrivers()`, `getDriver(url)` |
| **Connection** | `createStatement()`, `prepareStatement()`, `prepareCall()`; **Transaction**: `setAutoCommit(false)`, `commit()`, `rollback()`, `setSavepoint()` |
| **Statement** | Static SQL; `executeQuery()`, `executeUpdate()`, `execute()` |
| **PreparedStatement** | **Parameterized**; prevents SQL injection; pre-compiled; **PREFERRED** for DML |
| **CallableStatement** | Stored procedures/functions; IN/OUT/INOUT params; `registerOutParameter()` |
| **ResultSet** | Forward-only by default; `next()`, getXXX(); scrollable/updatable in Unit 16 |
| **Transactions** | ACID; disable auto-commit; commit/rollback in try-catch-finally; savepoints for partial rollback |
| **Exception Handling** | `SQLException` — SQLState, ErrorCode, Message, chained exceptions |

---

## 15.15 Quick Reference: JDBC Template (Exam Cheat Sheet)

```java
// 1. CONNECTION (with Properties - best practice)
String url = "jdbc:mysql://localhost:3306/db?useSSL=false&serverTimezone=UTC";
Properties props = new Properties();
props.setProperty("user", "root");
props.setProperty("password", "pass");
props.setProperty("useSSL", "false");
props.setProperty("serverTimezone", "UTC");

try (Connection conn = DriverManager.getConnection(url, props)) {

    // 2. PREPAREDSTATEMENT (Best Practice for DML)
    String sql = "SELECT * FROM users WHERE email = ?";
    try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
        pstmt.setString(1, "test@example.com");
        try (ResultSet rs = pstmt.executeQuery()) {
            while (rs.next()) {
                // process: rs.getInt("id"), rs.getString("name"), etc.
            }
        }
    }

    // 3. TRANSACTION (when multiple updates)
    conn.setAutoCommit(false);
    try {
        // Multiple PreparedStatement executeUpdate() calls
        conn.commit();
    } catch (SQLException e) {
        conn.rollback();
        throw e;  // Re-throw or handle
    } finally {
        conn.setAutoCommit(true);
    }

    // 4. CALLABLESTATEMENT (Stored Procedure)
    // String call = "{call procName(?, ?)}";
    // try (CallableStatement cstmt = conn.prepareCall(call)) {
    //     cstmt.setInt(1, inParam);
    //     cstmt.registerOutParameter(2, Types.INTEGER);
    //     cstmt.execute();
    //     int outValue = cstmt.getInt(2);
    // }

} catch (SQLException e) {
    // Handle: e.getSQLState(), e.getErrorCode(), e.getMessage()
    e.printStackTrace();
}
```

---

## 15.16 Common Exam Mistakes to Avoid

| ❌ Mistake | ✅ Correct |
|-----------|-----------|
| `Class.forName()` required always | Optional since JDBC 4.0/Java 6 (auto SPI) |
| Concatenating SQL: `"SELECT * FROM t WHERE name='" + name + "'"` | Use `PreparedStatement` with `?` placeholders |
| Forgetting `conn.setAutoCommit(false)` before transaction | Always disable auto-commit for multi-statement transactions |
| Missing `conn.rollback()` in catch block | Always rollback on exception |
| Not closing resources (ResultSet, Statement, Connection) | Use **try-with-resources** (Java 7+) |
| `rs.getInt("id")` without checking `rs.next()` first | Always call `rs.next()` before getters |
| Using `Statement` for parameterized queries | Use `PreparedStatement` |
| Confusing `executeQuery()` (SELECT) vs `executeUpdate()` (INSERT/UPDATE/DELETE) | `executeQuery` → ResultSet; `executeUpdate` → int row count |
| Forgetting `registerOutParameter()` before `CallableStatement.execute()` | Register ALL OUT/INOUT params before execute |
| Not handling `SQLException` chain (`getNextException()`) | Loop through chained exceptions for complete diagnosis |

---

**End of Unit 15 Notes** — Next: **Unit 16: JDBC Part 2** (ResultSet types, advanced transactions, batch processing, RowSet, Metadata)