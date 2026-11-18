# Unit 5: Inheritance

## Unit Overview
This unit covers inheritance basics, advantages, member access, access specifiers in inheritance, types of inheritance, `super` keyword, multilevel hierarchy, constructor execution order, method overriding, `final` keyword in inheritance, and Object class methods.

## PYQ Frequency: 9/10 years (CRITICAL - Appeared 2021, 2022×2, 2023×2, 2024, 2025×2)
- **2-Mark**: Definition, types, why no multiple inheritance, super keyword uses, constructor order
- **5-Mark**: Advantages + example, super keyword with examples, types with diagrams, multilevel with constructor chaining, final keyword
- **10-Mark**: Inheritance + types + advantages + super keyword (appeared 2021, 2022, 2023, 2024, 2025), Method overriding with rules

---

## 5.1 Basics of Inheritance

### Topic Introduction
Inheritance is a mechanism where a new class acquires properties (fields and methods) of an existing class. It represents an **IS-A relationship** (parent-child).

### Definition
> **Inheritance** is the process by which one class (subclass/child) acquires the properties and behaviors of another class (superclass/parent).

### Syntax
```java
class ChildClass extends ParentClass {
    // Additional fields and methods
}
```

### Terminology
| Term | Synonym | Description |
|------|---------|-------------|
| **Superclass** | Parent class, Base class | Class being inherited from |
| **Subclass** | Child class, Derived class | Class that inherits |

### Key Points
- ✅ Subclass gets all **non-private** members of superclass
- ✅ Subclass can add **new** fields and methods
- ✅ Subclass can **override** inherited methods
- ✅ Java supports **single inheritance** only (one parent)
- ✅ Multiple inheritance achieved via **interfaces**

### Simple Example
```java
class Vehicle {
    void run() {
        System.out.println("Vehicle is running");
    }
}

class Car extends Vehicle {
    void wheels() {
        System.out.println("Car has 4 wheels");
    }
}

public class Test {
    public static void main(String[] args) {
        Car c = new Car();
        c.run();    // Inherited from Vehicle
        c.wheels(); // Own method
    }
}
```

**Output:**
```
Vehicle is running
Car has 4 wheels
```

---

## 5.2 Method Overriding (Runtime Polymorphism) — **CRITICAL: Appeared 2022, 2024, 2025, 2026**

### Definition
> **Method Overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. The method in subclass must have the **same signature** (name, parameters, return type).

### Rules for Method Overriding
| Rule | Description |
|------|-------------|
| **Same Method Signature** | Same name, same parameter list |
| **Return Type** | Same or **covariant** (subclass of superclass return type) — Java 5+ |
| **Access Modifier** | Must be **same or broader** (not narrower) |
| **`final` Methods** | **Cannot be overridden** |
| **`static` Methods** | **Cannot be overridden** (they are **hidden**) |
| **`private` Methods** | **Cannot be overridden** (not inherited) |
| **Constructors** | Cannot be overridden |
| **`@Override` Annotation** | Optional but **recommended** — catches errors at compile time |

### Overriding vs Overloading Comparison

| Aspect | Overloading (Compile-time) | Overriding (Runtime) |
|--------|---------------------------|---------------------|
| **Binding** | Static (early) | Dynamic (late) |
| **Signature** | Must differ (params) | Must be same |
| **Return Type** | Can differ | Same or covariant |
| **Access** | Can be different | Same or broader |
| **Scope** | Same class | Superclass & Subclass |
| **Polymorphism** | Ad-hoc | Subtype |

### Method Overriding Example
```java
class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks: Bow wow");
    }
}

class Cat extends Animal {
    @Override
    void sound() {
        System.out.println("Cat meows: Meow meow");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a1 = new Dog();
        Animal a2 = new Cat();
        Animal a3 = new Animal();
        
        a1.sound();  // Dog barks: Bow wow
        a2.sound();  // Cat meows: Meow meow
        a3.sound();  // Animal makes sound
    }
}
```

**Output:**
```
Dog barks: Bow wow
Cat meows: Meow meow
Animal makes sound
```

### Key Points for Exams
- **Dynamic Method Dispatch**: JVM determines which method to call at **runtime** based on **actual object type**, not reference type
- **Why use overriding?** To achieve **runtime polymorphism** — same interface, different behavior
- **`super.method()`**: Used to call parent's overridden method from child

