# Unit 4: Classes and Objects

## Unit Overview
This unit covers class definition, object creation, constructors, `this` keyword, `static` keyword, `final` keyword, encapsulation, access modifiers, garbage collection, and String handling.

> **📋 PYQ Insight**: Unit 4 topics (Class/Object, Constructor, this, static, final, Encapsulation, Access Modifiers, GC, String) have appeared **consistently across all 10 years** (2021-2026). High-frequency: Constructor (7×), Encapsulation (7×), final (7×), Access Modifiers (7×), this (5×), static (5×), GC+finalize (5×). Expect 5-10 mark questions with code.

---

## 4.1 Class and Object Fundamentals

### Topic Introduction
A class is a blueprint/template that defines the structure and behavior of objects. An object is an instance of a class.

> **📋 PYQ Insight**: "Class definition + Object creation + Memory allocation" appeared in **2021 Q1(a) (6m)** and **2024 Q1(a) (5m)**. "Object assignment/reference" appeared in **2024 Q1(d) (5m)**.

### Class Definition
```java
class ClassName {
    // Fields (attributes/data members) - Instance variables
    dataType fieldName;
    
    // Methods (behavior)
    returnType methodName(parameters) {
        // method body
    }
    
    // Constructors
    ClassName(parameters) {
        // initialization
    }
}
```

### Object Creation
```java
// Syntax: ClassName objectName = new ClassName();
Student s1 = new Student();
Student s2 = new Student();

// Each object has its own copy of instance variables
s1.name = "Alice";
s2.name = "Bob";  // Different from s1.name
```

### Memory Representation
```
Stack (References)          Heap (Objects)
┌─────────────┐           ┌─────────────────┐
│ Student s1  │──────────▶│ name: "Alice"   │
└─────────────┘           │ age: 20         │
                          └─────────────────┘
┌─────────────┐           ┌─────────────────┐
│ Student s2  │──────────▶│ name: "Bob"     │
└─────────────┘           │ age: 22         │
                          └─────────────────┘
```

### Object Assignment & Reference Behavior (⭐ 2024 Q1(d) - 5 marks)
```java
Student s1 = new Student("Alice", 20);
Student s2 = new Student("Bob", 22);
Student s3 = s1;        // s3 references SAME object as s1

s3.name = "Charlie";    // Changes s1.name too!
System.out.println(s1.name);  // "Charlie" - s1 and s3 share the object

s1 = null;              // s1 reference gone, but object still reachable via s3
// Object eligible for GC only when BOTH s1 and s3 are null/reassigned
```

**Key Points**:
- Assignment copies the **reference**, not the object
- Multiple references can point to the same object
- Object eligible for GC only when **no references** point to it
- `==` compares references, `.equals()` compares content (if overridden)

---

## 4.2 Constructors

### Topic Introduction
A constructor is a special method used to initialize objects. It has the same name as the class and no return type.

### Types of Constructors

| Type | Description | Syntax |
|------|-------------|--------|
| **Default Constructor** | Provided by compiler if no constructor defined; no parameters | `ClassName() {}` |
| **Parameterized Constructor** | Accepts arguments to initialize fields | `ClassName(type param) {}` |
| **Constructor Overloading** | Multiple constructors with different parameters | Multiple `ClassName(...)` |

### Examples

```java
class Student {
    String name;
    int age;
    int rollNo;
    
    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
        rollNo = 0;
        System.out.println("Default constructor called");
    }
    
    // Parameterized constructor
    Student(String n, int a) {
        name = n;
        age = a;
        rollNo = 0;
    }
    
    // Parameterized constructor (3 params)
    Student(String n, int a, int r) {
        name = n;
        age = a;
        rollNo = r;
    }
    
    void display() {
        System.out.println("Name: " + name + ", Age: " + age + ", Roll: " + rollNo);
    }
}

public class ConstructorDemo {
    public static void main(String[] args) {
        Student s1 = new Student();                    // Default
        Student s2 = new Student("Alice", 20);         // 2 params
        Student s3 = new Student("Bob", 22, 101);      // 3 params
        
        s1.display();
        s2.display();
        s3.display();
    }
}
```

### Constructor Characteristics
- ✅ Same name as class
- ✅ No return type (not even `void`)
- ✅ Called automatically with `new`
- ✅ Can be overloaded
- ✅ Cannot be `static`, `abstract`, `final`, `synchronized`
- ✅ If any constructor defined, default NOT provided by compiler

---

## 4.3 The `this` Keyword

### Uses of `this`

