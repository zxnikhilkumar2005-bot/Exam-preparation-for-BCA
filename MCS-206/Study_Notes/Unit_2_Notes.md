# Unit 2: Basics of Java

## Unit Overview
This unit covers Java data types, variables, literals, operators, statements, expressions, and the Scanner class for input handling.

---

## 2.1 Data Types in Java

### Topic Introduction
Java is a strongly typed language. Every variable must be declared with a data type before use. Data types define the size, range, and operations that can be performed on the data.

### Primitive Data Types (8 Types)

| Category | Type | Size | Range | Default Value |
|----------|------|------|-------|---------------|
| **Integer** | `byte` | 1 byte (8 bits) | -128 to 127 | 0 |
| | `short` | 2 bytes (16 bits) | -32,768 to 32,767 | 0 |
| | `int` | 4 bytes (32 bits) | -2³¹ to 2³¹-1 | 0 |
| | `long` | 8 bytes (64 bits) | -2⁶³ to 2⁶³-1 | 0L |
| **Floating Point** | `float` | 4 bytes (32 bits) | ±3.4×10³⁸ (6-7 digits) | 0.0f |
| | `double` | 8 bytes (64 bits) | ±1.7×10³⁰⁸ (15 digits) | 0.0 |
| **Character** | `char` | 2 bytes (16 bits) | '\u0000' to '￿' (0 to 65,535) | '\u0000' |
| **Boolean** | `boolean` | 1 bit (in 32-bit int) | true, false | false |

### Key Points
- ✅ Size and range are **platform-independent** (unlike C/C++)
- ✅ `int` is the default for integer literals
- ✅ `double` is the default for floating-point literals
- ✅ `char` uses **Unicode** (16-bit), not ASCII (8-bit)
- ✅ `boolean` is not numeric (cannot use 0/1)

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
```

### Wrapper Classes
Each primitive has a corresponding wrapper class:
| Primitive | Wrapper Class |
|-----------|---------------|
| byte | Byte |
| short | Short |
| int | Integer |
| long | Long |
| float | Float |
| double | Double |
| char | Character |
| boolean | Boolean |

**Useful Constants:**
```java
Integer.MAX_VALUE  // 2147483647
Integer.MIN_VALUE  // -2147483648
Integer.SIZE       // 32 (bits)
Double.MAX_VALUE   // 1.7976931348623157E308
Character.MIN_VALUE // '\u0000'
```

---

## 2.2 Variables

### Topic Introduction
A variable is a named memory location that stores data of a specific type.

### Variable Naming Rules
- Must start with: letter, underscore (`_`), or dollar sign (`$`)
- Can contain: letters, digits, underscore, dollar sign
- **Cannot** start with a digit
- **Cannot** use Java keywords
- Case-sensitive (`age` ≠ `Age`)
- No spaces or special characters (@, %, etc.)
- Convention: `camelCase` (e.g., `studentName`, `totalMarks`)

### Types of Variables

| Type | Scope | Lifetime | Default Value |
|------|-------|----------|---------------|
| **Local Variable** | Within method/block | Method execution | **Must initialize** |
| **Instance Variable** | Class level (non-static) | Object lifetime | 0, null, false |
| **Class Variable (static)** | Class level (static) | Program lifetime | 0, null, false |

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
```

### Literals
Literals are fixed values in source code.

| Type | Examples |
|------|----------|
| **Integer** | `145`, `104L`, `0XFF` (hex), `0b1010` (binary) |
| **Float** | `35.6f`, `86.4E2f`, `1.5F` |
| **Double** | `16.5`, `85.6`, `96.4E8` |
| **Boolean** | `true`, `false` |
| **Character** | `'c'`, `'#'`, `'\n'`, `'\\'`, `'\"'` |
| **String** | `"Java Programming"` |
| **Null** | `null` |

### Constants
```java
final int MAX_STUDENTS = 60;      // Compile-time constant
final double PI = 3.14159;
final String COLLEGE_NAME = "IGNOU";
// final variables cannot be modified after initialization
```

---

## 2.3 Unicode

