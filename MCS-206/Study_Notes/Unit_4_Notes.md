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

> **📋 PYQ Insight**: Constructors appeared **7 times** (2022 Q1(e) 6m, 2022 Q2(a) 10m, 2023 Q1(c) 5m, 2024 Q2(a) 5m, 2025 Q1(g) 5m, 2026 Q1(b) 5m). "Parameterized constructor + need" is a frequent 5-mark question. Constructor chaining with `this()` and `super()` in multilevel inheritance (2022 Q2(a) 10m) is critical.

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

### Constructor Chaining with `this()` and `super()` (⭐ 2022 Q2(a) 10 marks)

```java
// Parent class
class Person {
    String name;
    int age;
    
    Person() {
        this("Unknown", 0);  // this() chaining
        System.out.println("Person default constructor");
    }
    
    Person(String name, int age) {
        this.name = name;
        this.age = age;
        System.out.println("Person parameterized constructor");
    }
}

// Child class
class Student extends Person {
    int rollNo;
    
    Student() {
        super();  // Calls Person() - MUST be first statement
        this.rollNo = 0;
        System.out.println("Student default constructor");
    }
    
    Student(String name, int age, int rollNo) {
        super(name, age);  // Calls Person(String, int) - MUST be first statement
        this.rollNo = rollNo;
        System.out.println("Student parameterized constructor");
    }
}

public class ConstructorChainingDemo {
    public static void main(String[] args) {
        Student s = new Student("Alice", 20, 101);
        // Output order:
        // Person parameterized constructor
        // Student parameterized constructor
    }
}
```

**Execution Order in Multilevel Inheritance** (2022 Q2(a)):
1. Grandparent constructor → Parent constructor → Child constructor
2. `super()` must be **first statement** in constructor
3. If no `super()` written, `super()` (no-arg) is inserted automatically
4. If parent has no default constructor, child MUST explicitly call `super(args)`

### Why Parameterized Constructor? (2022 Q1(e), 2024 Q2(a), 2025 Q1(g), 2026 Q1(b))
- Ensures object is created in **valid state** with required data
- Prevents uninitialized fields
- Enables **immutable objects** (no setters needed)
- Supports **constructor overloading** for flexible object creation

---

## 4.3 The `this` Keyword

### Uses of `this`

> **📋 PYQ Insight**: `this` keyword appeared in **2022 Q1(e)** (constructors vs methods), **2025** (programs). "Explain `this` keyword with examples (all 4 uses)" is a frequent **5-mark question**.

| Use | Description | Example |
|-----|-------------|---------|
| **1. Refer to current object's instance variables** | Resolve name conflicts with parameters | `this.name = name;` |
| **2. Call current class constructor** | Constructor chaining (must be first statement) | `this("Default", 0);` |
| **3. Pass current object as argument** | In method calls | `method(this);` |
| **4. Return current object** | Method chaining / fluent API | `return this;` |

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

### Example: Passing `this` as Argument
```java
class Student {
    String name;
    
    Student(String name) {
        this.name = name;
    }
    
    void print(Student s) {
        System.out.println("Student: " + s.name);
    }
    
    void display() {
        print(this);  // Pass current object to method
    }
}
```

### Example: Method Chaining (Returning `this`)
```java
class StringBuilder {
    private StringBuilder sb = new StringBuilder();
    
    public StringBuilder append(String str) {
        sb.append(str);
        return this;  // Enable chaining
    }
    
    public StringBuilder reverse() {
        sb.reverse();
        return this;
    }
    
    @Override
    public String toString() {
        return sb.toString();
    }
}

// Usage
StringBuilder builder = new StringBuilder();
builder.append("Hello").append(" ").append("World").reverse();
// Output: "dlroW olleH"
```

### ⚠️ Important Rules for `this()`
- Must be **first statement** in constructor
- Cannot use `this()` and `super()` in same constructor
- Cannot use `this` in static context (static methods/blocks)

---

## 4.4 The `static` Keyword

### Topic Introduction
`static` members belong to the **class**, not to instances. Shared by all objects.

> **📋 PYQ Insight**: `static` keyword appeared in **2023 Q1(a)** (static binding + example, 5m), **2026 Q1(h)** (static methods in interface + multiple interface issues, 5m). "Explain `static` keyword with program" is a **5-mark question**.

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

### Static Block & Initialization Order (Important for Exams)
```java
class Demo {
    static int a = 10;          // 1. Static variable initialization
    
    static {                    // 2. Static block (in order of appearance)
        System.out.println("Static block 1");
        a = 20;
    }
    
    static int b = a + 5;       // 3. More static variables
    
    static {                    // 4. Another static block
        System.out.println("Static block 2: a=" + a + ", b=" + b);
    }
    
    {                           // 5. Instance block (runs per object, before constructor)
        System.out.println("Instance block");
    }
    
    Demo() {                    // 6. Constructor
        System.out.println("Constructor");
    }
}

// Output when: Demo d = new Demo();
// Static block 1
// Static block 2: a=20, b=25
// Instance block
// Constructor
```