| Use | Description | Example |
|-----|-------------|---------|
| **1. Refer to current object's instance variables** | Resolve name conflicts with parameters | `this.name = name;` |
| **2. Call current class constructor** | Constructor chaining (must be first statement) | `this("Default", 0);` |
| **3. Pass current object as argument** | In method calls | `method(this);` |
| **4. Return current object** | Method chaining | `return this;` |

### Example: Resolving Name Conflicts
```java
class Student {
    String name;
    int age;
    
    Student(String name, int age) {
        this.name = name;  // this.name = instance variable, name = parameter
        this.age = age;
    }
}
```

### Example: Constructor Chaining
```java
class Student {
    String name;
    int age;
    int rollNo;
    
    Student() {
        this("Unknown", 0, 0);  // Calls 3-param constructor
    }
    
    Student(String name, int age) {
        this(name, age, 0);     // Calls 3-param constructor
    }
    
    Student(String name, int age, int rollNo) {
        this.name = name;
        this.age = age;
        this.rollNo = rollNo;
    }
}
```

---

## 4.4 The `static` Keyword

### Topic Introduction
`static` members belong to the **class**, not to instances. Shared by all objects.

### Static Members

| Member Type | Declaration | Access | Memory |
|-------------|-------------|--------|--------|
| **Static Variable** | `static dataType varName;` | `ClassName.varName` or `obj.varName` | One copy in class area |
| **Static Method** | `static returnType methodName() {}` | `ClassName.methodName()` | No `this` reference |
| **Static Block** | `static { ... }` | Executes at class loading | For complex static initialization |

### Example
```java
class Student {
    String name;           // Instance variable
    static int count = 0;  // Static variable (shared)
    
    Student(String name) {
        this.name = name;
        count++;           // Increment for each object
    }
    
    static void showCount() {
        System.out.println("Total students: " + count);
        // Cannot access 'name' here - non-static!
    }
    
    void display() {
        System.out.println("Name: " + name + ", Count: " + count);
    }
}

public class StaticDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Alice");
        Student s2 = new Student("Bob");
        Student s3 = new Student("Charlie");
        
        Student.showCount();  // Output: Total students: 3
        
        System.out.println(Student.count);  // Direct access: 3
    }
}
```

### Static vs Instance

| Aspect | Static | Instance |
|--------|--------|----------|
| **Memory** | Class area (once) | Heap (per object) |
| **Access** | `ClassName.member` | `object.member` |
| **`this` reference** | Not available | Available |
| **Can access** | Only static members | Both static & instance |
| **Override** | Cannot override (can hide) | Can override |

---

## 4.5 The `final` Keyword

### Uses of `final`

| Context | Meaning | Example |
|---------|---------|---------|
| **Final Variable** | Constant (cannot change after initialization) | `final double PI = 3.14;` |
| **Final Method** | Cannot be overridden by subclasses | `final void display() {}` |
| **Final Class** | Cannot be extended (no inheritance) | `final class Constants {}` |
| **Final Parameter** | Parameter value cannot change in method | `void method(final int x) {}` |

### Final Variable Rules
```java
// 1. Initialize at declaration
final int MAX = 100;

// 2. Initialize in constructor (blank final)
class Circle {
    final double radius;
    Circle(double r) { radius = r; }  // Must initialize in ALL constructors
}

// 3. Static final (compile-time constant)
static final int MAX_STUDENTS = 60;
```

### Example
```java
final class Constants {
    static final double PI = 3.14159;
    static final int MAX = 100;
}

class MathUtil {
    // Cannot override this method
    final double calculateArea(double r) {
        return Constants.PI * r * r;
    }
}

// class ExtendedMath extends Constants {}  // ERROR: Cannot extend final class
// class Child extends MathUtil {
//     double calculateArea(double r) {}     // ERROR: Cannot override final method
// }
```

---

## 4.6 Encapsulation and Access Modifiers

### Encapsulation
**Definition**: Binding data and methods together; hiding internal state; providing controlled access via public methods.

```java
class BankAccount {
    // Private data - hidden from outside
    private double balance;
    private String accountNumber;
    
    // Public methods - controlled access
    public double getBalance() {
        return balance;
    }
    
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
    
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }
}
```

### Access Modifiers (Specifiers)

| Modifier | Class | Package | Subclass (diff package) | World |
|----------|-------|---------|------------------------|-------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` (no keyword) | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

#### Class-Level Access
| Modifier | Same Package | Different Package |
|----------|--------------|-------------------|
| `default` | ✅ Accessible | ❌ Not accessible |
| `public` | ✅ Accessible | ✅ Accessible |

> **Note**: A class can only be `public` or `default` (not `private`/`protected` unless nested).

### Example: Access Control
```java
package pack1;

