# Unit 6: Polymorphism

## Unit Overview
This unit covers polymorphism basics, types (static/dynamic), method overloading, method overriding, abstract classes, and abstract class vs interface comparison.

---

## 6.1 Introduction to Polymorphism

### Definition
> **Polymorphism** (Greek: *poly* = many, *morph* = forms) is the ability of an object to take many forms. It allows one interface to be used for a general class of actions.

### Core Concept
- One interface, multiple implementations
- Achieved through inheritance
- Object can pass multiple IS-A tests

```java
// Example: One interface, multiple forms
class Shape {
    void draw() { System.out.println("Drawing shape"); }
}

class Circle extends Shape {
    @Override void draw() { System.out.println("Drawing circle"); }
}

class Rectangle extends Shape {
    @Override void draw() { System.out.println("Drawing rectangle"); }
}

class Triangle extends Shape {
    @Override void draw() { System.out.println("Drawing triangle"); }
}

// Usage
Shape s1 = new Circle();
Shape s2 = new Rectangle();
Shape s3 = new Triangle();

s1.draw();  // Drawing circle
s2.draw();  // Drawing rectangle
s3.draw();  // Drawing triangle
```

---

## 6.2 Advantages of Polymorphism

| Advantage | Description |
|-----------|-------------|
| **Code Reusability** | Existing classes reused without modification |
| **Flexibility** | New classes added without changing existing code |
| **Extensibility** | Easy to add new types |
| **Maintainability** | Changes in superclass affect all subclasses |
| **Reduced Coupling** | Code depends on interface, not concrete implementation |
| **Single Variable** | One reference variable can hold multiple object types |

---

## 6.3 Types of Polymorphism

### Classification

```
                    Polymorphism
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
   Static Polymorphism          Dynamic Polymorphism
   (Compile-time)               (Runtime)
        │                             │
        ▼                             ▼
   Method Overloading          Method Overriding
```

### Comparison Table

| Aspect | Static (Compile-time) | Dynamic (Runtime) |
|--------|----------------------|-------------------|
| **Also Called** | Early Binding | Late Binding |
| **Resolved By** | Compiler | JVM |
| **Mechanism** | Method Overloading | Method Overriding |
| **Performance** | Faster | Slightly slower |
| **Flexibility** | Less | More |

---

## 6.4 Method Overloading (Static Polymorphism)

### Definition
Multiple methods in the **same class** with the **same name** but **different parameter lists**.

### Ways to Overload

| Method | Description | Example |
|--------|-------------|---------|
| **1. Different number of parameters** | Change parameter count | `sum(int, int)` vs `sum(int, int, int)` |
| **2. Different data types** | Change parameter types | `sum(int, int)` vs `sum(double, double)` |
| **3. Different sequence** | Change parameter order | `sum(int, double)` vs `sum(double, int)` |

> **Note**: Return type **alone** cannot differentiate overloaded methods.

### Rules
- ✅ Must have different parameter list (signature)
- ✅ Return type can be same or different
- ✅ Access modifiers can be different
- ✅ Can throw different exceptions
- ❌ Cannot overload based only on return type

### Example
```java
class Calculator {
    // 1. Different number of parameters
    int add(int a, int b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
    
    // 2. Different data types
    double add(double a, double b) { return a + b; }
    
    // 3. Different sequence
    void show(int a, String s) { System.out.println(s + ": " + a); }
    void show(String s, int a) { System.out.println(s + ": " + a); }
}

public class Test {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.println(c.add(10, 20));        // 30
        System.out.println(c.add(10, 20, 30));    // 60
        System.out.println(c.add(10.5, 20.3));    // 30.8
        c.show(10, "Value");   // Value: 10
        c.show("Value", 10);   // Value: 10
    }
}
```

---

## 6.5 Method Overriding (Dynamic Polymorphism)

### Definition
Subclass provides **specific implementation** of a method already defined in its superclass. Same name, same parameters, same return type (or covariant).

### Rules for Overriding

| Rule | Description |
|------|-------------|
| **1. Same signature** | Method name, parameter list, return type must match |
| **2. Access level** | Cannot be more restrictive (e.g., protected → public OK, public → private NOT OK) |
| **3. Final methods** | Cannot override `final` methods |
| **4. Static methods** | Cannot override (they are hidden, not overridden) |
| **5. Private methods** | Not inherited, so cannot be overridden |
| **6. Constructors** | Cannot be overridden |
| **7. Exceptions** | Can throw same, subclass, or no exception; cannot throw broader checked exceptions |

