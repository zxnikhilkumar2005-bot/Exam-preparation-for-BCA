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

> **📋 PYQ Insight**: String handling appeared in **2021 Q1(d)** (String vs StringBuffer, 5m), **2022 Q1(b)** (String length program, 5m), **2023 Q3(a)** (String reverse program, 5m), **2024 Q2(c)** (String reverse + length, 5m), **2025 Q1(f)** (String length + first char, 5m). "String reverse + length program" appeared **4 times** (2022, 2023, 2024, 2025). "Explain String immutability" and "Difference between String, StringBuilder, StringBuffer" are **5-10 mark questions**.

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

### String Constant Pool vs Heap (⭐ Important Concept)
```java
String s1 = "Hello";           // Pool
String s2 = "Hello";           // Pool (same as s1)
String s3 = new String("Hello"); // Heap (new object)
String s4 = new String("Hello"); // Heap (another new object)

s1 == s2   // true  (same pool reference)
s1 == s3   // false (pool vs heap)
s1.equals(s3) // true (content comparison)

// intern() - moves to pool / returns pool reference
String s5 = new String("Hello").intern();  // Returns pool reference
s1 == s5   // true
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

### Why String is Immutable? (Exam Theory)
1. **String Pool**: Sharing requires immutability
2. **Security**: Network params, file paths, DB URLs can't be changed
3. **Thread Safety**: Immutable = inherently thread-safe
4. **Performance**: Hashcode cached, substring sharing (pre-Java 7)
5. **Class Loading**: Class names as Strings must be immutable

### String Reverse + Length Program (⭐⭐⭐ High Yield - appeared 4 times)
```java
// Method 1: Using StringBuilder (recommended)
public static String reverse(String str) {
    return new StringBuilder(str).reverse().toString();
}

// Method 2: Using char array (manual - often asked in exams)
public static String reverseManual(String str) {
    char[] chars = str.toCharArray();
    int left = 0, right = chars.length - 1;
    while (left < right) {
        char temp = chars[left];
        chars[left] = chars[right];
        chars[right] = temp;
        left++;
        right--;
    }
    return new String(chars);
}

// Method 3: Using recursion (theoretical)
public static String reverseRecursive(String str) {
    if (str.isEmpty()) return str;
    return reverseRecursive(str.substring(1)) + str.charAt(0);
}

// Complete Exam Program
public class StringReverseDemo {
    public static void main(String[] args) {
        String input = "Hello World";
        
        // Length
        System.out.println("Length: " + input.length());  // 11
        
        // Reverse
        String reversed = reverse(input);
        System.out.println("Reversed: " + reversed);  // "dlroW olleH"
        
        // First character (2025 Q1(f))
        System.out.println("First char: " + input.charAt(0));  // 'H'
    }
    
