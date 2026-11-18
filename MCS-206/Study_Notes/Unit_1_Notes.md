# Unit 1: Introduction to Java

## Unit Overview
This unit covers the fundamentals of Object-Oriented Programming (OOP) concepts, features of Java programming language, Java development environment (JDK, JRE, JVM, JIT), **constructors, access specifiers, final/static/this/super keywords, garbage collection, and basic data types**.

> **⚡ PYQ Insight**: Unit 1 topics frequently appear as 5-6 mark questions in Q1. **Constructors (7/10 papers)**, **Access Specifiers (7/10)**, **final/finally/finalize (7/10)**, **super keyword (7/10)**, and **JVM/JRE/JDK (2022, 2026)** are HIGH priority.

---

## 1.1 Object-Oriented Programming Concepts

### Topic Introduction
Object-Oriented Programming (OOP) is a programming paradigm that models real-world entities as objects containing both data and behavior. Java is fundamentally an object-oriented language where everything revolves around classes and objects.

### Definitions

| Concept | Definition |
|---------|------------|
| **Class** | A template or blueprint that defines data fields and methods of objects of the same type. |
| **Object** | A real-world entity that can be distinctly identified, having states (attributes) and behaviors (methods). |
| **Data Hiding** | Protecting data by making variables private and providing access only through getter/setter methods. |
| **Abstraction** | Hiding implementation details and showing only essential features to the user. Achieved via abstract classes and interfaces. |
| **Encapsulation** | Binding data members and methods together in a single unit (class) with data fields declared as private. |
| **Inheritance** | Process by which one class acquires properties of another class. Supports code reusability and IS-A relationship. |
| **Polymorphism** | Ability of an object to take many forms. Implemented via method overloading (compile-time) and method overriding (runtime). |

### Detailed Explanation

#### 1.1.1 Objects and Class
- **Object**: Real-world entity with state (attributes) and behavior (methods). Example: A `Dog` has states (name, breed, color) and behaviors (barking, wagging tail).
- **Class**: Template defining structure. All objects of a class share the same methods but have their own data field values.

```
┌─────────────────────────────────┐
│         Circle Class            │
│  ─────────────────────────────  │
│  Data Field: radius             │
│  Methods: getArea(), getRadius()│
└─────────────────────────────────┘
        │              │              │
        ▼              ▼              ▼
   ┌─────────┐    ┌─────────┐    ┌─────────┐
   │ Circle1 │    │ Circle2 │    │ Circle3 │
   │ radius=1│    │ radius=2│    │ radius=3│
   └─────────┘    └─────────┘    └─────────┘
```

#### 1.1.2 Data Hiding
- Implemented using `private` access modifier
- Access via public getter (`getX()`) and setter (`setX()`) methods
- Prevents unauthorized access from outside the class

#### 1.1.3 Abstraction
- **Data Abstraction**: Hiding internal details, showing only essential features
- **Method Abstraction**: Using a method without knowing its implementation (e.g., `System.out.println()`)
- Achieved using `abstract` classes and `interfaces`

#### 1.1.4 Encapsulation
```
┌─────────────────────────────────────┐
│            Class                    │
│  ┌─────────────────────────────┐   │
│  │ private data fields         │   │  ← Hidden from outside
│  ├─────────────────────────────┤   │
│  │ public getter/setter methods│   │  ← Controlled access
│  ├─────────────────────────────┤   │
│  │ public methods              │   │  ← Interface to outside
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
```
- **Benefits**: Data security, implementation hiding, flexibility to change internal code

#### 1.1.5 Inheritance
- **Syntax**: `class ChildClass extends ParentClass`
- **Relationship**: IS-A (parent-child)
- **Types Supported in Java**:
  - Single Inheritance: One parent, one child
  - Multilevel Inheritance: A → B → C
  - Hierarchical Inheritance: One parent, multiple children
- **NOT Supported**: Multiple Inheritance (class extending multiple classes) - solved via Interfaces

#### 1.1.6 Polymorphism
- **Static Polymorphism (Compile-time)**: Method overloading - same name, different parameters
- **Dynamic Polymorphism (Runtime)**: Method overriding - same name, same parameters, different classes

