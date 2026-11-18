# Unit 2: Basics of Java

## Unit Overview
This unit covers Java data types, variables, literals, operators, statements, expressions, enumerated types, type casting, autoboxing/unboxing, and the Scanner class for input handling. Based on IGNOU MCS-206 Block 1 Unit 2 textbook and PYQ analysis (Dec 2021–June 2026).

---

## 2.1 Data Types in Java

### Topic Introduction
Java is a strongly typed language. Every variable must be declared with a data type before use. Data types define the size, range, and operations that can be performed on the data. Java's primitive types are **platform-independent** — sizes and ranges are fixed across all architectures.

### Primitive Data Types (8 Types)

| Category | Type | Size | Range | Default Value |
|----------|------|------|-------|---------------|
| **Integer** | `byte` | 1 byte (8 bits) | -128 to 127 | 0 |
| | `short` | 2 bytes (16 bits) | -32,768 to 32,767 | 0 |
| | `int` | 4 bytes (32 bits) | -2³¹ to 2³¹-1 (-2,147,483,648 to 2,147,483,647) | 0 |
| | `long` | 8 bytes (64 bits) | -2⁶³ to 2⁶³-1 | 0L |
| **Floating Point** | `float` | 4 bytes (32 bits) | ±3.4×10³⁸ (6-7 significant digits) | 0.0f |
| | `double` | 8 bytes (64 bits) | ±1.7×10³⁰⁸ (15 significant digits) | 0.0 |
| **Character** | `char` | 2 bytes (16 bits) | '\u0000' to '￿' (0 to 65,535) | '\u0000' |
| **Boolean** | `boolean` | 1 bit (stored in 32-bit int) | `true`, `false` | `false` |

### Key Points
- ✅ Size and range are **platform-independent** (unlike C/C++)
- ✅ `int` is the default for integer literals
- ✅ `double` is the default for floating-point literals
- ✅ `char` uses **Unicode** (16-bit), not ASCII (8-bit)
- ✅ `boolean` is not numeric (cannot use 0/1 directly)
- ✅ Integer types are **signed** (store both positive and negative)
- ✅ Floating-point literals default to `double`; use `F`/`f` suffix for `float`

### Declaration and Initialization
```java
// Declaration
int age;
double salary;
char grade;
boolean isStudent;

// Initialization
age = 25;
salary = 50000.50;
grade = 'A';
isStudent = true;

// Declaration with initialization
int score = 95;
final double PI = 3.14159;  // Constant

// Multiple variables of same type
int math = 90, science = 85, english = 88;
byte b = 10, c = 20;
```

### Wrapper Classes
Each primitive has a corresponding wrapper class (in `java.lang`):

| Primitive | Wrapper Class | Size Constant | Min Constant | Max Constant |
|-----------|---------------|---------------|--------------|--------------|
| `byte` | `Byte` | `Byte.SIZE` (8) | `Byte.MIN_VALUE` (-128) | `Byte.MAX_VALUE` (127) |
| `short` | `Short` | `Short.SIZE` (16) | `Short.MIN_VALUE` (-32,768) | `Short.MAX_VALUE` (32,767) |
| `int` | `Integer` | `Integer.SIZE` (32) | `Integer.MIN_VALUE` (-2,147,483,648) | `Integer.MAX_VALUE` (2,147,483,647) |
| `long` | `Long` | `Long.SIZE` (64) | `Long.MIN_VALUE` | `Long.MAX_VALUE` |
| `float` | `Float` | `Float.SIZE` (32) | `Float.MIN_VALUE` | `Float.MAX_VALUE` |
| `double` | `Double` | `Double.SIZE` (64) | `Double.MIN_VALUE` | `Double.MAX_VALUE` |
| `char` | `Character` | `Character.SIZE` (16) | `Character.MIN_VALUE` ('\u0000') | `Character.MAX_VALUE` ('￿') |
| `boolean` | `Boolean` | — | — | — |

**Useful Constants:**
```java
Integer.MAX_VALUE   // 2147483647
Integer.MIN_VALUE   // -2147483648
Integer.SIZE        // 32 (bits)
Double.MAX_VALUE    // 1.7976931348623157E308
Character.MIN_VALUE // '\u0000' (0)
Character.MAX_VALUE // '￿' (65535)
```

