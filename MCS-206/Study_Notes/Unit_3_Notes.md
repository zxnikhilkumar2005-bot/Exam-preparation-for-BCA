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
| Aspect | while | do-while |
|--------|-------|----------|
| Control | Entry-controlled | Exit-controlled |
| Minimum executions | 0 | 1 |
| Condition check | Before body | After body |
| Syntax end | No semicolon | Semicolon required |
| Use case | May not run at all | Must run at least once |

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

---

## 3.3 Arrays

### Topic Introduction
An array is a fixed-size container that stores multiple values of the same type in contiguous memory.

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

---

### 3.3.2 Array Access

```java
int[] arr = {10, 20, 30, 40, 50};

arr[0]    // 10 (first element)
arr[4]    // 50 (last element)
arr.length // 5 (size - property, not method!)

// Loop through array
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}

// Enhanced for loop
for (int num : arr) {
    System.out.println(num);
}
```

#### IndexOutOfBoundsException
```java
int[] a = new int[5];
a[5] = 10;  // Runtime Exception! Valid indices: 0-4
```

---

### 3.3.3 Multi-dimensional Arrays

#### 2D Array (Matrix)
```java
// Declaration
int[][] matrix;

// Creation
matrix = new int[3][4];  // 3 rows, 4 columns

// Initialization
int[][] mat = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Access
mat[0][0]  // 1 (row 0, col 0)
mat[1][2]  // 6 (row 1, col 2)
mat.length // 3 (number of rows)
mat[0].length // 3 (columns in row 0)
```

#### Jagged Arrays (rows of different lengths)
```java
int[][] jagged = new int[3][];
jagged[0] = new int[2];
jagged[1] = new int[5];
jagged[2] = new int[3];
```

---

### 3.3.4 Matrix Operations Example

```java
// Matrix Addition (3x3) - IMPORTANT FOR EXAMS
int[][] a = {{1,2,3}, {4,5,6}, {7,8,9}};
int[][] b = {{9,8,7}, {6,5,4}, {3,2,1}};
int[][] sum = new int[3][3];

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        sum[i][j] = a[i][j] + b[i][j];
    }
}
```

---

## 3.4 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. Difference between `while` and `do-while` loop.
2. Difference between `break` and `continue`.
3. What is an array? How to declare?
4. Syntax of `switch-case` statement.
5. What is fall-through in switch?
6. What is enhanced for loop?

**5-Mark Questions:**
1. Write a program to print multiplication table using for loop.
2. Write a program demonstrating `switch-case` for calculator (+,-,*,/).
3. Explain decision-making statements with examples.
4. Write a program to find largest of 3 numbers using if-else.
5. Explain `while` vs `do-while` with examples.
6. Write a program for matrix addition (3×3).
7. Write a program demonstrating `break` and `continue`.
8. Explain jump statements in Java.

**10-Mark Questions:**
1. Explain all loop constructs in Java with syntax, flow diagrams, and examples.
2. Write a menu-driven program using switch-case for arithmetic operations.
3. Explain arrays: declaration, initialization, types, and matrix operations.

### Programs to Practice (High Yield)
1. ✅ **Matrix Addition (3×3)** - appeared 2022, 2025
2. ✅ **Week days program (switch)** - appeared 2023
3. ✅ **Circle area program** - appeared 2024
4. ✅ **Average of 3 numbers** - appeared 2022
5. ✅ **Multiplication table 1-20** - appeared 2021
6. ✅ **Largest of 3 numbers** - appeared 2021
7. ✅ **Switch-case with break** - appeared 2022, 2024
8. ✅ **For loop programs** (patterns, series)

---

## 3.5 Summary of Unit 3

| Topic | Key Points |
|-------|------------|
| **if statement** | Single condition, optional braces for single statement |
| **if-else** | Two-way branch |
| **if-else-if** | Multi-way branch |
| **switch-case** | Multi-way for discrete values (int, char, String, enum) |
| **break** | Exits loop/switch immediately |
| **continue** | Skips to next iteration |
| **while** | Entry-controlled, may not execute |
| **do-while** | Exit-controlled, executes at least once |
| **for** | Counter-controlled, all parts in one line |
| **for-each** | Iterates over arrays/collections (no index) |
| **Arrays** | Fixed-size, zero-indexed, `length` property |
| **2D Arrays** | Array of arrays; `matrix[i][j]` access |
| **Matrix Addition** | Nested loops, same dimensions required |

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