```
         Shape Class
            │
     ┌──────┴──────┐
     ▼             ▼
  Triangle      Circle
  area(b,h)   area(r)
```

### Important Points
- ✅ Java is purely object-oriented (everything is an object except primitives)
- ✅ Encapsulation = Data Hiding + Abstraction
- ✅ Inheritance enables code reusability
- ✅ Polymorphism provides flexibility
- ✅ Multiple inheritance not supported directly (use interfaces)

### Types/Classification

| OOP Concept | Type | Implementation in Java |
|-------------|------|------------------------|
| Polymorphism | Static (Compile-time) | Method Overloading |
| Polymorphism | Dynamic (Runtime) | Method Overriding |
| Inheritance | Single | `class B extends A` |
| Inheritance | Multilevel | `class C extends B extends A` |
| Inheritance | Hierarchical | `class B extends A; class C extends A` |
| Abstraction | Partial | Abstract Class |
| Abstraction | Full | Interface |

### Examples

**Encapsulation Example:**
```java
class Student {
    private String name;
    private int age;
    
    // Getter
    public String getName() { return name; }
    // Setter
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { 
        if(age > 0) this.age = age; 
    }
}
```

**Inheritance Example:**
```java
class Vehicle {
    void run() { System.out.println("Vehicle is running"); }
}

class Car extends Vehicle {
    void wheels() { System.out.println("Car has 4 wheels"); }
}

// Usage
Car c = new Car();
c.run();      // Inherited from Vehicle
c.wheels();   // Own method
```

### Advantages and Disadvantages

| Concept | Advantages | Disadvantages |
|---------|------------|---------------|
| Encapsulation | Data security, flexibility, reusability | Slight performance overhead |
| Inheritance | Code reusability, less development time, easy maintenance | Tight coupling, complexity |
| Polymorphism | Flexibility, code reuse, extensibility | Can be confusing for beginners |
| Abstraction | Simplifies complexity, hides implementation | Over-abstraction can complicate |

### Differences

| Aspect | Abstract Class | Interface |
|--------|---------------|-----------|
| Keyword | `abstract class` | `interface` |
| Methods | Abstract + Concrete | Only abstract (Java 7), default/static (Java 8+) |
| Variables | Any type | public static final by default |
| Inheritance | Single (`extends`) | Multiple (`implements`) |
| Constructor | Can have | Cannot have |
| Instantiation | Cannot instantiate | Cannot instantiate |

| Aspect | Method Overloading | Method Overriding |
|--------|-------------------|-------------------|
| Polymorphism Type | Static (Compile-time) | Dynamic (Runtime) |
| Parameters | Different | Same |
| Return Type | Can differ | Must be same |
| Class | Same class | Parent-child classes |
| Binding | Early (Compiler) | Late (JVM) |

---

## 1.2 Constructors in Java

> **⚡ PYQ Insight**: Constructors appeared in **7/10 papers** (2022, 2023, 2024, 2025, 2026) — **CRITICAL TOPIC** for 5-10 mark questions.

### Definition
A **constructor** is a special method used to initialize objects. It has the same name as the class, no return type (not even void), and is automatically called when an object is created.

### Types of Constructors

| Type | Description | Syntax |
|------|-------------|--------|
| **Default Constructor** | No-argument constructor provided by Java if none defined | `ClassName() { }` |
| **Parameterized Constructor** | Accepts arguments to initialize fields with specific values | `ClassName(type param) { }` |
| **Constructor Overloading** | Multiple constructors with different parameter lists | `ClassName()`, `ClassName(int)`, `ClassName(int, String)` |

### Key Rules
- ✅ Constructor name = Class name
- ✅ No return type (not even `void`)
- ✅ Can be overloaded (different parameter lists)
- ✅ Cannot be `abstract`, `static`, `final`, `synchronized`
- ✅ Can use access modifiers (`public`, `private`, `protected`, default)
- ❌ Cannot be inherited (but `super()` calls parent constructor)

### Constructor Chaining (super() vs this())

