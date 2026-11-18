# Unit 10: Number, Character and Strings

## Unit Overview
This unit covers wrapper classes (Number class and subclasses), Character class, String class, StringBuilder, StringBuffer, and autoboxing/unboxing. **High exam relevance: String handling, Number class parsing, StringBuilder/StringBuffer, autoboxing/unboxing frequently appear as 5-mark programs and short notes.**

---

## 10.1 Wrapper Classes and Number Class

### Wrapper Classes
Each primitive type has a corresponding wrapper class:

| Primitive | Wrapper Class | Package | Autoboxing Cache Range |
|-----------|---------------|---------|------------------------|
| `byte` | `Byte` | `java.lang` | -128 to 127 |
| `short` | `Short` | `java.lang` | -128 to 127 |
| `int` | `Integer` | `java.lang` | -128 to 127 |
| `long` | `Long` | `java.lang` | -128 to 127 |
| `float` | `Float` | `java.lang` | -128 to 127 |
| `double` | `Double` | `java.lang` | -128 to 127 |
| `char` | `Character` | `java.lang` | '\u0000' to '\u007F' (0-127) |
| `boolean` | `Boolean` | `java.lang` | `Boolean.TRUE`, `Boolean.FALSE` (singletons) |

> **Key Exam Point**: Wrapper objects are **immutable**. Autoboxing uses `valueOf()` which caches small values. `new Integer(10)` creates a new object; `Integer.valueOf(10)` uses cache.

### Inheritance Hierarchy
```
                    Object
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        Number    Boolean    Character
          │
      ┌─────┼─────┐
      ▼     ▼     ▼     ▼     ▼     ▼
    Byte  Short  Integer  Long  Float  Double
```

> **Note**: `Boolean` and `Character` extend `Object` directly, **not** `Number`. Only numeric wrappers extend `Number`.

### Number Class (Abstract)
Abstract superclass of all numeric wrapper classes (`Byte`, `Short`, `Integer`, `Long`, `Float`, `Double`).

#### Common Methods (All Numeric Subclasses)
```java
// Conversion to primitives
byte byteValue()
short shortValue()
int intValue()
long longValue()
float floatValue()
double doubleValue()

// Comparison (defined in each subclass, NOT in Number class)
int compareTo(Byte/Short/Integer/Long/Float/Double another)
boolean equals(Object obj)

// Utility methods (static, in each subclass)
static <Type> parse<Type>(String s)           // String → primitive
static <Type> valueOf(String s)               // String → Wrapper object
static <Type> valueOf(primitive)              // primitive → Wrapper object (uses cache)
static String toString(primitive)             // primitive → String
static String toHexString(int i)              // Integer/Long only
static String toBinaryString(int i)           // Integer/Long only
static String toOctalString(int i)            // Integer/Long only
```

> **Exam Tip**: `compareTo()` and `equals()` are **instance methods** in each subclass (e.g., `Integer.compareTo(Integer)`), not in the abstract `Number` class. `parseInt()`, `valueOf()`, `toString()` are **static methods** in each subclass.

### Other Wrapper Class Constants (Frequently Asked)
```java
// Integer
Integer.MAX_VALUE   // 2147483647 (2^31 - 1)
Integer.MIN_VALUE   // -2147483648 (-2^31)
Integer.SIZE        // 32 (bits)
Integer.BYTES       // 4 (bytes)

// Long
Long.MAX_VALUE      // 9223372036854775807L
Long.MIN_VALUE      // -9223372036854775808L
Long.SIZE           // 64
Long.BYTES          // 8

// Double
Double.MAX_VALUE    // ~1.79e308
Double.MIN_VALUE    // ~4.9e-324 (smallest positive)
Double.NaN          // Not-a-Number
Double.POSITIVE_INFINITY
Double.NEGATIVE_INFINITY
Double.SIZE         // 64
Double.BYTES        // 8

// Float
Float.MAX_VALUE     // ~3.4e38f
Float.MIN_VALUE     // ~1.4e-45f
Float.NaN
Float.POSITIVE_INFINITY
Float.NEGATIVE_INFINITY
Float.SIZE          // 32
Float.BYTES         // 4

// Character
Character.MAX_VALUE // '￿' (65535)
Character.MIN_VALUE // '\u0000' (0)
Character.SIZE      // 16 (bits)
Character.BYTES     // 2 (bytes)
```

---

## 10.2 Integer Class (Most Used in Exams)

### Important Constants
```java
Integer.MAX_VALUE   // 2147483647
Integer.MIN_VALUE   // -2147483648
Integer.SIZE        // 32 (bits)
Integer.BYTES       // 4 (bytes)
```