### Can We Override? — **Frequent 2-Mark Question (2022, 2025)**
| Method Type | Can Override? | Reason |
|-------------|---------------|--------|
| **`private`** | ❌ **No** | Not inherited by subclass |
| **`final`** | ❌ **No** | Explicitly prevented |
| **`static`** | ❌ **No** (hidden) | Belongs to class, not instance |
| **`abstract`** | ✅ **Must override** | Unless subclass is also abstract |
| **`default` (interface)** | ✅ **Yes** | Can be overridden in implementing class |
| **`protected`/`public`** | ✅ **Yes** | Normal overriding rules apply |

> **Exam Answer Format**: "Private methods are not inherited, so cannot be overridden. Final methods cannot be overridden. Static methods are hidden, not overridden (binding is static)."

---

## 5.4 Advantages of Inheritance

| Advantage | Description |
|-----------|-------------|
| **Code Reusability** | Reuse existing code without rewriting |
| **Time & Effort Saving** | Less development and testing time |
| **Easy Maintenance** | Changes in parent automatically reflect in children |
| **Extensibility** | Add new features without modifying existing code |
| **Hierarchical Classification** | Models real-world relationships |
| **Polymorphism Foundation** | Enables runtime polymorphism via method overriding |

---

## 5.5 Member Access and Inheritance

### Access Rules in Inheritance

| Superclass Member | Accessible in Subclass? |
|-------------------|-------------------------|
| `public` | ✅ Yes |
| `protected` | ✅ Yes |
| `default` (package-private) | ✅ Only if same package |
| `private` | ❌ **No** (not inherited) |

### Private Members in Inheritance
```java
class Parent {
    private int secret = 100;
    int visible = 200;
    
    // Private accessible only within Parent
    void show() {
        System.out.println(secret);  // OK
    }
}

class Child extends Parent {
    void display() {
        // System.out.println(secret);  // COMPILE ERROR!
        System.out.println(visible);   // OK
    }
}
```

> **Key Rule**: A subclass inherits all members of superclass but **cannot directly access private members**. Use public/protected getters/setters.

---

## 5.6 Types of Access Specifiers (Summary)

| Modifier | Same Class | Same Package | Subclass (diff pkg) | Non-subclass (diff pkg) |
|----------|------------|--------------|---------------------|-------------------------|
| `private` | ✅ | ❌ | ❌ | ❌ |
| `default` | ✅ | ✅ | ❌ | ❌ |
| `protected` | ✅ | ✅ | ✅ | ❌ |
| `public` | ✅ | ✅ | ✅ | ✅ |

### Protected Access Detail
- **Within package**: Like default (accessible to all)
- **Outside package**: Only accessible in **subclasses** (via inheritance)
- **Not accessible** by non-subclass in different package

```java
package pack1;

class Parent {
    protected void protectedMethod() {
        System.out.println("Protected method");
    }
}

package pack2;
import pack1.Parent;

class Child extends Parent {
    void test() {
        protectedMethod();  // OK: subclass access
    }
}

class Other {
    void test() {
        Parent p = new Parent();
        // p.protectedMethod();  // ERROR: not subclass
    }
}
```

---

## 5.7 Object Class Methods — **Important for Complete Understanding**

Every class in Java implicitly extends `java.lang.Object`. These methods are inherited by all classes:

| Method | Description | Common Override |
|--------|-------------|-----------------|
| `toString()` | Returns string representation | ✅ **Very common** — return meaningful object state |
| `equals(Object obj)` | Checks logical equality | ✅ **Common** — compare content, not reference |
| `hashCode()` | Returns hash code | ✅ **Must override with equals** — contract: equal objects = equal hash |
| `getClass()` | Returns runtime class | ❌ final — cannot override |
| `clone()` | Creates copy | Sometimes — implements Cloneable |
| `finalize()` | Called by GC | Deprecated (Java 9+) — avoid |
| `wait()`, `notify()`, `notifyAll()` | Thread synchronization | Used in multithreading |