### Program: Display Size and Range of Primitive Types
```java
public class DataTypeRange {
    public static void main(String[] args) {
        System.out.println("Data Type\tSize(bits)\tMin Value\t\tMax Value");
        System.out.println("byte\t\t" + Byte.SIZE + "\t\t" + Byte.MIN_VALUE + "\t\t\t" + Byte.MAX_VALUE);
        System.out.println("short\t\t" + Short.SIZE + "\t\t" + Short.MIN_VALUE + "\t\t\t" + Short.MAX_VALUE);
        System.out.println("int\t\t" + Integer.SIZE + "\t\t" + Integer.MIN_VALUE + "\t\t" + Integer.MAX_VALUE);
        System.out.println("long\t\t" + Long.SIZE + "\t\t" + Long.MIN_VALUE + "\t\t" + Long.MAX_VALUE);
        System.out.println("float\t\t" + Float.SIZE + "\t\t" + Float.MIN_VALUE + "\t\t\t" + Float.MAX_VALUE);
        System.out.println("double\t\t" + Double.SIZE + "\t\t" + Double.MIN_VALUE + "\t\t" + Double.MAX_VALUE);
        System.out.println("char\t\t" + Character.SIZE + "\t\t" + (int)Character.MIN_VALUE + "\t\t\t" + (int)Character.MAX_VALUE);
        System.out.println("boolean\t\t1 (in 32-bit)\tfalse\t\t\ttrue");
    }
}
```

---

## 2.2 Variables

### Topic Introduction
A variable is a named memory location that stores data of a specific type.

### Variable Naming Rules
- Must start with: letter, underscore (`_`), or dollar sign (`$`)
- Can contain: letters, digits, underscore, dollar sign
- **Cannot** start with a digit
- **Cannot** use Java keywords/reserved words
- Case-sensitive (`age` ≠ `Age`)
- No spaces or special characters (@, %, etc.)
- Convention: `camelCase` (e.g., `studentName`, `totalMarks`, `accountNumber`)

### Types of Variables

| Type | Scope | Lifetime | Default Value |
|------|-------|----------|---------------|
| **Local Variable** | Within method/block `{}` | Method execution | **Must initialize before use** |
| **Instance Variable** | Class level (non-static) | Object lifetime | 0, 0.0, '\u0000', `false`, `null` |
| **Class Variable (static)** | Class level (`static`) | Program lifetime | 0, 0.0, '\u0000', `false`, `null` |

> **Note**: Instance and class variables get default values automatically. Local variables **must** be explicitly initialized before use.

### Variable Declaration Syntax
```java
datatype identifier [= value] {, identifier [= value]};
```

```java
// Single variable
int rollNumber;

// Multiple variables
int math = 90, science = 85, english = 88;

// With initialization
double price = 199.99;
boolean passed = true;
char grade = 'A';
```

### Literals
Literals are fixed values in source code representation.

| Type | Examples |
|------|----------|
| **Integer** | `145`, `104L`, `0XFF` (hex), `0b1010` (binary), `777` |
| **Float** | `35.6f`, `86.4E2f`, `1.5F`, `2.56F` |
| **Double** | `16.5`, `85.6`, `96.4E8`, `15e45`, `.36E2` |
| **Boolean** | `true`, `false` |
| **Character** | `'c'`, `'#'`, `'5'`, `'\n'`, `'\\'`, `'\"'`, `'\t'` |
| **String** | `"Java Programming"`, `"Hello IGNOU!"` |
| **Null** | `null` |

> **Important**: Character literals use **single quotes** (`'A'`). String literals use **double quotes** (`"Hello"`). `'\n'` is a character; `"\n"` is a string.

### Constants (`final` keyword)
```java
final int MAX_STUDENTS = 60;        // Compile-time constant
final double PI = 3.14159;
final String COLLEGE_NAME = "IGNOU";
// final variables cannot be modified after initialization
// Convention: UPPER_SNAKE_CASE for constants
```

---

## 2.3 Enumerated Types (`enum`)

### Topic Introduction
An **enumerated type** (`enum`) is a special user-defined data type consisting of a set of predefined constants. Added in JDK 5. Each enum constant is implicitly `public`, `static`, and `final`.