### Conversion Methods
```java
// String to int (throws NumberFormatException if invalid)
static int parseInt(String s)              // "123" → 123
static int parseInt(String s, int radix)   // "FF", 16 → 255

// int to String
static String toString(int i)              // 123 → "123"
static String toString(int i, int radix)   // 255, 16 → "ff"
static String toHexString(int i)           // 255 → "ff"
static String toBinaryString(int i)        // 5 → "101"
static String toOctalString(int i)         // 10 → "12"

// String to Integer object (uses cache -128 to 127)
static Integer valueOf(String s)           // "123" → Integer(123)
static Integer valueOf(String s, int radix)
static Integer valueOf(int i)              // 123 → Integer(123) (cached -128 to 127)

// Integer object to primitive (unboxing)
int intValue()                             // Unboxing

// Comparison
int compareTo(Integer another)             // Returns -1, 0, 1
boolean equals(Object obj)                 // Content equality
static int compare(int x, int y)           // Static compare (Java 7+)
static int compareUnsigned(int x, int y)   // Unsigned compare (Java 8+)

// Bit manipulation (Java 8+)
static int bitCount(int i)                 // Number of 1-bits
static int highestOneBit(int i)            // Highest set bit
static int lowestOneBit(int i)             // Lowest set bit
static int numberOfLeadingZeros(int i)
static int numberOfTrailingZeros(int i)
static int reverse(int i)                  // Reverse bit order
static int rotateLeft(int i, int distance)
static int rotateRight(int i, int distance)
static int signum(int i)                   // -1, 0, or 1
```

### Example
```java
public class NumberDemo {
    public static void main(String[] args) {
        Integer i = 20;           // Autoboxing: Integer.valueOf(20)
        Integer j = 25;
        String s = "28";
        
        int a = i.intValue();     // 20 (unboxing)
        int b = Integer.parseInt(s);  // 28
        int c = j.intValue();     // 25
        
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("a + b * c: " + (a + b * c));
        
        // Exam: Demonstrate cache behavior
        Integer x = 100;
        Integer y = 100;
        Integer p = 200;
        Integer q = 200;
        System.out.println(x == y);  // true (cached)
        System.out.println(p == q);  // false (not cached)
    }
}
```

---

## 10.3 Formatting Numeric Output

### printf and format Methods
```java
// System.out is a PrintStream
System.out.format("format", args);
System.out.printf("format", args);    // Same as format, returns PrintStream
String formatted = String.format("format", args);  // Returns formatted String
```

### Format Specifiers

| Specifier | Description | Example |
|-----------|-------------|---------|
| `%d` | Decimal integer | `%d` → `42` |
| `%f` | Floating point (6 decimals default) | `%f` → `3.140000` |
| `%.2f` | 2 decimal places | `%.2f` → `3.14` |
| `%n` | Platform-independent newline | |
| `%s` | String | |
| `%c` | Character | |
| `%x` | Hexadecimal (lowercase) | `255` → `ff` |
| `%X` | Hexadecimal (uppercase) | `255` → `FF` |
| `%o` | Octal | `10` → `12` |
| `%e` | Scientific notation (lowercase) | `1234.5` → `1.234500e+03` |
| `%E` | Scientific notation (uppercase) | `1234.5` → `1.234500E+03` |
| `%g` | General (shorter of %f or %e) | |
| `%a` | Hex floating-point | |
| `%t` / `%T` | Date/Time (prefix for time formats) | `%tF` → `2024-01-15` |

### Flags
| Flag | Description | Example |
|------|-------------|---------|
| `-` | Left justify | `%-10d` |
| `+` | Always show sign | `%+d` → `+42` |
| `0` | Pad with zeros | `%08d` → `00000042` |
| `,` | Locale-specific grouping | `%,d` → `1,000,000` |
| `(` | Enclose negative in parentheses | `%(d` → `(42)` |
| ` ` (space) | Leading space for positive | `% d` → ` 42` |
| `#` | Alternate form (0x, 0, 0b) | `%#x` → `0xff` |

### Width and Precision
```java
%10d      // Width 10, right-aligned
%-10d     // Width 10, left-aligned
%08d      // Width 8, zero-padded
%.3f      // 3 decimal places
%10.2f    // Width 10, 2 decimal places
%010.2f   // Width 10, zero-padded, 2 decimals
```

### Example
```java
import java.util.Locale;

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
        System.out.format(Locale.GERMAN, "pi=%-10.4f%n%n", pi); // pi=3,1416   (German uses comma)
        
        // Exam: Common formatting tasks
        System.out.format("Hex: %x, %X%n", 255, 255);    // ff, FF
        System.out.format("Octal: %o%n", 10);             // 12
        System.out.format("Binary: %s%n", Integer.toBinaryString(5)); // 101
    }
}
```

