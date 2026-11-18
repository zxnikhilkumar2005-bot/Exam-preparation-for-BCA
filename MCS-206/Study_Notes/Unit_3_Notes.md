# Unit 3: Decision and Loop Constructs

## Unit Overview
This unit covers decision-making statements (if, if-else, switch-case), looping statements (while, do-while, for), jump statements (break, continue), and arrays in Java.

> **⚡ PYQ Insight**: Unit 3 topics appear as **5-mark questions** in Q1. **HIGH PRIORITY**: if/if-else/switch-case (2022-2025), while/do-while/for loops (2022, 2023). **MEDIUM**: Arrays (2024, 2025). **Programs**: Matrix addition (2022, 2025), Week days (2023), Circle area (2024), Multiplication table (2022).

---

## 3.1 Decision Constructs

### Topic Introduction
Decision constructs allow programs to execute different code blocks based on conditions. Java provides `if`, `if-else`, and `switch-case` for selection.

### 3.1.0 Relational & Logical Operators (Foundation for Decisions)
> **⚡ PYQ Insight**: Relational operators asked in **DEC 2022 (6 marks)** and **JUNE 2024 (5 marks)**.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 3` | `false` |
| `!=` | Not equal | `5 != 3` | `true` |
| `>` | Greater than | `5 > 3` | `true` |
| `<` | Less than | `5 < 3` | `false` |
| `>=` | Greater/equal | `5 >= 5` | `true` |
| `<=` | Less/equal | `5 <= 3` | `false` |

| Logical Operator | Name | Short-circuit? |
|------------------|------|----------------|
| `&&` | AND | ✅ Yes |
| `||` | OR | ✅ Yes |
| `!` | NOT | - |

**Key**: Relational operators return `boolean`; used in `if`, `while`, `for` conditions.

---

### 3.1.1 The if Statement

#### Syntax
```java
if (condition) {
    // statements executed if condition is true
}
```

#### Key Points
- Condition must be a **boolean expression**
- Parentheses `()` around condition are mandatory
- Braces `{}` required for multiple statements (optional for single statement)
- If condition is true → execute block; if false → skip block

#### Example
```java
int a = 20;
if (a < 25) {
    System.out.println("20 is less than 25");
}
System.out.println("Outside if-block");
```

**Output:**
```
20 is less than 25
Outside if-block
```

---

### 3.1.2 The if-else Statement

#### Syntax
```java
if (condition) {
    // executed if true
} else {
    // executed if false
}
```

#### if-else-if Ladder
```java
if (condition1) {
    // code
} else if (condition2) {
    // code
} else if (condition3) {
    // code
} else {
    // default code
}
```

#### Example
```java
int score = 85;
if (score >= 90) {
    System.out.println("Grade A");
} else if (score >= 80) {
    System.out.println("Grade B");
} else if (score >= 70) {
    System.out.println("Grade C");
} else {
    System.out.println("Grade F");
}
```

**Output:** `Grade B`

---

### 3.1.3 The switch-case Statement

#### Syntax
```java
switch (expression) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    ...
    default:
        // default code
}
```

#### Key Points
- Expression type: `byte`, `short`, `int`, `char`, `String` (Java 7+), `enum`
- Each `case` must have unique constant value
- `break` is **optional** but recommended to prevent fall-through
- `default` is **optional** but good practice
- Without `break`, execution continues to next case (fall-through)

#### Example: Day of Week
```java
import java.util.Scanner;

public class DayOfWeek {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter day number (1-7): ");
        int day = sc.nextInt();
        