### Declaration and Usage
```java
// Basic enum
enum Size { SMALL, MEDIUM, LARGE, EXTRALARGE }

// Accessing constants
Size mySize = Size.MEDIUM;
System.out.println(mySize);  // Output: MEDIUM

// Enum with methods
enum Day {
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY;
    
    boolean isWeekend() {
        return this == SATURDAY || this == SUNDAY;
    }
}

// Usage
Day today = Day.WEDNESDAY;
if (today.isWeekend()) { ... }
```

### Example: Course Enumeration
```java
enum PGDCA_NEW_Courses_I { 
    MCS_201, MCS_202, MCS_203, MCS_204, MCSL_205 
}

public class EnumDemo {
    public static void main(String[] args) {
        System.out.println("Value of enum: " + PGDCA_NEW_Courses_I.MCS_201);
        System.out.println("Value of enum: " + PGDCA_NEW_Courses_I.MCS_202);
        
        // Iterate all constants
        for (PGDCA_NEW_Courses_I c : PGDCA_NEW_Courses_I.values()) {
            System.out.println(c + " - ordinal: " + c.ordinal());
        }
    }
}
```

**Key Points:**
- Enums are **reference types** (classes), not primitives
- Can have constructors, fields, methods
- Cannot extend other classes (already extends `java.lang.Enum`)
- Can implement interfaces
- `values()` returns array of all constants; `ordinal()` returns position (0-based)

---

## 2.4 Unicode

### Topic Introduction
Unicode is a universal character encoding standard supporting all world languages.

### Key Points
- **ASCII**: 1 byte (8 bits), 128 characters (English only)
- **Unicode**: 2 bytes (16 bits) in Java `char`, 65,536+ characters
- Java `char` is **16-bit Unicode** (UTF-16 code unit)
- Covers all writing systems (modern & ancient), technical symbols, punctuation

### Unicode Formats
| Format | Description |
|--------|-------------|
| **UTF-32** | 32-bit code units, one per code point |
| **UTF-16** | Default for Java; 1-2 16-bit code units per code point |
| **UTF-8** | 1-4 8-bit code units (bytes) per code point; web standard |

### Escape Sequences
| Sequence | Meaning |
|----------|---------|
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |
| `\b` | Backspace |
| `\f` | Form feed |
| `\n` | New line |
| `\r` | Carriage return |
| `\t` | Horizontal tab |
| `\uXXXX` | Unicode character (4 hex digits) |

```java
char c1 = '\n';           // Newline
char c2 = 'A';       // 'A' (Unicode for 'A')
char c3 = 'अ';       // 'अ' (Devanagari)
String s = "Line1\nLine2";
String unicode = "Java";  // "Java"
```

---

## 2.5 Java Keywords (Reserved Words)

### 53 Keywords (Java 17+)
Keywords have special meaning and **cannot** be used as identifiers.

| Category | Keywords |
|----------|----------|
| **Access Modifiers** | `public`, `private`, `protected` (`default` = no keyword) |
| **Class/Interface** | `class`, `interface`, `abstract`, `extends`, `implements` |
| **Primitive Types** | `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean` |
| **Control Flow** | `if`, `else`, `switch`, `case`, `default`, `break`, `continue`, `return` |
| **Loops** | `for`, `while`, `do` |
| **Exception Handling** | `try`, `catch`, `finally`, `throw`, `throws` |
| **Modifiers** | `final`, `static`, `synchronized`, `volatile`, `transient`, `native`, `strictfp` |
| **Others** | `this`, `super`, `new`, `instanceof`, `package`, `import`, `enum`, `assert`, `const*`, `goto*`, `var`, `record`, `sealed`, `permits`, `yield` |

> *`const` and `goto` are reserved but not used. `true`, `false`, `null` are literals, not keywords.*
> **Newer keywords**: `var` (Java 10), `record`/`sealed`/`permits` (Java 16+), `yield` (Java 13+).

---

## 2.6 Operators in Java

### Topic Introduction
Operators are symbols that perform operations on operands (variables/values).

### Operator Classification

| Category | Operators |
|----------|-----------|
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `++`, `--` |
| **Relational** | `>`, `>=`, `<`, `<=`, `==`, `!=` |
| **Logical** | `&&`, `||`, `!`, `&`, `|`, `^` |
| **Bitwise** | `&`, `|`, `^`, `~`, `<<`, `>>`, `>>>` |
| **Assignment** | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, `>>>=` |
| **Conditional** | `? :` |
| **Instance/Type** | `instanceof`, `(type)` |
| **Member Access** | `.` (dot), `[]` (array) |
| **Other** | `new`, `->` (lambda), `::` (method ref) |