---

## 10.4 Character Class

### Creating Character Objects
```java
Character c1 = 'A';                    // Autoboxing (preferred)
Character c2 = new Character('B');     // Constructor (DEPRECATED Java 9+)
Character c3 = Character.valueOf('C'); // Preferred factory method
```

### Common Methods
| Method | Description | Example |
|--------|-------------|---------|
| `isLetter(char ch)` | Is letter (A-Z, a-z)? | `isLetter('A')` → true |
| `isDigit(char ch)` | Is digit (0-9)? | `isDigit('5')` → true |
| `isWhitespace(char ch)` | Is whitespace (space, tab, newline)? | `isWhitespace(' ')` → true |
| `isUpperCase(char ch)` | Is uppercase? | `isUpperCase('a')` → false |
| `isLowerCase(char ch)` | Is lowercase? | `isLowerCase('a')` → true |
| `toUpperCase(char ch)` | To uppercase | `toUpperCase('a')` → 'A' |
| `toLowerCase(char ch)` | To lowercase | `toLowerCase('A')` → 'a' |
| `toString(char ch)` | To String | `toString('A')` → "A" |
| `compareTo(Character c)` | Compare (lexicographic) | `'A'.compareTo('B')` → -1 |
| `equals(Character c)` | Equality | `'A'.equals('A')` → true |
| `isLetterOrDigit(char ch)` | Letter or digit | `isLetterOrDigit('_')` → false |
| `isJavaIdentifierStart(char ch)` | Valid start of Java identifier | `isJavaIdentifierStart('$')` → true |
| `isJavaIdentifierPart(char ch)` | Valid part of Java identifier | `isJavaIdentifierPart('1')` → true |
| `getNumericValue(char ch)` | Unicode numeric value | `getNumericValue('5')` → 5, `getNumericValue('A')` → 10 |
| `forDigit(int digit, int radix)` | Char for digit in radix | `forDigit(10, 16)` → 'a' |
| `digit(char ch, int radix)` | Numeric value in radix | `digit('f', 16)` → 15 |
| `isDefined(char ch)` | Is defined in Unicode? | |
| `isISOControl(char ch)` | Is ISO control character? | |
| `getType(char ch)` | Unicode general category | |

> **Exam Focus**: `isLetter`, `isDigit`, `isWhitespace`, `toUpperCase`, `toLowerCase`, `getNumericValue`, `forDigit`, `digit` are frequently asked.

### Code Point Methods (Supplementary Characters)
```java
// For characters beyond BMP (Basic Multilingual Plane), use code points (int)
String s = "𝔸";  // Mathematical double-struck A (U+1D538)

s.length()                    // 2 (UTF-16 code units: surrogate pair)
s.codePointCount(0, s.length()) // 1 (actual Unicode code points)
s.codePointAt(0)              // 119864 (0x1D538)
Character.toChars(119864)     // char[] of surrogate pair
Character.isLetter(119864)    // true (code point version)
Character.toUpperCase(119864) // 119864 (already uppercase)
```

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
        else System.out.println("Not equal (diff: " + diff + ")");
        
        // Exam: Character classification
        char ch = '7';
        System.out.println("isDigit: " + Character.isDigit(ch));        // true
        System.out.println("getNumericValue: " + Character.getNumericValue(ch)); // 7
        System.out.println("forDigit(15, 16): " + Character.forDigit(15, 16));   // f
        
        // Exam: Check if valid Java identifier
        System.out.println("isJavaIdentifierStart('_'):" + Character.isJavaIdentifierStart('_')); // true
        System.out.println("isJavaIdentifierPart('1'):" + Character.isJavaIdentifierPart('1'));   // true
    }
}
```

---

## 10.5 String Class

### Key Characteristics
- **Immutable**: Cannot be changed after creation (creates new object on modification)
- **Final class**: Cannot be extended
- **String Constant Pool**: Literals stored in pool for reuse (saves memory)
- **Implements**: `Serializable`, `Comparable<String>`, `CharSequence`

### Creating Strings
```java
// 1. String literal (uses pool - preferred)
String s1 = "Hello";
String s2 = "Hello";  // Same object from pool (s1 == s2 is true)

// 2. new keyword (creates new object in heap, NOT in pool)
String s3 = new String("Hello");
String s4 = new String("Hello");  // Different objects (s3 == s4 is false)

// 3. From char array
char[] chars = {'H', 'e', 'l', 'l', 'o'};
String s5 = new String(chars);           // "Hello"
String s6 = new String(chars, 1, 3);     // "ell" (offset=1, count=3)