| Keyword | Purpose | Rules |
|---------|---------|-------|
| `this()` | Calls another constructor in **same class** | Must be **first statement** in constructor |
| `super()` | Calls parent class constructor | Must be **first statement**; if omitted, Java inserts `super()` implicitly |

**Execution Order in Multilevel Inheritance:**
```
Grandparent() → Parent() → Child()
```

### Example: Constructor Types & Chaining
```java
class Vehicle {
    String brand;
    
    // Default Constructor
    Vehicle() {
        this("Unknown");           // Calls parameterized constructor
        System.out.println("Vehicle default constructor");
    }
    
    // Parameterized Constructor
    Vehicle(String brand) {
        this.brand = brand;
        System.out.println("Vehicle parameterized: " + brand);
    }
}

class Car extends Vehicle {
    int wheels;
    
    Car() {
        super("Toyota");           // Calls parent parameterized constructor
        this.wheels = 4;
        System.out.println("Car constructor");
    }
    
    Car(String brand, int wheels) {
        super(brand);              // Calls Vehicle(String)
        this.wheels = wheels;
    }
}

// Usage
Car c1 = new Car();                // Output: Vehicle parameterized: Toyota → Car constructor
Car c2 = new Car("Honda", 4);      // Output: Vehicle parameterized: Honda → Car constructor
```

### Constructor vs Method
| Aspect | Constructor | Method |
|--------|-------------|--------|
| Name | Same as class | Any valid identifier |
| Return Type | None (not even void) | Must have (void or type) |
| Invocation | Automatic (via `new`) | Explicit call |
| Inheritance | Not inherited | Can be inherited/overridden |
| Default | Provided if none defined | Never provided |

---

## 1.3 Access Specifiers (Access Modifiers)

> **⚡ PYQ Insight**: Access specifiers appeared in **7/10 papers** (2022-2026) — **HIGH PRIORITY** for 5-6 mark questions.

### Four Access Levels

| Modifier | Class | Package | Subclass (Any Package) | World |
|----------|-------|---------|------------------------|-------|
| `public` | ✅ | ✅ | ✅ | ✅ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| **default** (no keyword) | ✅ | ✅ | ❌ | ❌ |
| `private` | ✅ | ❌ | ❌ | ❌ |

### Usage with Class Members

| Member | `public` | `protected` | `default` | `private` |
|--------|----------|-------------|-----------|-----------|
| **Class** | ✅ | ❌ (top-level) | ✅ | ❌ (top-level) |
| **Field/Variable** | ✅ | ✅ | ✅ | ✅ |
| **Method** | ✅ | ✅ | ✅ | ✅ |
| **Constructor** | ✅ | ✅ | ✅ | ✅ |

> **Note**: Top-level classes can only be `public` or `default`. `protected`/`private` only for nested classes.

### Practical Example
```java
package com.example;

public class AccessDemo {
    public int publicVar = 1;           // Accessible everywhere
    protected int protectedVar = 2;     // Same package + subclasses
    int defaultVar = 3;                 // Same package only
    private int privateVar = 4;         // Only within this class
    
    public void publicMethod() { }
    protected void protectedMethod() { }
    void defaultMethod() { }
    private void privateMethod() { }
}

// In same package - can access: public, protected, default
// In subclass (different package) - can access: public, protected
// In unrelated class (different package) - can access: public only
```

### Encapsulation Best Practice
```java
class Student {
    // Data hiding: private fields
    private String name;
    private int age;
    
    // Controlled access: public getters/setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public int getAge() { return age; }
    public void setAge(int age) { 
        if (age > 0 && age < 150) this.age = age;  // Validation
    }
}
```

---

## 1.4 Important Keywords

> **⚡ PYQ Insight**: `final` (5-6 marks), `static` (2023, 2026), `super` (7/10 papers), `this` (2022, 2025) — all **HIGH PRIORITY**.

### 1.4.1 `this` Keyword
Refers to the **current object instance**.