---

### 2.6.1 Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `a + b` | Sum |
| `-` | Subtraction | `a - b` | Difference |
| `*` | Multiplication | `a * b` | Product |
| `/` | Division | `a / b` | Quotient |
| `%` | Modulus | `a % b` | Remainder |
| `++` | Increment | `++a` / `a++` | Add 1 |
| `--` | Decrement | `--a` / `a--` | Subtract 1 |

#### Pre/Post Increment/Decrement
| Form | Name | Behavior |
|------|------|----------|
| `++a` | Pre-increment | Increment first, then use value |
| `a++` | Post-increment | Use value first, then increment |
| `--a` | Pre-decrement | Decrement first, then use value |
| `a--` | Post-decrement | Use value first, then decrement |

```java
int a = 5;
int b = ++a;  // a=6, b=6
int c = a++;  // c=6, a=7
int d = --a;  // a=6, d=6
int e = a--;  // e=6, a=5

// Division behavior
int x = 7 / 2;      // 3 (integer division)
double y = 7.0 / 2; // 3.5 (floating-point division)
```

---

### 2.6.2 Relational Operators

| Operator | Name | Example | Returns `true` if |
|----------|------|---------|-------------------|
| `>` | Greater than | `a > b` | a is greater than b |
| `>=` | Greater than or equal | `a >= b` | a ≥ b |
| `<` | Less than | `a < b` | a is less than b |
| `<=` | Less than or equal | `a <= b` | a ≤ b |
| `==` | Equal to | `a == b` | a equals b |
| `!=` | Not equal to | `a != b` | a does not equal b |

**Result**: Always `boolean` (`true`/`false`)

```java
int a = 10, b = 20;
System.out.println(a > b);   // false
System.out.println(a <= b);  // true
System.out.println(a != b);  // true
```

---

### 2.6.3 Logical Operators

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&&` | Conditional AND | `a && b` | True if both true; **short-circuit** |
| `||` | Conditional OR | `a || b` | True if either true; **short-circuit** |
| `!` | Logical NOT | `!a` | Inverts boolean value |
| `&` | Boolean AND | `a & b` | True if both true; **no** short-circuit |
| `|` | Boolean OR | `a \| b` | True if either true; **no** short-circuit |
| `^` | Boolean XOR | `a ^ b` | True if exactly one is true |

**Short-Circuit Evaluation:**
```java
// && stops if first is false
if (a != 0 && b/a > 2) { ... }  // Safe: won't divide by zero

// & evaluates both always
if (a != 0 & b/a > 2) { ... }   // Risk: evaluates both sides

// Practical example
boolean result = (5 > 3) && (10 < 5);  // false (second not evaluated)
boolean result2 = (5 > 3) & (10 < 5);  // false (both evaluated)
```

---

### 2.6.4 Bitwise Operators
Operate on integer types (`byte`, `short`, `int`, `long`, `char`) at bit level.

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&` | Bitwise AND | `a & b` | 1 if both bits are 1 |
| `|` | Bitwise OR | `a \| b` | 1 if either bit is 1 |
| `^` | Bitwise XOR | `a ^ b` | 1 if bits are different |
| `~` | Bitwise Complement | `~a` | Flips all bits (1→0, 0→1) |
| `<<` | Left Shift | `a << 2` | Shift left, fill with 0 |
| `>>` | Right Shift | `a >> 2` | Shift right, preserve sign (arithmetic) |
| `>>>` | Unsigned Right Shift | `a >>> 2` | Shift right, fill with 0 (logical) |

```java
int a = 6;   // Binary: 0110
int b = 4;   // Binary: 0100

a & b  = 4   // 0100
a | b  = 6   // 0110
a ^ b  = 2   // 0010
~a     = -7  // Complement (2's complement: 11111001)
a << 1 = 12  // 1100 (6 * 2)
a >> 1 = 3   // 0011 (6 / 2)
a >>> 1 = 3  // 0011 (same for positive)

// Use cases: fast multiply/divide by powers of 2, bit flags, encryption
int flags = 0;
flags = flags | (1 << 0);  // Set bit 0
flags = flags | (1 << 2);  // Set bit 2
boolean isSet = (flags & (1 << 2)) != 0;  // Check bit 2
```