        switch (day) {
            case 1: System.out.println("Monday"); break;
            case 2: System.out.println("Tuesday"); break;
            case 3: System.out.println("Wednesday"); break;
            case 4: System.out.println("Thursday"); break;
            case 5: System.out.println("Friday"); break;
            case 6: System.out.println("Saturday"); break;
            case 7: System.out.println("Sunday"); break;
            default: System.out.println("Invalid day!");
        }
    }
}
```

#### Fall-through Example
```java
int num = 2;
switch (num) {
    case 1: System.out.print("One ");
    case 2: System.out.print("Two ");
    case 3: System.out.print("Three ");
    default: System.out.print("Default");
}
// Output: Two Three Default
```

#### switch-case with String (Java 7+)
```java
String day = "MONDAY";
switch (day.toUpperCase()) {
    case "MONDAY": System.out.println("Start of work week"); break;
    case "FRIDAY": System.out.println("Weekend coming!"); break;
    case "SATURDAY":
    case "SUNDAY": System.out.println("Weekend"); break;
    default: System.out.println("Midweek");
}
```

#### switch-case vs if-else Comparison
> **⚡ PYQ Insight**: Asked in **JUNE 2023 (5 marks Theory+Code)**

| Aspect | switch-case | if-else-if |
|--------|-------------|------------|
| **Best for** | Multiple discrete values | Range/boolean conditions |
| **Types** | byte, short, int, char, String, enum | Any boolean expression |
| **Performance** | O(1) jump table (compiler optimized) | O(n) sequential evaluation |
| **Readability** | Clean for many cases | Better for complex conditions |
| **Fall-through** | Supported (intentional) | Not applicable |
| **Null handling** | Throws NPE on null (pre-Java 12) | Handles null naturally |

**When to use which:**
- **switch**: Menu systems, enum handling, known discrete values
- **if-else**: Range checks (score >= 90), complex boolean logic, null checks

---

### 3.1.5 Nested Decision Constructs
```java
// Nested if-else: Find largest of 3 numbers
int a = 10, b = 25, c = 15;
int largest;

if (a > b) {
    if (a > c) largest = a;
    else largest = c;
} else {
    if (b > c) largest = b;
    else largest = c;
}
System.out.println("Largest: " + largest);  // Output: 25
```

```java
// Nested switch (avoid if possible - use if-else)
int month = 2, year = 2024;
int days;
switch (month) {
    case 1: case 3: case 5: case 7: case 8: case 10: case 12:
        days = 31; break;
    case 4: case 6: case 9: case 11:
        days = 30; break;
    case 2:
        // Nested leap year check
        if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
            days = 29;
        else
            days = 28;
        break;
    default: days = -1; // Invalid month
}
```

### 3.1.6 Labeled break/continue (Advanced)
```java
// Labeled break - exit outer loop
outerLoop:
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (i == 2 && j == 2) break outerLoop;
        System.out.println("i=" + i + ", j=" + j);
    }
}
// Output: i=1,j=1 | i=1,j=2 | i=1,j=3 | i=2,j=1

// Labeled continue - skip to next iteration of outer loop
outerLoop:
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) continue outerLoop;
        System.out.println("i=" + i + ", j=" + j);
    }
}
// Output: i=1,j=1 | i=1,j=3 | i=2,j=1 | i=2,j=3 | i=3,j=1 | i=3,j=3
```
---

### 3.1.4 Jump Statements

#### break Statement
- Exits immediately from `switch`, `for`, `while`, `do-while`
- Transfers control to statement after the loop/switch

```java
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;
    System.out.print(i + " ");
}
// Output: 1 2 3 4
```

#### continue Statement
- Skips current iteration, continues with next iteration
- In `for` loop: jumps to update expression
- In `while`/`do-while`: jumps to condition check

```java
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    System.out.print(i + " ");
}
// Output: 1 2 4 5
```

#### Comparison: break vs continue
| Aspect | break | continue |
|--------|-------|----------|
| Action | Exits loop completely | Skips current iteration |
| Loop continues? | No | Yes (next iteration) |
| Use case | Found target, error condition | Skip invalid data |

---

## 3.2 Loop Constructs

### Topic Introduction
Loops execute a block of code repeatedly until a condition becomes false. Java provides three loop types.

---

### 3.2.1 while Loop

#### Syntax
```java
while (condition) {
    // body of loop
}
```

#### Characteristics
- **Entry-controlled loop** (condition checked before each iteration)
- May execute **zero times** if condition initially false
- Condition must be boolean expression

#### Example
```java
int i = 4;
while (i > 0) {
    System.out.println("IGNOU " + i);
    i--;
}
```

**Output:**
```
IGNOU 4
IGNOU 3
IGNOU 2
IGNOU 1
```

#### Infinite Loop
```java
while (true) {
    // runs forever - use break to exit
}
```

---

### 3.2.2 do-while Loop

#### Syntax
```java
do {
    // body of loop
} while (condition);
```

#### Characteristics
- **Exit-controlled loop** (condition checked after each iteration)
- Executes **at least once** even if condition is false initially
- Semicolon `;` required after `while(condition)`

#### Example
```java
int i = 1;
do {
    System.out.println("Value: " + i);
    i++;
} while (i <= 3);
```

**Output:**
```
Value: 1
Value: 2
Value: 3
```

#### while vs do-while
> **⚡ PYQ Insight**: Asked in **DEC 2023 (5 marks Theory+Code)**

| Aspect | while | do-while |
|--------|-------|----------|
| Control | Entry-controlled | Exit-controlled |
| Minimum executions | 0 | 1 |
| Condition check | Before body | After body |
| Syntax end | No semicolon | Semicolon required |
| Use case | May not run at all | Must run at least once |

**Example showing the difference:**
```java
// while - may not execute
int x = 5;
while (x < 5) {
    System.out.println("while: " + x);  // Never prints
    x++;
}

