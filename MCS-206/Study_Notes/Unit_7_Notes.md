# Unit 7: Assertions, Annotations and Exception Handling

## Unit Overview
This unit covers Java assertions (enable/disable), annotations (built-in and custom), and comprehensive exception handling including hierarchy, try-catch-finally, throw/throws, custom exceptions, and final/finally/finalize differences.

---

## 7.1 Assertions

### Topic Introduction
Assertions are a debugging/testing feature to verify assumptions during development. They are **disabled by default** and only enabled explicitly for testing.

### Definition
> An **assertion** is a statement that tests a boolean expression. If false, it throws `AssertionError`.

### Syntax
```java
// Simple assertion
assert booleanExpression;

// Assertion with message
assert booleanExpression : "Error message expression";
```

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

### Enabling/Disabling Assertions

| Command | Description |
|---------|-------------|
| `java -ea ClassName` | Enable assertions for all classes (except system) |
| `java -enableassertions ClassName` | Same as above |
| `java -ea:ClassName` | Enable for specific class |
| `java -ea:com.package...` | Enable for package and subpackages |
| `java -ea:...` | Enable for unnamed package (current directory) |
| `java -esa` | Enable for system classes |
| `java -da ClassName` | Disable assertions (default) |
| `java -disableassertions ClassName` | Same as above |

### Example
```java
public class CovidTest {
    public static void main(String[] args) {
        int ctValue = 31;
        assert ctValue >= 29 : "Covid-19 Positive: CT value " + ctValue;
        System.out.println("CT Value: " + ctValue);
    }
}
```

**Run with assertions enabled:**
```bash
java -ea CovidTest
```
**Output:**
```
Exception in thread "main" java.lang.AssertionError: Covid-19 Positive: CT value 31
    at CovidTest.main(CovidTest.java:5)
```

### Where to Use Assertions
- ✅ Pre-conditions (method entry)
- ✅ Post-conditions (method exit)
- ✅ Unreachable code (default case in switch)
- ✅ Internal invariants
- ✅ Private method arguments

### Where NOT to Use Assertions
- ❌ Public method argument validation (use exceptions)
- ❌ Command-line argument checking
- ❌ Production error handling
- ❌ Side-effect operations in assertion expression

### Assertions vs Exception Handling

| Aspect | Assertions | Exception Handling |
|--------|------------|-------------------|
| **Purpose** | Detect programming bugs | Handle runtime errors |
| **Default State** | Disabled | Always enabled |
| **Target** | Internal logic errors | External/runtime conditions |
| **Recovery** | No recovery (crash) | Graceful recovery possible |
| **Performance** | Zero cost when disabled | Always has overhead |
| **Use Case** | "Should never happen" | "Might happen" |

---

## 7.2 Annotations

### Topic Introduction
Annotations provide **metadata** (data about data) for code. They don't directly affect execution but provide information to compiler, tools, and runtime.

### Definition
> An **annotation** is a form of metadata that provides data about a program without being part of the program itself.

### Built-in Annotations (Applied to Java Code)

| Annotation | Purpose | Example |
|------------|---------|---------|
| `@Override` | Verifies method overrides superclass | `@Override void toString() {}` |
| `@SuppressWarnings` | Suppresses compiler warnings | `@SuppressWarnings("unchecked")` |
| `@Deprecated` | Marks element as obsolete | `@Deprecated void oldMethod() {}` |
| `@FunctionalInterface` | Marks interface as functional (Java 8+) | `@FunctionalInterface interface MyFunc {}` |
| `@SafeVarargs` | Suppresses varargs warnings (Java 7+) | `@SafeVarargs void method(T... args) {}` |

### Meta-Annotations (Applied to Other Annotations)

| Annotation | Purpose |
|------------|---------|
| `@Target` | Restricts where annotation can be applied |
| `@Retention` | Specifies how long annotation is retained |
| `@Inherited` | Allows annotation to be inherited by subclasses |
| `@Documented` | Includes annotation in Javadoc |
| `@Repeatable` | Allows annotation to be applied multiple times (Java 8+) |

