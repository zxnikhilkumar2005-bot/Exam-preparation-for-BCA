# Unit 11: I/O Streams

## Unit Overview
This unit covers Java I/O hierarchy, File class, stream classes (Byte and Character streams), serialization, and I/O exceptions. **Critical for exams: Appears 7+ times in last 10 years (Byte vs Character streams, File class, Serialization, Buffered streams, AutoCloseable/Flushable/Closeable).**

---

## 11.1 Java I/O Hierarchy

### Stream Concept
> A **stream** is a sequence of data flowing from source to destination. It abstracts I/O operations from physical devices.

### I/O Class Hierarchy (java.io package)

```
                              Object
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
         InputStream      OutputStream       File
              │                │
     ┌─────────┼─────────┐     ├─────────────┐
     ▼         ▼         ▼     ▼             ▼
FileInput  ByteArray  Filter    FileOutput  ByteArray
           Output     Input     Output     Filter
                              │             │
                    ┌─────────┼─────────┐ ┌──┴─────┐
                    ▼         ▼         ▼ ▼        ▼
               Buffered  Data    Object  Buffered Data
               Input     Input   Input  Output    Output
               
                              Object
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
            Reader           Writer            (Character Streams)
              │                │
     ┌─────────┼─────────┐     ├─────────────┐
     ▼         ▼         ▼     ▼             ▼
FileReader CharArray  Filter  FileWriter  CharArray
           Writer     Reader   Writer     Writer
                              │             │
                    ┌─────────┼─────────┐ ┌──┴─────┐
                    ▼         ▼         ▼ ▼        ▼
               Buffered   Print   Push  Buffered  Print
               Reader     Writer  Back   Writer    Writer
```

### Additional Important Stream Classes (Exam Relevant)

| Class | Type | Purpose |
|-------|------|---------|
| `PrintStream` / `PrintWriter` | Byte/Char | Formatted output (print, println, printf) |
| `PushbackInputStream` / `PushbackReader` | Byte/Char | Push back bytes/chars into stream |
| `SequenceInputStream` | Byte | Concatenate multiple input streams |
| `PipedInputStream` / `PipedOutputStream` | Byte | Inter-thread communication (pipes) |
| `PipedReader` / `PipedWriter` | Char | Inter-thread communication (pipes) |
| `RandomAccessFile` | Both | Random access file read/write (seek) |
| `StreamTokenizer` | Char | Parse stream into tokens |
| `Console` | Char | Advanced console I/O (password, formatting) |

### Stream Types

| Category | Base Classes | Data Type | Use Case |
|----------|-------------|-----------|----------|
| **Byte Streams** | InputStream, OutputStream | Binary (bytes) | Images, audio, video, raw data |
| **Character Streams** | Reader, Writer | Text (Unicode chars) | Text files, XML, JSON |

---

## 11.2 File Class

### Purpose
Represents file/directory pathnames. Does NOT use streams. **Appeared 4 times in PYQ (2021, 2022, 2024, 2025).**

### Constructors
```java
File(String pathname)                    // "path/to/file.txt"
File(String parent, String child)        // "path", "file.txt"
File(File parent, String child)          // File object, "file.txt"
File(URI uri)                            // From URI (Java 1.6+)
```

### Important Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getName()` | String | File/directory name |
| `getPath()` | String | Path as string |
| `getAbsolutePath()` | String | Absolute path |
| `getCanonicalPath()` | String | Canonical path (resolves ., .., symlinks) |
| `getParent()` | String | Parent directory path |
| `exists()` | boolean | True if exists |
| `canRead()` | boolean | True if readable |
| `canWrite()` | boolean | True if writable |
| `canExecute()` | boolean | True if executable |
| `isFile()` | boolean | True if file |
| `isDirectory()` | boolean | True if directory |
| `isHidden()` | boolean | True if hidden |
| `lastModified()` | long | Last modified timestamp |
| `length()` | long | File size in bytes |
| `list()` | String[] | Names of files in directory |
| `list(FilenameFilter filter)` | String[] | Filtered names |
| `listFiles()` | File[] | File objects in directory |
| `listFiles(FileFilter filter)` | File[] | Filtered File objects |
| `mkdir()` | boolean | Create directory |
| `mkdirs()` | boolean | Create parent dirs too |
| `createNewFile()` | boolean | Create new file |
| `createTempFile(prefix, suffix)` | File | Create temp file (static) |
| `delete()` | boolean | Delete file/directory |
| `deleteOnExit()` | void | Delete on JVM exit |
| `renameTo(File dest)` | boolean | Rename/move |
| `setReadable(boolean, boolean)` | boolean | Set read permission |
| `setWritable(boolean, boolean)` | boolean | Set write permission |
| `setExecutable(boolean, boolean)` | boolean | Set execute permission |
| `toURI()` | URI | Convert to URI |
| `toPath()` | Path | Convert to Path (NIO.2, Java 7+) |