### Static Methods in Interfaces (⭐ 2026 Q1(h) - 5 marks)
```java
interface MyInterface {
    // Static method in interface (Java 8+)
    static void staticMethod() {
        System.out.println("Interface static method");
    }
    
    // Default method (Java 8+)
    default void defaultMethod() {
        System.out.println("Interface default method");
    }
}

class MyClass implements MyInterface {
    // Static method NOT inherited - must call via InterfaceName.staticMethod()
    // Default method IS inherited - can be overridden
}

public class Test {
    public static void main(String[] args) {
        MyInterface.staticMethod();  // OK: InterfaceName.staticMethod()
        // MyClass.staticMethod();   // ERROR: Static methods not inherited
        
        MyClass obj = new MyClass();
        obj.defaultMethod();         // OK: Default method inherited
    }
}
```

### Why is `main` Method Static? (⭐ Frequent 2-mark question)
- JVM calls `main()` **without creating an object** of the class
- Static methods can be called via class name: `ClassName.main(args)`
- If `main` were non-static, JVM would need to instantiate the class first (which constructor? what args?)
- Entry point must be accessible without object creation

---

## 4.5 The `final` Keyword

### Uses of `final`

> **📋 PYQ Insight**: `final` keyword appeared **7 times** (2022 Q1(f) 6m, 2022 Q4(b) 5m, 2023 Q3(b) 5m, 2024 Q1(b) 5m, 2025 Q1(e) 5m, 2026 Q1(c) 5m). **Critical**: "final vs finally vs finalize" differentiation appeared in **2023 Q5(b) (6m)**, **2025 Q5(d)**. "Explain final keyword (variable, method, class) with examples" is a **5-10 mark question**.

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

// 4. Reference variable final (object can be modified, reference cannot)
final List<String> list = new ArrayList<>();
list.add("Hello");    // OK: modifying object
// list = new ArrayList<>();  // ERROR: cannot change reference
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

### Final vs Finally vs Finalize (⭐⭐⭐ 2023 Q5(b) 6 marks, 2025 Q5(d) 5 marks)

| Aspect | `final` | `finally` | `finalize()` |
|--------|---------|-----------|--------------|
| **Type** | Keyword / Modifier | Block | Method |
| **Purpose** | Restrict modification (var/method/class) | Execute cleanup code always | Cleanup before GC destroys object |
| **Usage** | Variable, Method, Class, Parameter | try-catch-finally | Object class, override in subclass |
| **Execution** | Compile-time restriction | **Always executes** (except System.exit) | Called by GC (not guaranteed) |
| **Since** | Java 1.0 | Java 1.0 | Java 1.0 (Deprecated Java 9) |
| **Example** | `final int x = 10;` | `finally { close(); }` | `protected void finalize() {}` |

```java
// Complete Example showing all three
class ResourceDemo {
    final String resourceName = "DBConnection";  // final variable
    
    void connect() {
        try {
            System.out.println("Connecting to " + resourceName);
            // ... connection logic
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {  // finally block - ALWAYS executes
            System.out.println("Finally: Closing resources");
            // cleanup code here
        }
    }
    
    @Override
    protected void finalize() throws Throwable {  // finalize method
        try {
            System.out.println("Finalize: Cleanup for " + resourceName);
        } finally {
            super.finalize();
        }
    }
}
```

### Effective Final (Java 8+ for Lambdas)
```java
void process() {
    int x = 10;           // Effectively final (not modified)
    // x = 20;           // If uncommented, NOT effectively final
    
    Runnable r = () -> System.out.println(x);  // OK: x is effectively final
}
```

---

## 4.6 Encapsulation and Access Modifiers

### Encapsulation
**Definition**: Binding data and methods together; hiding internal state; providing controlled access via public methods.

> **📋 PYQ Insight**: Encapsulation appeared **7 times** (2021 Q1(a) 6m, 2022 Q5(a) 5m, 2023 Q1(c) 5m, 2024 Q1(a) 5m, 2025 Q1(a) 5m, 2025 Q1(b) 5m, 2026 Q1(d) 5m). "Explain encapsulation with getter/setter program" is a **high-yield 5-10 mark question**. Also appears as short note (2022 Q5(a), 2026 Q1(d)).

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

### Benefits of Encapsulation (Exam Answer Points)
1. **Data Hiding**: Internal implementation hidden from outside
2. **Controlled Access**: Validation in setters (e.g., no negative balance)
3. **Flexibility**: Can change internal logic without breaking external code
4. **Reusability**: Class can be reused with confidence
5. **Testing**: Easier to unit test with controlled interfaces

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

> **Note**: A top-level class can only be `public` or `default` (not `private`/`protected` unless nested).

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