| Use Case | Example |
|----------|---------|
| Resolve variable shadowing | `this.name = name;` |
| Call current class constructor | `this(10, "default");` |
| Call current class method | `this.display();` |
| Pass current object as argument | `method(this);` |
| Return current object | `return this;` (builder pattern) |

```java
class Student {
    String name;
    int age;
    
    Student(String name, int age) {
        this.name = name;    // this.name = field, name = parameter
        this.age = age;
    }
    
    Student() {
        this("Unknown", 0);  // Constructor chaining
    }
}
```

### 1.4.2 `static` Keyword
Belongs to **class**, not instance. Shared across all objects.

| Member Type | Behavior |
|-------------|----------|
| **static variable** | Single copy shared by all instances (class variable) |
| **static method** | Can be called without object: `ClassName.method()` |
| **static block** | Executes once when class loads (initialization) |
| **static nested class** | Can exist without outer class instance |

```java
class Counter {
    static int count = 0;          // Shared by all instances
    int instanceCount = 0;         // Separate per instance
    
    Counter() {
        count++;
        instanceCount++;
    }
    
    static void showCount() {
        System.out.println("Total objects: " + count);
        // Cannot access instanceCount here!
    }
    
    static {                       // Static initialization block
        System.out.println("Class loaded");
    }
}
```

**Static vs Instance:**
| Aspect | Static | Instance |
|--------|--------|----------|
| Memory | Class area (Method Area) | Heap (per object) |
| Access | `ClassName.member` | `object.member` |
| `this` reference | Not available | Available |
| Overriding | Hidden (not overridden) | Can be overridden |

### 1.4.3 `final` Keyword
Imposes **restrictions** — cannot be changed.

| Applied To | Effect |
|------------|--------|
| **Variable** | Constant (must initialize once): `final int MAX = 100;` |
| **Method** | Cannot be overridden in subclass |
| **Class** | Cannot be extended (e.g., `String`, `Integer`) |
| **Parameter** | Value cannot be changed in method |

```java
final class Immutable { }                    // Cannot extend
class Parent {
    final void show() { }                    // Cannot override
}
final int VALUE = 10;                         // Compile-time constant
final int CONST;                              // Blank final - init in constructor
```

**`final` Variable Types:**
- **Static final** (constant): `static final double PI = 3.14159;`
- **Instance final**: Initialized in constructor, different per object
- **Local final**: Method-level constant

### 1.4.4 `super` Keyword
Refers to **parent class** object.

| Use Case | Example |
|----------|---------|
| Call parent constructor | `super();` or `super(args);` |
| Access parent field (hidden by child) | `super.fieldName` |
| Call parent method (overridden by child) | `super.methodName()` |

```java
class Animal {
    String type = "Animal";
    void sound() { System.out.println("Some sound"); }
}

class Dog extends Animal {
    String type = "Dog";
    
    void sound() {
        super.sound();           // Calls Animal.sound()
        System.out.println("Bark");
    }
    
    void printTypes() {
        System.out.println(super.type);  // Prints "Animal"
        System.out.println(this.type);   // Prints "Dog"
    }
    
    Dog() {
        super();                 // Calls Animal() - must be first line
    }
}
```

### Key Differences Summary

| Keyword | Purpose | Scope |
|---------|---------|-------|
| `this` | Current object | Instance only |
| `super` | Parent object | Inheritance context |
| `static` | Class-level (shared) | Class & instance contexts |
| `final` | Restriction/constant | Variable, method, class |

---

## 1.5 Garbage Collection & `finalize()`

> **⚡ PYQ Insight**: Appeared in **5/10 papers** (2022-2026) — **MEDIUM-HIGH PRIORITY** for 5-10 marks.

### What is Garbage Collection?
Automatic memory management in Java. JVM reclaims memory from objects **no longer reachable** (no live references).

### How It Works
1. **Reachability Analysis**: Object is *live* if reachable from GC roots (stack frames, static fields, JNI references)
2. **Mark Phase**: Mark all reachable objects
3. **Sweep Phase**: Remove unmarked objects
4. **Compact Phase** (optional): Defragment memory