### Example - Comprehensive File Operations
```java
import java.io.File;
import java.io.FilenameFilter;

public class FileDemo {
    public static void main(String[] args) {
        File f = new File("test.txt");
        
        System.out.println("Name: " + f.getName());
        System.out.println("Path: " + f.getPath());
        System.out.println("Absolute: " + f.getAbsolutePath());
        System.out.println("Canonical: " + f.getCanonicalPath());
        System.out.println("Parent: " + f.getParent());
        System.out.println("Exists: " + f.exists());
        System.out.println("Size: " + f.length() + " bytes");
        System.out.println("Is File: " + f.isFile());
        System.out.println("Is Dir: " + f.isDirectory());
        System.out.println("Readable: " + f.canRead());
        System.out.println("Writable: " + f.canWrite());
        System.out.println("Hidden: " + f.isHidden());
        System.out.println("Last Modified: " + f.lastModified());
        
        // List directory with filter
        File dir = new File(".");
        String[] files = dir.list(new FilenameFilter() {
            public boolean accept(File dir, String name) {
                return name.endsWith(".java");
            }
        });
        for (String name : files) {
            System.out.println(name);
        }
        
        // Create directory structure
        File newDir = new File("src/main/java");
        newDir.mkdirs();
        
        // Create temp file
        File temp = File.createTempFile("app", ".tmp");
        temp.deleteOnExit();
    }
}
```

---

## 11.3 Byte Stream Classes

### InputStream (Abstract) - Reading Bytes

#### Common Methods
```java
int read()                           // Read single byte, -1 if EOF
int read(byte[] b)                   // Read into array, returns count or -1
int read(byte[] b, int off, int len) // Read into subarray
long skip(long n)                    // Skip bytes
int available()                      // Bytes available without blocking
void close()                         // Close stream
void mark(int readlimit)             // Mark position
void reset()                         // Reset to mark
boolean markSupported()              // Supports mark/reset?
```

### OutputStream (Abstract) - Writing Bytes

#### Common Methods
```java
void write(int b)                      // Write single byte (low 8 bits)
void write(byte[] b)                   // Write array
void write(byte[] b, int off, int len) // Write subarray
void flush()                           // Flush buffer
void close()                           // Close stream
```

### FileInputStream
```java
// Constructors
FileInputStream(String name)
FileInputStream(File file)
FileInputStream(FileDescriptor fdObj)

// Reading file - byte by byte (slow)
FileInputStream fis = new FileInputStream("input.txt");
int data;
while ((data = fis.read()) != -1) {
    System.out.print((char) data);
}
fis.close();

// Better: read into buffer (recommended)
FileInputStream fis = new FileInputStream("input.txt");
byte[] buffer = new byte[1024];
int bytesRead;
while ((bytesRead = fis.read(buffer)) != -1) {
    System.out.write(buffer, 0, bytesRead);
}
fis.close();
```

### FileOutputStream
```java
// Constructors
FileOutputStream(String name)
FileOutputStream(String name, boolean append)
FileOutputStream(File file)
FileOutputStream(File file, boolean append)
FileOutputStream(FileDescriptor fdObj)

// Writing file
FileOutputStream fos = new FileOutputStream("output.txt");
String text = "Hello Java I/O";
fos.write(text.getBytes());
fos.close();

// Append mode
FileOutputStream fos = new FileOutputStream("output.txt", true);
fos.write("\nAppended line".getBytes());
fos.close();
```

