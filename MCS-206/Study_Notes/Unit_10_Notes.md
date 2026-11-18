# Unit 10: Number, Character and Strings

## Unit Overview
This unit covers wrapper classes (Number class and subclasses), Character class, String class, StringBuilder, StringBuffer, and autoboxing/unboxing.

---

## 10.1 Wrapper Classes and Number Class

### Wrapper Classes
Each primitive type has a corresponding wrapper class:

| Primitive | Wrapper Class | Package |
|-----------|---------------|---------|
| `byte` | `Byte` | `java.lang` |
| `short` | `Short` | `java.lang` |
| `int` | `Integer` | `java.lang` |
| `long` | `Long` | `java.lang` |
| `float` | `Float` | `java.lang` |
| `double` | `Double` | `java.lang` |
| `char` | `Character` | `java.lang` |
| `boolean` | `Boolean` | `java.lang` |

### Inheritance Hierarchy
```
                    Object
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        Number    Boolean    Character
          │
    ┌─────┼─────┐
    ▼     ▼     ▼
  Byte  Short  Integer  Long  Float  Double
```

### Number Class (Abstract)
Abstract superclass of all numeric wrapper classes.

#### Common Methods (All Subclasses)
```java
// Conversion to primitives
byte byteValue()
short shortValue()
int intValue()
long longValue()
float floatValue()
double doubleValue()

// Comparison
int compareTo(Byte/Short/Integer/Long/Float/Double another)
boolean equals(Object obj)
```

---

## 10.2 Integer Class (Most Used)

### Important Constants
```java
Integer.MAX_VALUE   // 2147483647
Integer.MIN_VALUE   // -2147483648
Integer.SIZE        // 32 (bits)
Integer.BYTES       // 4 (bytes)
```

### Conversion Methods
```java
// String to int
static int parseInt(String s)              // "123" → 123
static int parseInt(String s, int radix)   // "FF", 16 → 255

// int to String
static String toString(int i)              // 123 → "123"
static String toString(int i, int radix)   // 255, 16 → "ff"
static String toHexString(int i)           // 255 → "ff"
static String toBinaryString(int i)        // 5 → "101"
static String toOctalString(int i)         // 10 → "12"

// String to Integer object
static Integer valueOf(String s)           // "123" → Integer(123)
static Integer valueOf(String s, int radix)
static Integer valueOf(int i)              // 123 → Integer(123) (cached -128 to 127)

// Integer object to primitive
int intValue()                             // Unboxing
```

### Example
```java
public class NumberDemo {
    public static void main(String[] args) {
        Integer i = 20;           // Autoboxing
        Integer j = 25;
        String s = "28";
        
        int a = i.intValue();     // 20
        int b = Integer.parseInt(s);  // 28
        int c = j.intValue();     // 25
        
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("a + b * c: " + (a + b * c));
    }
}
```

---

## 10.3 Formatting Numeric Output

### printf and format Methods
```java
// System.out is a PrintStream
System.out.format("format", args);
System.out.printf("format", args);
```

### Format Specifiers

| Specifier | Description | Example |
|-----------|-------------|---------|
| `%d` | Decimal integer | `%d` → `42` |
| `%f` | Floating point | `%f` → `3.140000` |
| `%.2f` | 2 decimal places | `%.2f` → `3.14` |
| `%n` | Platform-independent newline | |
| `%s` | String | |
| `%c` | Character | |
| `%x` | Hexadecimal (lowercase) | |
| `%X` | Hexadecimal (uppercase) | |
| `%o` | Octal | |
| `%e` | Scientific notation | |

### Flags
| Flag | Description |
|------|-------------|
| `-` | Left justify |
| `+` | Always show sign |
| `0` | Pad with zeros |
| `,` | Locale-specific grouping |
| `(` | Enclose negative in parentheses |