### Object Eligibility for GC
```java
Object obj = new Object();   // Eligible when:
obj = null;                  // 1. Reference set to null
obj = new Object();          // 2. Reference reassigned
{ Object o = new Object(); } // 3. Scope ends (local variable)
// 4. Island of isolation (circular references with no external refs)
```

### `finalize()` Method
```java
protected void finalize() throws Throwable {
    try {
        // Cleanup: close files, release resources
        System.out.println("Object being garbage collected");
    } finally {
        super.finalize();    // Always call parent finalize
    }
}
```

**Important Points:**
- ✅ Called by GC **once** per object (before memory reclaim)
- ❌ **NOT guaranteed** to run (program may exit before GC)
- ❌ **Deprecated since Java 9** (use `try-with-resources` or `AutoCloseable`)
- ⚠️ Can "resurrect" object by assigning `this` to static field (bad practice)

### Modern Replacement: `try-with-resources` / `AutoCloseable`
```java
// Java 7+ - Preferred approach
try (FileInputStream fis = new FileInputStream("file.txt")) {
    // Use fis
} // auto-closes even if exception thrown

// Custom resource
class Resource implements AutoCloseable {
    public void close() { /* cleanup */ }
}
```

### JVM Memory Areas (GC Relevant)
| Area | Description | GC Target |
|------|-------------|-----------|
| **Heap** | Objects allocated here | ✅ Main GC target |
| **Method Area** | Class metadata, static vars | Rarely |
| **Stack** | Local variables, frames | Auto (stack unwind) |
| **Native Method Stack** | Native code | No |

---

## 1.6 Data Types, Variables & Operators

> **⚡ PYQ Insight**: Data Types/Variables/`final` variable (2024, 2025, 2026), Operators (2022, 2023, 2024) — **MEDIUM PRIORITY** for 5 marks.

### Primitive Data Types (8 Types)

| Type | Size | Default | Range | Wrapper |
|------|------|---------|-------|---------|
| `byte` | 1 byte | 0 | -128 to 127 | Byte |
| `short` | 2 bytes | 0 | -32,768 to 32,767 | Short |
| `int` | 4 bytes | 0 | -2³¹ to 2³¹-1 | Integer |
| `long` | 8 bytes | 0L | -2⁶³ to 2⁶³-1 | Long |
| `float` | 4 bytes | 0.0f | ~±3.4×10³⁸ | Float |
| `double` | 8 bytes | 0.0d | ~±1.8×10³⁰⁸ | Double |
| `char` | 2 bytes | '\u0000' | 0 to 65,535 (Unicode) | Character |
| `boolean` | ~1 bit | false | true/false | Boolean |

### Variable Declaration & Initialization
```java
// Syntax: type identifier [= value];
int age = 25;
double salary;
salary = 50000.0;

char grade = 'A';
boolean isStudent = true;
final int MAX_SCORE = 100;    // Constant (cannot change)
```

### Variable Scope & Lifetime

| Type | Scope | Lifetime | Default Value |
|------|-------|----------|---------------|
| **Instance Variable** | Class level | Object lifetime | 0/0.0/false/null |
| **Static Variable** | Class level | Program lifetime | 0/0.0/false/null |
| **Local Variable** | Method/block | Until block exits | **Must initialize** |
| **Parameter** | Method | Method execution | Passed value |

### Type Casting
```java
// Widening (Implicit) - smaller to larger
int i = 100;
long l = i;       // Auto
double d = i;     // Auto

// Narrowing (Explicit) - larger to smaller
double d = 100.5;
int i = (int) d;  // i = 100 (truncated)

// Reference casting
Animal a = new Dog();
Dog d = (Dog) a;  // Downcasting - needs instanceof check
```

### Operators

#### Arithmetic
| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus | `a % b` |
| `++` / `--` | Increment/Decrement | `++a`, `a++` |

#### Relational (return `boolean`)
| Operator | Name | Example |
|----------|------|---------|
| `==` | Equal to | `a == b` |
| `!=` | Not equal | `a != b` |
| `>` | Greater than | `a > b` |
| `<` | Less than | `a < b` |
| `>=` | Greater/equal | `a >= b` |
| `<=` | Less/equal | `a <= b` |

