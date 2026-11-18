# Unit 5: Inheritance

## Unit Overview
This unit covers inheritance basics, advantages, member access, access specifiers in inheritance, types of inheritance, `super` keyword, multilevel hierarchy, constructor execution order, and `final` keyword in inheritance.

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

## 5.2 Advantages of Inheritance

| Advantage | Description |
|-----------|-------------|
| **Code Reusability** | Reuse existing code without rewriting |
| **Time & Effort Saving** | Less development and testing time |
| **Easy Maintenance** | Changes in parent automatically reflect in children |
| **Extensibility** | Add new features without modifying existing code |
| **Hierarchical Classification** | Models real-world relationships |
| **Polymorphism Foundation** | Enables runtime polymorphism via method overriding |

---

## 5.3 Member Access and Inheritance

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

## 5.4 Types of Access Specifiers (Summary)

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

## 5.5 Types of Inheritance

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

## 5.6 The `super` Keyword

### Uses of `super`

| Use | Syntax | Description |
|-----|--------|-------------|
| **1. Call superclass constructor** | `super(args);` | Must be **first statement** in constructor |
| **2. Access superclass method** | `super.methodName();` | When overridden in subclass |
| **3. Access superclass variable** | `super.variableName` | When hidden by subclass variable |

### 5.6.1 Calling Superclass Constructor

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

### 5.6.2 Accessing Superclass Method (Method Overriding)

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

### 5.6.3 Accessing Superclass Variable (Variable Hiding)

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

## 5.7 Creating Multilevel Class Hierarchy

### Concept
Each subclass inherits from its immediate superclass, forming a chain.

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

### Constructor Execution Order in Multilevel Hierarchy
**Order**: Superclass → Subclass (top to bottom)

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

> **Reason**: Superclass has no knowledge of subclass; its initialization may be prerequisite.

---

## 5.8 `final` Keyword in Inheritance

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

## 5.9 Important Exam Questions (from PYQ Analysis)

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

## 5.10 Summary of Unit 5

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

---

## 5.11 Quick Reference: Inheritance Rules

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