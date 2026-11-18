# Unit 6: Polymorphism

## Unit Overview
This unit covers polymorphism basics, types (static/dynamic), method overloading, method overriding, abstract classes, and abstract class vs interface comparison. Based on IGNOU MCS-206 Block 2 Unit 6 textbook and PYQ analysis (Dec 2021–June 2026).

---

## 6.1 Introduction to Polymorphism

### Definition
> **Polymorphism** (Greek: *poly* = many, *morph* = forms) is the ability of an object to take many forms. It allows one interface to be used for a general class of actions.

### Core Concept
- One interface, multiple implementations
- Achieved through inheritance
- Object can pass multiple IS-A tests (e.g., a `Circle` IS-A `Shape`, IS-A `Object`)

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

### Real-World Analogy (from Textbook)
- A person plays multiple roles: father, employee, salesperson — one entity, many forms
- Saving two phone numbers under same contact name — one name, multiple values

---

## 6.2 Advantages of Polymorphism (from Textbook)

| Advantage | Description |
|-----------|-------------|
| **Code Reusability** | Existing tested classes reused without modification |
| **Flexibility** | New classes added without changing existing code |
| **Extensibility** | Easy to add new types |
| **Maintainability** | Changes in superclass affect all subclasses |
| **Reduced Coupling** | Code depends on interface, not concrete implementation |
| **Single Variable** | One reference variable can hold multiple object types |
| **Consistency** | Consistent method names across class hierarchy |
| **Debugging** | Less code = easier debugging |

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
| **Scope** | Same class | Superclass & Subclass |

---

## 6.4 Method Overloading (Static Polymorphism)

### Definition
Multiple methods in the **same class** with the **same name** but **different parameter lists** (signatures).

### Ways to Overload (3 Ways from Textbook)

| Method | Description | Example |
|--------|-------------|---------|
| **1. Different number of parameters** | Change parameter count | `sum(int, int)` vs `sum(int, int, int)` |
| **2. Different data types** | Change parameter types | `sum(int, int)` vs `sum(double, double)` |
| **3. Different sequence** | Change parameter order | `sum(int, double)` vs `sum(double, int)` |

> **Note**: Return type **alone** cannot differentiate overloaded methods. (Textbook: "return type does not play any role in method overloading")

### Rules
- ✅ Must have different parameter list (signature: number, type, or order)
- ✅ Return type can be same or different
- ✅ Access modifiers can be different
- ✅ Can throw different exceptions
- ❌ Cannot overload based **only** on return type
- ❌ Cannot have two methods with same name and same parameter list (compile error)

### Example (from Textbook)
```java
class DemoOverload {
    void test() { System.out.println("No parameters"); }
    void test(int a) { System.out.println("a : " + a); }
    void test(int a, int b) { System.out.println("a and b : " + a + " " + b); }
    double test(double a) { System.out.println("double a :" + a); return a*a; }
}

public class MyOverloading {
    public static void main(String args[]) {
        DemoOverload obj = new DemoOverload();
        double result;
        obj.test();
        obj.test(10);
        obj.test(10, 20);
        result = obj.test(123.25);
        System.out.println("Result of obj.test(123.25) :" + result);
    }
}
```

**Output:**
```
No parameters
a : 10
a and b : 10 20
double a :123.25
Result of obj.test(123.25) :15190.5625
```

### Textbook Check Your Progress - 1 Questions
1. **What is method overloading?** — Same name, different signatures in same class
2. **What is compile-time polymorphism?** — Method overloading; compiler resolves at compile time by checking signatures
3. **Write a program demonstrating overloading of three methods with same name.**

---

## 6.5 Method Overriding (Dynamic Polymorphism)

### Definition
Subclass provides **specific implementation** of a method already defined in its superclass. Same name, same parameters, same return type (or covariant).

### Rules for Overriding (from Textbook)

| Rule | Description |
|------|-------------|
| **1. Same signature** | Method name, parameter list, return type must match |
| **2. Return type** | Must be same (or covariant — subclass of original return type, Java 5+) |
| **3. Final methods** | Cannot override `final` methods |
| **4. Static methods** | Cannot override (they are **hidden**, not overridden) |
| **5. Private methods** | Not inherited, so cannot be overridden |
| **6. Constructors** | Cannot be overridden |
| **7. Access level** | Cannot be more restrictive (e.g., `protected` → `public` OK, `public` → `private` NOT OK) |
| **8. Exceptions** | Can throw same, subclass, or no exception; cannot throw broader checked exceptions |