### Buffered Byte Streams (Performance)
```java
// BufferedInputStream - wraps InputStream, adds internal buffer (default 8KB)
BufferedInputStream bis = new BufferedInputStream(
    new FileInputStream("large.dat"));

// BufferedOutputStream - wraps OutputStream, adds internal buffer
BufferedOutputStream bos = new BufferedOutputStream(
    new FileOutputStream("copy.dat"));

// Efficient copy
byte[] buffer = new byte[8192];
int bytesRead;
while ((bytesRead = bis.read(buffer)) != -1) {
    bos.write(buffer, 0, bytesRead);
}
bis.close();
bos.close();
```

### DataInputStream / DataOutputStream (Primitive Types)
```java
// Writing primitives - machine-independent format
DataOutputStream dos = new DataOutputStream(
    new FileOutputStream("data.dat"));
dos.writeInt(100);
dos.writeDouble(3.14);
dos.writeUTF("Hello");  // Modified UTF-8
dos.writeBoolean(true);
dos.writeChar('A');
dos.writeLong(123456789L);
dos.close();

// Reading primitives - MUST read in SAME ORDER as written
DataInputStream dis = new DataInputStream(
    new FileInputStream("data.dat"));
int i = dis.readInt();
double d = dis.readDouble();
String s = dis.readUTF();
boolean b = dis.readBoolean();
char c = dis.readChar();
long l = dis.readLong();
dis.close();
```

### PrintStream (Formatted Output)
```java
// System.out is a PrintStream
PrintStream ps = new PrintStream(new FileOutputStream("log.txt"));
ps.println("Line 1");
ps.printf("Value: %d, %.2f%n", 42, 3.14);
ps.print("No newline");
ps.close();
```

### RandomAccessFile (Random Access)
```java
// Mode: "r" (read), "rw" (read/write), "rws" (sync), "rwd" (sync data)
RandomAccessFile raf = new RandomAccessFile("data.dat", "rw");
raf.writeInt(100);
raf.writeUTF("Hello");
raf.seek(0);  // Go back to start
int i = raf.readInt();
String s = raf.readUTF();
raf.close();
```

---

## 11.4 Character Stream Classes

### Reader (Abstract) - Reading Characters

#### Common Methods
```java
int read()                           // Read single char, -1 if EOF
int read(char[] cbuf)                // Read into array
int read(char[] cbuf, int off, int len)
long skip(long n)
void close()
void mark(int readAheadLimit)
void reset()
boolean markSupported()
boolean ready()                      // Ready to read without blocking?
```

### Writer (Abstract) - Writing Characters

#### Common Methods
```java
void write(int c)                      // Write single char
void write(char[] cbuf)                // Write array
void write(char[] cbuf, int off, int len)
void write(String str)                 // Write string
void write(String str, int off, int len)
void flush()
void close()
```

### FileReader / FileWriter
```java
// FileReader - reads characters using default encoding
FileReader fr = new FileReader("text.txt");
int ch;
while ((ch = fr.read()) != -1) {
    System.out.print((char) ch);
}
fr.close();

// FileWriter - writes characters using default encoding
FileWriter fw = new FileWriter("output.txt");
fw.write("Hello Character Streams");
fw.write('\n');
fw.write("Line 2");
fw.close();

// Append mode
FileWriter fw = new FileWriter("output.txt", true);
```

### Buffered Character Streams (Efficient Line Reading)
```java
// BufferedReader - readLine() is KEY for exams!
BufferedReader br = new BufferedReader(
    new FileReader("text.txt"));
String line;
while ((line = br.readLine()) != null) {  // Returns null at EOF
    System.out.println(line);
}
br.close();

// BufferedWriter - newLine() for platform-independent newline
BufferedWriter bw = new BufferedWriter(
    new FileWriter("output.txt"));
bw.write("Line 1");
bw.newLine();  // \n on Unix, \r\n on Windows
bw.write("Line 2");
bw.close();
```