// do-while - executes once
int y = 5;
do {
    System.out.println("do-while: " + y);  // Prints once: "do-while: 5"
    y++;
} while (y < 5);
```

**Program: Menu-driven calculator using do-while**
```java
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();
            
            if (choice >= 1 && choice <= 4) {
                System.out.print("Enter two numbers: ");
                double a = sc.nextDouble(), b = sc.nextDouble();
                switch (choice) {
                    case 1: System.out.println("Result: " + (a + b)); break;
                    case 2: System.out.println("Result: " + (a - b)); break;
                    case 3: System.out.println("Result: " + (a * b)); break;
                    case 4: System.out.println("Result: " + (b != 0 ? a / b : "Error")); break;
                }
            }
        } while (choice != 5);
        System.out.println("Calculator exited.");
    }
}
```
---

### 3.2.3 for Loop

#### Syntax
```java
for (initialization; condition; update) {
    // body of loop
}
```

#### Components
| Part | Executed | Description |
|------|----------|-------------|
| Initialization | Once at start | Declare/initialize loop variable |
| Condition | Before each iteration | Boolean expression; loop continues if true |
| Update | After each iteration | Modify loop variable (increment/decrement) |
| Body | Each iteration | Statements to repeat |

#### Example
```java
for (int i = 1; i <= 5; i++) {
    System.out.println("Iteration " + i);
}
```

**Output:**
```
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

#### Variations
```java
// Multiple variables
for (int i = 0, j = 10; i < j; i++, j--) { ... }

// Omitting parts (semicolons required)
int i = 0;
for (; i < 5; ) {      // no init
    System.out.println(i++);
}

// Infinite loop
for (;;) { ... }       // equivalent to while(true)

// Enhanced for loop (for-each) - Java 5+
int[] arr = {1, 2, 3, 4, 5};
for (int num : arr) {
    System.out.println(num);
}
```

#### Nested for Loops (Pattern Programs)
> **⚡ PYQ Insight**: Multiplication table 1-20 asked in **DEC 2022 (6 marks)**

```java
// Multiplication Table 1-20 (DEC 2022 Q1g)
for (int i = 1; i <= 20; i++) {
    for (int j = 1; j <= 10; j++) {
        System.out.println(i + " x " + j + " = " + (i * j));
    }
    System.out.println(); // Blank line between tables
}
```

```java
// Pattern Programs (common in exams)
/*
Pattern 1: Right Triangle
*
**
***
****
*/

for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print("*");
    }
    System.out.println();
}

/*
Pattern 2: Number Pyramid
1
2 2
3 3 3
*/

for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        System.out.print(i + " ");
    }
    System.out.println();
}
```

