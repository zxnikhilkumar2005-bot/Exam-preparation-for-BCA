# Important Questions for MCS-206 (Object Oriented Programming using Java)

## Based on PYQ Analysis (Dec 2021 - June 2026)

---

## 📋 EXAM PATTERN RECAP
- **Duration**: 3 Hours | **Max Marks**: 100
- **Q1**: Compulsory (8 sub-questions × 5 marks = 40 marks)
- **Q2-Q5**: Attempt any 3 (each 20 marks)
- **Short Notes**: 4×5=20 marks (appears frequently in Q5)

---

## 🔴 CRITICAL PRIORITY (90%+ Probability) - MASTER THESE COMPLETELY

### 1. INHERITANCE (9/10 years)
**Subtopics:**
- Concept, advantages, types (Single, Multilevel, Hierarchical)
- `super` keyword (constructor call, method access, variable access)
- Method overriding rules and example
- Constructor execution order in multilevel hierarchy
- `final` keyword in inheritance (variable, method, class)
- Why multiple inheritance not supported; interface solution

**Expected Questions:**
- 10 marks: "What is inheritance? Explain types with code. Explain advantages and `super` keyword."
- 5 marks: "Explain `super` keyword with examples."
- 5 marks: "Method overriding with program."

### 2. POLYMORPHISM & ABSTRACT CLASS vs INTERFACE (8/10 years)
**Subtopics:**
- Static vs Dynamic binding (Overloading vs Overriding)
- Method overloading (3 ways) with program
- Method overriding rules with program
- Abstract class: concept, advantages, why not instantiated
- Interface: definition, implementation, default/static methods (Java 8+)
- **Abstract Class vs Interface** - Detailed comparison table
- When to use which

**Expected Questions:**
- 10 marks: "What is polymorphism? Explain static vs dynamic binding. Explain abstract class advantages and difference from interface."
- 5 marks: "Difference between abstract class and interface with examples."
- 5 marks: "Method overloading vs overriding."

### 3. EXCEPTION HANDLING (9/10 years)
**Subtopics:**
- Exception hierarchy (Throwable → Error/Exception → RuntimeException)
- Checked vs Unchecked exceptions
- try-catch-finally with multiple catch blocks
- `throw` vs `throws`
- Custom/User-defined exceptions
- `final` vs `finally` vs `finalize`
- Assertions (enable/disable, vs exceptions)

**Expected Questions:**
- 10 marks: "Explain exception handling mechanism. Checked vs unchecked. Custom exception with program."
- 5 marks: "`throw` vs `throws` with example."
- 5 marks: "`final` vs `finally` vs `finalize`."
- 5 marks: "Assertions: enable/disable and use cases."

### 4. MULTITHREADING (9/10 years)
**Subtopics:**
- Thread creation (Thread class + Runnable interface) - Runnable preferred
- Thread life cycle with diagram (NEW, RUNNABLE, RUNNING, BLOCKED, WAITING, TERMINATED)
- Thread synchronization (`synchronized` method/block)
- Inter-thread communication (`wait`, `notify`, `notifyAll`)
- Thread priority, `isAlive()`, `join()`
- Producer-Consumer problem
- Thread issues: deadlock, race condition, starvation + solutions

**Expected Questions:**
- 10 marks: "What is multithreading? Thread creation methods. Synchronization with program."
- 10 marks: "Thread life cycle with diagram. Inter-thread communication."
- 5 marks: "`isAlive()` and `join()` methods."
- 5 marks: "Thread synchronization with example."

### 5. JDBC (8/10 years)
**Subtopics:**
- **JDBC Architecture**: 2-tier vs 3-tier with diagrams
- **4 Driver Types** (Type 1-4) with comparison; Type 4 recommended
- **Connection Steps** (6 steps) with code
- **Statement Types**: Statement, PreparedStatement, CallableStatement
- **Transactions**: ACID, commit/rollback, savepoints, isolation levels
- **Concurrency Problems**: Dirty read, Non-repeatable read, Phantom read
- **Batch Processing**: `addBatch`, `executeBatch`
- **ResultSet**: Types, Concurrency, Navigation, Updatable
- **RowSet**: JdbcRowSet vs CachedRowSet

