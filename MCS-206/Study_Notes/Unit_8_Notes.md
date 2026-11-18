# Unit 8: Packages and Interfaces

## Unit Overview
This unit covers packages (built-in and user-defined), access rules in packages, CLASSPATH, creating and importing packages, and interfaces (definition, implementation, extension, default/static methods, multiple interface issues, abstract class vs interface comparison).

## PYQ Priority (Based on 10 Years Analysis: Dec 2021 - June 2026)
| Topic | Frequency | Priority | Years Appeared | Typical Marks |
|-------|-----------|----------|----------------|---------------|
| Package (creation, import, accessibility rules) | 6/10 | **HIGH** | 2021, 2022, 2023, 2024×2, 2025 | 5-8 |
| Interface (declaration, implementation, extension) | 5/10 | **HIGH** | 2022, 2023, 2024, 2025, 2026 | 5-10 |
| Types of packages (built-in, user-defined) | 1/10 | **MEDIUM** | 2024 | 8 |
| Static & Default methods in interface | 2/10 | **MEDIUM** | 2023, 2026 | 5 |
| Package access protection | 1/10 | **LOW** | 2022 | 7 |
| **Abstract Class vs Interface** (cross-unit) | 8/10 | **CRITICAL** | 2021, 2022, 2023×2, 2024, 2025×2 | 5-10 |

**Key Exam Questions from PYQ:**
- 2021 Q1(e): User-defined Package creation (6m) - Theory+Code
- 2022 Q1(d): Package accessibility rules (7m) - Theory
- 2023 Q1(g): Class vs Interface (5m) - Differentiate
- 2023 Q1(g): Static vs Default methods in interface (5m) - Differentiate
- 2024 Q1(f): Package creation + types (8m) - Theory
- 2025 Q1(d): Package + accessibility rules (5m) - Theory
- 2025 Q1(e): Access specifiers (5m) - Theory
- 2026 Q1(h): Static methods in interface + multiple interface issues (5m) - Theory
- 2024 Q5(c): Java Interface short note (5m)

---

## 8.1 Packages

### Topic Introduction
A package is a namespace that organizes related classes and interfaces. It prevents naming conflicts and provides access control.

### Definition
> A **package** is a collection of related classes, interfaces, and sub-packages. It acts like a folder in a file system.

### Types of Packages

| Type | Description | Examples |
|------|-------------|----------|
| **Built-in** | Provided by Java API | `java.lang`, `java.util`, `java.io`, `java.sql` |
| **User-defined** | Created by programmer | `com.company.project.module` |

### Difference: Built-in vs User-defined Packages

| Aspect | Built-in Packages | User-defined Packages |
|--------|-------------------|----------------------|
| **Origin** | Provided by Java API / JDK | Created by programmer |
| **Naming Convention** | `java.*`, `javax.*`, `javafx.*` | Reverse domain name (e.g., `com.company.project`) |
| **Location** | JDK installation (`jre/lib/rt.jar`) | Custom directory structure (`-d` option) |
| **Availability** | Always available, auto-imported for `java.lang` | Must be compiled and added to CLASSPATH |
| **Purpose** | Core functionality (I/O, Collections, Networking, GUI, DB) | Organize project-specific code |
| **Modification** | Cannot be modified | Fully controllable by developer |

**Key Point:** `java.lang` is the only package implicitly imported. All other built-in packages require explicit import.

### Common Built-in Packages

| Package | Purpose |
|---------|---------|
| `java.lang` | Fundamental classes (Object, String, Math, wrapper classes) - **auto-imported** |
| `java.util` | Utility classes (Collections, Date, Scanner, Random) |
| `java.io` | Input/Output classes (File, Streams, Reader/Writer) |
| `java.sql` | JDBC database connectivity |
| `java.net` | Networking (Socket, URL, InetAddress) |
| `java.awt` | Abstract Window Toolkit (GUI) |
| `javax.swing` | Swing GUI components |
| `javafx.*` | JavaFX GUI components |

---

## 8.2 Access Rules in Packages

### Package-Level Access Control

| Modifier | Same Class | Same Package | Subclass (diff pkg) | Non-subclass (diff pkg) |
|----------|------------|--------------|---------------------|-------------------------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

### Class-Level Access

| Modifier | Same Package | Different Package |
|----------|--------------|-------------------|
| `default` (no modifier) | ✅ | ❌ |
| `public` | ✅ | ✅ |

### Detailed Access Rules with Examples

**1. Private:** Only within same class
```java
class A {
    private int x = 10;
    void show() { System.out.println(x); }  // OK
}
class B {
    void test() { 
        A a = new A();
        // System.out.println(a.x);  // ERROR
    }
}
```

