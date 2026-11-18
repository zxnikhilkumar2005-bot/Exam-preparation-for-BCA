# Unit 15: JDBC Part 1

## Unit Overview
This unit covers JDBC Architecture (2-tier vs 3-tier), JDBC Driver Types (I-IV), database connection steps, DriverManager class, Connection interface, Statement types (Statement, PreparedStatement, CallableStatement), and basic JDBC programming.

---

## 15.1 Introduction to JDBC

### Definition
> **JDBC (Java Database Connectivity)** is a Java API for connecting to and executing queries on relational databases. It provides a standard interface for database-independent connectivity.

### Why JDBC?
- Database-independent code
- Standard API across all RDBMS (MySQL, Oracle, PostgreSQL, SQL Server, etc.)
- Part of Java SE (java.sql, javax.sql packages)

### JDBC Packages
| Package | Description |
|---------|-------------|
| `java.sql` | Core JDBC API (DriverManager, Connection, Statement, ResultSet, etc.) |
| `javax.sql` | Extended JDBC API (DataSource, ConnectionPool, RowSet) |

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
- **Use Case**: Simple applications, desktop apps

### Three-Tier Architecture
```
┌─────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Client     │     │  Middle Tier    │     │  Database       │
│  (Browser/  │◄───►│  (App Server/   │◄───►│  (Data Source)  │
│   GUI)      │     │   Business Logic)     │                 │
└─────────────┘     └─────────────────┘     └─────────────────┘
```
- **Client**: Presentation layer (HTML, JavaFX, Swing)
- **Middle Tier**: Business logic, connection pooling, transaction management
- **Database**: Data storage
- **Use Case**: Enterprise applications, web apps

### JDBC Architecture Components
```
Java Application
       │
       ▼
┌──────────────────┐
│   JDBC API       │  (java.sql.* interfaces)
│  (DriverManager, │
│   Connection,    │
│   Statement,     │
│   ResultSet)     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  JDBC Driver     │  (Vendor-specific implementation)
│  (Type I-IV)     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Database        │  (MySQL, Oracle, PostgreSQL, etc.)
└──────────────────┘
```

---

## 15.3 JDBC Driver Types

### Type 1: JDBC-ODBC Bridge Driver
- **Mechanism**: JDBC → ODBC → Database
- **Pros**: Works with any ODBC-compliant database
- **Cons**: Requires ODBC driver; not portable; deprecated (removed in Java 8)
- **Example**: `sun.jdbc.odbc.JdbcOdbcDriver`

### Type 2: Native-API Driver
- **Mechanism**: JDBC → Native Client Library → Database
- **Pros**: Better performance than Type 1
- **Cons**: Requires native library on client; not fully portable
- **Example**: Oracle OCI Driver

### Type 3: Network Protocol Driver (Middleware)
- **Mechanism**: JDBC → Middleware Server → Database
- **Pros**: Pure Java; database-independent middleware; flexible
- **Cons**: Extra network hop; middleware complexity
- **Example**: IDS Server, DataDirect SequeLink

### Type 4: Thin Driver (Pure Java) - **RECOMMENDED**
- **Mechanism**: JDBC → Direct Database Protocol (TCP/IP)
- **Pros**: Pure Java; no client installation; best performance; portable
- **Cons**: Database-specific protocol
- **Examples**: 
  - MySQL: `com.mysql.cj.jdbc.Driver`
  - PostgreSQL: `org.postgresql.Driver`
  - Oracle: `oracle.jdbc.OracleDriver`
  - SQL Server: `com.microsoft.sqlserver.jdbc.SQLServerDriver`
  - H2: `org.h2.Driver`

### Driver Comparison

| Type | Portability | Performance | Installation | Use Case |
|------|-------------|-------------|--------------|----------|
| Type 1 | Low | Low | ODBC needed | Legacy only |
| Type 2 | Medium | Medium | Native lib | Legacy Oracle |
| Type 3 | High | Medium | Middleware | App servers |
| **Type 4** | **High** | **High** | **None** | **Modern apps** |

---

## 15.4 JDBC Connection Steps (6 Steps)

```java
// 1. Load Driver (Optional since JDBC 4.0 / Java 6 - auto-loaded via SPI)
Class.forName("com.mysql.cj.jdbc.Driver");

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

// 6. Close Resources (in reverse order)
rs.close();
stmt.close();
conn.close();
```