// 4. From byte array (encoding)
byte[] bytes = {72, 101, 108, 108, 111};
String s7 = new String(bytes);           // "Hello" (platform default charset)
String s8 = new String(bytes, "UTF-8");  // Explicit charset

// Comparison
s1 == s2        // true (same reference from pool)
s1 == s3        // false (different objects)
s1.equals(s3)   // true (same content)
s1.intern()     // Returns pooled reference (adds to pool if not present)
```

> **Exam Key Point**: Always use `.equals()` for content comparison, NOT `==`. `==` compares references. `intern()` forces string into constant pool.

### Important Constructors
```java
String()                              // Empty string ""
String(String original)               // Copy constructor
String(char[] value)                  // From char array
String(char[] value, int offset, int count)  // Subarray
String(byte[] bytes)                  // From bytes (default charset)
String(byte[] bytes, int offset, int length)
String(byte[] bytes, String charsetName)
String(byte[] bytes, Charset charset)
String(StringBuilder builder)         // From StringBuilder (Java 5+)
String(StringBuffer buffer)           // From StringBuffer
```

### Important Methods

| Method | Description |
|--------|-------------|
| `int length()` | Returns length (number of `char` code units) |
| `char charAt(int index)` | Character at index (0-based) |
| `int codePointAt(int index)` | Unicode code point at index |
| `int codePointBefore(int index)` | Code point before index |
| `int codePointCount(int begin, int end)` | Number of code points in range |
| `String substring(int begin)` | From begin to end |
| `String substring(int begin, int end)` | Range [begin, end) |
| `String concat(String str)` | Concatenation (returns new String) |
| `boolean equals(Object obj)` | Content equality |
| `boolean equalsIgnoreCase(String str)` | Case-insensitive equality |
| `int compareTo(String str)` | Lexicographic comparison (returns -ve, 0, +ve) |
| `int compareToIgnoreCase(String str)` | Case-insensitive comparison |
| `boolean startsWith(String prefix)` | Starts with prefix |
| `boolean endsWith(String suffix)` | Ends with suffix |
| `boolean contains(CharSequence s)` | Contains sequence |
| `int indexOf(int ch)` | First occurrence of char |
| `int indexOf(int ch, int fromIndex)` | First occurrence from index |
| `int lastIndexOf(int ch)` | Last occurrence of char |
| `int indexOf(String str)` | First occurrence of substring |
| `int lastIndexOf(String str)` | Last occurrence of substring |
| `String replace(char old, char new)` | Replace all char occurrences |
| `String replace(CharSequence target, CharSequence replacement)` | Replace sequence |
| `String replaceAll(String regex, String replacement)` | Regex replace all |
| `String replaceFirst(String regex, String replacement)` | Regex replace first |
| `String toLowerCase()` | Convert to lowercase |
| `String toUpperCase()` | Convert to uppercase |
| `String trim()` | Remove leading/trailing whitespace (ASCII ≤ 32) |
| `String strip()` | Remove leading/trailing whitespace (Unicode-aware, Java 11+) |
| `String stripLeading()` | Remove leading whitespace only (Java 11+) |
| `String stripTrailing()` | Remove trailing whitespace only (Java 11+) |
| `String[] split(String regex)` | Split into array |
| `String[] split(String regex, int limit)` | Split with limit (limit > 0: max parts; limit < 0: no limit; limit = 0: trim trailing empty) |
| `char[] toCharArray()` | Convert to char array |
| `byte[] getBytes()` | Convert to byte array (default charset) |
| `byte[] getBytes(Charset charset)` | Convert with specific charset |
| `static String valueOf(...)` | Static: convert any type to String |
| `static String join(CharSequence delimiter, CharSequence... elements)` | Join with delimiter (Java 8+) |
| `static String join(CharSequence delimiter, Iterable<? extends CharSequence> elements)` | Join from Iterable (Java 8+) |
| `String repeat(int count)` | Repeat string (Java 11+) |
| `String indent(int n)` | Adjust indentation (Java 12+) |
| `String transform(Function<String, R> f)` | Apply function (Java 12+) |
| `boolean isBlank()` | True if empty or only whitespace (Java 11+) |
| `Stream<String> lines()` | Stream of lines (Java 11+) |

### Search Methods
```java
String str = "Java is Object Oriented Programming Language";

str.length()                    // 45
str.charAt(0)                   // 'J'
str.charAt(str.length()-1)      // 'e'
str.indexOf('a')                // 1 (first 'a')
str.lastIndexOf('a')            // 37 (last 'a')
str.indexOf('a', 10)            // 21 (search from index 10)
str.contains("Object")          // true
str.startsWith("Java")          // true
str.endsWith("Language")        // true
str.compareTo("Java")           // > 0 (this string is "greater")
```

### Modification Methods (Return NEW String - Original Unchanged!)
```java
String s = "Hello World";