### Overriding `toString()` Example
```java
class Student {
    int rollNo;
    String name;
    
    Student(int r, String n) {
        rollNo = r; name = n;
    }
    
    @Override
    public String toString() {
        return "Student[rollNo=" + rollNo + ", name=" + name + "]";
    }
}

public class Test {
    public static void main(String[] args) {
        Student s = new Student(101, "Nikhil");
        System.out.println(s);  // Automatically calls toString()
        // Output: Student[rollNo=101, name=Nikhil]
    }
}
```

### Overriding `equals()` and `hashCode()` Contract
```java
class Student {
    int rollNo;
    String name;
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Student other = (Student) obj;
        return rollNo == other.rollNo && name.equals(other.name);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(rollNo, name);
    }
}
```

> **Exam Tip**: If asked about Object class methods, focus on `toString()`, `equals()`, and `hashCode()` — most commonly tested.

---

## 5.8 Types of Inheritance

### Supported in Java

| Type | Description | Diagram |
|------|-------------|---------|
| **Single** | One parent, one child | A → B |
| **Multilevel** | Chain of inheritance | A → B → C |
| **Hierarchical** | One parent, multiple children | A → B, A → C |

### NOT Supported
| Type | Reason | Alternative |
|------|--------|-------------|
| **Multiple** | Ambiguity (diamond problem) | Use **Interfaces** |

### Examples

#### Single Inheritance
```java
class A { void methodA() {} }
class B extends A { void methodB() {} }
// B has methodA() and methodB()
```

#### Multilevel Inheritance
```java
class GrandParent { void gpMethod() {} }
class Parent extends GrandParent { void pMethod() {} }
class Child extends Parent { void cMethod() {} }
// Child has gpMethod(), pMethod(), cMethod()
```

#### Hierarchical Inheritance
```java
class Parent { void pMethod() {} }
class Child1 extends Parent { void c1Method() {} }
class Child2 extends Parent { void c2Method() {} }
// Both children have pMethod()
```

### Why No Multiple Inheritance?
```java
// This would cause ambiguity:
class A { void show() { System.out.println("A"); } }
class B { void show() { System.out.println("B"); } }

// class C extends A, B {}  // COMPILE ERROR!
// C c = new C();
// c.show();  // Which show()? A's or B's?
```

---

## 5.9 The `super` Keyword — **CRITICAL: Appeared 2021, 2022, 2023, 2024×2, 2025**

### Uses of `super`

| Use | Syntax | Description |
|-----|--------|-------------|
| **1. Call superclass constructor** | `super(args);` | Must be **first statement** in constructor |
| **2. Access superclass method** | `super.methodName();` | When overridden in subclass |
| **3. Access superclass variable** | `super.variableName` | When hidden by subclass variable |

### 5.9.1 Calling Superclass Constructor

```java
class Box {
    double width, height, depth;
    
    Box(double w, double h, double d) {
        width = w; height = h; depth = d;
    }
    
    Box() { width = height = depth = -1; }
    
    Box(double len) { width = height = depth = len; }
    
    double volume() { return width * height * depth; }
}

class BoxWeight extends Box {
    double weight;
    
    BoxWeight(double w, double h, double d, double m) {
        super(w, h, d);  // Calls Box(w, h, d)
        weight = m;
    }
    
    BoxWeight() {
        super();  // Calls Box()
        weight = -1;
    }
    
    BoxWeight(double len, double m) {
        super(len);  // Calls Box(len)
        weight = m;
    }
}
```

### 5.9.2 Accessing Superclass Method (Method Overriding)

```java
class Animal {
    void sound() {
        System.out.println("Animal makes sound");
    }
}

class Dog extends Animal {
    @Override
    void sound() {
        super.sound();  // Calls Animal's sound()
        System.out.println("Dog barks: Bow wow");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.sound();
    }
}
```

**Output:**
```
Animal makes sound
Dog barks: Bow wow
```

### 5.9.3 Accessing Superclass Variable (Variable Hiding)

```java
class A {
    int i = 10;
}

class B extends A {
    int i = 20;  // Hides A's i
    
    B(int a, int b) {
        super.i = a;  // A's i
        i = b;        // B's i
    }
    
    void show() {
        System.out.println("Superclass i: " + super.i);
        System.out.println("Subclass i: " + i);
    }
}

public class Test {
    public static void main(String[] args) {
        B obj = new B(5, 10);
        obj.show();
    }
}
```