---

### 2.6.5 Assignment Operators

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `a = 5` | `a = 5` |
| `+=` | `a += 3` | `a = a + 3` |
| `-=` | `a -= 2` | `a = a - 2` |
| `*=` | `a *= 4` | `a = a * 4` |
| `/=` | `a /= 2` | `a = a / 2` |
| `%=` | `a %= 3` | `a = a % 3` |
| `&=` | `a &= b` | `a = a & b` |
| `\|=` | `a \|= b` | `a = a \| b` |
| `^=` | `a ^= b` | `a = a ^ b` |
| `<<=` | `a <<= 2` | `a = a << 2` |
| `>>=` | `a >>= 2` | `a = a >> 2` |
| `>>>=` | `a >>>= 2` | `a = a >>> 2` |

**Multiple Assignment:**
```java
int a = b = c = 10;  // All get value 10 (right-to-left associativity)
int x = 5, y = 10;
x += y += 5;         // y=15, x=20
```

---

### 2.6.6 Conditional (Ternary) Operator
```java
variable = (condition) ? valueIfTrue : valueIfFalse;
```

```java
int max = (a > b) ? a : b;
String result = (score >= 40) ? "Pass" : "Fail";
int abs = (n < 0) ? -n : n;

// Nested ternary (use sparingly)
String grade = (marks >= 90) ? "A" : (marks >= 75) ? "B" : (marks >= 60) ? "C" : "F";
```

---

### 2.6.7 `instanceof` Operator
```java
objectReference instanceof ClassName
```
Returns `true` if object is an instance of the class (or subclass/implementing interface).

```java
String s = "Hello";
System.out.println(s instanceof String);  // true
System.out.println(s instanceof Object);  // true
System.out.println(s instanceof Integer); // false

// Pattern matching (Java 16+)
if (obj instanceof String str) {
    System.out.println(str.length());  // str is already cast
}
```

---

### 2.6.8 Operator Precedence (High to Low)

| Precedence | Operators | Associativity |
|------------|-----------|---------------|
| 1 (Highest) | `[]` `.` `()` (method call) | Left → Right |
| 2 | `++` `--` `+` `-` `~` `!` (unary) `new` `(type)` | Right → Left |
| 3 | `*` `/` `%` | Left → Right |
| 4 | `+` `-` | Left → Right |
| 5 | `<<` `>>` `>>>` | Left → Right |
| 6 | `<` `>` `<=` `>=` `instanceof` | Left → Right |
| 7 | `==` `!=` | Left → Right |
| 8 | `&` | Left → Right |
| 9 | `^` | Left → Right |
| 10 | `\|` | Left → Right |
| 11 | `&&` | Left → Right |
| 12 | `\|\|` | Left → Right |
| 13 | `?:` (ternary) | Right → Left |
| 14 (Lowest) | `=` `+=` `-=` `*=` `/=` `%=` `&=` `^=` `\|=` `<<=` `>>=` `>>>=` | Right → Left |

> **Tip**: Use parentheses `()` to make precedence explicit and improve readability.
> ```java
> // Unclear
> int result = a + b * c / d;
> // Clear
> int result = a + ((b * c) / d);
> ```

---

## 2.7 Type Casting and Type Promotion

### Implicit Casting (Widening / Automatic)
Smaller type → Larger type. No data loss.
```
byte → short → int → long → float → double
           char → int → long → float → double
```
```java
int i = 100;
long l = i;        // Automatic
float f = l;       // Automatic
double d = f;      // Automatic
```

### Explicit Casting (Narrowing)
Larger type → Smaller type. **Possible data loss**. Requires cast operator.
```java
double d = 9.78;
int i = (int) d;   // i = 9 (truncates decimal)

long l = 10000000000L;
int i2 = (int) l;  // Overflow! Data loss

float f = 3.14f;
int i3 = (int) f;  // i3 = 3
```

### Type Promotion in Expressions
When operands differ, Java promotes to the **largest type** in the expression.
```java
byte b = 10;
short s = 20;
int result = b + s;  // byte and short promoted to int

// All integer literals are int by default
byte b2 = 10;
b2 = b2 + 5;         // Error! int + byte = int, cannot assign to byte
b2 = (byte)(b2 + 5); // OK with cast
b2 += 5;             // OK! Compound assignment includes implicit cast
```

---