### Width and Precision
```java
%10d      // Width 10, right-aligned
%-10d     // Width 10, left-aligned
%08d      // Width 8, zero-padded
%.3f      // 3 decimal places
%10.2f    // Width 10, 2 decimal places
```

### Example
```java
public class FormatDemo {
    public static void main(String[] args) {
        int n = 461012;
        double pi = Math.PI;
        
        System.out.format("n=%d%n", n);           // n=461012
        System.out.format("n=%08d%n", n);         // n=00461012
        System.out.format("n=%+8d%n", n);         // n= +461012
        System.out.format("n=%,8d%n", n);         // n= 461,012
        System.out.format("pi=%f%n", pi);         // pi=3.141593
        System.out.format("pi=%.4f%n", pi);       // pi=3.1416
        System.out.format("pi=%10.3f%n", pi);     // pi=     3.142
        System.out.format(Locale.GERMAN, "pi=%-10.4f%n%n", pi); // pi=3,1416
    }
}
```

---

## 10.4 Character Class

### Creating Character Objects
```java
Character c1 = 'A';                    // Autoboxing
Character c2 = new Character('B');     // Constructor (deprecated Java 9+)
Character c3 = Character.valueOf('C'); // Preferred
```

### Common Methods

| Method | Description | Example |
|--------|-------------|---------|
| `isLetter(char ch)` | Is letter? | `isLetter('A')` → true |
| `isDigit(char ch)` | Is digit? | `isDigit('5')` → true |
| `isWhitespace(char ch)` | Is whitespace? | `isWhitespace(' ')` → true |
| `isUpperCase(char ch)` | Is uppercase? | `isUpperCase('a')` → false |
| `isLowerCase(char ch)` | Is lowercase? | `isLowerCase('a')` → true |
| `toUpperCase(char ch)` | To uppercase | `toUpperCase('a')` → 'A' |
| `toLowerCase(char ch)` | To lowercase | `toLowerCase('A')` → 'a' |
| `toString(char ch)` | To String | `toString('A')` → "A" |
| `compareTo(Character c)` | Compare | `'A'.compareTo('B')` → -1 |
| `equals(Character c)` | Equality | `'A'.equals('A')` → true |

### Example
```java
public class CharDemo {
    public static void main(String[] args) {
        Character c1 = 'J';
        Character c2 = 'a';
        
        System.out.println("c1: " + c1);
        System.out.println("c1 lowercase: " + Character.toLowerCase(c1));
        System.out.println("c1 isUpperCase: " + Character.isUpperCase(c1));
        
        int diff = c1.compareTo(c2);
        if (diff == 0) System.out.println("Equal");
        else System.out.println("Not equal");
    }
}
```

---

## 10.5 String Class

### Key Characteristics
- **Immutable**: Cannot be changed after creation
- **Final class**: Cannot be extended
- **String Constant Pool**: Literals stored in pool for reuse

### Creating Strings
```java
// 1. String literal (uses pool)
String s1 = "Hello";
String s2 = "Hello";  // Same object from pool

// 2. new keyword (creates new object in heap)
String s3 = new String("Hello");
String s4 = new String("Hello");  // Different objects

// Comparison
s1 == s2        // true (same reference)
s1 == s3        // false (different objects)
s1.equals(s3)   // true (same content)
```

### Important Constructors
```java
String()                              // Empty string
String(String original)               // Copy
String(char[] value)                  // From char array
String(char[] value, int offset, int count)  // Subarray
String(byte[] bytes)                  // From bytes
String(byte[] bytes, int offset, int length)
```

### Important Methods