### InputStreamReader / OutputStreamWriter (Encoding Bridge)
```java
// Convert byte stream to character stream with SPECIFIC encoding
InputStreamReader isr = new InputStreamReader(
    new FileInputStream("file.txt"), "UTF-8");  // or "UTF-16", "ISO-8859-1"

OutputStreamWriter osw = new OutputStreamWriter(
    new FileOutputStream("file.txt"), "UTF-8");

// Get encoding name
System.out.println(isr.getEncoding());  // Prints actual encoding used
```

### PrintWriter (Formatted Character Output)
```java
// Preferred for text output over PrintStream
PrintWriter pw = new PrintWriter(new FileWriter("report.txt"));
pw.println("Report");
pw.printf("Total: %,d%n", 1000000);
pw.close();

// Auto-flush constructor
PrintWriter pw = new PrintWriter(new FileWriter("log.txt"), true);
pw.println("Auto-flushed");
```

### Console Class (Java 6+) - Advanced Console I/O
```java
Console console = System.console();  // Returns null if not run from terminal
if (console != null) {
    String name = console.readLine("Enter name: ");
    char[] password = console.readPassword("Password: ");  // No echo!
    console.printf("Hello %s%n", name);
    // Secure: password char[] should be zeroed after use
    java.util.Arrays.fill(password, ' ');
}
```

---

## 11.5 Serialization

### Definition
> **Serialization** is the process of converting an object's state to a byte stream for storage or transmission. **Appeared 5 times in PYQ (2021, 2022, 2023, 2024, 2025).**

### Requirements
- Class must implement `java.io.Serializable` (marker interface - no methods)
- All non-transient instance fields serialized automatically
- `static` fields NOT serialized (class-level)
- `transient` fields NOT serialized
- Referenced objects serialized recursively (entire object graph)
- **Constructor NOT called during deserialization**

### Serializable Interface
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;  // CRITICAL: Version control
    
    int id;
    String name;
    transient double salary;  // NOT serialized - will be 0.0 after deserialization
    static String company = "ABC Corp";  // NOT serialized - class-level
    
    Employee(int id, String name, double salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
}
```

### Serialization (Writing Object)
```java
Employee emp = new Employee(101, "John", 50000);

FileOutputStream fos = new FileOutputStream("emp.ser");
ObjectOutputStream oos = new ObjectOutputStream(fos);

oos.writeObject(emp);  // Serialize entire object graph
oos.flush();  // Ensure data written

oos.close();
fos.close();
```

### Deserialization (Reading Object)
```java
FileInputStream fis = new FileInputStream("emp.ser");
ObjectInputStream ois = new ObjectInputStream(fis);

Employee emp = (Employee) ois.readObject();  // Deserialize - returns Object, must cast

System.out.println("ID: " + emp.id);           // 101
System.out.println("Name: " + emp.name);       // "John"
System.out.println("Salary: " + emp.salary);   // 0.0 (transient)
System.out.println("Company: " + Employee.company);  // "ABC Corp" (static - loaded from class)

ois.close();
fis.close();
```

### Key Points
| Aspect | Detail |
|--------|--------|
| `serialVersionUID` | **MUST declare explicitly.** Mismatched → `InvalidClassException`. Use `serialver` tool or IDE to generate. |
| `transient` | Skip field during serialization. Value becomes default (0, null, false) on deserialization. |
| `static` | Not serialized (class-level). Retains current class value after deserialization. |
| Object graph | Referenced objects also serialized recursively. All must be Serializable. |
| Constructor | **NOT called** during deserialization. Object created via reflection. |
| `writeObject` / `readObject` | Private methods for custom serialization logic (see below). |

### Custom Serialization (writeObject / readObject)
```java
import java.io.*;

public class Account implements Serializable {
    private static final long serialVersionUID = 1L;
    
    String username;
    transient String password;  // Never serialize password!
    transient String encryptedPassword;  // Computed field
    
    // Custom serialization
    private void writeObject(ObjectOutputStream out) throws IOException {
        out.defaultWriteObject();  // Write non-transient fields
        // Encrypt password before writing
        String encrypted = encrypt(password);
        out.writeObject(encrypted);
    }
    