    static String reverse(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}
```

### String vs StringBuilder vs StringBuffer

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread Safety** | N/A (immutable) | Not synchronized | Synchronized |
| **Performance** | Fast for reads | Fastest for modifications | Slower (sync overhead) |
| **Use Case** | Constant strings | Single-threaded modifications | Multi-threaded modifications |
| **Java Version** | 1.0 | 5.0 | 1.0 |

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

// Performance Demo
public class PerformanceDemo {
    public static void main(String[] args) {
        long start, end;
        
        // String concatenation (slow - creates many objects)
        String s = "";
        start = System.currentTimeMillis();
        for (int i = 0; i < 10000; i++) s += "a";
        end = System.currentTimeMillis();
        System.out.println("String: " + (end - start) + "ms");
        
        // StringBuilder (fast)
        StringBuilder sb = new StringBuilder();
        start = System.currentTimeMillis();
        for (int i = 0; i < 10000; i++) sb.append("a");
        end = System.currentTimeMillis();
        System.out.println("StringBuilder: " + (end - start) + "ms");
        
        // StringBuffer (slower due to sync)
        StringBuffer sbf = new StringBuffer();
        start = System.currentTimeMillis();
        for (int i = 0; i < 10000; i++) sbf.append("a");
        end = System.currentTimeMillis();
        System.out.println("StringBuffer: " + (end - start) + "ms");
    }
}
```

### Additional String Methods for Exams
```java
String s = "  Hello World  ";

// Formatting
String.format("Name: %s, Age: %d", "Alice", 20);  // "Name: Alice, Age: 20"

// Join (Java 8+)
String.join(", ", "Apple", "Banana", "Cherry");  // "Apple, Banana, Cherry"

// Lines (Java 11+)
"Line1\nLine2\nLine3".lines().forEach(System.out::println);

// Strip (Java 11+) - Unicode-aware trim
"  Hello  ".strip();  // "Hello" (better than trim() for Unicode)

// Repeat (Java 11+)
"Ha".repeat(3);  // "HaHaHa"

// Blank check (Java 11+)
"  ".isBlank();  // true (only whitespace)
"".isBlank();    // true
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
13. **Difference between `final`, `finally`, `finalize`** (⭐ 2023 Q5(b) 6m, 2025 Q5(d))
14. **Difference between `throw` and `throws`** (⭐ 2023 Q5(b), 2025, 2026)
15. **Difference between overloading and overriding** (⭐ 2023 Q1(e), 2026)
16. **Difference between abstract class and interface** (⭐ 2022, 2023, 2024, 2025, 2026)

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
11. **Explain constructor chaining with `this()` and `super()`** (⭐ 2022 Q2(a) 10m)
12. **Why parameterized constructor needed?** (⭐ 2022, 2024, 2025, 2026)
13. **Static block vs instance block vs constructor execution order** (⭐ Theory)
14. **Protected access in different package via inheritance vs reference** (⭐ Nuance)

**10-Mark Questions:**
1. What is a class? Explain constructors, `this`, `static`, `final` with comprehensive example.
2. Explain encapsulation in detail with access modifiers and a complete program.
3. Explain memory management in Java: object creation, garbage collection, finalize.
4. **Inheritance + Constructor chaining order in multilevel** (⭐ 2022 Q2(a) 10m)
5. **final vs finally vs finalize with examples** (⭐ 2023 Q5(b) 6m)

### Programs to Practice (High Yield)
1. ✅ **Encapsulation with getter/setter** - appeared 2021, 2022, 2024, 2025, 2026
2. ✅ **Constructor overloading** - appeared 2022, 2023, 2024, 2025, 2026
3. ✅ **Constructor chaining with `this`** - appeared 2022
4. ✅ **Static variable/method demo** - appeared 2023, 2026
5. ✅ **Final variable/method/class** - appeared 2022, 2023, 2024, 2025, 2026
6. ✅ **String reverse + length** - appeared 2022, 2023, 2024, 2025
7. ✅ **Object assignment/reference** - appeared 2024
8. ✅ **Constructor chaining with `super()` in multilevel inheritance** - 2022 Q2(a)
9. ✅ **final vs finally vs finalize demo** - 2023 Q5(b), 2025 Q5(d)
10. ✅ **Protected access demo (inheritance vs reference)** - Theory nuance

---

## 4.10 Summary of Unit 4

| Topic | Key Points |
|-------|------------|
| **Class** | Blueprint with fields, methods, constructors |
| **Object** | Instance of class; created with `new`; reference vs object |
| **Constructor** | Same name as class; no return type; default/parameterized/overloaded; chaining with `this()`/`super()` |
| **`this`** | Current object reference; resolves conflicts; constructor chaining; pass/return self |
| **`static`** | Class-level; shared; accessed via class name; no `this`; static blocks init order |
| **`final`** | Variable=constant, Method=can't override, Class=can't extend; blank final in constructor |
| **Encapsulation** | Private fields + public getters/setters; validation in setters |
| **Access Modifiers** | private < default < protected < public; protected=package+subclass(inheritance) |
| **Garbage Collection** | Automatic; daemon thread; non-deterministic; finalize() deprecated Java 9; Cleaner API |
| **String** | Immutable; pool for literals; many utility methods; reverse/length high yield |
| **StringBuilder** | Mutable; non-synchronized; fast; single-threaded |
| **StringBuffer** | Mutable; synchronized; thread-safe; legacy |

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

### final vs finally vs finalize (⭐⭐⭐ 2023 Q5(b) 6m, 2025 Q5(d))
| Aspect | `final` | `finally` | `finalize()` |
|--------|---------|-----------|--------------|
| **Type** | Keyword/Modifier | Block | Method |
| **Purpose** | Restrict modification | Cleanup (always runs) | GC cleanup (deprecated) |
| **Applies To** | Variable, Method, Class, Parameter | try-catch-finally | Object class |
| **Guarantee** | Compile-time | Runtime (always*) | Not guaranteed |
| **Since/Deprecated** | Java 1.0 | Java 1.0 | Java 1.0 / Deprecated Java 9 |

*except `System.exit()`, infinite loop, or JVM crash

### Access Modifiers Quick Reference
| Modifier | Same Class | Same Package | Subclass (Diff Pkg) | World |
|----------|------------|--------------|---------------------|-------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ (via inheritance) | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

### Static vs Instance Members
| Aspect | Static | Instance |
|--------|--------|----------|
| Memory | Class area (once) | Heap (per object) |
| Access | `ClassName.member` | `object.member` |
| `this` reference | Not available | Available |
| Can access | Only static members | Both static & instance |
| Override | Cannot override (can hide) | Can override |

### Protected Access Nuance (⭐ Exam Important)
| Access Via | Same Package | Different Package (Subclass) | Different Package (Non-subclass) |
|------------|--------------|------------------------------|----------------------------------|
| `this.protectedVar` | ✅ | ✅ | ❌ |
| `super.protectedVar` | ✅ | ✅ | ❌ |
| `parentRef.protectedVar` | ✅ | ❌ | ❌ |

**Rule**: Protected = Package access + **Inheritance-based** access in subclass (not reference-based)

### String Creation Methods
| Method | Pool? | New Object? | Use Case |
|--------|-------|-------------|----------|
| `String s = "Hello"` | ✅ Yes | ❌ (reuse) | Preferred for literals |
| `String s = new String("Hello")` | ❌ No | ✅ Always | Rarely needed |
| `String s = "Hello".intern()` | ✅ Yes | ❌ (pool) | Explicit pooling |

---

## 4.12 Comprehensive 10-Mark Exam Program (Combines Multiple Topics)

This program demonstrates: **Class/Object, Constructor Overloading, `this` chaining, `static`, `final`, Encapsulation, Access Modifiers, String handling**

```java
// ⭐⭐⭐ COMPREHENSIVE 10-MARK PROGRAM - Covers Unit 4 Core Topics ⭐⭐⭐

// Base class demonstrating final, static, encapsulation
final class University {  // final class - cannot extend
    static final String UNIVERSITY_NAME = "IGNOU";  // final static constant
    static int totalStudents = 0;  // static variable
    
