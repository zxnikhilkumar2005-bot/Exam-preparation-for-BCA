# Unit 7: Assertions, Annotations and Exception Handling

## Unit Overview
This unit covers Java assertions (enable/disable, use cases, performance), annotations (built-in, meta-annotations, custom), and comprehensive exception handling including hierarchy, try-catch-finally, throw/throws, custom exceptions, and final/finally/finalize differences. Based on IGNOU MCS-206 Block 2 Unit 7 textbook and PYQ analysis (Dec 2021–June 2026).

---

## 7.1 Assertions

### Topic Introduction
Assertions are a debugging/testing feature to verify assumptions during development. They are **disabled by default** and only enabled explicitly for testing. Unlike normal exception handling, assertions are meant for **non-production environments**.

### Definition (from Textbook)
> An **assertion** is a statement that tests a boolean expression. If false, it throws `AssertionError`. Used to check logically impossible situations or inconceivable circumstances (pre-conditions, post-conditions, unreachable code).

### Syntax (Textbook Format)
```java
// Simple assertion
assert booleanExpression;

// Assertion with message (Textbook: assert :< boolean condition > : < string message >)
assert booleanExpression : "Error message expression";
```

> **Note**: Textbook shows `assert : condition : message` format but standard Java syntax is `assert condition : message;`

### Execution Flow
```
Evaluate boolean expression
         │
    ┌────┴────┐
    ▼         ▼
  true       false
    │         │
    ▼         ▼
Continue   Throw AssertionError
           (with optional message)
```

### Enabling/Disabling Assertions (Textbook Variations)

| Command | Description |
|---------|-------------|
| `java -ea ClassName` | Enable assertions for all classes (except system) |
| `java -enableassertions ClassName` | Same as above |
| `java -ea:ClassName` | Enable for specific class |
| `java -ea:com.package...` | Enable for package and subpackages |
| `java -ea:...` | Enable for unnamed package (current directory) |
| `java -esa` / `java -enablesystemassertions` | Enable for system classes |
| `java -da ClassName` | Disable assertions (default) |
| `java -disableassertions ClassName` | Same as above |

### Examples from Textbook

**Example 1: Covid Test (CT Value)**
```java
class CovidTest {
    public static void main(String args[]) {
        int RTPCRvalue = 31;
        assert RTPCRvalue >= 29 : "Covid-19 Positive";
        System.out.println("value is " + RTPCRvalue);
    }
}
```
**With `-ea`**: `Exception in thread "main" java.lang.AssertionError: Covid-19 Positive`
**Without `-ea`**: `value is 31` (assertion ignored)

**Example 2: Bluetooth Proximity Alert**
```java
public void setup_connection() {
    Connection conn = getConnection();
    assert conn == null : "Proximity to infection";
}
```

### Why Use Assertions? (Textbook - Performance Benefit)
- Conditional statements for debugging remain in production code → waste CPU cycles
- Assertions **disabled by default** → zero overhead in production
- No need to add/remove debugging code → saves rework

### Where to Use Assertions (Textbook)
- ✅ Ensure inaccessible code is really inaccessible
- ✅ Private method arguments (developer-provided)
- ✅ Conditional cases / pre-conditions at method start
- ✅ Verify `default` switch case is not reached
- ✅ Document assumptions in comments
- ✅ Check object state
- ✅ Post-conditions after method invocation

### Where NOT to Use Assertions (Textbook)
- ❌ Replace error messages
- ❌ Check arguments in **public methods** (user-provided)
- ❌ Command line arguments
- ❌ Use exception handling for user input validation

### Assertions vs Exception Handling (Textbook)

| Aspect | Assertions | Exception Handling |
|--------|------------|-------------------|
| **Purpose** | Check logically impossible situations | Handle runtime errors |
| **Default State** | Disabled | Always enabled |
| **Target** | Internal logic errors (pre/post conditions) | External/runtime conditions |
| **Recovery** | No recovery (crash with AssertionError) | Graceful recovery possible |
| **Performance** | Zero cost when disabled | Always has overhead |
| **Use Case** | "Should never happen" (bugs) | "Might happen" (expected errors) |

### Common Usage Scenarios (Textbook)
1. **Unreachable Code** - `default: assert false : dayOfWeek + " is invalid day";`
2. **Documenting Assumptions** - Pre-conditions, post-conditions, invariants