#### Logical
| Operator | Name | Short-circuit? |
|----------|------|----------------|
| `&&` | AND | ✅ Yes |
| `||` | OR | ✅ Yes |
| `!` | NOT | - |
| `&` | AND (bitwise/boolean) | ❌ No |
| `|` | OR (bitwise/boolean) | ❌ No |
| `^` | XOR | - |

#### Bitwise (operate on bits)
| Operator | Name | Example |
|----------|------|---------|
| `&` | AND | `a & b` |
| `|` | OR | `a | b` |
| `^` | XOR | `a ^ b` |
| `~` | Complement | `~a` |
| `<<` | Left shift | `a << 2` |
| `>>` | Right shift | `a >> 2` |
| `>>>` | Unsigned right shift | `a >>> 2` |

#### Assignment
| Operator | Example | Equivalent |
|----------|---------|------------|
| `=` | `a = 5` | - |
| `+=` | `a += 3` | `a = a + 3` |
| `-=` | `a -= 3` | `a = a - 3` |
| `*=` | `a *= 3` | `a = a * 3` |
| `/=` | `a /= 3` | `a = a / 3` |
| `%=` | `a %= 3` | `a = a % 3` |

#### Special
| Operator | Description |
|----------|-------------|
| `?:` | Ternary: `condition ? val1 : val2` |
| `instanceof` | Type check: `obj instanceof Class` |
| `.` | Member access |
| `new` | Object creation |
| `[]` | Array index |

### Operator Precedence (High to Low)
1. Postfix: `expr++`, `expr--`
2. Unary: `++expr`, `--expr`, `+expr`, `-expr`, `~`, `!`
3. Multiplicative: `*`, `/`, `%`
4. Additive: `+`, `-`
5. Shift: `<<`, `>>`, `>>>`
6. Relational: `<`, `>`, `<=`, `>=`, `instanceof`
7. Equality: `==`, `!=`
8. Bitwise AND: `&`
9. Bitwise XOR: `^`
10. Bitwise OR: `|`
11. Logical AND: `&&`
12. Logical OR: `||`
13. Ternary: `?:`
14. Assignment: `=`, `+=`, `-=`, etc.

---

## 1.7 Features of Java Programming Language

### Topic Introduction
Java's popularity stems from its robust feature set designed for modern software development.

### Key Features (10 Features)

| Feature | Description |
|---------|-------------|
| **1. Object-Oriented** | Everything is an object; supports encapsulation, inheritance, polymorphism |
| **2. Simple** | Easy syntax, no pointers, automatic garbage collection |
| **3. Secure** | No explicit pointers, runs in sandbox, bytecode verification |
| **4. Portable** | Write Once, Run Anywhere (WORA) via bytecode and JVM |
| **5. Robust** | Strong memory management, exception handling, type checking |
| **6. Multithreaded** | Built-in support for concurrent execution |
| **7. Architecture-Neutral** | Fixed data type sizes, JVM abstracts hardware |
| **8. Interpreted & High Performance** | JIT compiler optimizes hot code paths |
| **9. Distributed** | Built-in TCP/IP, RMI support |
| **10. Dynamic** | Runtime type info, dynamic class loading, reflection |

### Portability Types (3 Types)
1. **Source Code Portability** - Same results on any platform
2. **CPU Architecture Portability** - Bytecode runs on any CPU with JVM
3. **OS/GUI Portability** - Virtual OS/GUI via Java libraries (AWT, Swing, JavaFX)

### Diagram: Java Architecture Neutrality
```
Java Code (.java)
       │
       ▼
Java Compiler (javac)
       │
       ▼
Bytecode (.class)  ← Platform Independent
       │
       ├────────────┬────────────┐
       ▼            ▼            ▼
     JVM          JVM          JVM
  (Windows)    (Linux)      (Mac)
       │            │            │
       ▼            ▼            ▼
  Machine Code  Machine Code  Machine Code
```

### Important Exam Questions