    private String campus;  // encapsulated
    
    University(String campus) {
        this.campus = campus;
    }
    
    public String getCampus() { return campus; }
    public void setCampus(String campus) { this.campus = campus; }
    
    static void showTotalStudents() {
        System.out.println("Total Students: " + totalStudents);
    }
}

// Student class - demonstrates all Unit 4 concepts
class Student {
    // Private fields (Encapsulation)
    private String name;
    private int age;
    private final String studentId;  // final instance variable (blank final)
    private double gpa;
    private static int idCounter = 0;  // static counter
    
    // Constructor overloading with this() chaining
    public Student() {
        this("Unknown", 0, 0.0);  // this() chaining
    }
    
    public Student(String name, int age) {
        this(name, age, 0.0);  // this() chaining
    }
    
    public Student(String name, int age, double gpa) {
        // this resolves name conflicts
        this.name = validateName(name);
        this.age = validateAge(age);
        this.gpa = validateGpa(gpa);
        this.studentId = "STU" + (++idCounter);  // blank final initialized
        University.totalStudents++;  // access static from other class
    }
    
    // Private validation methods (encapsulation helper)
    private String validateName(String name) {
        if (name == null || name.trim().isEmpty()) 
            throw new IllegalArgumentException("Name required");
        return name.trim();
    }
    
    private int validateAge(int age) {
        if (age < 16 || age > 100) 
            throw new IllegalArgumentException("Age 16-100");
        return age;
    }
    