## 2.8 Autoboxing and Unboxing

### Autoboxing (Primitive → Wrapper)
Automatic conversion by compiler.
```java
Integer i = 10;        // int → Integer
Double d = 3.14;       // double → Double
Character c = 'A';     // char → Character
Boolean b = true;      // boolean → Boolean
List<Integer> list = new ArrayList<>();
list.add(5);           // int → Integer (autoboxing)
```

### Unboxing (Wrapper → Primitive)
Automatic conversion when primitive is needed.
```java
Integer i = 10;
int n = i;             // Integer → int

Double d = 3.14;
double val = d;        // Double → double

// In expressions
Integer a = 5, b = 10;
int sum = a + b;       // Unboxing happens automatically
```

### Caveats
```java
Integer a = 1000, b = 1000;
System.out.println(a == b);  // false! Different objects

Integer c = 100, d = 100;
System.out.println(c == d);  // true! Cached (-128 to 127)

// Always use .equals() for wrapper comparison
System.out.println(a.equals(b));  // true

// NullPointerException risk
Integer x = null;
int y = x;  // NullPointerException at runtime!
```

---

## 2.9 Expressions and Statements

### Expressions
Combination of variables, operators, method calls that evaluates to a single value.
```java
a + b * c                    // Arithmetic expression
Math.sqrt(x)                 // Method call expression
"Hello" + "World"            // String concatenation
(score >= 40) ? "Pass":"Fail" // Ternary expression
new Student()                // Object creation expression
```

### Statements
Complete unit of execution ending with semicolon `;`.

**Types:**
1. **Expression Statements**: Assignment, increment/decrement, method call, object creation
2. **Declaration Statements**: Variable declarations
3. **Control Statements**: `if`, `for`, `while`, `switch`, etc.

```java
int x = 10;                  // Declaration statement
x = x + 5;                   // Expression statement (assignment)
x++;                         // Expression statement (increment)
System.out.println(x);       // Expression statement (method call)
Student s = new Student();   // Expression statement (object creation)
```

### Blocks
Group of statements enclosed in `{ }`. Defines scope for local variables.
```java
{
    int blockVar = 5;  // Local to this block
}
```

---

## 2.10 Scanner Class for Input

### Topic Introduction
`Scanner` class (in `java.util` package) reads input from various sources (console, file, string).

### Common Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `nextInt()` | `int` | Reads integer |
| `nextLong()` | `long` | Reads long |
| `nextShort()` | `short` | Reads short |
| `nextByte()` | `byte` | Reads byte |
| `nextFloat()` | `float` | Reads float |
| `nextDouble()` | `double` | Reads double |
| `nextBoolean()` | `boolean` | Reads boolean |
| `next()` | `String` | Reads next token (word, space-delimited) |
| `nextLine()` | `String` | Reads entire line (including spaces) |

### Important: `next()` vs `nextLine()` Pitfall
```java
Scanner sc = new Scanner(System.in);
int age = sc.nextInt();      // Reads number, leaves \n in buffer
sc.nextLine();               // CONSUME the leftover newline!
String name = sc.nextLine(); // Now reads full name correctly
```

### Example Programs

**Basic Input:**
```java
import java.util.Scanner;

public class InputDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter name: ");
        String name = sc.nextLine();
        
        System.out.print("Enter age: ");
        int age = sc.nextInt();
        sc.nextLine();  // Consume newline
        
        System.out.print("Enter height: ");
        double height = sc.nextDouble();
        
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Height: " + height);
        
        sc.close();
    }
}
```

**Even/Odd Check:**
```java
import java.util.Scanner;

public class EvenOdd {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        
        if (num % 2 == 0)
            System.out.println("Even");
        else
            System.out.println("Odd");
    }
}
```

**Circle Area (using `final` constant):**
```java
import java.util.Scanner;

public class CircleArea {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter radius: ");
        double r = sc.nextDouble();
        
        final double PI = 3.14;
        double area = PI * r * r;
        
        System.out.println("Area: " + area);
    }
}
```