**Expected Questions:**
- 10 marks: "JDBC Architecture (2/3 tier). Driver types. Connection steps with code."
- 10 marks: "JDBC Transactions: ACID, isolation levels, savepoints. Concurrency problems."
- 10 marks: "ResultSet types, concurrency, navigation. Batch processing."
- 5 marks: "PreparedStatement vs Statement."
- 5 marks: "CallableStatement for stored procedures."

### 6. ENCAPSULATION (7/10 years)
**Subtopics:**
- Concept: private fields + public getters/setters
- Access modifiers (private, default, protected, public) with table
- Implementation with program
- Benefits: data hiding, validation, flexibility

**Expected Questions:**
- 5 marks: "Explain encapsulation with program."
- 5 marks: "Access specifiers with table."

### 7. CONSTRUCTOR (7/10 years)
**Subtopics:**
- Default vs Parameterized constructor
- Constructor overloading
- Constructor chaining (`this()`, `super()`)
- Execution order in inheritance

**Expected Questions:**
- 5 marks: "Constructor types with example."
- 5 marks: "Constructor overloading and chaining."

### 8. FINAL/FINALLY/FINALIZE (7/10 years)
**Subtopics:**
- `final` variable, method, class
- `finally` block (always executes)
- `finalize()` method (GC, deprecated)
- Clear differentiation with examples

**Expected Questions:**
- 5 marks: "Differentiate final, finally, finalize with examples."

### 9. BYTE STREAM vs CHARACTER STREAM (7/10 years)
**Subtopics:**
- Byte streams: InputStream/OutputStream hierarchy
- Character streams: Reader/Writer hierarchy
- When to use which
- Buffered streams for performance
- FileInputStream/FileOutputStream vs FileReader/FileWriter

**Expected Questions:**
- 5 marks: "Byte Stream vs Character Stream with hierarchy."
- 10 marks: "Stream classes hierarchy. Byte vs Character streams with examples."

### 10. JAVA FX / AWT / SWING (7/10 years)
**Subtopics:**
- AWT vs Swing vs JavaFX comparison table
- JavaFX: Architecture (Stage, Scene, Scene Graph), Features
- JavaFX Layouts: VBox, HBox, BorderPane, GridPane, FlowPane, StackPane
- JavaFX Controls: Label, Button, TextField, ComboBox, TableView, DatePicker
- Event Handling: Lambda, EventHandler, FXML Controller
- CSS Styling in JavaFX (`-fx-` prefix)
- FXML: Structure, `fx:id`, `fx:controller`, `onAction`
- Effects: DropShadow, Glow, Reflection
- Animation: Timeline, Transitions (Translate, Rotate, Scale, Fade)
- Media: MediaPlayer, MediaView

**Expected Questions:**
- 5 marks: "AWT vs Swing vs JavaFX."
- 10 marks: "JavaFX features, components, layouts, event handling, CSS/FXML."
- 5 marks: "JavaFX event handling with lambda."
- 5 marks: "CSS styling in JavaFX."

---

## 🟡 HIGH PRIORITY (60-80% Probability) - SHOULD KNOW

### 11. PACKAGES (6/10 years)
- Built-in vs User-defined packages
- Package creation, compilation (`javac -d .`), execution
- Import statements (specific vs `*`)
- Access rules in packages
- CLASSPATH

### 12. COLLECTIONS FRAMEWORK (4-6/10 years)
- Collection hierarchy (Collection → List/Set/Queue → implementations)
- **List**: ArrayList, LinkedList, Vector - differences
- **Set**: HashSet, LinkedHashSet, TreeSet - differences
- **Map**: HashMap, LinkedHashMap, TreeMap, Hashtable - differences
- Iterator vs ListIterator
- Date class (after, before, compareTo, getTime)
- Stack (push, pop, peek, search)