**Output:**
```
Superclass i: 5
Subclass i: 10
```

---

## 5.10 Creating Multilevel Class Hierarchy — **CRITICAL: Constructor Order Appeared 2022 (10 marks)**

### Concept
Each subclass inherits from its immediate superclass, forming a chain.

### Constructor Execution Order in Multilevel Hierarchy — **Exam Favorite**
**Order**: Superclass → Subclass (top to bottom)

**Reason**: Superclass has no knowledge of subclass; its initialization may be prerequisite.

```java
class Student {
    int rollNo;
    String name;
    
    Student(int r, String n) {
        rollNo = r; name = n;
    }
    
    void show() {
        System.out.println("Roll: " + rollNo + ", Name: " + name);
    }
}

class Marks extends Student {
    int m1, m2, m3, total;
    
    Marks(int r, String n, int m1, int m2, int m3) {
        super(r, n);  // Call Student constructor
        this.m1 = m1; this.m2 = m2; this.m3 = m3;
    }
    
    void showMarks() {
        show();  // Call Student's show()
        total = m1 + m2 + m3;
        System.out.println("Total: " + total);
    }
}

class Percentage extends Marks {
    float percent;
    
    Percentage(int r, String n, int m1, int m2, int m3, float p) {
        super(r, n, m1, m2, m3);  // Call Marks constructor
        percent = p;
    }
    
    void showPercent() {
        showMarks();  // Call Marks's showMarks()
        percent = total / 3;
        System.out.println("Percentage: " + percent + "%");
    }
}
```

```java
class GrandParent {
    GrandParent() { System.out.println("GrandParent constructor"); }
}

class Parent extends GrandParent {
    Parent() { System.out.println("Parent constructor"); }
}

class Child extends Parent {
    Child() { System.out.println("Child constructor"); }
}

public class Test {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
```

**Output:**
```
GrandParent constructor
Parent constructor
Child constructor
```

---

## 5.11 `final` Keyword in Inheritance — **Appeared 2022, 2025**

### 1. Final Variable
- Cannot be modified after initialization
- Used for constants

### 2. Final Method
- **Cannot be overridden** by subclass
- Ensures implementation is fixed

```java
class Parent {
    final void show() {
        System.out.println("Final method - cannot override");
    }
}

class Child extends Parent {
    // void show() {}  // COMPILE ERROR!
}
```

### 3. Final Class
- **Cannot be extended** (no inheritance)
- All methods implicitly final

```java
final class Parent {
    void method() {}
}

// class Child extends Parent {}  // COMPILE ERROR!
```

---

## 5.12 Important Exam Questions (from PYQ Analysis)

### High Priority (CRITICAL - Appeared 9/10 years)

**2-Mark Questions:**
1. What is inheritance? Syntax.
2. Types of inheritance supported in Java.
3. Why multiple inheritance not supported?
4. What is `super` keyword? Two uses.
5. Difference between `super()` and `this()`.
6. What is method overriding?
7. Can we override private method? Final method? Static method?
8. Constructor execution order in multilevel inheritance.

**5-Mark Questions:**
1. Explain inheritance with advantages and example program.
2. Explain `super` keyword with examples (constructor call, method access, variable access).
3. Explain types of inheritance with diagrams.
4. Explain multilevel inheritance with constructor chaining example.
5. Explain `final` keyword in inheritance (variable, method, class).
6. Why Java doesn't support multiple inheritance? How to achieve it?

**10-Mark Questions:**
1. **What is inheritance? Explain types with code. Explain advantages. Explain `super` keyword uses.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Explain method overriding with rules. Difference between overloading and overriding.
3. Explain multilevel inheritance with constructor execution order.

### Programs to Practice
1. ✅ **Inheritance demo (Vehicle → Car/Truck)** - appeared 2022, 2024, 2025
2. ✅ **`super` keyword (constructor call)** - appeared 2021, 2022, 2023, 2024, 2025
3. ✅ **Method overriding example** - appeared 2022, 2024, 2025, 2026
4. ✅ **Multilevel inheritance (Student → Marks → Percentage)** - appeared 2022
5. ✅ **Constructor execution order** - appeared 2022