**Comprehensive Scanner Demo (All Types):**
```java
import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter byte: ");    byte b = sc.nextByte();
        System.out.print("Enter short: ");   short s = sc.nextShort();
        System.out.print("Enter int: ");     int i = sc.nextInt();
        System.out.print("Enter long: ");    long l = sc.nextLong();
        System.out.print("Enter float: ");   float f = sc.nextFloat();
        System.out.print("Enter double: ");  double d = sc.nextDouble();
        System.out.print("Enter boolean: "); boolean bool = sc.nextBoolean();
        sc.nextLine(); // consume newline
        System.out.print("Enter string: ");  String str = sc.nextLine();
        
        System.out.println("\n--- Values Entered ---");
        System.out.println("byte: " + b);
        System.out.println("short: " + s);
        System.out.println("int: " + i);
        System.out.println("long: " + l);
        System.out.println("float: " + f);
        System.out.println("double: " + d);
        System.out.println("boolean: " + bool);
        System.out.println("String: " + str);
        
        sc.close();
    }
}
```

---

## 2.11 Check Your Progress (Textbook Exercises)

### Check Your Progress - 1
1. **What is literal in Java?**
   > A literal represents a value of a certain type. It is the source code representation of a fixed value in memory. Types: number literals (integer, float), character literals, boolean literals, string literals.

2. **Write a program to calculate Area of a circle using `final` keyword.**
   ```java
   import java.util.Scanner;
   public class CircleArea {
       public static void main(String[] args) {
           final float PI = 3.14F;
           int r; float area;
           Scanner sc = new Scanner(System.in);
           System.out.println("Enter the Radius of Circle: ");
           r = sc.nextInt();
           area = PI * r * r;
           System.out.println("Area of Circle: " + area);
       }
   }
   ```

3. **What is boolean data type in Java?**
   > Boolean data type is used to define logical variables with only two values: `true` or `false`. Default value is `false`. Size is 1 bit (stored in 32-bit int).

### Check Your Progress - 2
1. **Use of relational operators with example.**
   > Relational operators compare two operands and return boolean. Example: `a > b`, `a == b`, `a <= b`. Used for decision making.