    // Custom deserialization
    private void readObject(ObjectInputStream in) throws IOException, ClassNotFoundException {
        in.defaultReadObject();  // Read non-transient fields
        encryptedPassword = (String) in.readObject();
        // Password remains null - user must re-enter
    }
    
    private String encrypt(String pwd) { /* encryption logic */ return "enc_" + pwd; }
}
```

### Serialization with Inheritance
```java
class Person implements Serializable {
    String name;
    Person(String name) { this.name = name; }
}

class Employee extends Person implements Serializable {
    private static final long serialVersionUID = 1L;
    int id;
    Employee(String name, int id) {
        super(name);
        this.id = id;
    }
}

// Parent class fields serialized automatically if parent implements Serializable
// If parent does NOT implement Serializable:
// - Parent's no-arg constructor called during deserialization
// - Parent fields NOT serialized (must be reinitialized)
```

### Externalizable Interface (Full Custom Control)
```java
import java.io.Externalizable;
import java.io.ObjectInput;
import java.io.ObjectOutput;
import java.io.IOException;

class CustomData implements Externalizable {
    int value;
    String data;
    
    public CustomData() {}  // **No-arg constructor REQUIRED**
    
    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeInt(value * 2);  // Custom logic
        out.writeUTF(data.toUpperCase());
    }
    
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        value = in.readInt() / 2;  // Reverse logic
        data = in.readUTF().toLowerCase();
    }
}
```

| Serializable | Externalizable |
|--------------|----------------|
| Marker interface | Has 2 methods: writeExternal, readExternal |
| Automatic serialization | Manual control |
| Default serialVersionUID | No serialVersionUID needed |
| Constructor not called | No-arg constructor REQUIRED |
| Easier to use | More flexible, faster for complex objects |

---

## 11.6 I/O Exceptions

### Common I/O Exceptions

| Exception | Description |
|-----------|-------------|
| `IOException` | Base class for I/O errors (checked) |
| `FileNotFoundException` | File not found (extends IOException) |
| `EOFException` | Unexpected end of file/stream |
| `InterruptedIOException` | I/O operation interrupted |
| `UnsupportedEncodingException` | Character encoding not supported |
| `ObjectStreamException` | Base for serialization errors |
| `NotSerializableException` | Object doesn't implement Serializable |
| `InvalidClassException` | Class version mismatch (serialVersionUID) |
| `StreamCorruptedException` | Stream control info inconsistent |
| `OptionalDataException` | Primitive data found where object expected |
| `WriteAbortedException` | Exception during write (wraps cause) |

### Exception Handling Pattern
```java
try {
    FileInputStream fis = new FileInputStream("file.txt");
    // ... read file
    fis.close();
} catch (FileNotFoundException e) {
    System.err.println("File not found: " + e.getMessage());
} catch (IOException e) {
    System.err.println("I/O error: " + e.getMessage());
}
```

### Try-with-resources (Java 7+) - **PREFERRED**
```java
// Auto-closes resources implementing AutoCloseable (in reverse order)
try (FileInputStream fis = new FileInputStream("file.txt");
     BufferedInputStream bis = new BufferedInputStream(fis);
     FileOutputStream fos = new FileOutputStream("copy.txt");
     BufferedOutputStream bos = new BufferedOutputStream(fos)) {
    
    byte[] buffer = new byte[8192];
    int bytesRead;
    while ((bytesRead = bis.read(buffer)) != -1) {
        bos.write(buffer, 0, bytesRead);
    }
} catch (IOException e) {
    e.printStackTrace();
}
// No finally needed - auto-closed even if exception occurs!
```

### Multi-catch (Java 7+)
```java
try {
    // ...
} catch (FileNotFoundException | UnsupportedEncodingException e) {
    System.err.println("File/Encoding error: " + e.getMessage());
} catch (IOException e) {
    System.err.println("I/O error: " + e.getMessage());
}
```

---

## 11.7 Closeable, Flushable, AutoCloseable

### Interfaces - **IMPORTANT: Appeared in 2023 Q2(a) and 2026 Q5(c) as short notes**

| Interface | Package | Method | Purpose | Since |
|-----------|---------|--------|---------|-------|
| `Closeable` | java.io | `void close()` | Release resources, idempotent | Java 1.5 |
| `Flushable` | java.io | `void flush()` | Flush buffers to destination | Java 1.5 |
| `AutoCloseable` | java.lang | `void close()` | Auto-close in try-with-resources | Java 1.7 |

### Hierarchy
```
AutoCloseable (java.lang, Java 7+)
    │
    ├─ Closeable (java.io)          ← extends AutoCloseable
    │     │
    │     ├─ InputStream
    │     ├─ OutputStream
    │     ├─ Reader
    │     └─ Writer
    │
    └─ Flushable (java.io)
          │
          ├─ OutputStream
          └─ Writer