### Protected Access Nuance (⭐ Important for Exams)
```java
package pack1;
public class Parent {
    protected int protectedVar = 10;
}

package pack2;
import pack1.Parent;

class Child extends Parent {
    void test() {
        // Access via INHERITANCE (child object)
        System.out.println(this.protectedVar);    // OK
        System.out.println(super.protectedVar);   // OK
        
        // Access via REFERENCE (parent object) - NOT ALLOWED
        Parent p = new Parent();
        // System.out.println(p.protectedVar);    // ERROR: not in same package
    }
}
```

**Key Rule**: `protected` = package access **PLUS** subclass access (via inheritance only, not via parent reference from outside package)

### Encapsulation Program for Exam (Complete 10-mark version)
```java
// 10-mark encapsulation program with all features
class Student {
    // Private fields (data hiding)
    private String name;
    private int age;
    private double gpa;
    private String studentId;
    private static int count = 0;  // Shared counter
    
    // Constructor with validation
    public Student(String name, int age, double gpa) {
        setName(name);
        setAge(age);
        setGpa(gpa);
        this.studentId = "STU" + (++count);  // Auto-generate ID
    }
    
    // Getters (accessors)
    public String getName() { return name; }
    public int getAge() { return age; }
    public double getGpa() { return gpa; }
    public String getStudentId() { return studentId; }
    public static int getCount() { return count; }
    
    // Setters (mutators) with validation
    public void setName(String name) {
        if (name != null && !name.trim().isEmpty()) {
            this.name = name.trim();
        } else {
            throw new IllegalArgumentException("Name cannot be empty");
        }
    }
    
    public void setAge(int age) {
        if (age >= 16 && age <= 100) {
            this.age = age;
        } else {
            throw new IllegalArgumentException("Age must be 16-100");
        }
    }
    
    public void setGpa(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) {
            this.gpa = gpa;
        } else {
            throw new IllegalArgumentException("GPA must be 0.0-4.0");
        }
    }
    
    // Additional behavior
    public boolean isHonorsStudent() {
        return gpa >= 3.5;
    }
    
    @Override
    public String toString() {
        return String.format("Student[%s: %s, Age: %d, GPA: %.2f, Honors: %s]",
            studentId, name, age, gpa, isHonorsStudent());
    }
}

public class EncapsulationDemo {
    public static void main(String[] args) {
        Student s1 = new Student("Alice", 20, 3.8);
        Student s2 = new Student("Bob", 22, 3.2);
        
        System.out.println(s1);
        System.out.println(s2);
        System.out.println("Total students: " + Student.getCount());
        
        // Validation in action
        try {
            s1.setGpa(5.0);  // Throws exception
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
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

> **📋 PYQ Insight**: GC + `finalize()` appeared **5 times** (2022, 2023 Q4(b) 10m, 2024, 2025 Q5(b) 5m, 2026). "Explain garbage collection and finalize() method" is a **5-10 mark question**. Also appears as short note (2025 Q5(b) 5m).

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

// 4. Island of Isolation (circular references)
class Island {
    Island ref;
}
Island i1 = new Island();
Island i2 = new Island();
i1.ref = i2;
i2.ref = i1;
i1 = null;
i2 = null;  // Both eligible (island of isolation)
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
- ✅ **Deprecated since Java 9** (use try-with-resources or Cleaner API)
- ✅ `System.gc()` only **suggests** GC to run

### Object Resurrection (⭐ Exam Trick Question)
```java
class Resurrect {
    static Resurrect savedRef;  // Static reference to "save" object
    
    @Override
    protected void finalize() throws Throwable {
        System.out.println("finalize() called - resurrecting!");
        savedRef = this;  // Object resurrected! Not eligible for GC anymore
    }
}

public class Test {
    public static void main(String[] args) {
        Resurrect r = new Resurrect();
        r = null;
        System.gc();  // Request GC
        Thread.sleep(100);  // Wait for finalize
        
        if (Resurrect.savedRef != null) {
            System.out.println("Object resurrected!");
        }
        
        // Second GC - finalize() WON'T be called again (only once per object)
        Resurrect.savedRef = null;
        System.gc();
        Thread.sleep(100);
    }
}
```

### Modern Alternatives (Java 7+)
```java
// 1. try-with-resources (AutoCloseable) - Preferred
try (FileInputStream fis = new FileInputStream("file.txt")) {
    // use fis
} // automatically closed

// 2. Cleaner API (Java 9+) - Replaces finalize
class Resource implements AutoCloseable {
    private static final Cleaner cleaner = Cleaner.create();
    private final Cleaner.Cleanable cleanable;
    
    Resource() {
        cleanable = cleaner.register(this, () -> {
            System.out.println("Cleaning up resource");
        });
    }
    
    @Override
    public void close() {
        cleanable.clean();
    }
}
```

### GC Algorithms (Conceptual - Good for Theory)
- **Serial GC**: Single thread, simple, for small apps
- **Parallel GC**: Multiple threads, throughput-focused (default Java 8)
- **G1 GC**: Garbage First, low latency, large heaps (default Java 9+)
- **ZGC / Shenandoah**: Ultra-low latency, large heaps (Java 11+)

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