s.toUpperCase()         // "HELLO WORLD"
s.toLowerCase()         // "hello world"
s.trim()                // Remove leading/trailing spaces
s.strip()               // Unicode-aware trim (Java 11+)
s.replace('l', 'L')     // "HeLLo WorLd"
s.replace("World", "Java")  // "Hello Java"
s.replaceAll("\\s+", "_")   // "Hello_World" (regex)
s.substring(0, 5)       // "Hello"
s.substring(6)          // "World"
s.concat("!!!")         // "Hello World!!!"
```

### Comparison Methods
```java
String s1 = "Hello";
String s2 = "hello";
String s3 = "World";

s1.equals(s2)           // false
s1.equalsIgnoreCase(s2) // true
s1.compareTo(s2)        // negative ('H' < 'h')
s1.compareToIgnoreCase(s2) // 0
s1.startsWith("He")     // true
s1.endsWith("lo")       // true
s1.regionMatches(true, 0, s2, 0, 5)  // Case-insensitive region match
```

### Conversion Between Numbers and Strings
```java
// String to Number (throws NumberFormatException if invalid)
int i = Integer.parseInt("123");
long l = Long.parseLong("1234567890");
double d = Double.parseDouble("3.14");
float f = Float.parseFloat("2.5");    // Note: NO 'f' suffix in string!
boolean b = Boolean.parseBoolean("true");

// Number to String
String s1 = String.valueOf(123);      // "123" (handles null → "null")
String s2 = String.valueOf(3.14);     // "3.14"
String s3 = Integer.toString(42);     // "42"
String s4 = Double.toString(3.14);    // "3.14"
String s5 = Integer.toString(255, 16); // "ff" (radix 16)
String s6 = Integer.toHexString(255);  // "ff"
String s7 = Integer.toBinaryString(5); // "101"
String s8 = Integer.toOctalString(10); // "12"

// Concatenation (creates new String - inefficient in loops)
String s = "Age: " + 25;              // "Age: 25"

// String.format (powerful formatting)
String formatted = String.format("Name: %s, Age: %d, Score: %.2f", "John", 25, 95.5);
// "Name: John, Age: 25, Score: 95.50"
```

> **Common Mistake**: `Float.valueOf("2.5f")` throws `NumberFormatException` — the string should NOT contain 'f' or 'd' suffixes.

### Palindrome Check Example
```java
// Using String (inefficient - creates many intermediate strings)
String str = "MADAM";
String rev = "";
for (int i = str.length()-1; i >= 0; i--) {
    rev += str.charAt(i);  // String concatenation in loop - BAD
}
if (str.equalsIgnoreCase(rev)) System.out.println("Palindrome");

// Using StringBuilder (efficient - mutable)
StringBuilder sb = new StringBuilder(str);
if (str.equalsIgnoreCase(sb.reverse().toString())) 
    System.out.println("Palindrome");