### Example (from Textbook — Figure/Rectangle/Triangle)
```java
class Figure {
    double dim1, dim2;
    Figure(double a, double b) { dim1 = a; dim2 = b; }
    double area() {
        System.out.println("Area for Figure is undefined.");
        return 0;
    }
}

class Rectangle extends Figure {
    Rectangle(double a, double b) { super(a, b); }
    double area() {
        System.out.println("Inside Area for Rectangle.");
        return dim1 * dim2;
    }
}

class Triangle extends Figure {
    Triangle(double a, double b) { super(a, b); }
    double area() {
        System.out.println("Inside Area for Triangle.");
        return dim1 * dim2 / 2;
    }
}

class FindAreas {
    public static void main(String args[]) {
        Figure f = new Figure(10, 10);
        Rectangle r = new Rectangle(9, 5);
        Triangle t = new Triangle(10, 8);
        Figure ref;
        
        ref = r;
        System.out.println("Area is " + ref.area());
        
        ref = t;
        System.out.println("Area is " + ref.area());
        
        ref = f;
        System.out.println("Area is " + ref.area());
    }
}
```

**Output:**
```
Inside Area for Rectangle.
Area is 45.0
Inside Area for Triangle.
Area is 40.0
Area for Figure is undefined.
Area is 0.0
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

### Covariant Return Types (Java 5+)
```java
class Parent {
    Object getValue() { return new Object(); }
}
class Child extends Parent {
    @Override
    String getValue() { return "Hello"; }  // String is subclass of Object — allowed
}
```

---

## 6.6 Abstract Class

### Definition
A class that **cannot be instantiated** and may contain **abstract methods** (methods without body). Declared with `abstract` keyword.

### Characteristics (from Textbook)
- ✅ Can have **abstract** and **concrete** (non-abstract) methods
- ✅ Can have **constructors**, fields, static methods
- ✅ Can have `final` methods (forces subclasses not to change)
- ❌ Cannot be instantiated directly (`new AbstractClass()` illegal)
- ❌ Subclass must implement all abstract methods OR be abstract itself
- ❌ Abstract constructors NOT allowed (but **regular constructors ARE allowed**)
- ❌ Abstract static methods NOT allowed
- ❌ Abstract final methods NOT allowed (contradiction)

> **Important Correction**: Textbook says "Abstract constructors cannot be declared" — this means you cannot declare a constructor AS abstract. But abstract classes **CAN and DO have regular constructors** (used by subclasses via `super()`).

### Syntax
```java
abstract class ClassName {
    // Abstract method (no body)
    abstract returnType methodName(parameters);
    
    // Concrete method (has body)
    void concreteMethod() { ... }
    
    // Constructor (allowed!)
    ClassName() { ... }
}
```

### Example (from Textbook — Bank/SBI/PNB)
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
    public static void main(String args[]) {
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

### Abstract Class with Constructor (Important!)
```java
abstract class Employee {
    String name;
    int id;
    
    // Constructor in abstract class — ALLOWED!
    Employee(String name, int id) {
        this.name = name;
        this.id = id;
    }
    
    abstract double calculateSalary();
    
    void displayInfo() {
        System.out.println("ID: " + id + ", Name: " + name);
    }
}

class Manager extends Employee {
    double bonus;
    
    Manager(String name, int id, double bonus) {
        super(name, id);  // Must call super constructor
        this.bonus = bonus;
    }
    
    @Override
    double calculateSalary() { return 50000 + bonus; }
}
```

### Key Points About Abstract Classes
| Rule | Description |
|------|-------------|
| Abstract method | Only declaration, no body, ends with `;` |
| Class with abstract method | Must be declared `abstract` |
| Subclass of abstract class | Must implement all abstract methods or be abstract |
| Abstract constructor | Not allowed (but regular constructors ARE allowed) |
| Abstract static method | Not allowed |
| Abstract final method | Not allowed (contradiction) |
| `abstract` + `final` class | Not allowed (contradiction) |

---

## 6.7 Abstract Class vs Interface

### Comparison Table (Updated for Java 8+)

| Aspect | Abstract Class | Interface |
|--------|---------------|-----------|
| **Keyword** | `abstract class` | `interface` |
| **Methods** | Abstract + Concrete | Abstract + default + static + private (Java 8+) |
| **Variables** | Any type (instance, static, final) | `public static final` only (constants) |
| **Access Modifiers** | Any (private, protected, etc.) | `public` only (implicit); private methods allowed in Java 9+ |
| **Inheritance** | Single (`extends`) | Multiple (`implements`) |
| **Constructor** | Can have (called via `super()`) | Cannot have |
| **Instantiation** | No | No |
| **Extension** | Extends class, implements interfaces | Extends interfaces only |
| **Use Case** | "Is-a" relationship, shared code/state | "Can-do" capability, contract |
| **Default Methods** | N/A | Java 8+ — provide implementation |
| **Static Methods** | Allowed | Java 8+ — allowed |
| **Functional Interface** | No | Yes (single abstract method) |

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

// Interface (Java 8+)
interface Payable {
    double getPaymentAmount();  // Implicitly public abstract
    
    // Java 8+ default method — provides implementation
    default void printPayment() {
        System.out.println("Payment: " + getPaymentAmount());
    }
    
    // Java 8+ static method
    static void companyPolicy() {
        System.out.println("Standard payment policy");
    }
    
    // Java 9+ private method (helper for default methods)
    private void helper() { ... }
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

### Textbook Application Example (Payee/Employee/PaymentSystem)
The textbook shows how abstract class **reduces code duplication** compared to interface-only approach:

```
Payee <Interface>
  ↑