class Parent {
    private int privateVar = 1;
    int defaultVar = 2;              // package-private
    protected int protectedVar = 3;
    public int publicVar = 4;
}

class ChildInSamePackage extends Parent {
    void access() {
        // privateVar;    // ERROR: not accessible
        defaultVar = 10;           // OK
        protectedVar = 10;         // OK
        publicVar = 10;            // OK
    }
}
```

```java
package pack2;
import pack1.Parent;

class ChildInDiffPackage extends Parent {
    void access() {
        // privateVar;    // ERROR
        // defaultVar;    // ERROR: default not accessible outside package
        protectedVar = 10;         // OK: protected accessible in subclass
        publicVar = 10;            // OK
    }
}

class Unrelated {
    void test() {
        Parent p = new Parent();
        // p.privateVar;    // ERROR
        // p.defaultVar;    // ERROR
        // p.protectedVar;  // ERROR: not in subclass
        p.publicVar = 10;          // OK
    }
}
```

---

## 4.7 Garbage Collection and `finalize()`

### Garbage Collection
- **Automatic memory management** in Java
- JVM reclaims memory from objects no longer referenced
- Runs as a **daemon thread** in background
- Non-deterministic (cannot predict when it runs)

### Making Objects Eligible for GC
```java
// 1. Nullify reference
Student s = new Student();
s = null;  // Object eligible for GC

// 2. Reassign reference
Student s1 = new Student();
Student s2 = new Student();
s1 = s2;   // First object eligible for GC

// 3. Object created in method (local reference)
void method() {
    Student s = new Student();
}  // s goes out of scope → eligible for GC
```

### `finalize()` Method
```java
class Resource {
    String name;
    
    Resource(String name) { this.name = name; }
    
    // Called by GC before object is destroyed
    @Override
    protected void finalize() throws Throwable {
        try {
            System.out.println("Cleaning up: " + name);
            // Release resources (files, connections, etc.)
        } finally {
            super.finalize();  // Call parent finalize
        }
    }
}
```

### Important Points
- ✅ `finalize()` called **at most once** per object
- ✅ Not guaranteed to be called (program may exit)
- ✅ Can "resurrect" object by assigning `this` to a reference
- ✅ Deprecated since Java 9 (use try-with-resources or Cleaner API)
- ✅ `System.gc()` only **suggests** GC to run

---

## 4.8 String Handling

### String Class
- **Immutable**: Once created, cannot be changed
- **In `java.lang` package** (auto-imported)
- String literals stored in **String Constant Pool**

### Creating Strings
```java
// 1. String literal (uses pool)
String s1 = "Hello";
String s2 = "Hello";  // Same object from pool

// 2. new keyword (creates new object in heap)
String s3 = new String("Hello");
String s4 = new String("Hello");  // Different objects

s1 == s2   // true (same reference)
s1 == s3   // false (different objects)
s1.equals(s3)  // true (same content)
```

### Important Methods

| Method | Description | Example |
|--------|-------------|---------|
| `length()` | Returns length | `"Hello".length()` → 5 |
| `charAt(index)` | Character at index | `"Hello".charAt(0)` → 'H' |
| `substring(begin)` | Substring from index | `"Hello".substring(1)` → "ello" |
| `substring(begin, end)` | Substring range | `"Hello".substring(1,4)` → "ell" |
| `equals(str)` | Content comparison (case-sensitive) | `"Hello".equals("Hello")` → true |
| `equalsIgnoreCase(str)` | Case-insensitive comparison | `"Hello".equalsIgnoreCase("hello")` → true |
| `compareTo(str)` | Lexicographic comparison | `"Hello".compareTo("World")` → negative |
| `concat(str)` | Concatenation | `"Hello".concat(" World")` → "Hello World" |
| `toUpperCase()` | Convert to uppercase | `"hello".toUpperCase()` → "HELLO" |
| `toLowerCase()` | Convert to lowercase | `"HELLO".toLowerCase()` → "hello" |
| `trim()` | Remove leading/trailing spaces | `"  hi  ".trim()` → "hi" |
| `replace(old, new)` | Replace characters | `"hello".replace('l','L')` → "heLLo" |
| `split(regex)` | Split into array | `"a,b,c".split(",")` → ["a","b","c"] |
| `indexOf(ch/str)` | First occurrence index | `"hello".indexOf('l')` → 2 |
| `lastIndexOf(ch/str)` | Last occurrence index | `"hello".lastIndexOf('l')` → 3 |
| `contains(str)` | Check if contains | `"hello".contains("ell")` → true |
| `startsWith(str)` | Check prefix | `"hello".startsWith("he")` → true |
| `endsWith(str)` | Check suffix | `"hello".endsWith("lo")` → true |
| `valueOf(x)` | Convert to string | `String.valueOf(123)` → "123" |

### String Immutability Example
```java
String s = "Hello";
s.concat(" World");  // Returns new string, s unchanged
System.out.println(s);  // "Hello"