### 7.2.1 @Override
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

### 7.2.2 @SuppressWarnings
```java
// Suppress unchecked warning for raw types
@SuppressWarnings("unchecked")
void rawTypeExample() {
    List list = new ArrayList();  // Raw type warning suppressed
    list.add("test");
}

// Common values: "unchecked", "deprecation", "rawtypes", "serial", "all"
```

### 7.2.3 @Deprecated
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

### 7.2.4 Custom Annotations
```java
// Declaration
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

### Annotation Targets
```java
@Target({ElementType.TYPE, ElementType.METHOD, ElementType.FIELD})
@interface MyAnnotation {}
```

**ElementType values:** TYPE, FIELD, METHOD, PARAMETER, CONSTRUCTOR, LOCAL_VARIABLE, ANNOTATION_TYPE, PACKAGE, TYPE_PARAMETER, TYPE_USE

---

## 7.3 Exception Handling

### 7.3.1 Basics

#### Definition
> An **exception** is an event that disrupts the normal flow of program execution. It represents an error condition.

#### Error vs Exception

| Aspect | Error | Exception |
|--------|-------|-----------|
| **Recoverable** | No | Yes |
| **Type** | Unchecked only | Checked or Unchecked |
| **Cause** | Environment (JVM) | Application code |
| **Examples** | OutOfMemoryError, StackOverflowError | IOException, NullPointerException |

#### Exception Hierarchy
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

### 7.3.2 Checked vs Unchecked Exceptions

| Aspect | Checked Exceptions | Unchecked Exceptions |
|--------|-------------------|---------------------|
| **Also Called** | Compile-time exceptions | Runtime exceptions |
| **Inheritance** | Extend `Exception` (not RuntimeException) | Extend `RuntimeException` |
| **Compiler Check** | Must handle or declare | No compile-time check |
| **Handling** | try-catch OR throws | Optional |
| **Examples** | IOException, SQLException, ClassNotFoundException | NullPointerException, ArrayIndexOutOfBoundsException, ArithmeticException |

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

#### Key Rules
- ✅ `try` must be followed by `catch` OR `finally` (or both)
- ✅ Multiple `catch` blocks allowed
- ✅ Catch order: **Subclass before Superclass**
- ✅ `finally` executes **always** (even if return in try/catch)
- ✅ `finally` won't execute if `System.exit()` called

#### Example: Multiple Catch
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

#### Java 7+ Multi-catch
```java
// Single catch for multiple exceptions
try {
    // code
} catch (IOException | NumberFormatException e) {
    System.out.println("Error: " + e.getMessage());
}
```

### 7.3.4 throw vs throws

| Aspect | `throw` | `throws` |
|--------|---------|----------|
| **Purpose** | Explicitly throw an exception | Declare exceptions method may throw |
| **Used With** | Exception **instance** | Exception **class** |
| **Location** | Inside method body | Method signature |
| **Multiple** | One at a time | Multiple allowed |
| **Checked Exception** | Must be caught or declared | Propagates to caller |

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

#### Purpose
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

## 7.4 Custom Exceptions

### Creating User-Defined Exception
```java
// 1. Extend Exception (checked) or RuntimeException (unchecked)
class InsufficientFundsException extends Exception {
    private double amount;
    
    public InsufficientFundsException(String message, double amount) {
        super(message);
        this.amount = amount;
    }
    
    public double getAmount() { return amount; }
}

// 2. Use in code
class BankAccount {
    private double balance = 1000;
    
    void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Insufficient balance", amount);
        }
        balance -= amount;
    }
}