Employee <Abstract Class>  ← Implements common fields/methods
  ↑              ↑
SalaryEmployee   CommissionEmployee  ← Only implement specific logic
```

---

## 6.8 Advanced Topics

### Method Hiding (Static Methods)
```java
class Parent {
    static void show() { System.out.println("Parent"); }
}
class Child extends Parent {
    static void show() { System.out.println("Child"); }  // HIDES, not overrides
}

Parent p = new Child();
p.show();  // "Parent" — resolved at compile time by reference type!
```

### Polymorphic Parameters (from Textbook Check Your Progress)
```java
// Parametric polymorphism — same method works with different types
void process(Object obj) { ... }  // Accepts any object
process("String");
process(123);
process(new Employee());

// Problem: Variable hiding
class Dept extends Employee {
    private String content;
    public void setContentDelimiter() {
        int content = 100;  // Local hides instance variable!
        this.content = this.content + content;  // Need 'this' to access field
    }
}
```

### `@Override` Annotation
```java
@Override
void draw() { ... }  // Compiler verifies this actually overrides a superclass method
```
- **Recommended** for all overridden methods
- Catches errors: wrong signature, spelling mistakes, superclass method removed

### Object Class Methods in Polymorphism
```java
@Override
public String toString() { return "Circle[radius=5]"; }

@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (!(obj instanceof Circle)) return false;
    Circle other = (Circle) obj;
    return this.radius == other.radius;
}