```

### Key Differences
```java
// Closeable.close() - throws IOException
// AutoCloseable.close() - throws Exception (broader)
// Flushable.flush() - throws IOException

// try-with-resources works with AutoCloseable (broader than Closeable)
// All stream classes implement Closeable → AutoCloseable
// OutputStream/Writer implement Flushable

// Best practice: Implement AutoCloseable for custom resources
class MyResource implements AutoCloseable {
    public void close() throws Exception {  // Can throw Exception
        // cleanup
    }
}
```

---

## 11.8 NIO.2 (java.nio.file) - Modern File I/O (Java 7+)
**Brief overview - exam may ask comparison with File class**

```java
import java.nio.file.*;
import java.nio.file.attribute.*;
import java.io.IOException;

// Path - immutable, thread-safe
Path path = Paths.get("src/main/java/File.java");

// Files utility class - static methods
Files.exists(path);
Files.isRegularFile(path);
Files.isDirectory(path);
Files.size(path);  // long
Files.readAllLines(path);  // List<String>
Files.readAllBytes(path);  // byte[]
Files.write(path, "content".getBytes());
Files.write(path, lines, StandardOpenOption.APPEND);
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.move(source, target);
Files.delete(path);
Files.deleteIfExists(path);
Files.createDirectory(path);
Files.createDirectories(path);
Files.createTempFile("prefix", ".suffix");
Files.walk(path)  // Stream<Path> - lazy, efficient
    .filter(p -> p.toString().endsWith(".java"))
    .forEach(System.out::println);