// 3. Handle in caller
public static void main(String[] args) {
    BankAccount acc = new BankAccount();
    try {
        acc.withdraw(1500);
    } catch (InsufficientFundsException e) {
        System.out.println(e.getMessage() + ". Short by: " + (e.getAmount() - 1000));
    }
}
```

### Rules for Custom Exceptions
- ✅ Must extend `Exception` (checked) or `RuntimeException` (unchecked)
- ✅ Should provide constructors (message, cause)
- ✅ Override `getMessage()` if needed
- ✅ Follow naming convention: `XxxException`

---

## 7.5 final vs finally vs finalize

### Comparison Table

| Aspect | `final` | `finally` | `finalize()` |
|--------|---------|-----------|--------------|
| **Type** | Keyword | Block | Method |
| **Purpose** | Restrict modification | Cleanup code | GC cleanup |
| **Used With** | Variables, methods, classes | try-catch | Object class |
| **Execution** | Compile-time | Runtime (always) | Before GC (uncertain) |
| **Override** | N/A | N/A | Yes (protected) |

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

// finalize method
class Resource {
    @Override
    protected void finalize() throws Throwable {
        try {
            System.out.println("Cleaning up resource");
        } finally {
            super.finalize();
        }
    }
}
```

---

## 7.6 Important Exam Questions (from PYQ Analysis)

### High Priority (CRITICAL - Appeared 9/10 years)

**2-Mark Questions:**
1. Difference between `throw` and `throws`.
2. Difference between `final`, `finally`, `finalize`.
3. Difference between checked and unchecked exceptions.
4. What is an assertion? How to enable/disable?
5. What is `@Override`, `@SuppressWarnings`, `@Deprecated`?
6. Can we catch `AssertionError`?
7. Difference between Error and Exception.
8. What is exception hierarchy?
9. Can try exist without catch? (Java 7+)
10. Order of catch blocks (subclass first).

**5-Mark Questions:**
1. Explain exception handling mechanism with try-catch-finally.
2. Explain `throw` vs `throws` with examples.
3. Explain custom exception creation with program.
4. Explain assertions: syntax, enable/disable, use cases.
5. Explain built-in annotations with examples.
6. Difference between `final`, `finally`, `finalize` with examples.
7. Explain exception hierarchy with diagram.
8. Write program: ArrayIndexOutOfBounds + multiple catch + finally.

**10-Mark Questions:**
1. **Explain exception handling in detail: hierarchy, checked/unchecked, try-catch-finally, throw/throws, custom exceptions.** (Appeared 2021, 2022, 2023, 2024, 2025, 2026)
2. Explain assertions vs exception handling. Enable/disable assertions.
3. Explain annotations: built-in, meta-annotations, custom annotations.

### Programs to Practice
1. ✅ **Exception handling with ArrayIndexOutOfBounds + multiple catch + finally** - appeared 2022, 2024, 2025
2. ✅ **Custom exception (InsufficientFunds, InvalidInput)** - appeared 2024, 2026
3. ✅ **throw vs throws demonstration** - appeared 2022, 2023, 2025, 2026
4. ✅ **Assertions enable/disable example** - appeared 2023, 2024, 2025, 2026
5. ✅ **Built-in annotations (@Override, @SuppressWarnings, @Deprecated)** - appeared 2023, 2024

---

## 7.7 Summary of Unit 7

| Topic | Key Points |
|-------|------------|
| **Assertions** | `assert condition;` or `assert condition : message;`; disabled by default; enable with `-ea` |
| **Annotations** | Metadata; `@Override`, `@SuppressWarnings`, `@Deprecated`, `@FunctionalInterface` |
| **Meta-Annotations** | `@Target`, `@Retention`, `@Inherited`, `@Documented`, `@Repeatable` |
| **Exception** | Disrupts normal flow; `Throwable` → `Error`/`Exception` |
| **Checked Exceptions** | Compile-time checked; must handle/declare; extend `Exception` |
| **Unchecked Exceptions** | Runtime; extend `RuntimeException`; optional handling |
| **try-catch-finally** | try + (catch OR finally); multiple catch allowed; finally always executes |
| **throw** | Throw exception instance; inside method |
| **throws** | Declare exceptions in signature; propagates checked exceptions |
| **Custom Exception** | Extend `Exception` (checked) or `RuntimeException` (unchecked) |
| **final** | Keyword: variable=constant, method=no override, class=no extend |
| **finally** | Block: cleanup code, always executes |
| **finalize()** | Method: GC cleanup, deprecated since Java 9 |

---

## 7.8 Quick Reference: Exception Handling Flow

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