### Topic Introduction
Unicode is a universal character encoding standard that supports all world languages.

### Key Points
- **ASCII**: 1 byte (8 bits), 128 characters (English only)
- **Unicode**: 2 bytes (16 bits) in Java, 65,536+ characters
- Java `char` is **16-bit Unicode**
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
char c1 = '\n';        // Newline
char c2 = 'A';    // 'A' (Unicode)
String s = "Line1\nLine2";
```

---

## 2.4 Java Keywords

### Reserved Words (53 Keywords)
Keywords have special meaning and **cannot** be used as identifiers.

| Category | Keywords |
|----------|----------|
| **Access Modifiers** | `public`, `private`, `protected`, `default` (no keyword) |
| **Class/Interface** | `class`, `interface`, `abstract`, `extends`, `implements` |
| **Primitive Types** | `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean` |
| **Control Flow** | `if`, `else`, `switch`, `case`, `default`, `break`, `continue`, `return` |
| **Loops** | `for`, `while`, `do` |
| **Exception Handling** | `try`, `catch`, `finally`, `throw`, `throws` |
| **Modifiers** | `final`, `static`, `synchronized`, `volatile`, `transient`, `native`, `strictfp` |
| **Others** | `this`, `super`, `new`, `instanceof`, `package`, `import`, `enum`, `assert`, `const*`, `goto*` |

> *`const` and `goto` are reserved but not used.

---

## 2.5 Operators in Java

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

---

### 2.5.1 Arithmetic Operators

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
```

---

### 2.5.2 Relational Operators

| Operator | Name | Example | Returns true if |
|----------|------|---------|-----------------|
| `>` | Greater than | `a > b` | a is greater than b |
| `>=` | Greater than or equal | `a >= b` | a ≥ b |
| `<` | Less than | `a < b` | a is less than b |
| `<=` | Less than or equal | `a <= b` | a ≤ b |
| `==` | Equal to | `a == b` | a equals b |
| `!=` | Not equal to | `a != b` | a does not equal b |

**Result**: Always `boolean` (true/false)

---

### 2.5.3 Logical Operators

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&&` | Conditional AND | `a && b` | True if both true; short-circuit |
| `||` | Conditional OR | `a || b` | True if either true; short-circuit |
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
```

---

### 2.5.4 Bitwise Operators

| Operator | Name | Example | Description |
|----------|------|---------|-------------|
| `&` | Bitwise AND | `a & b` | 1 if both bits are 1 |
| `|` | Bitwise OR | `a \| b` | 1 if either bit is 1 |
| `^` | Bitwise XOR | `a ^ b` | 1 if bits are different |
| `~` | Bitwise Complement | `~a` | Flips all bits (1→0, 0→1) |
| `<<` | Left Shift | `a << 2` | Shift left, fill with 0 |
| `>>` | Right Shift | `a >> 2` | Shift right, preserve sign |
| `>>>` | Unsigned Right Shift | `a >>> 2` | Shift right, fill with 0 |

```java
int a = 6;   // Binary: 0110
int b = 4;   // Binary: 0100

a & b  = 4   // 0100
a | b  = 6   // 0110
a ^ b  = 2   // 0010
~a     = -7  // Complement (2's complement)
a << 1 = 12  // 1100
a >> 1 = 3   // 0011
```

---