#### for Loop vs while Loop vs do-while
| Aspect | for | while | do-while |
|--------|-----|-------|----------|
| **Best for** | Known iteration count | Unknown iterations | At least one execution |
| **Control** | Counter-controlled | Entry-controlled | Exit-controlled |
| **Scope** | Variable in init stays in loop | Variable declared outside | Variable declared outside |
| **Parts** | Init, condition, update in one line | Condition only | Condition only |

---

## 3.3 Arrays

### Topic Introduction
An array is a fixed-size container that stores multiple values of the same type in contiguous memory.

> **⚡ PYQ Insight**: Arrays asked in **JUNE 2024 (5 marks Short Note)** and **DEC 2025 (5 marks Matrix Addition)**. Programs: Matrix addition (2022, 2025).

---

### 3.3.1 Array Declaration and Creation

#### Syntax Options
```java
// Declaration
int[] numbers;           // Preferred style
int numbers[];           // C-style (valid but not preferred)

// Creation
numbers = new int[5];    // Size 5, all elements = 0

// Declaration + Creation
int[] scores = new int[10];

// Declaration + Initialization
int[] marks = {90, 85, 78, 92, 88};

// Anonymous array (for method arguments)
method(new int[] {1, 2, 3});
```

#### Default Values
| Type | Default |
|------|---------|
| Numeric (int, double, etc.) | 0 |
| boolean | false |
| char | '\u0000' |
| Object reference | null |

#### Array Memory Model
```java
int[] arr = new int[3];  // Stack: arr (reference) → Heap: [0, 0, 0]
                         // arr.length = 3 (fixed after creation)

// Object array
String[] names = new String[3];  // [null, null, null]
names[0] = "Amit";               // [Amit, null, null]
```

---

### 3.3.2 Array Operations (Exam-Important)

#### Finding Min/Max
```java
int[] arr = {45, 12, 78, 23, 56};
int max = arr[0], min = arr[0];

for (int i = 1; i < arr.length; i++) {
    if (arr[i] > max) max = arr[i];
    if (arr[i] < min) min = arr[i];
}
System.out.println("Max: " + max + ", Min: " + min);
```

#### Searching (Linear Search)
```java
int[] arr = {10, 20, 30, 40, 50};
int key = 30, index = -1;

for (int i = 0; i < arr.length; i++) {
    if (arr[i] == key) {
        index = i;
        break;
    }
}
System.out.println(index != -1 ? "Found at: " + index : "Not found");
```

#### Sorting (Bubble Sort - simple version)
```java
int[] arr = {64, 34, 25, 12, 22, 11, 90};
int n = arr.length;

for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            // swap
            int temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
    }
}
// Use Arrays.sort(arr) in practice
```

#### Copying Arrays
```java
int[] src = {1, 2, 3, 4, 5};
int[] dest = new int[src.length];

// Method 1: Manual copy
for (int i = 0; i < src.length; i++) dest[i] = src[i];

// Method 2: System.arraycopy (fastest)
System.arraycopy(src, 0, dest, 0, src.length);

// Method 3: Arrays.copyOf
int[] dest2 = Arrays.copyOf(src, src.length);

// Method 4: clone()
int[] dest3 = src.clone();
```

---

### 3.3.3 Command-Line Arguments (String[] args)
```java
// Run: java MyProgram 10 20 30
public class ArgsDemo {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("No arguments provided");
            return;
        }
        
        int sum = 0;
        for (String arg : args) {
            sum += Integer.parseInt(arg);  // Convert String to int
        }
        System.out.println("Sum: " + sum);
    }
}
```

---

### 3.3.4 Matrix Operations (CRITICAL FOR EXAMS)

> **⚡ PYQ Insight**: **3×3 Matrix Addition** appeared in **JUNE 2022 (5 marks)** and **DEC 2025 (5 marks)**.

#### Complete Matrix Addition Program
```java
import java.util.Scanner;

public class MatrixAddition {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = 3, cols = 3;
        
        int[][] a = new int[rows][cols];
        int[][] b = new int[rows][cols];
        int[][] sum = new int[rows][cols];
        
        System.out.println("Enter elements of Matrix A (3x3):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("Enter elements of Matrix B (3x3):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                b[i][j] = sc.nextInt();
            }
        }
        
        // Addition
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                sum[i][j] = a[i][j] + b[i][j];
            }
        }
        
        System.out.println("Resultant Matrix (A + B):");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(sum[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```