**2. Default (Package-Private):** Same package only
```java
// pack1/A.java
package pack1;
class A {  // default class
    void show() { System.out.println("A"); }  // default method
}

// pack1/B.java
package pack1;
class B { void test() { new A().show(); } }  // OK: same package

// pack2/C.java
package pack2;
import pack1.A;
class C { void test() { new A().show(); } }  // ERROR: different package
```

**3. Protected:** Same package + subclasses (even in different package)
```java
// pack1/Parent.java
package pack1;
public class Parent {
    protected void protectedMethod() { System.out.println("Parent"); }
    protected int protectedVar = 100;
}

// pack2/Child.java
package pack2;
import pack1.Parent;

class Child extends Parent {
    void test() {
        protectedMethod();       // OK: subclass
        System.out.println(protectedVar);  // OK: subclass
        
        Parent p = new Parent();
        // p.protectedMethod();  // ERROR: not through subclass reference
        // System.out.println(p.protectedVar);  // ERROR
    }
}

class Other {
    void test() {
        Parent p = new Parent();
        // p.protectedMethod();  // ERROR: not a subclass
    }
}
```

**Key Protected Rule:** A subclass in a different package can only access protected members **through inheritance** (using `this` or `super`), NOT through a parent class reference.

### Access Rules Summary for Exam (PYQ 2022 Q1d - 7 marks)

| Scenario | private | default | protected | public |
|----------|---------|---------|-----------|--------|
| Same class | ✅ | ✅ | ✅ | ✅ |
| Same package, different class | ❌ | ✅ | ✅ | ✅ |
| Subclass in different package | ❌ | ❌ | ✅* | ✅ |
| Non-subclass in different package | ❌ | ❌ | ❌ | ✅ |

*\*protected: Only through inheritance (this/super), not via parent reference*

### Non-Access Modifiers with Packages

| Modifier | Class | Method | Variable | Notes |
|----------|-------|--------|----------|-------|
| `final` | Cannot extend | Cannot override | Constant | Class: no subclass; Method: no override; Variable: init once |
| `abstract` | Cannot instantiate | No body | N/A | Abstract class can have non-abstract methods |
| `static` | Nested class only | Class method | Class variable | Belongs to class, not instance |
| `strictfp` | Class/Method | Method | N/A | Strict floating-point precision |

### Example: Protected Across Packages
```java
// pack1/Parent.java
package pack1;

public class Parent {
    protected void protectedMethod() {
        System.out.println("Protected method");
    }
}

// pack2/Child.java
package pack2;
import pack1.Parent;

class Child extends Parent {
    void test() {
        protectedMethod();  // OK: subclass in different package
    }
}

class Other {
    void test() {
        Parent p = new Parent();
        // p.protectedMethod();  // ERROR: not a subclass
    }
}
```

---

## 8.3 CLASSPATH

### Definition
`CLASSPATH` is an environment variable that tells the Java compiler and runtime where to find `.class` files.

### Setting CLASSPATH

**Windows:**
```cmd
set CLASSPATH=.;C:\javaclasses;C:\libs\mylib.jar
```

**Linux/Mac:**
```bash
export CLASSPATH=.:/home/user/javaclasses:/home/user/libs/mylib.jar
```

### Key Points
- `.` (dot) = current directory
- Separator: `;` (Windows), `:` (Linux/Mac)
- Can include JAR files
- `-cp` or `-classpath` command-line option overrides environment variable

### Using `-cp` / `-classpath` Option (Exam Important)

**Compile with custom output directory:**
```cmd
javac -d C:\classes mypack\Student.java
```

**Run from any directory using -cp:**
```cmd
# From any directory
java -cp C:\classes mypack.Student

# Multiple paths (Windows)
java -cp C:\classes;C:\libs\mylib.jar mypack.Student

# Multiple paths (Linux/Mac)
java -cp /home/user/classes:/home/user/libs/mylib.jar mypack.Student
```

**Compile with external JAR in classpath:**
```cmd
javac -cp ".;C:\libs\gson.jar" mypack\Student.java
```

### Complete Compilation & Execution Workflow (PYQ 2021 Q1e - 6 marks)

**Step 1:** Create directory structure matching package name
```
C:\javaclasses\mypack\Student.java
```

**Step 2:** Write source file with `package` statement as FIRST line
```java
package mypack;
public class Student { ... }
```

**Step 3:** Compile from PARENT directory using `-d .`
```cmd
cd C:\javaclasses
javac -d . mypack\Student.java
# Creates: C:\javaclasses\mypack\Student.class
```