### 13. OBJECT SERIALIZATION (5/10 years)
- Serializable interface, serialVersionUID
- ObjectOutputStream/ObjectInputStream
- `transient` and `static` fields
- Externalizable interface
- Serialization steps with program

### 14. FILE CLASS (4/10 years)
- File creation, deletion, listing, mkdir
- File methods: getName, getPath, getAbsolutePath, exists, canRead, canWrite, isFile, isDirectory, length, list, listFiles, mkdir, mkdirs, createNewFile, delete, renameTo

### 15. GARBAGE COLLECTION (5/10 years)
- Concept, eligibility, finalize()
- GC algorithms (brief), System.gc()
- Advantages/disadvantages

### 16. ASSERTIONS (4/10 years)
- Syntax: `assert condition;`, `assert condition : message;`
- Enable: `-ea`, Disable: `-da`
- Where to use/not use
- Assertions vs Exception Handling

### 17. ANNOTATIONS (2/10 years)
- Built-in: @Override, @SuppressWarnings, @Deprecated, @FunctionalInterface
- Meta-annotations: @Target, @Retention, @Inherited, @Documented, @Repeatable
- Custom annotations

### 18. STRING HANDLING (4/10 years)
- String immutability, String Constant Pool
- Important methods: length, charAt, substring, concat, equals, equalsIgnoreCase, compareTo, indexOf, lastIndexOf, replace, toUpperCase, toLowerCase, trim, split, valueOf
- StringBuilder vs StringBuffer vs String
- Autoboxing/Unboxing

### 19. NUMBER/CHARACTER CLASSES
- Wrapper classes, Number class methods (parseInt, valueOf, toString)
- Character class methods (isLetter, isDigit, toUpperCase, compareTo)
- Formatting with printf/format (%d, %f, %s, flags, width, precision)

---

## 🟢 MEDIUM PRIORITY (30-50% Probability) - NICE TO KNOW

### 20. DECISION/LOOP CONSTRUCTS (3/10 years)
- if, if-else, switch-case
- while, do-while, for (including enhanced for)
- break, continue
- Arrays (1D, 2D, matrix programs)

### 21. RELATIONAL/LOGICAL OPERATORS (3/10 years)
- <, >, <=, >=, ==, !=
- &&, ||, !, &, |, ^
- Bitwise operators

### 22. STATIC/DEFAULT METHODS IN INTERFACE (2/10 years)
- Default methods (Java 8+)
- Static methods in interface
- Multiple interface default method conflict resolution

### 23. MULTIPLE INHERITANCE VIA INTERFACE (2/10 years)
- Interface extending interface
- Class implementing multiple interfaces

### 24. AUTOCLOSEABLE/CLOSEABLE/FLUSHABLE (2/10 years)
- try-with-resources (Java 7+)

### 25. CALLABLESTATEMENT / PREPAREDSTATEMENT (2/10 years)
- Stored procedures with IN/OUT parameters

### 26. JAVA FX ADVANCED (CSS, FXML, Animation, Media) (1-2/10 years)
- CSS pseudo-classes
- FXML with Scene Builder
- ParallelTransition, SequentialTransition
- MediaPlayer, MediaView

---

## 📝 2-MARK QUESTIONS (Very Short Answers)

### Most Frequently Asked Differentiations:
1. `throw` vs `throws`
2. `final` vs `finally` vs `finalize`
3. Overloading vs Overriding
4. Abstract class vs Interface
5. AWT vs Swing vs JavaFX
6. ByteStream vs CharacterStream
7. Checked vs Unchecked Exception
8. Thread class vs Runnable interface
9. HashSet vs TreeSet
10. HashMap vs Hashtable
11. Vector vs ArrayList
12. 2-tier vs 3-tier JDBC
13. ResultSet vs RowSet
14. Statement vs PreparedStatement vs CallableStatement
15. Multiple vs Multilevel Inheritance
16. String vs StringBuffer
17. Private vs Protected vs Default vs Public
18. Process vs Thread
19. Final vs Abstract
20. Serializable vs Externalizable