// Exam: Without using reverse()
public static boolean isPalindrome(String s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right)))
            return false;
        left++; right--;
    }
    return true;
}
```

### Important String Programs for Exams

**Program 1: String Length and First Character** (JUNE 2025 Q1(f))
```java
public class StringLengthFirstChar {
    public static void main(String[] args) {
        String str = "Hello World";
        System.out.println("Length: " + str.length());        // 11
        System.out.println("First char: " + str.charAt(0));   // H
        System.out.println("Last char: " + str.charAt(str.length()-1)); // d
    }
}
```

**Program 2: String Reverse** (DEC 2022, 2023, 2024, 2025)
```java
public class StringReverse {
    public static void main(String[] args) {
        String str = "Hello";
        
        // Method 1: StringBuilder
        String rev1 = new StringBuilder(str).reverse().toString();
        
        // Method 2: Loop (exam often asks without StringBuilder)
        String rev2 = "";
        for (int i = str.length()-1; i >= 0; i--) {
            rev2 += str.charAt(i);
        }
        
        // Method 3: Char array swap (most efficient without StringBuilder)
        char[] arr = str.toCharArray();
        for (int i = 0, j = arr.length-1; i < j; i++, j--) {
            char temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
        }
        String rev3 = new String(arr);
        
        System.out.println(rev1); // olleH
    }
}
```

**Program 3: Count Vowels, Consonants, Digits, Spaces**
```java
public class StringAnalysis {
    public static void main(String[] args) {
        String str = "Hello World 123";
        int vowels = 0, consonants = 0, digits = 0, spaces = 0;
        
        for (int i = 0; i < str.length(); i++) {
            char ch = Character.toLowerCase(str.charAt(i));
            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
                vowels++;
            else if (Character.isLetter(ch))
                consonants++;
            else if (Character.isDigit(ch))
                digits++;
            else if (Character.isWhitespace(ch))
                spaces++;
        }
        System.out.println("Vowels: " + vowels + ", Consonants: " + consonants 
                         + ", Digits: " + digits + ", Spaces: " + spaces);
    }
}
```

**Program 4: Number Class parseInt Demo** (DEC 2024 Q2(b))
```java
public class NumberParseIntDemo {
    public static void main(String[] args) {
        String[] nums = {"123", "-456", "789", "FF", "1010"};
        
        for (String s : nums) {
            try {
                // Parse decimal
                int dec = Integer.parseInt(s);
                System.out.println(s + " (dec) = " + dec);
            } catch (NumberFormatException e) {
                try {
                    // Try hex
                    int hex = Integer.parseInt(s, 16);
                    System.out.println(s + " (hex) = " + hex);
                } catch (NumberFormatException e2) {
                    try {
                        // Try binary
                        int bin = Integer.parseInt(s, 2);
                        System.out.println(s + " (bin) = " + bin);
                    } catch (NumberFormatException e3) {
                        System.out.println(s + " = Invalid number");
                    }
                }
            }
        }
        
        // Convert int to String in different bases
        int num = 255;
        System.out.println("Decimal: " + Integer.toString(num));
        System.out.println("Hex: " + Integer.toHexString(num));
        System.out.println("Binary: " + Integer.toBinaryString(num));
        System.out.println("Octal: " + Integer.toOctalString(num));
    }
}
```

---

## 10.6 StringBuilder Class

### Characteristics
- **Mutable**: Can be modified without creating new objects
- **Not synchronized**: Not thread-safe (single-threaded use)
- **Faster** than StringBuffer
- **Preferred** for single-threaded string manipulation
- **Capacity growth**: When exceeded, new capacity = (old capacity * 2) + 2

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
| `int length()` | Current length |
| `int capacity()` | Current capacity |
| `void ensureCapacity(int min)` | Ensure minimum capacity |
| `void setLength(int newLength)` | Set length (truncate or pad with `\0`) |
| `char charAt(int index)` | Character at index |
| `void setCharAt(int index, char ch)` | Set character |
| `StringBuilder append(...)` | Append (overloaded for all types) - **returns this** for chaining |
| `StringBuilder insert(int offset, ...)` | Insert at offset - **returns this** |
| `StringBuilder delete(int start, int end)` | Delete range [start, end) - **returns this** |
| `StringBuilder deleteCharAt(int index)` | Delete single character - **returns this** |
| `StringBuilder replace(int start, int end, String str)` | Replace range - **returns this** |
| `StringBuilder reverse()` | Reverse sequence - **returns this** |
| `String toString()` | Convert to String |
| `String substring(int start)` | Substring (returns String) |
| `String substring(int start, int end)` | Substring range (returns String) |
| `int indexOf(String str)` | First occurrence (Java 8+) |
| `int lastIndexOf(String str)` | Last occurrence (Java 8+) |
| `int codePointAt(int index)` | Unicode code point |
| `int codePointBefore(int index)` | Code point before |
| `int codePointCount(int begin, int end)` | Code point count |

### Example
```java
public class SBExample {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder(20);
        System.out.println("Length: " + sb.length());      // 0
        System.out.println("Capacity: " + sb.capacity());  // 20
        
        sb.append("Welcome to Java");
        System.out.println("After append: " + sb);
        System.out.println("Length: " + sb.length());      // 17
        System.out.println("Capacity: " + sb.capacity());  // 20 (unchanged)
        
        sb.ensureCapacity(50);
        System.out.println("Capacity after ensure: " + sb.capacity()); // 50
        
        // Method chaining
        sb.insert(0, "Start: ").append(" :End").reverse();
        System.out.println("Reverse: " + sb);
        