| Method | Description |
|--------|-------------|
| `length()` | Returns length |
| `charAt(int index)` | Character at index |
| `substring(int begin)` | From begin to end |
| `substring(int begin, int end)` | Range [begin, end) |
| `concat(String str)` | Concatenation |
| `equals(Object obj)` | Content equality |
| `equalsIgnoreCase(String str)` | Case-insensitive equality |
| `compareTo(String str)` | Lexicographic comparison |
| `compareToIgnoreCase(String str)` | Case-insensitive comparison |
| `startsWith(String prefix)` | Starts with prefix |
| `endsWith(String suffix)` | Ends with suffix |
| `contains(CharSequence s)` | Contains sequence |
| `indexOf(int ch)` | First occurrence of char |
| `lastIndexOf(int ch)` | Last occurrence of char |
| `indexOf(String str)` | First occurrence of substring |
| `replace(char old, char new)` | Replace all occurrences |
| `replace(CharSequence target, CharSequence replacement)` | Replace sequence |
| `toLowerCase()` | Convert to lowercase |
| `toUpperCase()` | Convert to uppercase |
| `trim()` | Remove leading/trailing whitespace |
| `split(String regex)` | Split into array |
| `toCharArray()` | Convert to char array |
| `getBytes()` | Convert to byte array |
| `valueOf(...)` | Static: convert to String |

### Search Methods
```java
String str = "Java is Object Oriented Programming Language";

str.length()                    // 45
str.charAt(0)                   // 'J'
str.charAt(str.length()-1)      // 'e'
str.indexOf('a')                // 1
str.lastIndexOf('a')            // 37
str.indexOf('a', 10)            // 21 (search from index 10)
str.contains("Object")          // true
```

### Modification Methods (Return NEW String)
```java
String s = "Hello World";

s.toUpperCase()         // "HELLO WORLD"
s.toLowerCase()         // "hello world"
s.trim()                // Remove spaces
s.replace('l', 'L')     // "HeLLo WorLd"
s.replace("World", "Java")  // "Hello Java"
s.substring(0, 5)       // "Hello"
s.substring(6)          // "World"
```

### Comparison Methods
```java
String s1 = "Hello";
String s2 = "hello";
String s3 = "World";

s1.equals(s2)           // false
s1.equalsIgnoreCase(s2) // true
s1.compareTo(s2)        // negative (H < h)
s1.compareToIgnoreCase(s2) // 0
s1.startsWith("He")     // true
s1.endsWith("lo")       // true
```

### Conversion Between Numbers and Strings
```java
// String to Number
int i = Integer.parseInt("123");
double d = Double.parseDouble("3.14");
float f = Float.valueOf("2.5f");

// Number to String
String s1 = String.valueOf(123);      // "123"
String s2 = String.valueOf(3.14);     // "3.14"
String s3 = Integer.toString(42);     // "42"
String s4 = Double.toString(3.14);    // "3.14"

// Concatenation (creates new String)
String s = "Age: " + 25;              // "Age: 25"
```

### Palindrome Check Example
```java
// Using String (inefficient)
String str = "MADAM";
String rev = "";
for (int i = str.length()-1; i >= 0; i--) {
    rev += str.charAt(i);
}
if (str.equalsIgnoreCase(rev)) System.out.println("Palindrome");

// Using StringBuilder (efficient)
StringBuilder sb = new StringBuilder(str);
if (str.equalsIgnoreCase(sb.reverse().toString())) 
    System.out.println("Palindrome");
```

---

## 10.6 StringBuilder Class

### Characteristics
- **Mutable**: Can be modified
- **Not synchronized**: Not thread-safe
- **Faster** than StringBuffer
- **Preferred** for single-threaded use

### Constructors
```java
StringBuilder()                    // Empty, capacity 16
StringBuilder(int capacity)        // Empty, specified capacity
StringBuilder(String str)          // From string, capacity = len+16
StringBuilder(CharSequence cs)     // From CharSequence
```

### Important Methods