---

## 📝 5-MARK QUESTIONS (Short Answers)

### Theory + Code:
1. **Encapsulation** with getter/setter program
2. **Constructor** types with example
3. **`super` keyword** uses (3 uses) with examples
4. **`final` keyword** (variable, method, class) with examples
5. **`static` keyword** (variable, method, block) with examples
6. **Access Specifiers** with table and example
7. **Method Overloading** with program (3 ways)
8. **Method Overriding** with program
9. **Abstract Class** with example + why not instantiated
10. **Interface** with example
11. **Thread Creation** (Thread class & Runnable) with program
12. **Thread Life Cycle** with Diagram
13. **`isAlive()` and `join()`** methods with program
14. **Thread Synchronization** with program
15. **Exception Hierarchy** with diagram
16. **try-catch-finally** with example
17. **`throws` clause** with example
18. **Custom Exception** creation with program
19. **Package** creation + accessibility rules
20. **JDBC Driver Types** (I-IV) with comparison
21. **JDBC Connection Steps** with code
22. **ResultSet Types** with navigation methods
23. **Byte Stream vs Character Stream** with hierarchy
24. **Object Serialization** steps with program
25. **Garbage Collection** + finalize()
26. **Assertions** enable/disable
27. **Annotations** (@Override, @SuppressWarnings, @Deprecated)
28. **Date Class** (after, before, compareTo)
29. **HashSet/TreeSet/HashMap** with methods
30. **Decision Constructs** (if-else, switch) with programs
31. **PreparedStatement** with example
32. **HashSet/HashMap** role
33. **Assertion Statement** syntax and use
34. **CallableStatement** with example
35. **Flushable Interface** with example
36. **Thread Life Cycle** short note
37. **Dynamic Binding** short note
38. **Polymorphism** short note
39. **Java Interface** short note
40. **User-Defined Exceptions** short note
41. **JavaFX Features** short note

---

## 📝 10-MARK QUESTIONS (Long Answers - Theory + Code)

### Must-Prepare Topics:
1. **Inheritance**: Concept, types, advantages, `super` keyword, constructor chaining
2. **Polymorphism**: Static vs Dynamic binding, Overloading vs Overriding, Abstract class vs Interface
3. **Abstract Class vs Interface**: Differences, advantages, when to use which, examples
4. **Exception Handling**: Hierarchy, checked/unchecked, try-catch-finally, throw/throws, custom exceptions
5. **Multithreading**: Creation, life cycle (diagram), synchronization, inter-thread communication, deadlock
6. **JDBC**: Architecture (2/3 tier diagrams), Driver types, Connection steps, Statement types, Transactions (ACID, isolation, savepoints)
7. **JDBC Transactions**: ACID, commit/rollback, isolation levels, dirty/non-repeatable/phantom reads
8. **Streams**: Byte vs Character hierarchy, File I/O, Buffered streams, Serialization
9. **Collections**: Hierarchy, HashSet/TreeSet/HashMap/Vector - any two with methods
10. **GUI**: AWT vs Swing vs JavaFX, Event handling in JavaFX, Layouts
11. **Serialization**: Steps, transient, serialVersionUID, Externalizable
12. **Package**: Creation, import, access rules, user-defined package demo
13. **File Class**: Methods, file operations program
14. **Thread Issues**: Deadlock, race condition, starvation + solutions
15. **Batch Processing**: addBatch, executeBatch with PreparedStatement
16. **ResultSet**: Scrollable/Updatable, navigation, updatable methods
17. **RowSet**: JdbcRowSet vs CachedRowSet

---

## 🎯 PROGRAMS TO PRACTICE (High Yield - Appeared Multiple Times)