        // Exam: Efficient string building in loop
        StringBuilder efficient = new StringBuilder();
        for (int i = 0; i < 100; i++) {
            efficient.append(i).append(" ");  // No intermediate strings
        }
        System.out.println(efficient.length());
    }
}
```

---

## 10.7 StringBuffer Class

### Characteristics
- **Mutable**: Can be modified
- **Synchronized**: Thread-safe (all methods are `synchronized`)
- **Slower** than StringBuilder due to synchronization overhead
- **Legacy**: Exists since Java 1.0 (StringBuilder added in Java 5)

### Constructors
```java
StringBuffer()                    // Empty, capacity 16
StringBuffer(int capacity)        // Empty, specified capacity
StringBuffer(String str)          // From string
```

### Methods (Same as StringBuilder + synchronized)
```java
// All methods are synchronized
public synchronized int length()
public synchronized int capacity()
public synchronized StringBuffer append(String str)
public synchronized StringBuffer insert(int offset, String str)
public synchronized StringBuffer delete(int start, int end)
public synchronized StringBuffer replace(int start, int end, String str)
public synchronized StringBuffer reverse()
// ... etc.
```

### When to Use StringBuffer
- Multi-threaded environment where multiple threads modify the same buffer
- Legacy code compatibility (pre-Java 5)
- **Exam Answer**: "Use StringBuffer when thread-safety is required; otherwise prefer StringBuilder for better performance."

---

## 10.8 StringBuilder vs StringBuffer vs String

| Feature | String | StringBuilder | StringBuffer |
|---------|--------|---------------|--------------|
| **Mutability** | Immutable | Mutable | Mutable |
| **Thread Safety** | Yes (immutable) | No | Yes (synchronized) |
| **Performance** | Slow for concat | Fastest | Moderate |
| **Java Version** | 1.0 | 5.0 | 1.0 |
| **Use Case** | Constant strings | Single-threaded | Multi-threaded |
| **Memory** | Pool for literals | Heap (resizable) | Heap (resizable) |

### Performance Demonstration
```java
public class PerformanceDemo {
    public static void main(String[] args) {
        int iterations = 50000;
        
        // String concatenation (SLOW - creates 50000 intermediate objects)
        long start = System.currentTimeMillis();
        String s = "";
        for (int i = 0; i < iterations; i++) s += "a";
        System.out.println("String: " + (System.currentTimeMillis() - start) + " ms");
        
        // StringBuilder (FAST)
        start = System.currentTimeMillis();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < iterations; i++) sb.append("a");
        System.out.println("StringBuilder: " + (System.currentTimeMillis() - start) + " ms");
        
        // StringBuffer (MODERATE)
        start = System.currentTimeMillis();
        StringBuffer sbf = new StringBuffer();
        for (int i = 0; i < iterations; i++) sbf.append("a");
        System.out.println("StringBuffer: " + (System.currentTimeMillis() - start) + " ms");
    }
}
```

---

## 10.9 Autoboxing and Unboxing

### Autoboxing
Automatic conversion of **primitive** to **wrapper object** by the compiler.

```java
// Primitive → Wrapper (compiler inserts valueOf())
Integer i = 10;           // Integer.valueOf(10)
Double d = 3.14;          // Double.valueOf(3.14)
Boolean b = true;         // Boolean.valueOf(true)
Character c = 'A';        // Character.valueOf('A')

// In collections (must use wrapper)
List<Integer> list = new ArrayList<>();
list.add(10);             // Autoboxing: list.add(Integer.valueOf(10))
list.add(20);
```

### Unboxing
Automatic conversion of **wrapper object** to **primitive** by the compiler.

```java
// Wrapper → Primitive (compiler inserts intValue(), etc.)
Integer i = new Integer(10);
int n = i;                // i.intValue()

// In expressions
Integer a = 10, b = 20;
int sum = a + b;          // Unboxing: a.intValue() + b.intValue()

// In method calls
void print(int n) {}
print(new Integer(42));   // Unboxing to int

// In control structures
Integer x = 5;
if (x > 3) { }            // Unboxing for comparison
while (x-- > 0) { }       // Unboxing, decrement, re-boxing!
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
        
        System.out.println("Sum: " + sum); // 6
        
        // Exam: Demonstrate cache
        Integer a = 100, b = 100;
        Integer c = 200, d = 200;
        System.out.println(a == b);  // true (cached -128 to 127)
        System.out.println(c == d);  // false (new objects)
        System.out.println(a.equals(b)); // true (content)
        System.out.println(c.equals(d)); // true (content)
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
- **Exam**: "Autoboxing creates wrapper objects; unboxing calls xxxValue(). In loops, this creates many objects causing GC overhead."

---

## 10.10 Important Exam Questions (from PYQ Analysis - Dec 2021 to June 2026)

### High Priority (Appeared Multiple Times)

#### 2-Mark Questions:
1. **Difference between String and StringBuffer/StringBuilder** (DEC 2021)
2. **What is wrapper class? When is Number class used?**
3. **What is autoboxing and unboxing?** (JUNE 2024)
4. **Difference between StringBuilder and StringBuffer**
5. **How to convert String to int and int to String?** (DEC 2024 Q2b, JUNE 2025 Q1f)
6. **What is String constant pool?**
7. **What are Character class methods?** (`isLetter`, `isDigit`, `toUpperCase`, `getNumericValue`)
8. **What is `valueOf()` method?**
9. **Difference between `==` and `.equals()` for String**
10. **What is `parseInt()` vs `valueOf()`?**