**Step 4:** Run from PARENT directory using fully qualified name
```cmd
cd C:\javaclasses
java mypack.Student
```

**Alternative (using -cp from anywhere):**
```cmd
# From anywhere
java -cp C:\javaclasses mypack.Student
```

### Package Directory Structure
```
javaclasses/
├── com/
│   └── company/
│       └── project/
│           ├── MyClass.class
│           └── utils/
│               └── Helper.class
```

---

## 8.4 Creating User-Defined Packages

### Steps

1. **Create directory structure** matching package name
2. **Add package statement** as first line in source file
3. **Compile** with `-d` option
4. **Run** with fully qualified name

### Example

**Directory Structure:**
```
C:\javaclasses\
    └── mypack\
        └── Student.java
```

**Student.java:**
```java
package mypack;

public class Student {
    String name;
    int rollNo;
    
    public Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }
    
    public void display() {
        System.out.println("Name: " + name + ", Roll: " + rollNo);
    }
}
```

### Compilation
```cmd
cd C:\javaclasses
javac -d . mypack\Student.java
```
Creates: `C:\javaclasses\mypack\Student.class`

### Execution
```cmd
cd C:\javaclasses
java mypack.Student
```

### Sub-packages
```java
package mypack.subpack;  // Package: mypack.subpack
```

```cmd
javac -d . mypack\subpack\MyClass.java
java mypack.subpack.MyClass
```

### Complete Package Program (Exam-Ready - PYQ 2021 Q1e, 2024 Q1f)

**File: `C:\javaclasses\mypack\Student.java`**
```java
package mypack;

public class Student {
    // Default (package-private) access
    String name;
    int rollNo;
    
    // Public constructor
    public Student(String name, int rollNo) {
        this.name = name;
        this.rollNo = rollNo;
    }
    
    // Public method
    public void display() {
        System.out.println("Student Details:");
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
    }
    
    // Protected method (accessible in subclass in different package)
    protected void protectedMethod() {
        System.out.println("Protected method in Student");
    }
}
```

**File: `C:\javaclasses\mypack\subpack\GraduateStudent.java`**
```java
package mypack.subpack;

import mypack.Student;  // Import parent package class

public class GraduateStudent extends Student {
    String researchTopic;
    
    public GraduateStudent(String name, int rollNo, String researchTopic) {
        super(name, rollNo);  // Call parent constructor
        this.researchTopic = researchTopic;
    }
    
    @Override
    public void display() {
        super.display();  // Call parent method
        System.out.println("Research Topic: " + researchTopic);
    }
    
    public void testProtected() {
        protectedMethod();  // OK: subclass in different package
    }
}
```

**File: `C:\javaclasses\testpack\TestPackage.java`**
```java
package testpack;

import mypack.Student;
import mypack.subpack.GraduateStudent;

public class TestPackage {
    public static void main(String[] args) {
        Student s = new Student("Alice", 101);
        s.display();
        
        System.out.println();
        
        GraduateStudent gs = new GraduateStudent("Bob", 202, "AI");
        gs.display();
        gs.testProtected();  // Calls protected method from subclass
    }
}
```

### Compilation & Execution Steps (Memorize for Exam)

```cmd
# 1. Go to root directory (parent of package structure)
cd C:\javaclasses

# 2. Compile ALL files from root (creates proper directory structure)
javac -d . mypack\Student.java mypack\subpack\GraduateStudent.java testpack\TestPackage.java

# 3. Run from root using fully qualified class name
java testpack.TestPackage
```

**Expected Output:**
```
Student Details:
Name: Alice
Roll No: 101

Student Details:
Name: Bob
Roll No: 202
Research Topic: AI
Protected method in Student
```

### Common Exam Mistakes to Avoid
| Mistake | Correct Approach |
|---------|-----------------|
| `javac mypack\Student.java` (no -d) | Use `javac -d . mypack\Student.java` |
| Running from inside package folder | Run from PARENT of package root: `java mypack.Student` |
| Forgetting package statement as FIRST line | `package mypack;` must be line 1 |
| Using `java Student` instead of `java mypack.Student` | Always use fully qualified name |
| Importing `mypack.*` and expecting subpackages | Subpackages NOT imported automatically; need `import mypack.subpack.*` |

---

## 8.5 Importing Packages

### Import Statements
```java
// Import specific class
import java.util.ArrayList;
import java.util.Date;

// Import entire package (all classes)
import java.util.*;

// Import static members (Java 5+)
import static java.lang.Math.PI;
import static java.lang.Math.sqrt;
```

### Rules
- Written **after** package statement, **before** class declaration
- Multiple import statements allowed
- `java.lang` is **implicitly imported**
- Fully qualified name can be used without import