    private double validateGpa(double gpa) {
        if (gpa < 0.0 || gpa > 4.0) 
            throw new IllegalArgumentException("GPA 0.0-4.0");
        return gpa;
    }
    
    // Getters (accessors)
    public String getName() { return name; }
    public int getAge() { return age; }
    public String getStudentId() { return studentId; }
    public double getGpa() { return gpa; }
    
    // Setters (mutators) with validation
    public void setName(String name) { this.name = validateName(name); }
    public void setAge(int age) { this.age = validateAge(age); }
    public void setGpa(double gpa) { this.gpa = validateGpa(gpa); }
    
    // Method demonstrating this reference return (method chaining)
    public Student updateGpa(double newGpa) {
        setGpa(newGpa);
        return this;  // return current object for chaining
    }
    
    // final method - cannot override
    public final void printIdCard() {
        System.out.println("=== ID CARD ===");
        System.out.println("University: " + University.UNIVERSITY_NAME);
        System.out.println("ID: " + studentId);
        System.out.println("Name: " + name);
    }
    
    // String handling demo
    public String getReversedName() {
        return new StringBuilder(name).reverse().toString();
    }
    
    public int getNameLength() {
        return name.length();
    }
    
    @Override
    public String toString() {
        return String.format("Student[%s: %s, Age: %d, GPA: %.2f]", 
            studentId, name, age, gpa);
    }
}

// Demo class
public class ComprehensiveDemo {
    public static void main(String[] args) {
        System.out.println("=== UNIT 4 COMPREHENSIVE DEMO ===\n");
        
        // 1. Constructor overloading + this() chaining
        Student s1 = new Student();
        Student s2 = new Student("Alice", 20);
        Student s3 = new Student("Bob", 22, 3.8);
        
        System.out.println("1. Constructor Overloading:");
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
        
        // 2. Encapsulation with validation
        System.out.println("\n2. Encapsulation + Validation:");
        try {
            s2.setGpa(5.0);  // Will throw exception
        } catch (IllegalArgumentException e) {
            System.out.println("Validation Error: " + e.getMessage());
        }
        s2.setGpa(3.9);
        System.out.println("Updated: " + s2);
        
        // 3. Method chaining (this return)
        System.out.println("\n3. Method Chaining:");
        s3.updateGpa(4.0).updateGpa(3.7);  // Chaining!
        System.out.println("After chaining: " + s3);
        
        // 4. Static members
        System.out.println("\n4. Static Variables/Methods:");
        University.showTotalStudents();  // 3
        System.out.println("University: " + University.UNIVERSITY_NAME);
        
        // 5. Final variable (studentId cannot change)
        System.out.println("\n5. Final Instance Variable:");
        System.out.println("ID (final): " + s3.getStudentId());
        // s3.studentId = "NEW";  // COMPILE ERROR
        
        // 6. String handling
        System.out.println("\n6. String Methods:");
        System.out.println("Name: " + s3.getName());
        System.out.println("Reversed: " + s3.getReversedName());
        System.out.println("Length: " + s3.getNameLength());
        
        // 7. Object reference vs object (assignment)
        System.out.println("\n7. Object Reference Behavior:");
        Student s4 = s3;  // Same object!
        s4.setName("Charlie");
        System.out.println("s3 name: " + s3.getName());  // "Charlie"
        System.out.println("s4 name: " + s4.getName());  // "Charlie"
        System.out.println("s3 == s4: " + (s3 == s4));   // true
        
        // 8. Final class cannot extend
        // class NewUni extends University {}  // COMPILE ERROR
        
        // 9. Final method cannot override
        s3.printIdCard();  // Works
        // class GradStudent extends Student { void printIdCard(){} } // ERROR
        
        System.out.println("\n=== ALL UNIT 4 CONCEPTS DEMONSTRATED ===");
    }
}
```

---

## 4.13 Common Exam Pitfalls & Mistakes to Avoid

| Pitfall | Wrong | Correct | Why |
|---------|-------|---------|-----|
| **`this()` not first** | `Student() { int x=1; this("a"); }` | `Student() { this("a"); int x=1; }` | `this()`/`super()` MUST be first statement |
| **Static accessing instance** | `static void m() { this.x = 1; }` | `static void m() { /* no this */ }` | Static has no `this` reference |
| **Final variable not init** | `final int x; // in class` | `final int x = 10;` or init in ALL constructors | Blank final must be initialized |
| **Protected via reference** | `Parent p = new Parent(); p.protectedVar` (diff pkg) | `this.protectedVar` or `super.protectedVar` | Protected = inheritance access only in diff pkg |
| **== vs equals** | `s1 == s2` for content | `s1.equals(s2)` | `==` compares references |
| **String concat in loop** | `s += "a"` in loop | `StringBuilder sb; sb.append("a")` | String immutable = O(n²) objects |
| **finalize() reliance** | Rely on finalize for cleanup | Use try-with-resources / Cleaner | finalize deprecated, not guaranteed |
| **Default constructor gone** | Define param constructor, use default | Define default explicitly if needed | Compiler only provides if NO constructor defined |
| **Constructor override** | `@Override Student() {}` | Not possible | Constructors not inherited, cannot override |
| **Static method override** | `@Override static void m() {}` | `static void m()` in child (hiding) | Static methods hidden, not overridden |

---

## 4.14 Memory Management Deep Dive (For 10-Mark Theory)

### Object Memory Layout
```
┌─────────────────────────────────────────────────────────────┐
│                      HEAP                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Object Header│  │ Instance     │  │ Padding      │      │
│  │ (12-16 bytes)│  │ Data         │  │ (alignment)  │      │
│  │ - Mark Word  │  │ - Fields     │  │              │      │
│  │ - Class Ptr  │  │ - final      │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Reference (4/8 bytes on 32/64-bit)
                              │
┌─────────────────────────────────────────────────────────────┐
│                      STACK                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Local Vars   │  │ Operand Stack│  │ Frame Data   │      │
│  │ (references) │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

### GC Roots (What Keeps Objects Alive)
1. **Local variables** in stack frames
2. **Active threads** 
3. **Static variables** of loaded classes
4. **JNI references** (native code)
5. **Synchronized locks** (monitor objects)

### Generational GC (Conceptual)
```
Young Generation (Eden + S0 + S1)     Old Generation (Tenured)
├─ Minor GC (fast, frequent)          ├─ Major GC (slow, rare)
├─ Short-lived objects                ├─ Long-lived objects
└─ Survivor spaces                    └─ Promoted from Young
```

### Memory Leaks in Java (Yes, they exist!)
```java
// 1. Static collections holding references
static List<Object> cache = new ArrayList<>();
cache.add(largeObject);  // Never removed = leak

// 2. Listeners not removed
button.addListener(listener);  // If button lives longer = leak

// 3. ThreadLocal not cleaned
ThreadLocal<Connection> tl = new ThreadLocal<>();
tl.set(conn);  // Thread pool reuses threads = leak

// 4. String.intern() abuse (pre-Java 7 PermGen, now Metaspace)
String s = hugeString.intern();  // Stays in pool forever
```

---

## 4.15 Quick Revision Checklist (Before Exam)

- [ ] **Class vs Object**: Definition, memory, reference vs object
- [ ] **Constructors**: Default, parameterized, overloading, chaining (`this()`/`super()`)
- [ ] **`this` keyword**: 4 uses (variable, constructor, argument, return)
- [ ] **`static`**: Variables, methods, blocks, initialization order, why main static
- [ ] **`final`**: Variable (blank final), method, class, parameter, effectively final
- [ ] **Encapsulation**: Private + getters/setters, validation, benefits
- [ ] **Access Modifiers**: Table, protected nuance (inheritance vs reference)
- [ ] **Garbage Collection**: Eligibility, finalize(), resurrection, modern alternatives
- [ ] **String**: Immutable, pool vs heap, == vs equals, reverse/length program
- [ ] **StringBuilder/Buffer**: Differences, performance, when to use
- [ ] **final vs finally vs finalize**: Clear differentiation with examples
- [ ] **Programs**: Encapsulation, Constructor chaining, String reverse, Object reference

---

*Unit 4 Complete - Ready for Exam Preparation!*