---

### 2024 Q1(d) - 10 Marks: Vehicle → Two-wheeler/Four-wheeler (Exact Exam Question)
```java
class Vehicle {
    String brand;
    int maxSpeed;
    
    Vehicle(String b, int s) {
        brand = b;
        maxSpeed = s;
    }
    
    void display() {
        System.out.println("Brand: " + brand);
        System.out.println("Max Speed: " + maxSpeed);
    }
}

class TwoWheeler extends Vehicle {
    boolean hasCarrier;
    
    TwoWheeler(String b, int s, boolean c) {
        super(b, s);  // Call Vehicle constructor
        hasCarrier = c;
    }
    
    @Override
    void display() {
        super.display();  // Call Vehicle's display()
        System.out.println("Has Carrier: " + hasCarrier);
    }
}

class FourWheeler extends Vehicle {
    int numDoors;
    boolean hasAC;
    
    FourWheeler(String b, int s, int d, boolean ac) {
        super(b, s);  // Call Vehicle constructor
        numDoors = d;
        hasAC = ac;
    }
    
    @Override
    void display() {
        super.display();  // Call Vehicle's display()
        System.out.println("Number of Doors: " + numDoors);
        System.out.println("Has AC: " + hasAC);
    }
}

public class Test {
    public static void main(String[] args) {
        TwoWheeler tw = new TwoWheeler("Honda", 120, true);
        FourWheeler fw = new FourWheeler("Toyota", 180, 4, true);
        
        System.out.println("--- Two Wheeler ---");
        tw.display();
        
        System.out.println("\n--- Four Wheeler ---");
        fw.display();
    }
}
```

**Output:**
```
--- Two Wheeler ---
Brand: Honda
Max Speed: 120
Has Carrier: true

--- Four Wheeler ---
Brand: Toyota
Max Speed: 180
Number of Doors: 4
Has AC: true
```

> **Exam Pattern**: This exact hierarchy appeared in **2024 Q1(d) for 10 marks** — "Inheritance + Vehicle/Two-wheeler/Four-wheeler". Practice this thoroughly!

---

## 5.13 Summary of Unit 5

| Topic | Key Points |
|-------|------------|
| **Inheritance** | IS-A relationship; `extends` keyword; code reusability |
| **Types Supported** | Single, Multilevel, Hierarchical |
| **Not Supported** | Multiple (use interfaces) |
| **Member Access** | Private not inherited; protected accessible in subclass across packages |
| **`super`** | 1) Call super constructor `super()` 2) Call super method `super.method()` 3) Access super variable `super.var` |
| **Constructor Order** | Top-down (superclass first) |
| **`final`** | Variable=constant, Method=can't override, Class=can't extend |
| **Method Overriding** | Same signature; runtime polymorphism; `@Override` annotation |
| **Object Class** | `toString()`, `equals()`, `hashCode()` commonly overridden |

---

## 5.14 Quick Reference: Inheritance Rules

| Rule | Description |
|------|-------------|
| Private members | Not inherited (not accessible in subclass) |
| Constructors | Not inherited (but superclass constructor called via `super()`) |
| Static methods | Hidden, not overridden |
| Final methods | Cannot be overridden |
| Final class | Cannot be extended |
| `super()` call | Must be first statement in constructor |
| Overriding rules | Same signature, same/broader access, same return (covariant allowed) |
| `@Override` | Annotation to catch errors at compile time |

---

## 5.15 PYQ Comparison Questions (Frequently Asked 2-5 Marks)

Based on 10-year analysis, these comparison questions appear frequently:

### 1. Multiple vs Multilevel Inheritance (2023 Q1d - 5 marks)
| Aspect | Multiple Inheritance | Multilevel Inheritance |
|--------|---------------------|------------------------|
| **Definition** | One class inherits from **multiple** parents | Chain of inheritance: A → B → C |
| **Java Support** | ❌ **Not supported** (directly) | ✅ **Supported** |
| **Ambiguity** | Diamond problem | No ambiguity |
| **Alternative** | Use **interfaces** | Native `extends` chain |

```java
// Multiple - NOT ALLOWED
// class C extends A, B {}  // Error

// Multilevel - ALLOWED
class A {}
class B extends A {}
class C extends B {}
```