### Example
```java
package myapp;

import mypack.Student;          // Specific class
import java.util.*;             // Entire package
import static java.lang.Math.*; // Static imports

public class Test {
    public static void main(String[] args) {
        Student s = new Student("Alice", 101);  // Without mypack.
        ArrayList<String> list = new ArrayList<>();  // Without java.util.
        double area = PI * 5 * 5;  // Without Math.
    }
}
```

---

## 8.6 Interfaces

### Definition
> An **interface** is a reference type that defines a contract of abstract methods. It can contain constants, abstract methods, default methods (Java 8+), static methods (Java 8+), and nested types.

### Interface vs Class

| Aspect | Class | Interface |
|--------|-------|-----------|
| **Keyword** | `class` | `interface` |
| **Methods** | Abstract + Concrete | Abstract only (Java 7); Default/Static (Java 8+) |
| **Variables** | Instance, static, final | `public static final` only |
| **Access Modifiers** | Any | `public` only (implicit) |
| **Instantiation** | `new Class()` | Not directly |
| **Inheritance** | Single (`extends`) | Multiple (`implements`) |
| **Constructor** | Yes | No |

### Abstract Class vs Interface (CRITICAL - Appeared 8/10 years, 5-10 marks)

| Aspect | Abstract Class | Interface |
|--------|----------------|-----------|
| **Keyword** | `abstract class` | `interface` |
| **Methods** | Abstract + Concrete (both) | Abstract (pre-Java 8); Default/Static/Private (Java 8+) |
| **Variables** | Instance, static, final, any modifier | `public static final` only (implicitly) |
| **Access Modifiers** | Any (`private`, `protected`, `public`, default) | `public` only (implicit for methods) |
| **Constructors** | Yes (can have constructors) | **No constructors** |
| **Inheritance** | Single (`extends` one abstract class) | Multiple (`implements` multiple interfaces) |
| **State** | Can have instance variables (state) | Cannot have instance variables (no state) |
| **Instantiation** | Cannot instantiate directly | Cannot instantiate directly |
| **Purpose** | **"Is-a" relationship** - shared code/state among related classes | **"Can-do" relationship** - contract for unrelated classes |
| **Method Body** | Allowed for concrete methods | Not allowed for abstract methods; allowed for default/static (Java 8+) |
| **Static Methods** | Allowed | Allowed (Java 8+) |
| **Private Methods** | Allowed | Allowed (Java 9+) |

**When to Use Which?**
- **Abstract Class:** When classes share code/state, need constructors, or have "is-a" relationship (e.g., `Animal` → `Dog`, `Cat`)
- **Interface:** When unrelated classes need common behavior, multiple implementations needed, or defining capabilities (e.g., `Serializable`, `Comparable`, `Runnable`)

**Example Showing Both:**
```java
// Abstract class - shared state and behavior
abstract class Vehicle {
    String brand;  // Instance variable (state)
    int wheels;
    
    Vehicle(String brand, int wheels) {  // Constructor
        this.brand = brand;
        this.wheels = wheels;
    }
    
    void displayInfo() {  // Concrete method
        System.out.println(brand + " has " + wheels + " wheels");
    }
    
    abstract void start();  // Abstract method
}

// Interface - contract for capability
interface Electric {
    void charge();  // Abstract method
    default void ecoMode() {  // Default method (Java 8+)
        System.out.println("Eco mode enabled");
    }
}

// Class using both
class Tesla extends Vehicle implements Electric {
    Tesla() { super("Tesla", 4); }  // Calls abstract class constructor
    
    @Override
    void start() { System.out.println("Tesla starting silently"); }
    
    @Override
    public void charge() { System.out.println("Charging battery..."); }
}
```

### Syntax
```java
[modifiers] interface InterfaceName [extends ParentInterface] {
    // Constant declarations (implicitly public static final)
    type CONSTANT_NAME = value;
    
    // Abstract method declarations (implicitly public abstract)
    returnType methodName(parameters);
    
    // Default method (Java 8+)
    default returnType methodName(parameters) { body }
    
    // Static method (Java 8+)
    static returnType methodName(parameters) { body }
}
```

### Example
```java
interface Drawable {
    // Constant
    int DEFAULT_COLOR = 0xFFFFFF;
    
    // Abstract method
    void draw();
    
    // Default method (Java 8+)
    default void printInfo() {
        System.out.println("Drawing shape...");
    }
    
    // Static method (Java 8+)
    static void reset() {
        System.out.println("Resetting canvas");
    }
}
```

### Complete Interface Implementation Program (PYQ 2022, 2023, 2024, 2025 - Area Calculation)