### Connection URL Formats
| Database | URL Format |
|----------|------------|
| **MySQL** | `jdbc:mysql://host:port/dbname?useSSL=false&serverTimezone=UTC` |
| **PostgreSQL** | `jdbc:postgresql://host:port/dbname` |
| **Oracle** | `jdbc:oracle:thin:@host:port:sid` |
| **SQL Server** | `jdbc:sqlserver://host:port;databaseName=dbname` |
| **H2** | `jdbc:h2:~/test` or `jdbc:h2:mem:test` |
| **Derby** | `jdbc:derby:dbname;create=true` |

---

## 15.5 DriverManager Class

### Purpose
Manages loaded JDBC drivers and establishes connections.

### Key Methods
```java
// Register driver (automatic in JDBC 4.0+)
DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());

// Get connection
Connection getConnection(String url)
Connection getConnection(String url, String user, String password)
Connection getConnection(String url, Properties info)

// Get driver info
Enumeration<Driver> getDrivers()
Driver getDriver(String url)
```

### Connection Properties (via Properties object)
```java
Properties props = new Properties();
props.setProperty("user", "root");
props.setProperty("password", "password");
props.setProperty("useSSL", "false");
props.setProperty("serverTimezone", "UTC");
props.setProperty("autoReconnect", "true");

Connection conn = DriverManager.getConnection(url, props);
```

---

## 15.6 Connection Interface

### Key Methods
```java
// Create statements
Statement createStatement()
PreparedStatement prepareStatement(String sql)
CallableStatement prepareCall(String sql)

// Transaction management
void setAutoCommit(boolean autoCommit)  // Default: true
void commit()
void rollback()
void rollback(Savepoint savepoint)
Savepoint setSavepoint()
void releaseSavepoint(Savepoint savepoint)

// Metadata
DatabaseMetaData getMetaData()

// Close
void close()
boolean isClosed()
```

### Auto-Commit Mode
```java
Connection conn = DriverManager.getConnection(url, user, pass);

// Default: autoCommit = true (each statement committed)
conn.setAutoCommit(false);  // Start transaction

try {
    stmt.executeUpdate("INSERT ...");
    stmt.executeUpdate("UPDATE ...");
    conn.commit();  // Commit transaction
} catch (SQLException e) {
    conn.rollback();  // Rollback on error
} finally {
    conn.setAutoCommit(true);  // Restore default
}
```

---

## 15.7 Statement Types

### 1. Statement (Static SQL)
```java
Statement stmt = conn.createStatement();

// Execute queries
ResultSet rs = stmt.executeQuery("SELECT * FROM students");

// Execute updates (INSERT, UPDATE, DELETE, DDL)
int rows = stmt.executeUpdate("INSERT INTO students(name) VALUES('John')");

// Execute any SQL (returns boolean)
boolean hasResults = stmt.execute("SELECT * FROM students");
```

### 2. PreparedStatement (Parameterized SQL) - **PREFERRED**
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

#### Advantages of PreparedStatement
| Advantage | Description |
|-----------|-------------|
| **Prevention of SQL Injection** | Parameters escaped automatically |
| **Performance** | SQL parsed/compiled once; reused |
| **Readability** | Clean separation of SQL and data |
| **Type Safety** | setXxx() methods enforce types |

#### Parameter Setter Methods
```java
pstmt.setString(1, "text");
pstmt.setInt(2, 42);
pstmt.setLong(3, 123L);
pstmt.setDouble(4, 3.14);
pstmt.setBoolean(5, true);
pstmt.setDate(6, java.sql.Date.valueOf("2024-01-15"));
pstmt.setTimestamp(7, java.sql.Timestamp.valueOf("2024-01-15 10:30:00"));
pstmt.setNull(8, Types.VARCHAR);
pstmt.setObject(9, someObject);
```

### 3. CallableStatement (Stored Procedures)
```java
// Stored procedure: CREATE PROCEDURE getStudentCount(OUT count INT)
String sql = "{call getStudentCount(?)}";
CallableStatement cstmt = conn.prepareCall(sql);

// Register OUT parameter
cstmt.registerOutParameter(1, Types.INTEGER);

// Execute
cstmt.execute();

// Get result
int count = cstmt.getInt(1);

// With IN/OUT parameters
// Procedure: CREATE PROCEDURE updateSalary(IN id INT, INOUT salary DECIMAL(10,2))
String sql2 = "{call updateSalary(?, ?)}";
CallableStatement cstmt2 = conn.prepareCall(sql2);
cstmt2.setInt(1, 101);
cstmt2.setDouble(2, 50000.0);
cstmt2.registerOutParameter(2, Types.DECIMAL);
cstmt2.execute();
double newSalary = cstmt2.getDouble(2);
```

---

## 15.8 Basic JDBC Program Example