// BasicFileAttributes
BasicFileAttributes attrs = Files.readAttributes(path, BasicFileAttributes.class);
attrs.creationTime();
attrs.lastModifiedTime();
attrs.size();
attrs.isDirectory();
```

---

## 11.9 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. Difference between Byte Streams and Character Streams.
2. What is File class? Common methods (createNewFile, mkdir, list, delete, renameTo).
3. What is serialization? Serializable interface.
4. Difference between `close()`, `flush()`, `finalize()`.
5. What is `transient` keyword?
6. Difference between `FileInputStream` and `FileReader`.
7. What is try-with-resources?
8. Difference between `BufferedInputStream` and `BufferedReader`.
9. **Difference between `Closeable`, `Flushable`, `AutoCloseable`** (2023, 2026).
10. **What is `serialVersionUID`?** Why is it important?
11. **Difference between `Serializable` and `Externalizable`.**

**5-Mark Questions:**
1. Explain Java I/O stream hierarchy with diagram.
2. Explain File class with methods and example.
3. Explain Byte Streams vs Character Streams (table + when to use each).
4. Explain serialization with example program (transient, static, serialVersionUID).
5. Explain Buffered Streams and their advantage (performance).
6. Write program: File copy using byte streams (with buffer).
7. Write program: Read file line by line using BufferedReader.
8. Explain `DataInputStream` and `DataOutputStream` with example.
9. **Explain `AutoCloseable`, `Closeable`, `Flushable` interfaces** (2023 Q2(a), 2026 Q5(c)).
10. **Explain `RandomAccessFile` and its use cases.**

**10-Mark Questions:**
1. **Explain I/O Streams: Byte vs Character, File class, Buffered streams, Serialization, try-with-resources.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Serialization and deserialization with transient, static, serialVersionUID, custom writeObject/readObject.
3. File class operations: create, delete, list, rename, mkdir, permissions.
4. **Stream classes hierarchy + Byte vs Character streams with examples** (2023 Q2(b), 2025 Q4(b), 2026 Q1(e)).

### Programs to Practice
1. ✅ **File operations (create, delete, list, mkdir)** - appeared 2021, 2022, 2024
2. ✅ **File copy (byte streams with buffer)** - appeared 2023, 2025
3. ✅ **Read file line by line (BufferedReader)** - appeared 2022, 2023, 2024
4. ✅ **Serialization/Deserialization with transient/static** - appeared 2021, 2022, 2024, 2025
5. ✅ **Object serialization steps explanation** - appeared 2021, 2022, 2024, 2025
6. ✅ **DataInputStream/DataOutputStream demo** - appeared 2022, 2025
7. ✅ **Custom serialization (writeObject/readObject)** - potential 10-marker

---

## 11.10 Summary of Unit 11

| Topic | Key Points |
|-------|------------|
| **Streams** | Sequence of data; Input (read) / Output (write); abstraction over devices |
| **Byte Streams** | InputStream/OutputStream; binary data; FileInputStream, BufferedInputStream, DataInputStream |
| **Character Streams** | Reader/Writer; text (Unicode); FileReader, BufferedReader (readLine!), InputStreamReader |
| **File Class** | Path representation; create, delete, list, rename, mkdir; NO streams |
| **Buffered Streams** | Performance boost (8KB buffer); BufferedInputStream, BufferedReader (readLine!) |
| **Data Streams** | DataInputStream/DataOutputStream; primitive types in portable format |
| **Print Streams** | PrintStream/PrintWriter; formatted output (print, println, printf) |
| **Serialization** | Object → byte stream; implements Serializable; ObjectOutputStream/ObjectInputStream |
| **transient** | Skip field in serialization; default value on deserialize |
| **static** | Not serialized (class-level); current class value used after deserialize |
| **serialVersionUID** | **MUST declare**; version control; mismatch → InvalidClassException |
| **Custom Serialization** | Private writeObject/readObject; call defaultWriteObject/defaultReadObject first |
| **Externalizable** | Full control; writeExternal/readExternal; no-arg constructor REQUIRED |
| **Try-with-resources** | Auto-close AutoCloseable resources (Java 7+); reverse order; suppresses exceptions |
| **AutoCloseable/Closeable/Flushable** | Closeable extends AutoCloseable; Flushable separate; all streams implement |
| **Exceptions** | IOException hierarchy; FileNotFoundException, EOFException, NotSerializableException |
| **RandomAccessFile** | Random access via seek(); "rw" mode; not a stream |
| **NIO.2 (Paths/Files)** | Modern API (Java 7+); Path immutable; Files utility; Stream<Path> for walking |

---

## 11.11 Quick Reference: Stream Selection

```java
// Binary files (images, PDF, etc.) - Byte Streams
FileInputStream / FileOutputStream
BufferedInputStream / BufferedOutputStream  (USE BUFFER!)
DataInputStream / DataOutputStream          (primitives)
ObjectOutputStream / ObjectInputStream      (objects)
RandomAccessFile                            (random access)

// Text files - Character Streams
FileReader / FileWriter
BufferedReader / BufferedWriter             (USE readLine()/newLine()!)
PrintWriter                                 (formatted output)
InputStreamReader / OutputStreamWriter      (SPECIFY ENCODING: "UTF-8")

// Console Input
BufferedReader br = new BufferedReader(new InputStreamReader(System.in))
String line = br.readLine()

// Console (advanced, Java 6+)
Console c = System.console()
String pwd = new String(c.readPassword("Password: "))

// Encoding specific
new InputStreamReader(byteStream, "UTF-8")
new OutputStreamWriter(byteStream, "UTF-8")