2. **Combined assignment operator with example.**
   > Combination of arithmetic operator with assignment. Example: `a += 2` equivalent to `a = a + 2`. Others: `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, `>>>=`.

3. **Program using `&` and `|` operators.**
   ```java
   public class BitwiseDemo {
       public static void main(String[] args) {
           int A = 16, B = 4;
           System.out.println("A & B = " + (A & B));  // 0
           System.out.println("A | B = " + (A | B));  // 20
           System.out.println("A ^ B = " + (A ^ B));  // 20
       }
   }
   ```

### Check Your Progress - 3
1. **Output of CircleArea program if input is 7:**
   > Area of Circle: 153.86

2. **Program to read name, address, mobile and display.**
   ```java
   import java.util.Scanner;
   public class UserDetails {
       public static void main(String[] args) {
           Scanner sc = new Scanner(System.in);
           System.out.print("Enter name: ");    String name = sc.nextLine();
           System.out.print("Enter address: "); String addr = sc.nextLine();
           System.out.print("Enter mobile: ");  String mob = sc.nextLine();
           System.out.println("Name: " + name);
           System.out.println("Address: " + addr);
           System.out.println("Mobile: " + mob);
       }
   }
   ```

---

## 2.12 Important Exam Questions (from PYQ Analysis)

### HIGH Priority (Frequently Asked — 2022–2026)

#### 2-Mark Questions:
1. **List Java primitive data types with sizes and ranges.** (2022, 2024)
2. **Difference between `int` and `Integer`.** (Autoboxing, null, methods)
3. **What is a literal? Give examples of each type.** (2023)
4. **Difference between `float` and `double`.** (Precision, size, default)
5. **What is Unicode? How many bits in Java `char`?** (16 bits, UTF-16)
6. **What are escape sequences? List any 4 with meanings.**
7. **Difference between `++i` and `i++`.** (Pre vs post)
8. **What is type casting? Implicit vs explicit with examples.**
9. **Difference between `&&` and `&`, `||` and `|`.** (Short-circuit)
10. **What is `final` keyword? Use with variable, method, class.**
11. **What is an enumerated type (`enum`)? Give example.**

#### 5-Mark Questions:
1. **Explain all data types in Java with sizes, ranges, and default values.** (2024)
2. **Write a program to calculate area of circle/rectangle using Scanner class.** (2022, 2024)
3. **Explain arithmetic operators with examples and pre/post increment.** (2023)
4. **Explain relational and logical operators with truth tables.** (2022, 2024)
5. **Write a program demonstrating pre/post increment/decrement.**
6. **Explain bitwise operators with examples.** (2023, 2024)
7. **Write a program to swap two numbers without third variable.**
8. **Explain operator precedence with example expression evaluation.**
9. **Difference between `&&` and `&`, `||` and `|` with code example.**
10. **Explain `enum` with example. How to iterate enum values?**
11. **What is autoboxing and unboxing? Explain with examples and caveats.**
12. **Explain type promotion in expressions with examples.**
13. **Write a program demonstrating all Scanner methods.**

#### 10-Mark Questions:
1. **Explain all types of operators in Java with examples and precedence table.** (2023, 2024)
2. **Write a comprehensive program demonstrating Scanner class with all data types.**
3. **Explain data types, variables, literals, and constants with examples.**

### MEDIUM Priority
- **Java Keywords** — List categories, explain `const`/`goto` reserved
- **Unicode** — UTF-8/16/32, escape sequences, char vs String
- **Variable types** — Local, instance, static — scope, lifetime, defaults

### LOW Priority
- **Type casting** — Widening/narrowing, promotion rules
- **Autoboxing/Unboxing** — Caching, NPE risk, `==` vs `.equals()`

---

## 2.13 Programs to Practice

1. ✅ Area of circle / rectangle
2. ✅ Even/Odd check
3. ✅ Largest of three numbers (ternary operator)
4. ✅ Swap two numbers (with/without third variable)
5. ✅ Temperature conversion (C↔F)
6. ✅ Simple interest calculator
7. ✅ Character classification (vowel/consonant/digit/special)
8. ✅ **Enum demonstration** (days, sizes, courses)
9. ✅ **Scanner with all data types**
10. ✅ **Bitwise operations demo** (flags, multiplication by 2)
11. ✅ **Operator precedence evaluation** (with parentheses)
12. ✅ **Autoboxing/unboxing demo** (cache behavior, NPE)

---

## 2.14 Summary of Unit 2

| Topic | Key Points |
|-------|------------|
| **Primitive Types** | 8 types: byte, short, int, long, float, double, char, boolean |
| **Sizes** | Fixed, platform-independent (1, 2, 4, 8 bytes) |
| **Variables** | Local (must init), Instance (default), Static (default) |
| **Literals** | Fixed values; suffixes: `L`/`l` (long), `F`/`f` (float) |
| **Constants** | `final` keyword; UPPER_SNAKE_CASE convention |
| **Enum** | User-defined constants; `enum` keyword; implicit `public static final` |
| **Unicode** | 16-bit char; UTF-16 default; `\uXXXX` escapes |
| **Keywords** | 53 reserved words; case-sensitive; `true`/`false`/`null` are literals |
| **Operators** | Arithmetic, Relational, Logical, Bitwise, Assignment, Ternary, `instanceof` |
| **Precedence** | High: `[]`, `.`, `()` → Low: Assignment (right-associative) |
| **Type Casting** | Implicit (widening) vs Explicit (narrowing, data loss) |
| **Autoboxing** | Primitive ↔ Wrapper; cache -128 to 127; NPE risk |
| **Scanner** | `java.util.Scanner`; `nextInt()`, `nextLine()`, etc.; consume newline after `nextInt()` |

---

## 2.15 Quick Reference: Operator Precedence Cheat Sheet

```
HIGHEST
  [] . ()           // Postfix
  ++ -- + - ~ !     // Unary
  * / %             // Multiplicative
  + -               // Additive
  << >> >>>         // Shift
  < > <= >= instanceof  // Relational
  == !=             // Equality
  &                 // Bitwise AND
  ^                 // Bitwise XOR
  |                 // Bitwise OR
  &&                // Logical AND
  ||                // Logical OR
  ?:                // Ternary
  = += -= *= /= %= &= ^= |= <<= >>= >>>=  // Assignment
LOWEST
```

> **Memory aid**: **"Uncle Charlie Makes Amazing Soup; Eager Brothers Like Oranges, And Try Conditional Assignments"**
> (Unary, Cast, Multiplicative, Additive, Shift, Equality/Relational, Bitwise AND, Bitwise XOR, Bitwise OR, Logical AND, Logical OR, Ternary, Assignment)

---

*Based on IGNOU MCS-206 Block 1 Unit 2 "Basics of Java" and PYQ Analysis (Dec 2021 – June 2026)*