```java
// Interface defining the contract
interface Shape {
    double PI = 3.14159;  // Implicitly public static final
    
    void draw();           // Implicitly public abstract
    double area();         // Abstract method
    double perimeter();    // Abstract method
}

// Rectangle implements Shape
class Rectangle implements Shape {
    double length, breadth;
    
    Rectangle(double length, double breadth) {
        this.length = length;
        this.breadth = breadth;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Rectangle...");
    }
    
    @Override
    public double area() {
        return length * breadth;
    }
    
    @Override
    public double perimeter() {
        return 2 * (length + breadth);
    }
}

// Circle implements Shape
class Circle implements Shape {
    double radius;
    
    Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public void draw() {
        System.out.println("Drawing Circle...");
    }
    
    @Override
    public double area() {
        return PI * radius * radius;
    }
    
    @Override
    public double perimeter() {
        return 2 * PI * radius;
    }
}

// Test class
public class ShapeTest {
    public static void main(String[] args) {
        // Polymorphism via interface reference
        Shape s1 = new Rectangle(10, 5);
        Shape s2 = new Circle(7);
        
        s1.draw();
        System.out.println("Rectangle Area: " + s1.area());
        System.out.println("Rectangle Perimeter: " + s1.perimeter());
        
        System.out.println();
        
        s2.draw();
        System.out.println("Circle Area: " + s2.area());
        System.out.println("Circle Perimeter: " + s2.perimeter());
    }
}
```

**Output:**
```
Drawing Rectangle...
Rectangle Area: 50.0
Rectangle Perimeter: 30.0

Drawing Circle...
Circle Area: 153.93791
Circle Perimeter: 43.98226
```

---

## 8.7 Implementing Interfaces

### Syntax
```java
class ClassName implements Interface1, Interface2 {
    // Must implement all abstract methods
    // Can override default methods
}
```

### Example
```java
interface Payable {
    double getPaymentAmount();
}

interface Printable {
    void printDetails();
}

class Employee implements Payable, Printable {
    String name;
    double salary;
    
    Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }
    
    @Override
    public double getPaymentAmount() {
        return salary;
    }
    
    @Override
    public void printDetails() {
        System.out.println("Employee: " + name + ", Salary: " + salary);
    }
}

public class Test {
    public static void main(String[] args) {
        Employee e = new Employee("Alice", 50000);
        e.printDetails();
        System.out.println("Payment: " + e.getPaymentAmount());
    }
}
```

### Accessing Through Interface Reference
```java
interface Shape {
    void draw();
}

class Circle implements Shape {
    public void draw() { System.out.println("Drawing Circle"); }
}

class Rectangle implements Shape {
    public void draw() { System.out.println("Drawing Rectangle"); }
}

public class Test {
    public static void main(String[] args) {
        Shape s;  // Interface reference
        
        s = new Circle();
        s.draw();  // Drawing Circle
        
        s = new Rectangle();
        s.draw();  // Drawing Rectangle
    }
}
```

---

## 8.8 Extending Interfaces

### Interface Inheritance
- An interface can **extend** another interface
- A class implementing child interface must implement ALL methods in hierarchy

```java
interface A {
    void methodA();
}

interface B extends A {
    void methodB();
}

class Test implements B {
    public void methodA() { System.out.println("A"); }
    public void methodB() { System.out.println("B"); }
}
```

---

## 8.9 Default Methods (Java 8+)

### Purpose
Add new methods to interfaces without breaking existing implementations.

### Syntax
```java
interface MyInterface {
    default void newMethod() {
        System.out.println("Default implementation");
    }
}
```

### Rules
- ✅ Can be overridden by implementing class
- ✅ Can call other default/abstract methods
- ✅ Not mandatory to implement

### Example
```java
interface Vehicle {
    void start();
    
    default void stop() {
        System.out.println("Vehicle stopping...");
    }
}

class Car implements Vehicle {
    public void start() { System.out.println("Car starting"); }
    
    // Override default method
    @Override
    public void stop() {
        System.out.println("Car stopping with ABS");
    }
}

class Bike implements Vehicle {
    public void start() { System.out.println("Bike starting"); }
    // Uses default stop()
}
```

---

## 8.10 Static Methods in Interfaces (Java 8+)

### Characteristics
- Belong to interface, not implementing class
- **Cannot be overridden** (can be hidden by implementing class)
- Called using `InterfaceName.methodName()`
- **Cannot be called via implementing class reference** (unlike default methods)
- Useful for utility/helper methods related to the interface

