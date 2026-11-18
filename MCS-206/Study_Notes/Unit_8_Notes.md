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
- **Cannot be overridden** (can be hidden)
- Called using `InterfaceName.methodName()`

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

---

## 8.13 Summary of Unit 8

| Topic | Key Points |
|-------|------------|
| **Package** | Namespace for related classes; prevents naming conflicts |
| **Types** | Built-in (java.lang, java.util, etc.) and User-defined |
| **Access Rules** | private < default < protected < public |
| **CLASSPATH** | Environment variable for .class file location |
| **Creating Package** | `package pkgname;` first line; compile with `javac -d .` |
| **Importing** | `import pkg.Class;` or `import pkg.*;` after package statement |
| **Interface** | Contract of abstract methods; constants; multiple implementation |
| **Interface vs Class** | No constructors; no instance vars; multiple impl; public only |
| **Default Methods** | `default` keyword; can be overridden; Java 8+ |
| **Static Methods** | `static` keyword; cannot be overridden; called via InterfaceName |
| **Multiple Interfaces** | `implements A, B`; resolve default conflicts with `A.super.method()` |

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