**2-Mark Questions:**
1. Define Class and Object with example.
2. What is Encapsulation?
3. What is Polymorphism? Name its types.
4. List any four features of Java.
5. Difference between `final`, `finally`, `finalize`.
6. Difference between `throw` and `throws`.
7. Difference between abstract class and interface.

**5-Mark Questions:**
1. Explain Encapsulation with a program demonstrating getter/setter methods.
2. Explain Inheritance with its types supported in Java.
3. Differentiate between Method Overloading and Method Overriding.
4. Explain the features of Java that make it popular.
5. Explain Constructor types with example (default, parameterized, overloading).
6. Explain `super` keyword uses with program.
7. Explain `final` keyword (variable, method, class) with examples.
8. Explain `static` keyword (variables, methods, blocks) with examples.
9. Explain Access Specifiers (public, private, protected, default) with table.
10. Explain Garbage Collection and `finalize()` method.

**10-Mark Questions:**
1. What is OOP? Explain all four pillars of OOP with real-world examples and code snippets.
2. Explain Inheritance in detail: types, advantages, super keyword, and constructor chaining.

---

## 1.8 Java Development Environment and Tools

### Topic Introduction
Understanding JDK, JRE, JVM, and JIT is crucial for Java development and exams.

### Definitions

| Component | Full Form | Description |
|-----------|-----------|-------------|
| **JDK** | Java Development Kit | Complete development environment: JRE + development tools (javac, javadoc, jar, debugger) |
| **JRE** | Java Runtime Environment | Runtime environment: JVM + Java Class Libraries |
| **JVM** | Java Virtual Machine | Abstract machine that executes bytecode; makes Java platform-independent |
| **JIT** | Just-In-Time Compiler | Part of JVM; compiles bytecode to native machine code at runtime for performance |

### Detailed Explanation

#### JDK (Java Development Kit)
- **Contains**: JRE + Development Tools
- **Tools**: `javac` (compiler), `java` (launcher), `javadoc`, `jar`, `jdb` (debugger), `jconsole`
- **Purpose**: Write, compile, debug, and document Java programs

#### JRE (Java Runtime Environment)
- **Contains**: JVM + Java Class Libraries (`java.lang`, `java.util`, `java.io`, etc.)
- **Architecture**: ClassLoader → Bytecode Verifier → Interpreter
- **Purpose**: Run Java applications

#### JVM (Java Virtual Machine)
- **Role**: Executes bytecode; provides platform independence
- **Components**: 
  - Class Loader Subsystem
  - Runtime Data Areas (Method Area, Heap, Stack, PC Registers, Native Method Stack)
  - Execution Engine (Interpreter + JIT Compiler + Garbage Collector)
- **Process**: `.java` → `javac` → `.class` (bytecode) → `JVM` → Machine Code

#### JIT (Just-In-Time) Compiler
- **Function**: Compiles frequently executed bytecode to native machine code
- **Threshold**: ~10,000 executions (configurable)
- **Benefit**: Significantly improves performance over pure interpretation

### Program Execution Flow
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Welcome.java │────▶│  javac      │────▶│ Welcome.class│
│ (Source)     │     │ (Compiler)  │     │ (Bytecode)   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │    JVM      │
                                        │ (Executes)  │
                                        └─────────────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │  Output     │
                                        └─────────────┘
```

### IDEs for Java Development
| IDE | Features |
|-----|----------|
| **Eclipse** | Popular, ~1M downloads/month, extensive plugins |
| **NetBeans** | Free, open-source, supports latest JDK, JavaFX |
| **IntelliJ IDEA** | Smart code completion, excellent refactoring |

### Important Exam Questions

**2-Mark Questions:**
1. Difference between JDK, JRE, and JVM.
2. What is JIT compiler?
3. Name two popular Java IDEs.

**5-Mark Questions:**
1. Explain the flow of Java program execution with diagram.
2. Explain JDK, JRE, and JVM with their components.
3. What is JIT compiler? How does it improve performance?

**10-Mark Questions:**
1. Explain Java Development Environment in detail including JDK, JRE, JVM, and JIT with diagrams.

---

## 1.9 Environment Setup for Java Application Development

### Steps to Compile and Run (Command Line)

```bash
# Step 1: Write program (Welcome.java)
class Welcome {
    public static void main(String[] args) {
        System.out.println("Welcome to Java.");
    }
}