### Unit 1-4 (Basics & OOP)
1. ✅ **Encapsulation** with getter/setter
2. ✅ **Constructor overloading** (default + parameterized)
3. ✅ **Constructor chaining** with `this()` and `super()`
4. ✅ **Inheritance demo** (Vehicle → Car/Truck)
5. ✅ **Method overloading** (3+ methods same name)
6. ✅ **Method overriding** (Figure → Rectangle/Triangle)
7. ✅ **Abstract class** (Bank → SBI/PNB)
8. ✅ **Interface** (Area → Rectangle/Circle)

### Unit 5-8 (Inheritance, Polymorphism, Exceptions, Packages)
9. ✅ **Exception handling** (ArrayIndexOutOfBounds + multiple catch + finally)
10. ✅ **Custom exception** (InsufficientFunds, InvalidInput)
11. ✅ **throw vs throws** demonstration
12. ✅ **Package creation** (compile/run with `javac -d .`)
13. ✅ **Thread creation** (Thread class + Runnable)
12. ✅ **Thread priority** + `isAlive()`
13. ✅ **Synchronization** (Producer-Consumer or Counter)
14. ✅ **Inter-thread communication** (wait/notify)
15. ✅ **File operations** (create, read, write, delete)

### Unit 9-12 (Multithreading, I/O, Collections)
16. ✅ **Matrix Addition (3×3)**
17. ✅ **String Reverse + Length**
18. ✅ **Palindrome check** (StringBuilder)
19. ✅ **Date comparison** (after, before, compareTo)
20. ✅ **HashSet/TreeSet/HashMap** demo
21. ✅ **Vector vs Stack** demo
22. ✅ **Serialization/Deserialization**
23. ✅ **Autoboxing/Unboxing** demo

### Unit 13-16 (GUI & JDBC)
24. ✅ **JDBC Connection + CRUD** (MySQL/PostgreSQL)
25. ✅ **PreparedStatement** for INSERT/SELECT
26. ✅ **Transaction** with commit/rollback
27. ✅ **Batch processing** with PreparedStatement
28. ✅ **CallableStatement** for stored procedure
29. ✅ **Scrollable ResultSet** navigation
30. ✅ **Updatable ResultSet** (update/insert/delete row)
31. ✅ **Savepoint** in transaction
32. ✅ **CachedRowSet** offline editing
33. ✅ **JavaFX Hello World** (Stage, Scene, Label, Button)
34. ✅ **Event handling** (Button click → Label update)
35. ✅ **Layouts** (VBox, HBox, BorderPane, GridPane)
36. ✅ **Name/Email form** (GridPane)
37. ✅ **CSS styling** in JavaFX
38. ✅ **FXML login** with controller
39. ✅ **Effects** (DropShadow, Glow, Reflection)
40. ✅ **Animation** (TranslateTransition, FadeTransition)
41. ✅ **MediaPlayer** (audio/video)

---

## 📌 LAST MINUTE REVISION CHECKLIST

### Morning of Exam:
- [ ] All 4 differentiation tables (2-mark questions)
- [ ] Thread life cycle diagram
- [ ] JDBC 2-tier/3-tier diagrams
- [ ] Exception hierarchy diagram
- [ ] Collection framework hierarchy
- [ ] 6 JDBC connection steps
- [ ] 4 isolation levels table
- [ ] ACID properties
- [ ] AWT vs Swing vs JavaFX table
- [ ] Abstract class vs Interface table
- [ ] Overloading vs Overriding table
- [ ] final/finally/finalize table
- [ ] throw/throws table
- [ ] Package compilation commands
- [ ] StringBuilder vs StringBuffer vs String
- [ ] JavaFX CSS `-fx-` prefix
- [ ] FXML key attributes
- [ ] Transaction template with savepoint