#### Matrix Multiplication (Bonus)
```java
// Matrix Multiplication (2x3 × 3x2 = 2x2)
int[][] a = {{1, 2, 3}, {4, 5, 6}};  // 2x3
int[][] b = {{7, 8}, {9, 1}, {2, 3}};  // 3x2
int[][] product = new int[2][2];

for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 2; j++) {
        for (int k = 0; k < 3; k++) {
            product[i][j] += a[i][k] * b[k][j];
        }
    }
}
```

#### Transpose of Matrix
```java
int[][] mat = {{1, 2, 3}, {4, 5, 6}};  // 2x3
int[][] transpose = new int[3][2];      // 3x2

for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
        transpose[j][i] = mat[i][j];
    }
}
```

---

### 3.3.5 Array vs ArrayList (Quick Comparison)
| Aspect | Array | ArrayList |
|--------|-------|-----------|
| Size | Fixed | Dynamic |
| Primitives | Direct (int[]) | Wrapper (Integer) |
| Methods | `length` field | `size()`, `add()`, `remove()` |
| Performance | Faster | Slightly slower |
| Generics | No | Yes |

## 3.4 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. Difference between `while` and `do-while` loop.
2. Difference between `break` and `continue`.
3. What is an array? How to declare?
4. Syntax of `switch-case` statement.
5. What is fall-through in switch?
6. What is enhanced for loop?
7. Relational operators in Java (<, >, <=, >=, ==, !=).
8. Difference between switch-case and if-else-if.

**5-Mark Questions:**
1. Write a program to print multiplication table using for loop.
2. Write a program demonstrating `switch-case` for calculator (+,-,*,/).
3. Explain decision-making statements with examples.
4. Write a program to find largest of 3 numbers using if-else.
5. Explain `while` vs `do-while` with examples.
6. Write a program for matrix addition (3×3).
7. Write a program demonstrating `break` and `continue`.
8. Explain jump statements in Java.
9. Week days program using switch-case.
10. Average of 3 numbers using command-line arguments.
11. Circle area program using if-else for validation.
12. Switch-case vs if-else comparison with examples.

**10-Mark Questions:**
1. Explain all loop constructs in Java with syntax, flow diagrams, and examples.
2. Write a menu-driven program using switch-case for arithmetic operations.
3. Explain arrays: declaration, initialization, types, and matrix operations.
4. Nested loops for pattern printing and multiplication tables.

### Programs to Practice (High Yield)
1. ✅ **Matrix Addition (3×3)** - appeared 2022, 2025
2. ✅ **Week days program (switch)** - appeared 2023
3. ✅ **Circle area program** - appeared 2024
4. ✅ **Average of 3 numbers** - appeared 2022
5. ✅ **Multiplication table 1-20** - appeared 2022
6. ✅ **Largest of 3 numbers** - appeared 2021
7. ✅ **Switch-case with break** - appeared 2022, 2024
8. ✅ **For loop programs** (patterns, series)
9. ✅ **Menu-driven calculator (do-while + switch)** - 2023, 2024
10. ✅ **Command-line args sum/average** - 2022
11. ✅ **Linear search in array** - common
12. ✅ **Bubble sort array** - common

---

## 3.5 Summary of Unit 3