| Method | Description |
|--------|-------------|
| `length()` | Current length |
| `capacity()` | Current capacity |
| `ensureCapacity(int min)` | Ensure minimum capacity |
| `setLength(int newLength)` | Set length (truncate or pad) |
| `charAt(int index)` | Character at index |
| `setCharAt(int index, char ch)` | Set character |
| `append(...)` | Append (overloaded for all types) |
| `insert(int offset, ...)` | Insert at offset |
| `delete(int start, int end)` | Delete range [start, end) |
| `deleteCharAt(int index)` | Delete single character |
| `replace(int start, int end, String str)` | Replace range |
| `reverse()` | Reverse sequence |
| `toString()` | Convert to String |
| `substring(int start)` | Substring |
| `substring(int start, int end)` | Substring range |

### Example
```java
public class SBExample {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder(20);
        System.out.println("Length: " + sb.length());      // 0
        System.out.println("Capacity: " + sb.capacity());  // 20
        
        sb.append("Welcome to Java");
        System.out.println("After append: " + sb);
        System.out.println("Length: " + sb.length());
        System.out.println("Capacity: " + sb.capacity());
        
        sb.ensureCapacity(50);
        System.out.println("Capacity after ensure: " + sb.capacity());
        
        System.out.println("Reverse: " + sb.reverse());
    }
}
```

---

## 10.7 StringBuffer Class

### Characteristics
- **Mutable**: Can be modified
- **Synchronized**: Thread-safe
- **Slower** than StringBuilder
- **Legacy**: Exists since Java 1.0

### Constructors
```java
StringBuffer()                    // Empty, capacity 16
StringBuffer(int capacity)        // Empty, specified capacity
StringBuffer(String str)          // From string
```

### Methods (Same as StringBuilder + synchronized)
```java
// All StringBuilder methods are synchronized
public synchronized int length()
public synchronized int capacity()
public synchronized StringBuffer append(String str)
public synchronized StringBuffer insert(int offset, String str)
public synchronized StringBuffer delete(int start, int end)
public synchronized StringBuffer reverse()
// ... etc.
```

### When to Use StringBuffer
- Multi-threaded environment where multiple threads modify the same buffer
- Legacy code compatibility

---

## 10.8 StringBuilder vs StringBuffer vs String

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread Safety** | Yes (immutable) | No | Yes (synchronized) |
| **Performance** | Slow for concat | Fastest | Moderate |
| **Java Version** | 1.0 | 5.0 | 1.0 |
| **Use Case** | Constant strings | Single-threaded | Multi-threaded |

---

## 10.9 Autoboxing and Unboxing

### Autoboxing
Automatic conversion of **primitive** to **wrapper object**.

```java
// Primitive → Wrapper
Integer i = 10;           // Integer.valueOf(10)
Double d = 3.14;          // Double.valueOf(3.14)
Boolean b = true;         // Boolean.valueOf(true)
Character c = 'A';        // Character.valueOf('A')

// In collections
List<Integer> list = new ArrayList<>();
list.add(10);             // Autoboxing: list.add(Integer.valueOf(10))
```

### Unboxing
Automatic conversion of **wrapper object** to **primitive**.

```java
// Wrapper → Primitive
Integer i = new Integer(10);
int n = i;                // i.intValue()

// In expressions
Integer a = 10, b = 20;
int sum = a + b;          // Unboxing: a.intValue() + b.intValue()

// In method calls
void print(int n) {}
print(new Integer(42));   // Unboxing to int
```

### Example
```java
public class AutoBoxDemo {
    public static void main(String[] args) {
        // Autoboxing
        Integer i = 10;                    // Integer.valueOf(10)
        
        List<Integer> list = new ArrayList<>();
        list.add(1);                       // Autoboxing
        list.add(2);
        list.add(3);
        
        // Unboxing
        int sum = 0;
        for (Integer n : list) {           // Unboxing in enhanced for
            sum += n;                      // n.intValue()
        }
        
        System.out.println("Sum: " + sum);
    }
}
```

### Primitive ↔ Wrapper Mapping