```java
interface MathUtils {
    static int add(int a, int b) {
        return a + b;
    }
    
    static int multiply(int a, int b) {
        return a * b;
    }
}

public class Test {
    public static void main(String[] args) {
        System.out.println(MathUtils.add(5, 3));       // 8
        System.out.println(MathUtils.multiply(5, 3));  // 15
        
        // MathUtils m = new MathUtils(); // ERROR: cannot instantiate
        // m.add(1, 2); // ERROR: static method not accessible via instance
    }
}
```

### Static Method Hiding (Not Overriding)
```java
interface A {
    static void show() { System.out.println("A static"); }
}

class B implements A {
    // This is HIDING, not overriding!
    static void show() { System.out.println("B static"); }
}

public class Test {
    public static void main(String[] args) {
        A.show();  // Output: "A static"
        B.show();  // Output: "B static"
        
        A a = new B();
        // a.show(); // COMPILE ERROR: static method not accessible via interface reference
    }
}
```

### Interface Private Methods (Java 9+) - Helper for Default/Static Methods
```java
interface MyInterface {
    // Private static method (helper for static methods)
    private static int helper(int x) { return x * 2; }
    
    // Private instance method (helper for default methods) - Java 9+
    private void log(String msg) { System.out.println("[LOG] " + msg); }
    
    default void publicMethod() {
        log("publicMethod called");  // Can call private method
        System.out.println("Result: " + helper(5));
    }
    
    static void staticMethod() {
        System.out.println("Static: " + helper(10));
    }
}
```

---

## 8.11 Multiple Interface Issues

### Problem: Default Method Conflict
```java
interface A {
    default void show() { System.out.println("A"); }
}

interface B {
    default void show() { System.out.println("B"); }
}

class Test implements A, B {
    // COMPILE ERROR: Duplicate default method show()
    
    // MUST override to resolve
    @Override
    public void show() {
        A.super.show();  // Call A's default
        B.super.show();  // Call B's default
    }
}
```

### Resolution Syntax
```java
// Call specific interface's default method
InterfaceName.super.methodName();
```

### Detailed Conflict Scenarios & Resolutions (PYQ 2023, 2026)

#### Scenario 1: Two Interfaces with Same Default Method
```java
interface Printable {
    default void print() { System.out.println("Printable default"); }
}

interface Displayable {
    default void print() { System.out.println("Displayable default"); }
}

// MUST override to resolve conflict
class Document implements Printable, Displayable {
    @Override
    public void print() {
        // Option 1: Call one interface's default
        Printable.super.print();
        
        // Option 2: Call both
        // Displayable.super.print();
        
        // Option 3: Provide completely new implementation
        // System.out.println("Document custom print");
    }
}
```

#### Scenario 2: Interface Extends Another with Default Method
```java
interface Base {
    default void show() { System.out.println("Base default"); }
}

interface Derived extends Base {
    // Override default in sub-interface
    default void show() { System.out.println("Derived default"); }
}

class Test implements Derived {
    // Uses Derived's default (most specific wins)
    // No override needed unless further customization
}
```

#### Scenario 3: Class Provides Implementation vs Interface Default
```java
interface MyInterface {
    default void method() { System.out.println("Interface default"); }
}

class Parent {
    void method() { System.out.println("Parent class method"); }
}

class Child extends Parent implements MyInterface {
    // Class method WINS over interface default!
    // Output: "Parent class method"
}
```

#### Scenario 4: Multiple Default Methods with Different Signatures (No Conflict)
```java
interface A {
    default void show() { System.out.println("A"); }
    default void show(int x) { System.out.println("A int: " + x); }  // Overloaded - OK
}

interface B {
    default void show() { System.out.println("B"); }  // Same signature - CONFLICT
    default void display() { System.out.println("B display"); }  // Different - OK
}

class Test implements A, B {
    // Must override show() due to conflict
    @Override
    public void show() {
        A.super.show();
        B.super.show();
    }
    // show(int) and display() inherited without conflict
}
```

#### Complete Resolution Example (Exam-Ready)
```java
interface Drawable {
    default void draw() { System.out.println("Drawing shape"); }
    default void erase() { System.out.println("Erasing shape"); }
}

interface Fillable {
    default void draw() { System.out.println("Filling shape"); }  // CONFLICT
    default void fill(String color) { System.out.println("Fill with " + color); }
}

class Circle implements Drawable, Fillable {
    // Must resolve draw() conflict
    @Override
    public void draw() {
        Drawable.super.draw();   // Call Drawable's default
        Fillable.super.draw();   // Call Fillable's default
        System.out.println("Circle custom drawing");
    }
    
    // erase() inherited from Drawable - no conflict
    // fill() inherited from Fillable - no conflict
}

public class Test {
    public static void main(String[] args) {
        Circle c = new Circle();
        c.draw();      // Calls overridden method
        c.erase();     // Calls Drawable default
        c.fill("Red"); // Calls Fillable default
    }
}
```