### Check Your Progress Answers (Textbook)
1. **Default state?** Disabled. Enable: `java -ea`, Disable: `java -da`
2. **Does assert throw exception?** Throws `AssertionError` (subclass of `Error`, not `Exception`)
3. **What happens when assert fails?** `AssertionError` thrown, program terminates
4. **What does assert return?** Nothing (void); either continues or throws
5. **Can we catch AssertionError?** Yes, but **not recommended** - it's an `Error`, indicates bug
6. **How to assert an exception?** Not applicable - assertions check conditions, not throw exceptions

---

## 7.2 Annotations

### Topic Introduction (Textbook)
> **Annotations** are a form of **metadata** (data about data). They provide data about a program without being part of the program itself. They don't directly impact code functioning but serve essential purposes: compiler information, compile-time/delivery-time processing, runtime processing.

### Two Categories (Textbook)
1. **Annotations applied to Java code** (Built-in: `@Override`, `@SuppressWarnings`, `@Deprecated`, etc.)
2. **Meta-annotations** (Applied to other annotations: `@Target`, `@Retention`, etc.)

### 7.2.1 Built-In Annotations (Applied to Java Code)

| Annotation | Purpose | Example |
|------------|---------|---------|
| `@Override` | Verifies method overrides superclass; compile error if not | `@Override void toString() {}` |
| `@SuppressWarnings` | Suppresses compiler warnings | `@SuppressWarnings("unchecked")` |
| `@Deprecated` | Marks element as obsolete; warns users | `@Deprecated void oldMethod() {}` |
| `@FunctionalInterface` | Marks interface as functional (single abstract method) - Java 8+ | `@FunctionalInterface interface MyFunc {}` |
| `@SafeVarargs` | Suppresses varargs heap pollution warnings - Java 7+ | `@SafeVarargs void method(T... args) {}` |

### 7.2.2 Meta-Annotations (Applied to Other Annotations)

| Annotation | Purpose |
|------------|---------|
| `@Target` | Restricts where annotation can be applied (ElementType) |
| `@Retention` | Specifies how long annotation is retained (RetentionPolicy) |
| `@Inherited` | Allows annotation to be inherited by subclasses |
| `@Documented` | Includes annotation in Javadoc |
| `@Repeatable` | Allows annotation to be applied multiple times (Java 8+) |

### 7.2.3 @Override (Detailed)
```java
class Animal {
    void sound() { System.out.println("Animal sound"); }
}

class Dog extends Animal {
    @Override
    void sound() {  // Compile error if signature doesn't match
        System.out.println("Bark");
    }
    
    // @Override
    // void sound(String type) {}  // ERROR: doesn't override
}
```

### 7.2.4 @SuppressWarnings
```java
// Suppress unchecked warning for raw types
@SuppressWarnings("unchecked")
void rawTypeExample() {
    List list = new ArrayList();  // Raw type warning suppressed
    list.add("test");
}

// Common values: "unchecked", "deprecation", "rawtypes", "serial", "all"
```

### 7.2.5 @Deprecated
```java
class Legacy {
    @Deprecated
    void oldMethod() {
        System.out.println("Use newMethod() instead");
    }
    
    void newMethod() {
        System.out.println("New implementation");
    }
}
```

### 7.2.6 Custom Annotations
```java
// Declaration with meta-annotations
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
@interface MyAnnotation {
    String value() default "default";
    int count() default 0;
    String[] tags() default {};
}

// Usage
@MyAnnotation(value = "test", count = 5, tags = {"a", "b"})
public class AnnotatedClass {}
```

### Annotation Retention Policies
| Policy | Retention |
|--------|-----------|
| `RetentionPolicy.SOURCE` | Discarded by compiler |
| `RetentionPolicy.CLASS` | In .class file, not loaded by JVM (default) |
| `RetentionPolicy.RUNTIME` | Available at runtime via reflection |

### Annotation Targets (ElementType)
```java
@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
@interface MyAnnotation {}
```
**Values:** TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE, ANNOTATION_TYPE, PACKAGE, TYPE_PARAMETER, TYPE_USE

---

## 7.3 Exception Handling

### 7.3.1 Basics