s = s.concat(" World");  // Reassign
System.out.println(s);  // "Hello World"
```

### String vs StringBuilder vs StringBuffer

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread Safety** | N/A (immutable) | Not synchronized | Synchronized |
| **Performance** | Fast for reads | Fastest for modifications | Slower (sync overhead) |
| **Use Case** | Constant strings | Single-threaded modifications | Multi-threaded modifications |

```java
// StringBuilder example
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");      // Modifies same object
sb.insert(5, ",");
sb.reverse();
System.out.println(sb);   // "dlroW ,olleH"

// StringBuffer example (thread-safe)
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(" World");
```

---

## 4.9 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. Difference between class and object.
2. What is a constructor? Types of constructors.
3. Difference between default and parameterized constructor.
4. What is `this` keyword? Uses.
5. What is `static` keyword? Static vs instance variables.
6. What is `final` keyword? Final variable, method, class.
7. What is encapsulation? How to achieve it?
8. Difference between `private`, `default`, `protected`, `public`.
9. What is garbage collection? `finalize()` method.
10. Difference between `String` and `StringBuffer`/`StringBuilder`.
11. Why is `main` method static?
12. What is constructor overloading?

**5-Mark Questions:**
1. Explain constructor with types and example program.
2. Explain `this` keyword with examples (all 4 uses).
3. Explain `static` keyword with program.
4. Explain `final` keyword (variable, method, class) with examples.
5. Explain encapsulation with getter/setter program.
6. Explain access specifiers with table and example.
7. Explain garbage collection and `finalize()` method.
8. Write a program demonstrating String methods (length, reverse, compare).
9. Explain String immutability with example.
10. Difference between String, StringBuilder, StringBuffer.

**10-Mark Questions:**
1. What is a class? Explain constructors, `this`, `static`, `final` with comprehensive example.
2. Explain encapsulation in detail with access modifiers and a complete program.
3. Explain memory management in Java: object creation, garbage collection, finalize.

### Programs to Practice (High Yield)
1. ✅ **Encapsulation with getter/setter** - appeared 2021, 2022, 2024, 2025, 2026
2. ✅ **Constructor overloading** - appeared 2022, 2023, 2024, 2025, 2026
3. ✅ **Constructor chaining with `this`** - appeared 2022
4. ✅ **Static variable/method demo** - appeared 2023, 2026
5. ✅ **Final variable/method/class** - appeared 2022, 2023, 2024, 2025, 2026
6. ✅ **String reverse + length** - appeared 2022, 2023, 2024, 2025
7. ✅ **Object assignment/reference** - appeared 2024

---

## 4.10 Summary of Unit 4

| Topic | Key Points |
|-------|------------|
| **Class** | Blueprint with fields, methods, constructors |
| **Object** | Instance of class; created with `new` |
| **Constructor** | Same name as class; no return type; default/parameterized/overloaded |
| **`this`** | Current object reference; resolves conflicts; constructor chaining |
| **`static`** | Class-level; shared; accessed via class name; no `this` |
| **`final`** | Variable=constant, Method=can't override, Class=can't extend |
| **Encapsulation** | Private fields + public getters/setters |
| **Access Modifiers** | private < default < protected < public |
| **Garbage Collection** | Automatic; reclaims unreferenced objects; `finalize()` called before destruction |
| **String** | Immutable; pool for literals; many utility methods |
| **StringBuilder** | Mutable; non-synchronized; fast |
| **StringBuffer** | Mutable; synchronized; thread-safe |

---

## 4.11 Comparison Tables for Quick Revision

### Constructor vs Method
| Aspect | Constructor | Method |
|--------|-------------|--------|
| Name | Same as class | Any valid identifier |
| Return Type | None (not even void) | Required (void if none) |
| Call | Automatic with `new` | Explicit call |
| Purpose | Initialize object | Perform action |
| Overloading | Yes | Yes |
| Overriding | No | Yes |
| `this()` / `super()` | First line only | Not applicable |

### String vs StringBuffer vs StringBuilder
| Feature | String | StringBuffer | StringBuilder |
|---------|--------|--------------|---------------|
| Package | java.lang | java.lang | java.lang |
| Mutability | Immutable | Mutable | Mutable |
| Thread Safety | Yes (immutable) | Yes (synchronized) | No |
| Performance | Slow for concat | Moderate | Fast |
| Java Version | 1.0 | 1.0 | 5.0 |