@Override
public int hashCode() { return Objects.hash(radius); }
```

---

## 6.9 Important Exam Questions (from PYQ Analysis)

### CRITICAL Priority (Appeared 8-9/10 years: 2021-2026)

#### 2-Mark Questions:
1. **What is polymorphism? Types of polymorphism.**
2. **Difference between method overloading and overriding.**
3. **What is static binding vs dynamic binding?**
4. **What is an abstract class? Why can't it be instantiated?**
5. **Difference between abstract class and interface.**
6. **Can we instantiate abstract class? Why?**
7. **What is `@Override` annotation?**
8. **Can abstract class have constructor?**
9. **Can interface have constructor?**
10. **What is method hiding?**
11. **What is covariant return type?**
12. **What is dynamic method dispatch?**

#### 5-Mark Questions:
1. **Explain polymorphism with types and examples.**
2. **Explain method overloading with program (3 ways).**
3. **Explain method overriding with rules and program.**
4. **Explain abstract class with example. Why not instantiated?**
5. **Difference between abstract class and interface with table.**
6. **Explain dynamic method dispatch with example.**
7. **Write a program demonstrating static vs dynamic binding.**
8. **Explain abstract class constructor with example.**
9. **Explain interface default and static methods (Java 8+).**

#### 10-Mark Questions:
1. **What is polymorphism? Explain static vs dynamic binding with examples. Explain abstract class advantages and difference from interface.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. **Explain method overloading and overriding with detailed comparison.**
3. **Abstract class vs Interface: differences, when to use which.**
4. **Write a complete program demonstrating polymorphism with abstract class, interface, overloading, and overriding.**

### Programs to Practice (Critical for Exam)

1. ✅ **Method overloading (3+ methods same name)** — appeared 2022, 2024, 2025, 2026
2. ✅ **Method overriding (Figure → Rectangle/Triangle)** — appeared 2022, 2024, 2025, 2026
3. ✅ **Abstract class (Bank → SBI/PNB/ICICI)** — appeared 2021, 2022, 2023, 2024, 2025
4. ✅ **Abstract class vs Interface comparison** — appeared 2021, 2022, 2023, 2024, 2025
5. ✅ **Dynamic binding demonstration** — appeared 2023, 2024, 2026
6. ✅ **Abstract class with constructor** — NEW (textbook emphasis)
7. ✅ **Interface default/static methods demo** — NEW (Java 8+)

---

## 6.10 Textbook Check Your Progress Answers

### Check Your Progress - 1
1. **What is method overloading?**
   > Whenever several methods have the same names with: different method signatures, different numbers or types of parameters, same method signature but different number of parameters, or same method signature and same number of parameters but different data type.

2. **What is compile-time polymorphism?**
   > The best example is method overloading. Whenever an object is bound with their functionality at compile time is known as compile-time or static polymorphism.

3. **Program demonstrating overloading of three methods:**
   ```java
   public class Summation {
       public int SUM(int m, int n) { return (m + n); }
       public int SUM(int m, int n, int p) { return (m + n + p); }
       public double SUM(double m, double n) { return (m + n); }
       public static void main(String args[]) {
           Summation ob = new Summation();
           ob.SUM(15, 25);
           ob.SUM(15, 25, 35);
           ob.SUM(11.5, 22.5);
       }
   }
   ```

### Check Your Progress - 2
1. **Why do we use polymorphism in Java?**
   > Polymorphism makes it possible to write a method that can correctly process lots of different types of functionalities that have the same name. Provides consistency, reusability, single variable for multiple values, easier debugging.

2. **What do you mean by polymorphic parameters? Explain with program.**
   > Parametric polymorphism allows a name of a parameter or method in a class to be associated with different types. Example shows local variable hiding instance variable — use `this` keyword to access global reference.

3. **Find answer: Two methods with same return type, name, argument list.**
   > **Compile-time error** — cannot have more than one method with same name and argument list in same class.

4. **Find answer: Two methods with different return type, same name, argument list.**
   > **Compile-time error** — return type does not matter in case of overloading.

---

## 6.11 Summary of Unit 6

| Topic | Key Points |
|-------|------------|
| **Polymorphism** | One interface, many forms; enables flexibility, reusability |
| **Static Polymorphism** | Method overloading; compile-time; same class; early binding |
| **Dynamic Polymorphism** | Method overriding; runtime; parent-child; late binding |
| **Overloading Rules** | Different signature (number, type, order); return type irrelevant |
| **Overriding Rules** | Same signature; covariant return OK; access same/wider; no final/static/private |
| **Dynamic Dispatch** | Superclass ref → Subclass object; resolved at runtime by JVM |
| **Abstract Class** | Partial abstraction; abstract + concrete methods; constructors allowed; no instantiation |
| **Interface** | Full abstraction (Java 7); Java 8+: default, static, private methods; multiple impl |
| **Key Difference** | Abstract class: "is-a", shared state/code; Interface: "can-do", contract |
| **Method Hiding** | Static methods with same signature — resolved by reference type at compile time |

---

## 6.12 Quick Reference: Overloading vs Overriding

| Criteria | Overloading | Overriding |
|----------|-------------|------------|
| **Polymorphism Type** | Static (Compile-time) | Dynamic (Runtime) |
| **Classes** | Same class | Superclass & Subclass |
| **Method Name** | Same | Same |
| **Parameter List** | Different | Same |
| **Return Type** | Can differ | Same or covariant |
| **Access Modifier** | Can differ | Same or wider |
| **Exceptions** | Can differ | Same or narrower (checked) |
| **Binding** | Early (Compiler) | Late (JVM) |
| **Performance** | Faster | Slightly slower |
| **`@Override`** | Not used | **Recommended** |

---

## 6.13 Rules for Abstract Class vs Interface Decision

| Use Abstract Class When | Use Interface When |
|------------------------|-------------------|
| Shared code among closely related classes | Unrelated classes need common behavior |
| Need non-public access modifiers | Want multiple implementation |
| Need instance variables/state | Defining a contract/capability |
| Need constructors | Defining types for polymorphism |
| Template method pattern | Marker interfaces, callbacks |
| Need `final` methods | Functional interface (lambda target) |

---

## 6.14 Sample 10-Mark Answer Template

**Question:** What is polymorphism? Explain static vs dynamic binding with examples. Explain abstract class advantages and difference from interface.

**Answer Structure:**
1. **Definition** (2 marks): Polymorphism = many forms; one interface, multiple implementations; achieved via inheritance
2. **Types** (2 marks): 
   - Static (compile-time): Method overloading, early binding, compiler resolves
   - Dynamic (runtime): Method overriding, late binding, JVM resolves
3. **Examples** (3 marks): 
   - Overloading: `add(int,int)`, `add(double,double)`, `add(int,int,int)`
   - Overriding: `Shape` → `Circle`, `Rectangle` with `draw()`
4. **Abstract Class** (3 marks): 
   - Cannot instantiate; abstract + concrete methods; constructors allowed; shared code
   - Example: `Bank` → `SBI`, `PNB`
5. **Abstract Class vs Interface** (5 marks): 
   - Table with 8+ differences (keyword, methods, variables, inheritance, constructors, Java 8+ defaults)
   - When to use each

---

*Based on IGNOU MCS-206 Block 2 Unit 6 "Polymorphism" and PYQ Analysis (Dec 2021 – June 2026)*