// Modern NIO.2 (Java 7+)
Path path = Paths.get("file.txt");
Files.readAllLines(path);
Files.write(path, bytes);
Files.walk(root).filter(...).forEach(...)
```

---

## 11.12 PYQ-Focused Quick Answers (Memorize These)

### Q: Difference between Byte Stream and Character Stream (2-5 marks)
**Answer:**
| Aspect | Byte Stream | Character Stream |
|--------|-------------|------------------|
| Base Classes | InputStream, OutputStream | Reader, Writer |
| Data Unit | 8-bit bytes | 16-bit Unicode chars |
| Use Case | Binary data (images, audio) | Text files (XML, JSON, .txt) |
| Encoding | No conversion | Handles char encoding |
| Key Classes | FileInputStream, BufferedInputStream | FileReader, BufferedReader |
| Performance | Faster for binary | Better for text |

### Q: Difference between BufferedInputStream and BufferedReader (2 marks)
- **BufferedInputStream**: Byte stream, reads bytes, `read()` returns int (byte), good for binary
- **BufferedReader**: Character stream, reads chars, `readLine()` returns String, good for text lines

### Q: What is transient? (2 marks)
- Keyword to exclude field from serialization
- Field gets default value (0, null, false) after deserialization
- Use for sensitive data (passwords), derived fields, non-serializable objects

### Q: What is serialVersionUID? (2 marks)
- Unique version identifier for Serializable classes
- Used during deserialization to verify class compatibility
- Mismatch → `InvalidClassException`
- **Always declare explicitly** to avoid JVM-generated UID changes

### Q: Difference between Serializable and Externalizable (5 marks)
| Feature | Serializable | Externalizable |
|---------|-------------|----------------|
| Interface | Marker (no methods) | Has writeExternal, readExternal |
| Control | Automatic | Manual (full control) |
| Constructor | Not called | No-arg REQUIRED |
| serialVersionUID | Needed | Not needed |
| Performance | Slower (reflection) | Faster (direct) |
| Use Case | Simple objects | Complex/custom format |

### Q: Explain try-with-resources (5 marks)
- Java 7+ feature for automatic resource management
- Works with `AutoCloseable` (broader than `Closeable`)
- Resources declared in `try()` parentheses
- Closed automatically in reverse order, even if exception thrown
- Suppressed exceptions accessible via `getSuppressed()`
- Eliminates need for `finally` block

### Q: Closeable vs Flushable vs AutoCloseable (5 marks - 2023, 2026)
- **AutoCloseable** (java.lang): Root interface, `close()` throws `Exception`, used by try-with-resources
- **Closeable** (java.io): Extends AutoCloseable, `close()` throws `IOException`, for streams
- **Flushable** (java.io): `flush()` throws `IOException`, for output streams/writers
- Hierarchy: `OutputStream/Writer` → implement both `Closeable` & `Flushable`
- `InputStream/Reader` → implement `Closeable` only

### Q: Steps to Serialize/Deserialize an Object (5 marks)
**Serialize:**
1. Class implements `Serializable`
2. Declare `serialVersionUID`
3. Create `FileOutputStream`
4. Wrap in `ObjectOutputStream`
5. Call `writeObject(obj)`
6. Close streams (try-with-resources)

**Deserialize:**
1. Create `FileInputStream`
2. Wrap in `ObjectInputStream`
3. Call `readObject()` and cast
4. Close streams
5. `transient` fields = defaults, `static` = current class value

### Q: File class important methods (5 marks)
- **Path**: getName(), getPath(), getAbsolutePath(), getCanonicalPath(), getParent()
- **Status**: exists(), canRead(), canWrite(), canExecute(), isFile(), isDirectory(), isHidden()
- **Info**: length(), lastModified()
- **Directory**: list(), listFiles(), list(FilenameFilter), mkdir(), mkdirs()
- **Modification**: createNewFile(), delete(), renameTo(), setReadable(), setWritable()

### Q: Buffered Streams Advantage (2-5 marks)
- Reduces native I/O calls by using internal buffer (default 8KB)
- Reads/writes large chunks from/to disk instead of byte-by-byte
- **Massive performance improvement** for large files
- BufferedReader adds `readLine()` for convenient line reading
- BufferedWriter adds `newLine()` for platform-independent newlines