### 2.5.5 Assignment Operators

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
int a = b = c = 10;  // All get value 10
```

---

### 2.5.6 Conditional (Ternary) Operator
```java
variable = (condition) ? valueIfTrue : valueIfFalse;
```

```java
int max = (a > b) ? a : b;
String result = (score >= 40) ? "Pass" : "Fail";
```

---

### 2.5.7 Operator Precedence (High to Low)

| Precedence | Operators |
|------------|-----------|
| 1 (Highest) | `[]` `.` `()` (method call) |
| 2 | `++` `--` `+` `-` `~` `!` (unary) `new` `(type)` |
| 3 | `*` `/` `%` |
| 4 | `+` `-` |
| 5 | `<<` `>>` `>>>` |
| 6 | `<` `>` `<=` `>=` `instanceof` |
| 7 | `==` `!=` |
| 8 | `&` |
| 9 | `^` |
| 10 | `|` |
| 11 | `&&` |
| 12 | `\|\|` |
| 13 | `?:` (ternary) |
| 14 (Lowest) | `=` `+=` `-=` `*=` `/=` `%=` `&=` `^=` `\|=` `<<=` `>>=` `>>>=` |

> **Tip**: Use parentheses `()` to make precedence explicit and improve readability.

---

## 2.6 Expressions and Statements

### Expressions
- Combination of variables, operators, method calls that evaluates to a single value
- Example: `a + b * c`, `Math.sqrt(x)`, `"Hello" + "World"`

### Statements
- Complete unit of execution ending with semicolon `;`
- Types:
  1. **Expression Statements**: Assignment, increment/decrement, method call, object creation
  2. **Declaration Statements**: Variable declarations
  3. **Control Statements**: if, for, while, switch, etc.

```java
int x = 10;           // Declaration statement
x = x + 5;            // Expression statement (assignment)
x++;                  // Expression statement (increment)
System.out.println(x); // Expression statement (method call)
Student s = new Student(); // Expression statement (object creation)
```

---

## 2.7 Scanner Class for Input

### Topic Introduction
`Scanner` class (in `java.util` package) reads input from various sources (console, file, string).

### Common Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `nextInt()` | `int` | Reads integer |
| `nextFloat()` | `float` | Reads float |
| `nextDouble()` | `double` | Reads double |
| `nextLong()` | `long` | Reads long |
| `nextShort()` | `short` | Reads short |
| `nextByte()` | `byte` | Reads byte |
| `nextBoolean()` | `boolean` | Reads boolean |
| `next()` | `String` | Reads next token (word) |
| `nextLine()` | `String` | Reads entire line |

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

**Circle Area:**
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

---

## 2.8 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. List Java primitive data types with sizes.
2. Difference between `int` and `Integer`.
3. What is a literal? Give examples.
4. Difference between `float` and `double`.
5. What is Unicode? How many bits in Java `char`?
5. What are escape sequences? List any 4.
6. Difference between `++i` and `i++`.
7. What is type casting?

**5-Mark Questions:**
1. Explain all data types in Java with sizes and ranges.
2. Write a program to calculate area of circle using Scanner class.
3. Explain arithmetic operators with examples.
4. Explain relational and logical operators with truth tables.
5. Write a program demonstrating pre/post increment/decrement.
6. Explain bitwise operators with examples.
7. Write a program to swap two numbers without third variable.
8. Explain operator precedence with example.
9. Difference between `&&` and `&`, `||` and `|`.

**10-Mark Questions:**
1. Explain all types of operators in Java with examples and precedence table.
2. Write a comprehensive program demonstrating Scanner class with all data types.

### Short Answer Topics
- Primitive vs Reference types
- Wrapper classes purpose
- `final` keyword with variables
- Variable naming conventions
- Type promotion in expressions
- Implicit vs Explicit casting

### Programs to Practice
1. ✅ Area of circle/rectangle
2. ✅ Even/Odd check
3. ✅ Largest of three numbers
4. ✅ Swap two numbers
5. ✅ Temperature conversion (C↔F)
6. ✅ Simple interest calculator
7. ✅ Character classification (vowel/consonant/digit)

---

## 2.9 Summary of Unit 2

| Topic | Key Points |
|-------|------------|
| **Primitive Types** | 8 types: byte, short, int, long, float, double, char, boolean |
| **Sizes** | Fixed and platform-independent |
| **Variables** | Local, Instance, Class (static) |
| **Literals** | Fixed values in code; suffixes: L, F, D |
| **Constants** | `final` keyword |
| **Unicode** | 16-bit; UTF-16 default |
| **Keywords** | 53 reserved words |
| **Operators** | Arithmetic, Relational, Logical, Bitwise, Assignment, Ternary |
| **Precedence** | High: `[]`, `.`, `()` → Low: Assignment |
| **Scanner** | `java.util.Scanner`; methods: nextInt(), nextLine(), etc. |

---