### Complete CRUD Example
```java
import java.sql.*;

public class StudentCRUD {
    private static final String URL = "jdbc:mysql://localhost:3306/school";
    private static final String USER = "root";
    private static final String PASS = "password";
    
    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASS)) {
            
            // CREATE
            createStudent(conn, "Alice", 20, "alice@email.com");
            
            // READ
            readAllStudents(conn);
            
            // UPDATE
            updateStudent(conn, 1, "Alice Smith");
            
            // DELETE
            deleteStudent(conn, 2);
            
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    
    static void createStudent(Connection conn, String name, int age, String email) 
            throws SQLException {
        String sql = "INSERT INTO students(name, age, email) VALUES(?, ?, ?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setString(3, email);
            int rows = pstmt.executeUpdate();
            System.out.println(rows + " student(s) inserted.");
        }
    }
    
    static void readAllStudents(Connection conn) throws SQLException {
        String sql = "SELECT id, name, age, email FROM students";
        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            System.out.println("\n--- Students ---");
            while (rs.next()) {
                System.out.printf("ID: %d, Name: %s, Age: %d, Email: %s%n",
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getInt("age"),
                    rs.getString("email"));
            }
        }
    }
    
    static void updateStudent(Connection conn, int id, String newName) 
            throws SQLException {
        String sql = "UPDATE students SET name = ? WHERE id = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, newName);
            pstmt.setInt(2, id);
            int rows = pstmt.executeUpdate();
            System.out.println(rows + " student(s) updated.");
        }
    }
    
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

## 15.9 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. What is JDBC? Why is it used?
2. JDBC Architecture: 2-tier vs 3-tier.
3. Four types of JDBC drivers.
3. Why Type 4 driver is preferred?
4. Steps to connect to database using JDBC.
5. Difference between Statement, PreparedStatement, CallableStatement.
6. What is auto-commit? How to manage transactions?
7. What is DriverManager?
8. Connection URL for MySQL/PostgreSQL/Oracle.

**5-Mark Questions:**
1. Explain JDBC Architecture with diagram (2-tier and 3-tier).
2. Explain four types of JDBC drivers with comparison.
3. Explain database connection steps with example.
4. Explain PreparedStatement advantages with example.
5. Explain CallableStatement for stored procedures.
6. Write complete JDBC program for CRUD operations.

**10-Mark Questions:**
1. **JDBC Architecture (2/3 tier), Driver Types, Connection Steps, Statement types, Transaction Management.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Complete JDBC program with connection, CRUD, exception handling.

### Programs to Practice
1. ✅ **JDBC Connection + CRUD** - appeared 2021, 2022, 2023, 2024, 2025
2. ✅ **PreparedStatement demo** - appeared 2022, 2023, 2024, 2025
3. ✅ **Transaction management (commit/rollback)** - appeared 2023, 2024
4. ✅ **Driver types comparison table** - appeared 2022, 2023, 2024, 2025

---

## 15.10 Summary of Unit 15

| Topic | Key Points |
|-------|------------|
| **JDBC** | Java API for database connectivity; database-independent |
| **Architecture** | 2-tier (Client-Server) vs 3-tier (Client-Middle-DB) |
| **Driver Types** | Type 1: JDBC-ODBC; Type 2: Native-API; Type 3: Middleware; **Type 4: Pure Java (Best)** |
| **Connection Steps** | 1. Load Driver, 2. Get Connection, 3. Create Statement, 4. Execute, 5. Process, 6. Close |
| **DriverManager** | Manages drivers; getConnection() |
| **Connection** | createStatement, prepareStatement, prepareCall; commit, rollback, setAutoCommit |
| **Statement** | Static SQL; executeQuery, executeUpdate |
| **PreparedStatement** | Parameterized; prevents SQL injection; better performance |
| **CallableStatement** | Stored procedures; IN/OUT parameters |
| **Auto-commit** | Default true; set false for transactions |

---

## 15.11 Quick Reference: JDBC Template

```java
// 1. Connection
String url = "jdbc:mysql://localhost:3306/db?useSSL=false";
Connection conn = DriverManager.getConnection(url, "user", "pass");

// 2. PreparedStatement (Best Practice)
String sql = "SELECT * FROM users WHERE email = ?";
try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setString(1, "test@example.com");
    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
            // process
        }
    }
}

// 3. Transaction
conn.setAutoCommit(false);
try {
    // multiple updates
    conn.commit();
} catch (SQLException e) {
    conn.rollback();
} finally {
    conn.setAutoCommit(true);
}

// 4. Close (try-with-resources handles this)
```