| Primitive | Wrapper | Autoboxing | Unboxing |
|-----------|---------|------------|----------|
| `boolean` | `Boolean` | `Boolean.valueOf(b)` | `b.booleanValue()` |
| `byte` | `Byte` | `Byte.valueOf(b)` | `b.byteValue()` |
| `char` | `Character` | `Character.valueOf(c)` | `c.charValue()` |
| `short` | `Short` | `Short.valueOf(s)` | `s.shortValue()` |
| `int` | `Integer` | `Integer.valueOf(i)` | `i.intValue()` |
| `long` | `Long` | `Long.valueOf(l)` | `l.longValue()` |
| `float` | `Float` | `Float.valueOf(f)` | `f.floatValue()` |
| `double` | `Double` | `Double.valueOf(d)` | `d.doubleValue()` |

### Performance Note
- Avoid autoboxing/unboxing in performance-critical loops
- Creates temporary objects, increases GC pressure
- Use primitives for scientific computing

---

## 10.10 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. Difference between String and StringBuffer/StringBuilder.
2. What is wrapper class? When is Number class used?
3. What is autoboxing and unboxing?
4. Difference between StringBuilder and StringBuffer.
5. How to convert String to int and int to String?
6. What is String constant pool?
7. What are Character class methods?
8. What is `valueOf()` method?

**5-Mark Questions:**
1. Explain Number class and its conversion methods with example.
2. Explain String class methods: length, charAt, substring, concat, equals.
3. Explain StringBuilder class with append, insert, reverse methods.
4. Explain autoboxing and unboxing with example program.
5. Write program to check palindrome using StringBuilder.
6. Write program to display digits after decimal point.
7. Explain formatting with printf/format methods.

**10-Mark Questions:**
1. Explain wrapper classes, Number class, String, StringBuilder, StringBuffer, and autoboxing/unboxing.

### Programs to Practice
1. ✅ **String reverse + length** - appeared 2022, 2023, 2024, 2025
2. ✅ **Palindrome check (StringBuilder)** - appeared 2023, 2024
3. ✅ **Autoboxing/unboxing demo** - appeared 2024, 2025
4. ✅ **String methods demo** - appeared 2022, 2023, 2024
5. ✅ **Number parsing (parseInt)** - appeared 2024, 2025

---

## 10.11 Summary of Unit 10

| Topic | Key Points |
|-------|------------|
| **Wrapper Classes** | 8 classes for primitives; Number is abstract superclass |
| **Number Class** | parseInt, valueOf, toString, compareTo, equals |
| **Integer Constants** | MAX_VALUE, MIN_VALUE, SIZE |
| **Formatting** | printf/format with %d, %f, %s, flags, width, precision |
| **Character Class** | isLetter, isDigit, toUpperCase, compareTo, equals |
| **String** | Immutable; pool for literals; many utility methods |
| **StringBuilder** | Mutable; non-sync; fast; append, insert, reverse, delete |
| **StringBuffer** | Mutable; sync; thread-safe; legacy |
| **Autoboxing** | Primitive → Wrapper (auto) |
| **Unboxing** | Wrapper → Primitive (auto) |
| **Performance** | StringBuilder > StringBuffer > String for modifications |

---

## 10.12 Quick Reference: Common String Methods

```java
String s = "Hello World";

s.length()              // 11
s.charAt(0)             // 'H'
s.substring(6)          // "World"
s.substring(0, 5)       // "Hello"
s.indexOf('o')          // 4
s.lastIndexOf('o')      // 7
s.contains("World")     // true
s.equals("Hello")       // false
s.equalsIgnoreCase("hello world") // true
s.compareTo("Hello")    // >0
s.toUpperCase()         // "HELLO WORLD"
s.toLowerCase()         // "hello world"
s.trim()                // Remove spaces
s.replace('l', 'L')     // "HeLLo WorLd"
s.split(" ")            // ["Hello", "World"]
s.toCharArray()         // ['H','e','l','l','o',...]
String.valueOf(123)     // "123"
Integer.parseInt("123") // 123
```