**Output:**
```
Drawing shape
Filling shape
Circle custom drawing
Erasing shape
Fill with Red
```

---

## 8.12 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. What is a package? Advantages of packages.
2. Difference between built-in and user-defined packages.
3. How to compile and run a package program?
4. How to import packages?
5. What is an interface? Difference from class.
6. Can interface have variables? What type?
7. What are default and static methods in interface?
8. How to resolve multiple interface default method conflict?

**5-Mark Questions:**
1. Explain package creation with compilation and execution steps.
2. Explain access rules in packages with table.
3. Explain interface with example program.
4. Difference between abstract class and interface.
5. Explain default methods in interface with example.
6. Explain multiple interface implementation and conflict resolution.

**10-Mark Questions:**
1. **Explain packages: types, creation, import, access rules. Explain interfaces: definition, implementation, default/static methods, multiple interface issues.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Package and interface comparison with examples.

### Programs to Practice
1. ✅ **Package creation, compilation, execution** - appeared 2021, 2022, 2023, 2024, 2025
2. ✅ **Interface implementation (Area → Rectangle/Circle)** - appeared 2022, 2023, 2024, 2025
3. ✅ **Default method in interface** - appeared 2023, 2024, 2026
4. ✅ **Static method in interface** - appeared 2023, 2025, 2026
5. ✅ **Multiple interface conflict resolution** - appeared 2023, 2026

### Additional Important Programs (From PYQ)
6. ✅ **Abstract Class vs Interface with code** - appeared 2021, 2022, 2023, 2024, 2025
7. ✅ **Interface extending another interface** - appeared 2023, 2024
8. ✅ **Package with sub-package and inheritance across packages** - appeared 2021, 2024

---

## 8.13 Summary of Unit 8

| Topic | Key Points |
|-------|------------|
| **Package** | Namespace for related classes; prevents naming conflicts |
| **Types** | Built-in (java.lang, java.util, etc.) and User-defined |
| **Access Rules** | private < default < protected < public |
| **CLASSPATH** | Environment variable for .class file location; `-cp` overrides |
| **Creating Package** | `package pkgname;` first line; compile with `javac -d .`; run with FQN |
| **Importing** | `import pkg.Class;` or `import pkg.*;` after package statement; static import for static members |
| **Interface** | Contract of abstract methods; constants; multiple implementation |
| **Interface vs Class** | No constructors; no instance vars; multiple impl; public only |
| **Abstract Class vs Interface** | Abstract: state, constructors, single inheritance; Interface: contract, multiple impl, no state |
| **Default Methods** | `default` keyword; can be overridden; Java 8+; resolution via `Interface.super.method()` |
| **Static Methods** | `static` keyword; cannot be overridden (hidden); called via `InterfaceName.method()` |
| **Private Methods (Java 9+)** | Helper methods for default/static; not inherited |
| **Multiple Interfaces** | `implements A, B`; resolve default conflicts with `A.super.method()` |
| **Interface Extension** | `interface B extends A`; implementing class must implement all methods in hierarchy |

---

## 8.14 Quick Reference: Package Commands

```cmd
# Compile with package structure
javac -d . MyPackage/MyClass.java

# Compile to parent directory
javac -d .. MyPackage/MyClass.java

# Run package class
java MyPackage.MyClass

# Run sub-package class
java MyPackage.SubPackage.MyClass
```

## 8.15 Static vs Default Methods in Interface - Detailed Comparison (PYQ 2023 Q1g, 2026 Q1h)

| Aspect | Default Methods | Static Methods |
|--------|-----------------|----------------|
| **Keyword** | `default` | `static` |
| **Introduced** | Java 8 | Java 8 |
| **Purpose** | Add new functionality without breaking implementations | Utility/helper methods belonging to interface |
| **Override** | ✅ Can be overridden by implementing class | ❌ Cannot be overridden (can be hidden) |
| **Inheritance** | Inherited by implementing classes | NOT inherited by implementing classes |
| **Access via instance** | ✅ `obj.method()` | ❌ Not accessible via instance |
| **Access via Interface** | ❌ Not directly | ✅ `InterfaceName.method()` |
| **Reference to `this`** | ✅ Refers to implementing class instance | ❌ No `this` (belongs to interface) |
| **Can call other default methods** | ✅ Yes | ✅ Yes (via InterfaceName) |
| **Can call abstract methods** | ✅ Yes | ❌ No (no instance context) |
| **Multiple interface conflict** | ⚠️ Must resolve if same signature | ✅ No conflict (not inherited) |
| **Private helper methods** | ✅ Can use private instance methods (Java 9+) | ✅ Can use private static methods (Java 9+) |