### Formulas/Patterns to Memorize:
```
JDBC URL: jdbc:mysql://host:port/db?params
Connection: DriverManager.getConnection(url, user, pass)
PreparedStatement: conn.prepareStatement(sql)
Batch: pstmt.addBatch(); pstmt.executeBatch()
Transaction: setAutoCommit(false); commit(); rollback();
Savepoint: conn.setSavepoint(); conn.rollback(sp);
ResultSet types: TYPE_FORWARD_ONLY, SCROLL_INSENSITIVE, SCROLL_SENSITIVE
Concurrency: CONCUR_READ_ONLY, CONCUR_UPDATABLE
CSS: -fx-property: value;
FXML: fx:id, fx:controller, onAction="#method"
```

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Calling `run()` instead of `start()`** for threads
2. **Forgetting `conn.setAutoCommit(false)`** for transactions
3. **Not closing resources** (use try-with-resources)
4. **Wrong catch order** (subclass before superclass)
4. **Using `==` for String comparison** instead of `.equals()`
5. **Not handling `SQLException`** in JDBC
6. **Forgetting `Class.forName()`** for old drivers (JDBC 3.0)
7. **Confusing `wait()` (Object) with `sleep()` (Thread)**
8. **Using `Vector` instead of `ArrayList`** unless thread-safe needed
9. **Not overriding `equals()` and `hashCode()`** for custom objects in Sets/Maps
10. **Forgetting `serialVersionUID`** in Serializable classes
11. **Using `stop()`, `suspend()`, `resume()`** (deprecated)
12. **Wrong isolation level constants** (use `Connection.TRANSACTION_*`)

---

## 📚 QUICK REFERENCE: UNIT-WISE WEIGHTAGE

| Unit | Topic | Marks Weightage | Questions Type |
|------|-------|-----------------|----------------|
| 1 | Introduction to Java | 5-10 | 2, 5 |
| 2 | Basics of Java | 5-10 | 2, 5 |
| 3 | Decision & Loop | 5-10 | 2, 5, Program |
| 4 | Classes & Objects | 10-15 | 2, 5, 10, Program |
| 5 | Inheritance | 10-20 | 2, 5, 10, Program |
| 6 | Polymorphism | 10-20 | 2, 5, 10, Program |
| 7 | Exceptions | 10-20 | 2, 5, 10, Program |
| 8 | Packages & Interfaces | 5-15 | 2, 5, 10, Program |
| 9 | Multithreading | 15-20 | 2, 5, 10, Program |
| 10 | String/Number/Char | 5-10 | 2, 5, Program |
| 11 | I/O Streams | 10-15 | 2, 5, 10, Program |
| 12 | Collections | 5-15 | 2, 5, 10, Program |
| 13 | GUI (AWT/Swing/JavaFX) | 10-20 | 2, 5, 10, Program |
| 14 | UI Controls (CSS/FXML) | 5-15 | 2, 5, 10, Program |
| 15 | JDBC Part 1 | 15-20 | 2, 5, 10, Program |
| 16 | JDBC Part 2 | 15-20 | 2, 5, 10, Program |

**Total: 100 marks across Q1 (40) + Q2-Q5 (60)**

---

## 🎯 FINAL TIPS

1. **Draw diagrams** for: Thread Life Cycle, JDBC Architecture, Exception Hierarchy, Collection Hierarchy
2. **Write comparison tables** for all "Difference between" questions
3. **Include code snippets** in 10-mark answers
4. **Mention key interfaces/classes** by name (e.g., `Runnable`, `PreparedStatement`, `Serializable`)
5. **Don't skip short notes** - they're easy 5-markers
6. **Practice matrix programs** (3×3 addition, multiplication)
7. **Know exact syntax** for: FXML attributes, CSS properties, JDBC URLs
8. **Time management**: Q1 (40 min), Q2-Q5 (40 min each), Review (20 min)

---

**BEST OF LUCK FOR YOUR EXAM!** 🍀

*Prepared based on 10 years PYQ Analysis (Dec 2021 - June 2026)*