| Topic | Key Points |
|-------|------------|
| **Relational Operators** | `<`, `>`, `<=`, `>=`, `==`, `!=` — return boolean |
| **Logical Operators** | `&&`, `||`, `!` — short-circuit evaluation |
| **if statement** | Single condition, optional braces for single statement |
| **if-else** | Two-way branch |
| **if-else-if** | Multi-way branch |
| **switch-case** | Multi-way for discrete values (int, char, String, enum) |
| **switch vs if-else** | switch: discrete values, jump table; if-else: ranges, complex conditions |
| **break** | Exits loop/switch immediately; labeled break for nested loops |
| **continue** | Skips to next iteration; labeled continue for nested loops |
| **while** | Entry-controlled, may not execute (0 times) |
| **do-while** | Exit-controlled, executes at least once (1 time) |
| **for** | Counter-controlled, init/condition/update in one line |
| **for-each** | Iterates over arrays/collections (no index access) |
| **Nested loops** | Pattern programs, matrix operations, multiplication tables |
| **Arrays** | Fixed-size, zero-indexed, `length` property (not method) |
| **2D Arrays** | Array of arrays; `matrix[i][j]` access; jagged arrays possible |
| **3D Arrays** | Array of 2D arrays; `cube[x][y][z]` |
| **Matrix Addition** | Nested loops, same dimensions required |
| **Matrix Multiplication** | Triple nested loop; cols of A = rows of B |
| **Command-line args** | `String[] args`; parse with `Integer.parseInt()` |

---

## 3.6 Flow Diagrams

### if Statement
```
        ┌─────────┐
        │ Condition │
        └────┬────┘
             │
        ┌────┴────┐
        ▼         ▼
      True       False
        │         │
        ▼         ▼
    ┌───────┐   Next
    │ Body  │   Statement
    └───────┘
```

### while Loop
```
        ┌─────────┐
        │ Condition │◄──────┐
        └────┬────┘       │
             │            │
        ┌────┴────┐       │
        ▼         ▼       │
      True       False    │
        │         │       │
        ▼         │       │
    ┌───────┐     │       │
    │ Body  │     │       │
    └───────┘     │       │
        │         │       │
        └─────────┘       │
```

### for Loop
```
    ┌──────────────┐
    │ Initialization │ (once)
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Condition   │────False──► Exit
    └──────┬───────┘
           │ True
           ▼
    ┌──────────────┐
    │     Body     │
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │    Update    │
    └──────┬───────┘
           │
           └────────┘ (loop back)
```

### do-while Loop
```
    ┌──────────────┐
    │     Body     │ (executes first)
    └──────┬───────┘
           ▼
    ┌──────────────┐
    │  Condition   │────True──┐
    └──────┬───────┘          │
           │ False            │
           ▼                  │
         Exit ◄───────────────┘
```

### if-else Statement
```
        ┌─────────┐
        │ Condition │
        └────┬────┘
             │
        ┌────┴────┐
        ▼         ▼
      True       False
        │         │
        ▼         ▼
    ┌───────┐ ┌───────┐
    │ If-Block│ │Else-Block│
    └───────┘ └───────┘
        │         │
        └────┬────┘
             ▼
      Next Statement
```

### if-else-if Ladder
```
        ┌───────────┐
        │Condition 1│
        └─────┬─────┘
              │
         ┌────┴────┐
         ▼         ▼
       True       False
         │         │
         ▼         ▼
     ┌────────┐ ┌───────────┐
     │ Block 1│ │Condition 2│
     └────────┘ └─────┬─────┘
                       │
                  ┌────┴────┐
                  ▼         ▼
                True       False
                  │         │
                  ▼         ▼
              ┌────────┐ ┌───────────┐
              │ Block 2│ │Condition 3│
              └────────┘ └─────┬─────┘
                                │
                           ┌────┴────┐
                           ▼         ▼
                         True       False
                           │         │
                           ▼         ▼
                       ┌────────┐ ┌─────────┐
                       │ Block 3│ │ Else    │
                       └────────┘ │(Default)│
                                  └─────────┘
```

### switch-case Statement
```
        ┌─────────────┐
        │  Expression │
        └──────┬──────┘
               │
       ┌───────┼───────┐
       ▼       ▼       ▼
    case 1  case 2  case 3  ...  default
       │       │       │
       ▼       ▼       ▼
    ┌──────┐┌──────┐┌──────┐
    │Block ││Block ││Block │
    └──┬───┘└──┬───┘└──┬───┘
       │       │       │
    (break) (break) (break)
       │       │       │
       └───────┼───────┘
               ▼
       Next Statement
```