# Step 2: Compile
javac Welcome.java

# Step 3: Run
java Welcome
```

### Key Terms in `main` Method
| Term | Meaning |
|------|---------|
| `class` | Declares a class |
| `public` | Accessible from anywhere |
| `static` | Belongs to class, not object; called without object creation |
| `void` | No return value |
| `main` | Entry point of program |
| `String[] args` | Command-line arguments |
| `System.out.println()` | Prints to console (System → class, out → PrintStream object, println() → method) |

---

## 1.10 Summary of Unit 1

| Topic | Key Points |
|-------|------------|
| **OOP Concepts** | Class, Object, Encapsulation, Abstraction, Inheritance, Polymorphism |
| **Inheritance Types** | Single, Multilevel, Hierarchical (No Multiple) |
| **Polymorphism Types** | Static (Overloading), Dynamic (Overriding) |
| **Constructors** | Default, Parameterized, Overloading, Chaining (this/super) |
| **Access Specifiers** | public, protected, default, private — accessibility matrix |
| **Keywords** | this, super, static, final — uses and differences |
| **Garbage Collection** | Automatic memory management, finalize() deprecated |
| **Data Types** | 8 primitives, wrappers, casting, scope, operators |
| **Java Features** | 10 features: OOP, Simple, Secure, Portable, Robust, Multithreaded, Architecture-neutral, High Performance, Distributed, Dynamic |
| **JDK** | Development Kit = JRE + Tools |
| **JRE** | Runtime = JVM + Libraries |
| **JVM** | Executes bytecode; platform independence |
| **JIT** | Runtime compiler for performance |
| **Portability** | Source, CPU Architecture, OS/GUI |

---

## Unit 1: Important Exam Questions (from PYQ Analysis)

### Frequently Asked (High Priority)
1. **OOP Concepts**: Class, Object, Encapsulation, Inheritance, Polymorphism, Abstraction (2021, 2024)
2. **JVM/JRE/JDK**: Platform independence, architecture neutrality (2022, 2026)
3. **Encapsulation**: With program (2021, 2022, 2024, 2025, 2026)
4. **Constructor**: Default, parameterized, overloading, chaining (2022, 2023, 2024, 2025, 2026)
5. **Access Specifiers**: public, private, protected, default (2022, 2023, 2024, 2025, 2026)
6. **super keyword**: Constructor call, member access (2021, 2022, 2023, 2024, 2025)
7. **final/finally/finalize**: Differentiation (2022, 2023, 2024, 2025, 2026)
8. **static keyword**: Variables, methods, blocks (2023, 2026)

### Medium Priority
9. Features of Java (2022)
10. Data Types, Variables, final variable (2024, 2025, 2026)
11. Operators: Relational, Logical, Arithmetic (2022, 2023, 2024)
12. Garbage Collection & finalize() (2022, 2023, 2024, 2025, 2026)
13. this keyword (2022, 2025)
14. Abstract Class vs Interface (2021, 2022, 2023, 2024, 2025)

### Short Answer Topics (2-5 Marks)
- Difference between Class and Object
- What is Encapsulation?
- What is Polymorphism? Types?
- What is JDK/JRE/JVM/JIT?
- Features of Java (any 4-5)
- Types of Inheritance
- Method Overloading vs Overriding
- Difference between final, finally, finalize
- Difference between throw and throws
- Difference between abstract class and interface
- Difference between this and super
- Difference between static and instance members
- Access specifier accessibility table
- Constructor chaining (super() vs this())
- Garbage Collection eligibility

### Long Answer Topics (10 Marks)
- Complete OOP explanation with all pillars + code
- Inheritance with types, super keyword, constructor chaining
- Java program execution flow with diagram
- JDK/JRE/JVM/JIT detailed architecture
- Constructors: types, overloading, chaining with examples
- Access specifiers with accessibility matrix and encapsulation example
- Garbage Collection mechanism, finalize(), and modern alternatives