### Example
```java
class Figure {
    double dim1, dim2;
    
    Figure(double a, double b) { dim1 = a; dim2 = b; }
    
    double area() {
        System.out.println("Area for Figure undefined");
        return 0;
    }
}

class Rectangle extends Figure {
    Rectangle(double a, double b) { super(a, b); }
    
    @Override
    double area() {
        System.out.println("Inside Area for Rectangle");
        return dim1 * dim2;
    }
}

class Triangle extends Figure {
    Triangle(double a, double b) { super(a, b); }
    
    @Override
    double area() {
        System.out.println("Inside Area for Triangle");
        return dim1 * dim2 / 2;
    }
}

public class FindAreas {
    public static void main(String[] args) {
        Figure f = new Figure(10, 10);
        Rectangle r = new Rectangle(9, 5);
        Triangle t = new Triangle(10, 8);
        
        Figure ref;
        
        ref = r;
        System.out.println("Area: " + ref.area());
        
        ref = t;
        System.out.println("Area: " + ref.area());
        
        ref = f;
        System.out.println("Area: " + ref.area());
    }
}
```

**Output:**
```
Inside Area for Rectangle
Area: 45.0
Inside Area for Triangle
Area: 40.0
Area for Figure undefined
Area: 0.0
```

### Dynamic Method Dispatch
- Superclass reference variable can refer to subclass object
- Method call resolved at **runtime** based on actual object type
- Enables runtime polymorphism

```java
Shape s = new Circle();   // Shape reference, Circle object
s.draw();                 // Calls Circle's draw() at runtime

s = new Rectangle();
s.draw();                 // Calls Rectangle's draw() at runtime
```

---

## 6.6 Abstract Class

### Definition
A class that **cannot be instantiated** and may contain **abstract methods** (methods without body). Declared with `abstract` keyword.

### Characteristics
- ✅ Can have **abstract** and **concrete** (non-abstract) methods
- ✅ Can have constructors, fields, static methods
- ✅ Can have `final` methods
- ❌ Cannot be instantiated directly (`new AbstractClass()` illegal)
- ❌ Subclass must implement all abstract methods OR be abstract itself

### Syntax
```java
abstract class ClassName {
    // Abstract method (no body)
    abstract returnType methodName(parameters);
    
    // Concrete method (has body)
    void concreteMethod() { ... }
}
```

### Example
```java
abstract class Bank {
    abstract int getRateOfInterest();  // Abstract method
    
    void display() {                   // Concrete method
        System.out.println("Welcome to Bank");
    }
}

class SBI extends Bank {
    @Override
    int getRateOfInterest() { return 7; }
}

class PNB extends Bank {
    @Override
    int getRateOfInterest() { return 8; }
}

class ICICI extends Bank {
    @Override
    int getRateOfInterest() { return 9; }
}

public class TestBank {
    public static void main(String[] args) {
        Bank b;              // Reference of abstract type
        
        b = new SBI();
        System.out.println("SBI Rate: " + b.getRateOfInterest() + "%");
        
        b = new PNB();
        System.out.println("PNB Rate: " + b.getRateOfInterest() + "%");
        
        b = new ICICI();
        System.out.println("ICICI Rate: " + b.getRateOfInterest() + "%");
    }
}
```

**Output:**
```
SBI Rate: 7%
PNB Rate: 8%
ICICI Rate: 9%
```

### Key Points About Abstract Classes
| Rule | Description |
|------|-------------|
| Abstract method | Only declaration, no body, ends with `;` |
| Class with abstract method | Must be declared `abstract` |
| Subclass of abstract class | Must implement all abstract methods or be abstract |
| Abstract constructor | Not allowed |
| Abstract static method | Not allowed |
| Abstract final method | Not allowed (contradiction) |

---

## 6.7 Abstract Class vs Interface

### Comparison Table

| Aspect | Abstract Class | Interface |
|--------|---------------|-----------|
| **Keyword** | `abstract class` | `interface` |
| **Methods** | Abstract + Concrete | Only abstract (Java 7); default/static (Java 8+) |
| **Variables** | Any type (instance, static, final) | `public static final` only (constants) |
| **Access Modifiers** | Any (private, protected, etc.) | `public` only (implicit) |
| **Inheritance** | Single (`extends`) | Multiple (`implements`) |
| **Constructor** | Can have | Cannot have |
| **Instantiation** | No | No |
| **Extension** | Extends class, implements interfaces | Extends interfaces only |
| **Use Case** | "Is-a" relationship, shared code | "Can-do" capability, contract |

### Code Comparison