#### Definition (Textbook)
> An **exception** is a problem that arises during execution. It can occur for many reasons: invalid user data, file not found, network loss, JVM out of memory. If not handled → system failure. Exception handling provides **graceful exit**.

#### Error vs Exception (Textbook)

| Aspect | Error | Exception |
|--------|-------|-----------|
| **Recoverable** | No | Yes |
| **Type** | Unchecked only | Checked or Unchecked |
| **Cause** | Environment (JVM) | Application code |
| **Timing** | Runtime only | Compile-time or runtime |
| **Examples** | OutOfMemoryError, StackOverflowError | IOException, NullPointerException |

#### Exception Hierarchy (Textbook - Figure 7.2)
```
                    Throwable
                       │
        ┌──────────────┴──────────────┐
        ▼                             ▼
      Error                         Exception
        │                             │
        ▼                             ▼
   (JVM errors)              ┌────────┴────────┐
                            ▼                 ▼
                     RuntimeException    Checked Exceptions
                     (Unchecked)         (Compile-time checked)
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         NullPointer   ArrayIndexOutOf  Arithmetic
         Exception     BoundsException  Exception
```

> **Textbook Note**: "Exceptions that happen at compile time are Checked Exceptions" — *Correction: Checked exceptions are checked at compile time, they don't "happen" at compile time.*

### 7.3.2 Checked vs Unchecked Exceptions

| Aspect | Checked Exceptions | Unchecked Exceptions |
|--------|-------------------|---------------------|
| **Also Called** | Compile-time exceptions | Runtime exceptions |
| **Inheritance** | Extend `Exception` (not `RuntimeException`) | Extend `RuntimeException` |
| **Compiler Check** | Must handle or declare | No compile-time check |
| **Handling** | try-catch OR throws | Optional |
| **Examples** | IOException, SQLException, ClassNotFoundException | NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException, NumberFormatException |

### 7.3.3 try-catch-finally

#### Syntax
```java
try {
    // Code that may throw exception
} catch (ExceptionType1 e1) {
    // Handle ExceptionType1
} catch (ExceptionType2 e2) {
    // Handle ExceptionType2
} finally {
    // Always executes (cleanup code)
}
```

#### Key Rules (Textbook + Best Practices)
- ✅ `try` must be followed by `catch` OR `finally` (or both)
- ✅ Multiple `catch` blocks allowed
- ✅ **Catch order: Subclass before Superclass** (critical!)
- ✅ `finally` executes **always** (even if return in try/catch)
- ✅ `finally` won't execute if `System.exit()` called
- ✅ `try` without `catch` allowed in Java 7+ (with `finally` or try-with-resources)

#### Example: Multiple Catch (Textbook Style)
```java
public class MultiCatch {
    public static void main(String[] args) {
        try {
            int[] arr = new int[5];
            arr[7] = 10;  // ArrayIndexOutOfBoundsException
            int x = 10 / 0;  // ArithmeticException
        } 
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index error: " + e.getMessage());
        } 
        catch (ArithmeticException e) {
            System.out.println("Math error: " + e.getMessage());
        } 
        catch (Exception e) {
            System.out.println("Generic error: " + e.getMessage());
        }
        finally {
            System.out.println("Finally block executed");
        }
    }
}
```

#### Nested Try Blocks (Textbook Example)
```java
try {
    int a = 90, b = 0;
    int c = a / b;
    System.out.println("Resultant = " + c);
} catch (ArithmeticException e) {
    System.out.println("Hey!! You cannot divide any number by zero. Basic Maths");
}

try {
    try {
        int num = Integer.parseInt("PGDegree");  // NumberFormatException
        System.out.println(num);
    } catch (NumberFormatException e) {
        System.out.println("The argument given to parseInt should be a number");
    }
    try {
        int a[] = new int[5];
        a[7] = 25;  // ArrayIndexOutOfBoundsException
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Array index out of bounds exception");
    }
    System.out.println("Marks culmination of Nested Try block");
} catch (Exception e) {
    System.out.println("This will handle all exceptions and recover");
}
```