### Quick Differentiation for Exam (5 marks)

**Default Method:**
- Instance method with body in interface
- Can be overridden
- Called on implementing class object
- Resolves diamond problem via `InterfaceName.super.method()`

**Static Method:**
- Belongs to interface (like class static method)
- Cannot be overridden, only hidden
- Called via `InterfaceName.methodName()`
- Useful for factory methods, utilities
- No diamond problem (not inherited)

### Example Showing Both
```java
interface Utility {
    // Default method - instance behavior
    default void process() {
        System.out.println("Default processing");
        helper();  // Can call private helper
    }
    
    // Static method - utility behavior
    static void reset() {
        System.out.println("Resetting utility");
        staticHelper();  // Can call private static helper
    }
    
    // Private instance helper (Java 9+)
    private void helper() { System.out.println("Helper called"); }
    
    // Private static helper (Java 9+)
    private static void staticHelper() { System.out.println("Static helper"); }
}

class MyClass implements Utility {
    // Can override default
    @Override
    public void process() {
        Utility.super.process();  // Call default
        System.out.println("Custom processing");
    }
    
    // Static method in class HIDES interface static (not override)
    static void reset() {
        System.out.println("Class static reset");
    }
}

public class Test {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.process();      // Calls overridden default method
        
        Utility.reset();    // Calls interface static: "Resetting utility"
        MyClass.reset();    // Calls class static: "Class static reset"
        // obj.reset();     // ERROR: static not accessible via instance
    }
}
```

## 8.16 Common Exam Questions & Answers

### Q: "Explain package creation with compilation and execution steps" (5-8 marks)
**Answer Structure:**
1. **Definition** of package
2. **Types** (Built-in, User-defined)
3. **Steps to create:**
   - Create directory structure matching package name
   - Write `package` statement as first line
   - Compile with `javac -d .` from parent directory
   - Run with fully qualified name `java package.Class`
4. **Example code** (Student class in mypack)
5. **CLASSPATH** explanation

### Q: "Explain access rules in packages with table" (5-7 marks)
**Answer Structure:**
1. **Member-level access table** (private, default, protected, public) across 4 contexts
2. **Class-level access table** (default vs public)
3. **Protected rule detail**: subclass in different package accesses via inheritance only
4. **Code example** showing protected across packages

### Q: "What is an interface? Difference from class / abstract class" (5-10 marks)
**Answer Structure:**
1. **Definition** of interface
2. **Interface vs Class table** (7+ points)
3. **Interface vs Abstract Class table** (8+ points - CRITICAL)
4. **When to use which**
5. **Example** showing both in same program

### Q: "Explain default methods in interface with example" (5 marks)
**Answer Structure:**
1. **Purpose**: backward compatibility
2. **Syntax** with `default` keyword
3. **Rules**: can override, not mandatory, conflict resolution
4. **Complete example** (Vehicle → Car/Bike)

### Q: "Explain multiple interface implementation and conflict resolution" (5-10 marks)
**Answer Structure:**
1. **Syntax**: `class C implements A, B`
2. **Conflict scenarios**: same default method in multiple interfaces
3. **Resolution**: `InterfaceName.super.method()`
4. **Class method wins over interface default**
5. **Complete example** with Drawable/Fillable

## 8.17 Short Notes for Quick Revision (5 marks each)

| Topic | Key Points |
|-------|------------|
| **Package** | Namespace organizing classes; prevents naming conflicts; access control; `java.lang` auto-imported |
| **User-defined Package** | `package pkgname;` first line; compile `javac -d .`; run `java pkg.Class`; dir structure matches package |
| **CLASSPATH** | Env var for .class location; `.` = current dir; `;` Windows, `:` Linux; `-cp` overrides |
| **Import** | After package, before class; `import pkg.Class` or `import pkg.*`; static import for static members |
| **Access Specifiers** | private (class), default (package), protected (package+subclass), public (everywhere) |
| **Interface** | Contract of abstract methods; constants (`public static final`); multiple implementation; no constructors |
| **Default Method** | `default` body; Java 8+; backward compatible; overrideable; conflict via `Interface.super.method()` |
| **Static Method** | `static` body; Java 8+; utility; called via `Interface.method()`; not inherited; cannot override |
| **Abstract Class vs Interface** | Abstract: state, constructors, single extends; Interface: no state, no constructors, multiple implements |
| **Multiple Interface Conflict** | Same default method → compile error; resolve with `A.super.method()`; class method wins over default |

---