### 2. Hierarchical vs Multiple Inheritance (2023 Q1e - 5 marks)
| Aspect | Hierarchical Inheritance | Multiple Inheritance |
|--------|-------------------------|---------------------|
| **Definition** | One parent, **multiple children** | One child, **multiple parents** |
| **Java Support** | ✅ **Supported** | ❌ **Not supported** |
| **Example** | A → B, A → C | C extends A, B (not allowed) |
| **Use Case** | Common base class for variants | Need features from multiple classes |

```java
// Hierarchical - ALLOWED
class Parent {}
class Child1 extends Parent {}
class Child2 extends Parent {}

// Multiple - NOT ALLOWED
// class Child extends Parent1, Parent2 {}  // Error
```

### 3. Overloading vs Overriding (2023 Q1e - 5 marks, 2026 Q4b - 10 marks)
| Aspect | Overloading | Overriding |
|--------|-------------|------------|
| **Also Called** | Compile-time polymorphism | Runtime polymorphism |
| **Binding** | Static (early) | Dynamic (late) |
| **Signature** | Must differ (parameters) | Must be **same** |
| **Return Type** | Can be different | Same or covariant |
| **Access Modifier** | Can be different | Same or broader |
| **Scope** | Same class | Superclass & Subclass |
| **Inheritance** | Not required | **Required** |
| **`static` Methods** | Can be overloaded | **Hidden**, not overridden |
| **`final` Methods** | Can be overloaded | **Cannot** be overridden |
| **`private` Methods** | Can be overloaded | **Cannot** be overridden |

### 4. `super()` vs `this()` (2022 Q4b - 5 marks, 2025 Q1e - 5 marks)
| Aspect | `super()` | `this()` |
|--------|-----------|----------|
| **Calls** | **Superclass constructor** | **Same class constructor** |
| **Purpose** | Initialize parent state | Constructor chaining within class |
| **Position** | Must be **first statement** | Must be **first statement** |
| **Default** | `super()` called implicitly if not written | Never implicit |
| **Inheritance** | Related to inheritance | **No inheritance needed** |

```java
class Parent {
    Parent() { System.out.println("Parent"); }
    Parent(int x) { System.out.println("Parent: " + x); }
}

class Child extends Parent {
    Child() {
        super();        // Calls Parent() - OK
        // this();       // Would call Child() - recursive!
    }
    Child(int x) {
        this();         // Calls Child() - OK
        super(x);       // ERROR: super() not first!
    }
}
```

### 5. `final` vs `finally` vs `finalize` (2023 Q5b - 6 marks, 2024 Q2a - 5 marks)
| Keyword | Type | Purpose |
|---------|------|---------|
| **`final`** | Modifier | Variable=constant, Method=can't override, Class=can't extend |
| **`finally`** | Block | Executes **always** after try/catch (cleanup code) |
| **`finalize()`** | Method (Object) | Called by **GC** before object destruction (deprecated Java 9+) |

```java
final int MAX = 100;           // final variable - constant
final void show() {}           // final method - cannot override
final class MyClass {}         // final class - cannot extend

try {
    // risky code
} catch (Exception e) {
    // handle
} finally {
    // ALWAYS executes - cleanup (close resources)
}

// @Deprecated (Java 9+)
protected void finalize() throws Throwable {
    // cleanup before GC - avoid using
}
```

### 6. Abstract Class vs Interface (2022 Q5c - 5 marks, 2023 Q1e/1g - 5 marks each, 2024 Q2c - 10 marks, 2025 Q1b - 5 marks)
| Aspect | Abstract Class | Interface |
|--------|----------------|-----------|
| **Keyword** | `abstract class` | `interface` |
| **Inheritance** | `extends` (single) | `implements` (multiple) |
| **Methods** | Abstract + concrete | Abstract + default + static (Java 8+) |
| **Variables** | Any (instance, static, final) | Only `public static final` (constants) |
| **Constructors** | ✅ Can have | ❌ Cannot have |
| **Access Modifiers** | Any | Methods: `public` only (default for abstract) |
| **Multiple** | ❌ One only | ✅ Multiple allowed |
| **Use When** | Shared code + IS-A relationship | Contract + multiple implementations |