#### Java 7+ Multi-catch
```java
// Single catch for multiple exceptions (must be disjoint - no inheritance)
try {
    // code
} catch (IOException | NumberFormatException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### 7.3.4 throw vs throws (Textbook)

| Aspect | `throw` | `throws` |
|--------|---------|----------|
| **Purpose** | Explicitly throw an exception | Declare exceptions method may throw |
| **Used With** | Exception **instance** | Exception **class** |
| **Location** | Inside method body | Method signature |
| **Multiple** | One at a time | Multiple allowed (comma-separated) |
| **Checked Exception** | Must be caught or declared | Propagates to caller |

#### Textbook: "Only single exception is thrown by using throw method. Multiple exceptions can be thrown by using throws method."

#### throw Example
```java
void validateAge(int age) {
    if (age < 18) {
        throw new IllegalArgumentException("Age must be 18+");
    }
}
```

#### throws Example
```java
// Method declares it may throw IOException
void readFile(String path) throws IOException {
    FileReader fr = new FileReader(path);
    // No try-catch needed here; caller must handle
}

// Caller must handle
public static void main(String[] args) {
    try {
        readFile("test.txt");
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```

### 7.3.5 finally Block

#### Purpose (Textbook)
- Cleanup code: close files, database connections, release resources
- Executes **always**: exception or not, caught or not

```java
try {
    FileInputStream fis = new FileInputStream("file.txt");
    // read file
} catch (IOException e) {
    e.printStackTrace();
} finally {
    // This ALWAYS runs
    System.out.println("Cleanup: closing resources");
}
```

#### try-with-resources (Java 7+)
```java
// Auto-closes resources implementing AutoCloseable
try (FileInputStream fis = new FileInputStream("file.txt");
     BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    // Use resources
} catch (IOException e) {
    e.printStackTrace();
}
// No finally needed - auto-closed!
```

---

## 7.4 Custom Exceptions (User-Defined Exceptions)

### Textbook: Two Important Points
1. A user defined exception **must extend the Exception class**
2. Exception is thrown using a **throw keyword**

### Creating User-Defined Exception (Textbook Examples)

**Example 1: Simple Custom Exception**
```java
class MyException extends Exception {
    public MyException(String s) {
        super(s);  // Call constructor of parent Exception
    }
}

public class PGDException {
    public static void main(String args[]) {
        try {
            // Throw an object of user defined exception
            throw new MyException("MyException");
        } catch (MyException e) {
            System.out.println("Exception Caught");
            // Print the message from MyException object
            System.out.println(e.getMessage());
        }
    }
}
```
**Output:** `Exception Caught` / `MyException`

**Example 2: Covid Threshold Validation (Textbook)**
```java
import java.util.*;

class PGDException {
    static void ValidateThreshold(int threshold) throws InvalidInputException {
        if (threshold > 60) {
            throw new InvalidInputException("Invalid Threshold");
        }
        System.out.println("Valid Threshold");
    }
    
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a threshold value less than 60 :");
        int threshold = scanner.nextInt();
        try {
            ValidateThreshold(threshold);
        } catch (InvalidInputException e) {
            System.out.println("You can be Covid positive it is an exception: threshold is greater than 60");
        }
    }
}

class InvalidInputException extends Exception {
    InvalidInputException(String exceptionText) {
        super(exceptionText);
    }
}
```
**Output-1 (input 45):** `Valid Threshold`
**Output-2 (input 85):** `You can be Covid positive it is an exception: threshold is greater than 60`

### Rules for Custom Exceptions (Textbook + Best Practices)
- ✅ Must extend `Exception` (checked) or `RuntimeException` (unchecked)
- ✅ Should provide constructors: `String message`, `Throwable cause`
- ✅ Override `getMessage()` if needed
- ✅ Follow naming convention: `XxxException`
- ✅ Can add custom fields/methods for additional info

---

## 7.5 final vs finally vs finalize

### Comparison Table

| Aspect | `final` | `finally` | `finalize()` |
|--------|---------|-----------|--------------|
| **Type** | Keyword | Block | Method |
| **Purpose** | Restrict modification | Cleanup code | GC cleanup (deprecated) |
| **Used With** | Variables, methods, classes | try-catch | Object class |
| **Execution** | Compile-time | Runtime (always) | Before GC (uncertain timing) |
| **Override** | N/A | N/A | Yes (protected) |
| **Since** | Java 1.0 | Java 1.0 | Deprecated Java 9, removed Java 18 |

### Examples

```java
// final variable
final int MAX = 100;
// MAX = 200;  // COMPILE ERROR

// final method
class Parent {
    final void show() {}  // Cannot override
}

// final class
final class Constants {}  // Cannot extend

// finally block
try {
    // risky code
} catch (Exception e) {
    // handle
} finally {
    // cleanup - ALWAYS executes
}

// finalize method (DEPRECATED - avoid in new code)
class Resource {
    @Override
    @Deprecated(since = "9")
    protected void finalize() throws Throwable {
        try {
            System.out.println("Cleaning up resource");
        } finally {
            super.finalize();
        }
    }
}
```

> **Important**: `finalize()` is **deprecated since Java 9** (2017) and **removed in Java 18**. Use try-with-resources or `Cleaner` API instead.

---

## 7.6 Important Exam Questions (from PYQ Analysis)

### CRITICAL Priority (Appeared 9-10/10 years: 2021-2026)

#### 2-Mark Questions:
1. **Difference between `throw` and `throws`.** (2022-2026)
2. **Difference between `final`, `finally`, `finalize`.** (2022-2026)
3. **Difference between checked and unchecked exceptions.** (2024, 2026)
4. **What is an assertion? How to enable/disable?** (2023-2026)
5. **What is `@Override`, `@SuppressWarnings`, `@Deprecated`?** (2023-2024)
6. **Can we catch `AssertionError`?** (2023-2025)
7. **Difference between Error and Exception.** (2022-2026)
8. **What is exception hierarchy?** (2024, 2026)
9. **Can try exist without catch?** (Java 7+) (2022-2026)
10. **Order of catch blocks (subclass first).** (2022-2026)
11. **What is the purpose of `throws` keyword?**
12. **What is try-with-resources?**

#### 5-Mark Questions:
1. **Explain exception handling mechanism with try-catch-finally.** (2021-2026)
2. **Explain `throw` vs `throws` with examples.** (2022-2026)
3. **Explain custom exception creation with program.** (2024, 2026)
4. **Explain assertions: syntax, enable/disable, use cases.** (2023-2026)
5. **Explain built-in annotations with examples.** (2023-2024)
6. **Difference between `final`, `finally`, `finalize` with examples.** (2022-2026)
7. **Explain exception hierarchy with diagram.** (2024, 2026)
8. **Write program: ArrayIndexOutOfBounds + multiple catch + finally.** (2022, 2024, 2025)
9. **Explain nested try blocks with example.** (Textbook emphasis)
10. **Explain performance benefit of assertions over conditional statements.**

#### 10-Mark Questions:
1. **Explain exception handling in detail: hierarchy, checked/unchecked, try-catch-finally, throw/throws, custom exceptions.** (Appeared 2021, 2022, 2023, 2024, 2025, 2026)
2. **Explain assertions vs exception handling. Enable/disable assertions.** (2023-2026)
3. **Explain annotations: built-in, meta-annotations, custom annotations.** (2023-2024)
4. **Complete exception handling program with user-defined exception, multiple catch, finally, throws.**

### Programs to Practice (Critical for Exam)

1. ✅ **Exception handling with ArrayIndexOutOfBounds + multiple catch + finally** — appeared 2022, 2024, 2025
2. ✅ **Custom exception (InsufficientFunds, InvalidInput, MyException)** — appeared 2024, 2026
3. ✅ **throw vs throws demonstration** — appeared 2022, 2023, 2025, 2026
4. ✅ **Assertions enable/disable example** — appeared 2023, 2024, 2025, 2026
5. ✅ **Built-in annotations (@Override, @SuppressWarnings, @Deprecated)** — appeared 2023, 2024
6. ✅ **Nested try blocks** — Textbook emphasis
7. ✅ **try-with-resources / AutoCloseable** — Modern Java
8. ✅ **Exception hierarchy diagram with examples**

---

## 7.7 Textbook Check Your Progress Answers

### Check Your Progress - 1 (Assertions)
1. **Default state?** Disabled. Enable: `java -ea` / `-enableassertions`, Disable: `java -da` / `-disableassertions`
2. **Does assert throw exception?** Throws `AssertionError` (Error, not Exception)
3. **What happens when assert fails?** `AssertionError` thrown, execution aborts
4. **What does assert return?** Nothing (void)
5. **Can we catch assertion error?** Yes but not recommended (it's an Error)
6. **How to assert an exception?** Not applicable

### Check Your Progress - 2 (Exception Handling)
1. **Can try exist without catch?** Yes, with `finally` (Java 7+) or try-with-resources
2. **Highest level of Exception Handling classes?** `Throwable`
3. **Pre-defined exception hierarchy?** `Throwable` → `Error` / `Exception` → `RuntimeException` / checked exceptions
4. **How to create Custom Exception Classes?** Extend `Exception`, add constructors, use `throw`
5. **Difference between ClassNotFoundException and NoClassDefFoundError?** 
   - `ClassNotFoundException`: Checked, class not found at runtime (Class.forName)
   - `NoClassDefFoundError`: Error, class found at compile time but missing at runtime
6. **Code analysis question** — Multiple catch order matters (NullPointerException before Exception)
7. **Can Exception be rethrown?** Yes, `throw e;` in catch. Caller must catch/rethrow checked exceptions.

---

## 7.8 Summary of Unit 7

| Topic | Key Points |
|-------|------------|
| **Assertions** | `assert condition;` / `assert condition : message;`; disabled by default; `-ea` to enable; for testing/debugging only |
| **Performance** | Zero overhead when disabled; avoids conditional statement cleanup |
| **Where to Use** | Pre/post conditions, private args, unreachable code, switch default |
| **Where NOT** | Public method args, command line, production error handling |
| **Annotations** | Metadata; `@Override`, `@SuppressWarnings`, `@Deprecated`, `@FunctionalInterface` |
| **Meta-Annotations** | `@Target`, `@Retention`, `@Inherited`, `@Documented`, `@Repeatable` |
| **Exception** | Disrupts normal flow; `Throwable` → `Error`/`Exception` |
| **Checked Exceptions** | Compile-time checked; must handle/declare; extend `Exception` |
| **Unchecked Exceptions** | Runtime; extend `RuntimeException`; optional handling |
| **try-catch-finally** | try + (catch OR finally); multiple catch; subclass first; finally always |
| **throw** | Throw exception instance; inside method |
| **throws** | Declare exceptions in signature; propagates checked exceptions |
| **Custom Exception** | Extend `Exception` (checked) or `RuntimeException` (unchecked) |
| **final** | Variable=constant, method=no override, class=no extend |
| **finally** | Cleanup block, always executes |
| **finalize()** | Deprecated Java 9, removed Java 18; use try-with-resources |

---

## 7.9 Quick Reference: Exception Handling Flow

```
Method A
    │
    ├── try { risky code }
    │       │
    │       ├── Exception thrown
    │       │       │
    │       │       ├── catch (SpecificException) → handle
    │       │       │
    │       │       ├── catch (GeneralException) → handle
    │       │       │
    │       │       └── finally → ALWAYS execute
    │       │
    │       └── No exception → finally → continue
    │
    └── throws ExceptionType → Caller must handle
```

---

## 7.10 Sample 10-Mark Answer Template

**Question:** Explain exception handling in detail: hierarchy, checked/unchecked, try-catch-finally, throw/throws, custom exceptions.

**Answer Structure (10 marks):**

1. **Definition & Hierarchy** (2 marks):
   - Exception = runtime problem disrupting flow
   - Hierarchy: `Throwable` → `Error` (unrecoverable, JVM) / `Exception` (recoverable)
   - `Exception` → `RuntimeException` (unchecked) / checked exceptions

2. **Checked vs Unchecked** (2 marks):
   - Table with inheritance, compiler check, handling requirement, examples
   - Checked: `IOException`, `SQLException` — must catch or declare
   - Unchecked: `NullPointerException`, `ArrayIndexOutOfBoundsException` — optional

3. **try-catch-finally** (2 marks):
   - Syntax, rules (subclass first, finally always executes)
   - Nested try, multi-catch (Java 7+), try-with-resources
   - Code example with multiple catch + finally

4. **throw vs throws** (2 marks):
   - Table: instance vs class, body vs signature, single vs multiple
   - Example showing both in same program

5. **Custom Exception** (2 marks):
   - Steps: extend Exception, constructors, throw, handle
   - Complete program (e.g., InsufficientFundsException)

---

*Based on IGNOU MCS-206 Block 2 Unit 7 "Assertions, Annotations and Exception Handling" and PYQ Analysis (Dec 2021 – June 2026)*