#### 5-Mark Questions:
1. **Explain Number class and its conversion methods with example.** (DEC 2024 Q2b)
2. **Explain String class methods: length, charAt, substring, concat, equals.** (JUNE 2025 Q1f)
3. **Explain StringBuilder class with append, insert, reverse methods.**
4. **Explain autoboxing and unboxing with example program.** (JUNE 2024)
5. **Write program to check palindrome using StringBuilder.** (DEC 2023, 2024)
6. **Write program to display digits after decimal point.**
7. **Explain formatting with printf/format methods.**
8. **Write program to count vowels, consonants, digits in a string.**
9. **Explain Character class methods with examples.**

#### 10-Mark Questions:
1. **Explain wrapper classes, Number class, String, StringBuilder, StringBuffer, and autoboxing/unboxing.**

### Programs to Practice (Exact PYQ Matches)

| Program | Years Appeared | Marks |
|---------|---------------|-------|
| ✅ **String reverse + length** | 2022×2, 2023, 2024, 2025 | 5 |
| ✅ **Palindrome check (StringBuilder)** | 2023, 2024 | 5 |
| ✅ **Autoboxing/unboxing demo** | 2024, 2025 | 5 |
| ✅ **String methods demo (length, charAt, substring)** | 2022, 2023, 2024, 2025 | 5 |
| ✅ **Number parsing (parseInt, parseDouble)** | 2024, 2025 | 5 |
| ✅ **String length + first char** | 2025 | 5 |
| ✅ **Format output with printf** | 2021, 2024 | 5 |

---

## 10.11 Summary of Unit 10

| Topic | Key Points |
|-------|------------|
| **Wrapper Classes** | 8 classes for primitives; Number is abstract superclass for numeric wrappers |
| **Number Class** | parseXxx, valueOf, toString, compareTo, equals (in subclasses) |
| **Integer Constants** | MAX_VALUE, MIN_VALUE, SIZE, BYTES |
| **Formatting** | printf/format with %d, %f, %s, flags, width, precision; String.format() |
| **Character Class** | isLetter, isDigit, isWhitespace, toUpperCase, getNumericValue, forDigit, digit |
| **String** | Immutable; pool for literals; many utility methods; use .equals() not == |
| **StringBuilder** | Mutable; non-sync; fast; append, insert, reverse, delete; capacity grows 2n+2 |
| **StringBuffer** | Mutable; sync; thread-safe; legacy |
| **Autoboxing** | Primitive → Wrapper (auto, uses valueOf with cache) |
| **Unboxing** | Wrapper → Primitive (auto, calls xxxValue()) |
| **Performance** | StringBuilder > StringBuffer > String for modifications |
| **Cache Range** | -128 to 127 for Integer, Short, Byte, Long; 0-127 for Character; Boolean singletons |

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
s.trim()                // Remove spaces (ASCII)
s.strip()               // Remove spaces (Unicode, Java 11+)
s.replace('l', 'L')     // "HeLLo WorLd"
s.split(" ")            // ["Hello", "World"]
s.toCharArray()         // ['H','e','l','l','o',...]
String.valueOf(123)     // "123"
Integer.parseInt("123") // 123

// StringBuilder equivalents (mutable)
StringBuilder sb = new StringBuilder("Hello World");
sb.length()             // 11
sb.charAt(0)            // 'H'
sb.substring(6)         // "World" (returns String)
sb.reverse()            // "dlroW olleH" (mutates, returns this)
sb.toString()           // "dlroW olleH"
```

---

## 10.13 Common Pitfalls & Exam Traps

| Pitfall | Correct Approach |
|---------|------------------|
| `String s = "Hello"; s.toUpperCase();` doesn't modify s | `s = s.toUpperCase();` or use StringBuilder |
| `if (s1 == s2)` for string comparison | `if (s1.equals(s2))` |
| `Float.valueOf("3.14f")` | `Float.valueOf("3.14")` (no 'f' suffix) |
| `Integer.parseInt("FF")` throws exception | `Integer.parseInt("FF", 16)` for hex |
| String concatenation in loop: `s += i` | Use `StringBuilder.append(i)` |
| `new String("Hello")` creates 2 objects | Use `"Hello"` literal (1 object from pool) |
| `Character` constructor `new Character('A')` | Use `Character.valueOf('A')` (constructor deprecated) |
| `Double d = 3.14;` vs `Double d = 3.14f;` | `3.14` is double literal; `3.14f` is float — use correct type |
| Autoboxing `Integer i = null; int n = i;` | Throws NullPointerException on unboxing |
| `substring(begin, end)` excludes end index | Remember: `[begin, end)` — end is exclusive |