```java
// Abstract Class
abstract class Employee {
    String name;
    int id;
    
    Employee(String name, int id) {
        this.name = name; this.id = id;
    }
    
    abstract double calculateSalary();  // Must implement
    
    void displayInfo() {                // Shared code
        System.out.println("ID: " + id + ", Name: " + name);
    }
}

// Interface
interface Payable {
    double getPaymentAmount();  // Implicitly public abstract
    
    // Java 8+ default method
    default void printPayment() {
        System.out.println("Payment: " + getPaymentAmount());
    }
    
    // Java 8+ static method
    static void companyPolicy() {
        System.out.println("Standard payment policy");
    }
}

// Class implementing interface
class Manager extends Employee implements Payable {
    double bonus;
    
    Manager(String name, int id, double bonus) {
        super(name, id);
        this.bonus = bonus;
    }
    
    @Override
    double calculateSalary() { return 50000 + bonus; }
    
    @Override
    public double getPaymentAmount() { return calculateSalary(); }
}
```

---

## 6.8 Important Exam Questions (from PYQ Analysis)

### High Priority (CRITICAL - Appeared 8/10 years)

**2-Mark Questions:**
1. What is polymorphism? Types of polymorphism.
2. Difference between method overloading and overriding.
3. What is static binding vs dynamic binding?
4. What is an abstract class? Why can't it be instantiated?
5. Difference between abstract class and interface.
6. Can we instantiate abstract class? Why?
7. What is `@Override` annotation?
8. Can abstract class have constructor?
9. Can interface have constructor?

**5-Mark Questions:**
1. Explain polymorphism with types and examples.
2. Explain method overloading with program (3 ways).
3. Explain method overriding with rules and program.
4. Explain abstract class with example. Why not instantiated?
5. Difference between abstract class and interface with table.
6. Explain dynamic method dispatch with example.

**10-Mark Questions:**
1. **What is polymorphism? Explain static vs dynamic binding with examples. Explain abstract class advantages and difference from interface.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Explain method overloading and overriding with detailed comparison.
3. Abstract class vs Interface: differences, when to use which.

### Programs to Practice
1. ✅ **Method overloading (3+ methods same name)** - appeared 2022, 2024, 2025, 2026
2. ✅ **Method overriding (Figure → Rectangle/Triangle)** - appeared 2022, 2024, 2025, 2026
3. ✅ **Abstract class (Bank → SBI/PNB)** - appeared 2021, 2022, 2023, 2024, 2025
4. ✅ **Abstract class vs Interface comparison** - appeared 2021, 2022, 2023, 2024, 2025
5. ✅ **Dynamic binding demonstration** - appeared 2023, 2024, 2026

---

## 6.9 Summary of Unit 6

| Topic | Key Points |
|-------|------------|
| **Polymorphism** | One interface, many forms; enables flexibility |
| **Static Polymorphism** | Method overloading; compile-time; same class |
| **Dynamic Polymorphism** | Method overriding; runtime; parent-child classes |
| **Overloading Rules** | Different signature; return type irrelevant |
| **Overriding Rules** | Same signature; covariant return; access same/wider; no final/static/private |
| **Dynamic Dispatch** | Superclass ref → Subclass object; resolved at runtime |
| **Abstract Class** | Partial abstraction; abstract + concrete methods; no instantiation |
| **Interface** | Full abstraction (Java 7); constants + abstract methods; multiple impl |
| **Java 8+ Interface** | Default methods, static methods, functional interfaces |

---

## 6.10 Quick Reference: Overloading vs Overriding

| Criteria | Overloading | Overriding |
|----------|-------------|------------|
| **Polymorphism Type** | Static (Compile-time) | Dynamic (Runtime) |
| **Classes** | Same class | Superclass & Subclass |
| **Method Name** | Same | Same |
| **Parameter List** | Different | Same |
| **Return Type** | Can differ | Same or covariant |
| **Access Modifier** | Can differ | Same or wider |
| **Exceptions** | Can differ | Same or narrower |
| **Binding** | Early (Compiler) | Late (JVM) |
| **Performance** | Faster | Slightly slower |
| **`@Override`** | Not used | Recommended |

---

## 6.11 Rules for Abstract Class vs Interface Decision

| Use Abstract Class When | Use Interface When |
|------------------------|-------------------|
| Shared code among closely related classes | Unrelated classes need common behavior |
| Need non-public access modifiers | Want multiple implementation |
| Need instance variables/state | Defining a contract/capability |
| Need constructors | Defining types for polymorphism |
| Template method pattern | Marker interfaces, callbacks |