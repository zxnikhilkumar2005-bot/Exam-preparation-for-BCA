# Unit 11: I/O Streams

## Unit Overview
This unit covers Java I/O hierarchy, File class, stream classes (Byte and Character streams), serialization, and I/O exceptions.

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
                         ┌────┴────┐   ┌────┴────┐
                         ▼         ▼   ▼         ▼
                    Buffered   Data    Buffered  Data
                    Input      Input   Output    Output
                    
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
                         ┌────┴────┐   ┌────┴────┐
                         ▼         ▼   ▼         ▼
                    Buffered   Print   Buffered  Print
                    Reader     Writer  Writer    Writer
```

### Stream Types

| Category | Base Classes | Data Type | Use Case |
|----------|-------------|-----------|----------|
| **Byte Streams** | InputStream, OutputStream | Binary (bytes) | Images, audio, video, raw data |
| **Character Streams** | Reader, Writer | Text (Unicode chars) | Text files, XML, JSON |

---

## 11.2 File Class

### Purpose
Represents file/directory pathnames. Does NOT use streams.

### Constructors
```java
File(String pathname)                    // "path/to/file.txt"
File(String parent, String child)        // "path", "file.txt"
File(File parent, String child)          // File object, "file.txt"
```

### Important Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `getName()` | String | File/directory name |
| `getPath()` | String | Path as string |
| `getAbsolutePath()` | String | Absolute path |
| `exists()` | boolean | True if exists |
| `canRead()` | boolean | True if readable |
| `canWrite()` | boolean | True if writable |
| `isFile()` | boolean | True if file |
| `isDirectory()` | boolean | True if directory |
| `length()` | long | File size in bytes |
| `list()` | String[] | Names of files in directory |
| `listFiles()` | File[] | File objects in directory |
| `mkdir()` | boolean | Create directory |
| `mkdirs()` | boolean | Create parent dirs too |
| `createNewFile()` | boolean | Create new file |
| `delete()` | boolean | Delete file/directory |
| `renameTo(File dest)` | boolean | Rename/move |

### Example
```java
import java.io.File;

public class FileDemo {
    public static void main(String[] args) {
        File f = new File("test.txt");
        
        System.out.println("Name: " + f.getName());
        System.out.println("Path: " + f.getPath());
        System.out.println("Absolute: " + f.getAbsolutePath());
        System.out.println("Exists: " + f.exists());
        System.out.println("Size: " + f.length() + " bytes");
        System.out.println("Is File: " + f.isFile());
        System.out.println("Is Dir: " + f.isDirectory());
        
        // List directory
        File dir = new File(".");
        String[] files = dir.list();
        for (String name : files) {
            System.out.println(name);
        }
    }
}
```

---

## 11.3 Byte Stream Classes

### InputStream (Abstract) - Reading Bytes

#### Common Methods
```java
int read()                    // Read single byte, -1 if EOF
int read(byte[] b)            // Read into array
int read(byte[] b, int off, int len)  // Read into subarray
long skip(long n)             // Skip bytes
int available()               // Bytes available without blocking
void close()                  // Close stream
void mark(int readlimit)      // Mark position
void reset()                  // Reset to mark
boolean markSupported()       // Supports mark/reset?
```

### OutputStream (Abstract) - Writing Bytes

#### Common Methods
```java
void write(int b)                      // Write single byte
void write(byte[] b)                   // Write array
void write(byte[] b, int off, int len) // Write subarray
void flush()                           // Flush buffer
void close()                           // Close stream
```

### FileInputStream
```java
// Reading file
FileInputStream fis = new FileInputStream("input.txt");
int data;
while ((data = fis.read()) != -1) {
    System.out.print((char) data);
}
fis.close();

// Better: read into buffer
byte[] buffer = new byte[1024];
int bytesRead;
while ((bytesRead = fis.read(buffer)) != -1) {
    System.out.write(buffer, 0, bytesRead);
}
```

### FileOutputStream
```java
// Writing file
FileOutputStream fos = new FileOutputStream("output.txt");
String text = "Hello Java I/O";
fos.write(text.getBytes());
fos.close();

// Append mode
FileOutputStream fos = new FileOutputStream("output.txt", true);
```

### Buffered Byte Streams (Performance)
```java
// BufferedInputStream
BufferedInputStream bis = new BufferedInputStream(
    new FileInputStream("large.dat"));

// BufferedOutputStream
BufferedOutputStream bos = new BufferedOutputStream(
    new FileOutputStream("copy.dat"));

int data;
while ((data = bis.read()) != -1) {
    bos.write(data);
}
bis.close();
bos.close();
```

### DataInputStream / DataOutputStream (Primitive Types)
```java
// Writing primitives
DataOutputStream dos = new DataOutputStream(
    new FileOutputStream("data.dat"));
dos.writeInt(100);
dos.writeDouble(3.14);
dos.writeUTF("Hello");
dos.close();

// Reading primitives
DataInputStream dis = new DataInputStream(
    new FileInputStream("data.dat"));
int i = dis.readInt();
double d = dis.readDouble();
String s = dis.readUTF();
dis.close();
```

---

## 11.4 Character Stream Classes

### Reader (Abstract) - Reading Characters

#### Common Methods
```java
int read()                     // Read single char, -1 if EOF
int read(char[] cbuf)          // Read into array
int read(char[] cbuf, int off, int len)
long skip(long n)
void close()
void mark(int readAheadLimit)
void reset()
boolean markSupported()
boolean ready()                // Ready to read?
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

### FileReader
```java
FileReader fr = new FileReader("text.txt");
int ch;
while ((ch = fr.read()) != -1) {
    System.out.print((char) ch);
}
fr.close();
```

### FileWriter
```java
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
// BufferedReader - readLine() is key!
BufferedReader br = new BufferedReader(
    new FileReader("text.txt"));
String line;
while ((line = br.readLine()) != null) {
    System.out.println(line);
}
br.close();

// BufferedWriter
BufferedWriter bw = new BufferedWriter(
    new FileWriter("output.txt"));
bw.write("Line 1");
bw.newLine();  // Platform-independent newline
bw.write("Line 2");
bw.close();
```

### InputStreamReader / OutputStreamWriter (Encoding Bridge)
```java
// Convert byte stream to character stream with encoding
InputStreamReader isr = new InputStreamReader(
    new FileInputStream("file.txt"), "UTF-8");

OutputStreamWriter osw = new OutputStreamWriter(
    new FileOutputStream("file.txt"), "UTF-8");
```

### Console Input (System.in)
```java
// Reading from keyboard
BufferedReader br = new BufferedReader(
    new InputStreamReader(System.in));
System.out.print("Enter name: ");
String name = br.readLine();  // Reads full line
```

---

## 11.5 Serialization

### Definition
> **Serialization** is the process of converting an object's state to a byte stream for storage or transmission.

### Requirements
- Class must implement `java.io.Serializable` (marker interface)
- All non-transient fields serialized
- `static` and `transient` fields NOT serialized

### Serializable Interface
```java
import java.io.Serializable;

public class Employee implements Serializable {
    private static final long serialVersionUID = 1L;  // Recommended
    
    int id;
    String name;
    transient double salary;  // NOT serialized
    static String company = "ABC Corp";  // NOT serialized
    
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

oos.writeObject(emp);  // Serialize

oos.close();
fos.close();
```

### Deserialization (Reading Object)
```java
FileInputStream fis = new FileInputStream("emp.ser");
ObjectInputStream ois = new ObjectInputStream(fis);

Employee emp = (Employee) ois.readObject();  // Deserialize

System.out.println("ID: " + emp.id);
System.out.println("Name: " + emp.name);
System.out.println("Salary: " + emp.salary);  // 0.0 (transient)
System.out.println("Company: " + Employee.company);  // "ABC Corp" (static)

ois.close();
fis.close();
```

### Key Points
| Aspect | Detail |
|--------|--------|
| `serialVersionUID` | Version control; mismatched → `InvalidClassException` |
| `transient` | Skip field during serialization |
| `static` | Not serialized (class-level) |
| Object graph | Referenced objects also serialized recursively |
| Constructor | NOT called during deserialization |

### Externalizable Interface (Custom Serialization)
```java
import java.io.Externalizable;
import java.io.ObjectInput;
import java.io.ObjectOutput;
import java.io.IOException;

class CustomData implements Externalizable {
    int value;
    
    public CustomData() {}  // No-arg constructor REQUIRED
    
    @Override
    public void writeExternal(ObjectOutput out) throws IOException {
        out.writeInt(value * 2);  // Custom logic
    }
    
    @Override
    public void readExternal(ObjectInput in) throws IOException, ClassNotFoundException {
        value = in.readInt() / 2;  // Reverse logic
    }
}
```

---

## 11.6 I/O Exceptions

### Common I/O Exceptions

| Exception | Description |
|-----------|-------------|
| `IOException` | Base class for I/O errors |
| `FileNotFoundException` | File not found (extends IOException) |
| `EOFException` | Unexpected end of file/stream |
| `InterruptedIOException` | I/O operation interrupted |
| `UnsupportedEncodingException` | Character encoding not supported |
| `ObjectStreamException` | Serialization errors |
| `NotSerializableException` | Object doesn't implement Serializable |
| `InvalidClassException` | Class version mismatch |
| `StreamCorruptedException` | Stream control info inconsistent |

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

### Try-with-resources (Java 7+)
```java
// Auto-closes resources implementing AutoCloseable
try (FileInputStream fis = new FileInputStream("file.txt");
     BufferedInputStream bis = new BufferedInputStream(fis)) {
    
    int data;
    while ((data = bis.read()) != -1) {
        System.out.print((char) data);
    }
} catch (IOException e) {
    e.printStackTrace();
}
// No finally needed - auto-closed!
```

---

## 11.7 Closeable, Flushable, AutoCloseable

### Interfaces
| Interface | Method | Purpose |
|-----------|--------|---------|
| `Closeable` | `void close()` | Release resources |
| `Flushable` | `void flush()` | Flush buffers to destination |
| `AutoCloseable` | `void close()` | Auto-close in try-with-resources |

### Hierarchy
```
AutoCloseable (Java 7+)
    │
    ├─ Closeable
    │     │
    │     ├─ InputStream
    │     ├─ OutputStream
    │     ├─ Reader
    │     └─ Writer
    │
    └─ Flushable
          │
          ├─ OutputStream
          └─ Writer
```

---

## 11.8 Important Exam Questions (from PYQ Analysis)

### High Priority (Frequently Asked)

**2-Mark Questions:**
1. Difference between Byte Streams and Character Streams.
2. What is File class? Common methods.
3. What is serialization? Serializable interface.
4. Difference between `close()`, `flush()`, `finalize()`.
5. What is `transient` keyword?
6. Difference between `FileInputStream` and `FileReader`.
7. What is try-with-resources?
8. Difference between `BufferedInputStream` and `BufferedReader`.

**5-Mark Questions:**
1. Explain Java I/O stream hierarchy with diagram.
2. Explain File class with methods and example.
3. Explain Byte Streams vs Character Streams.
4. Explain serialization with example program.
5. Explain Buffered Streams and their advantage.
6. Write program: File copy using byte streams.
7. Write program: Read file line by line using BufferedReader.
8. Explain `DataInputStream` and `DataOutputStream`.

**10-Mark Questions:**
1. **Explain I/O Streams: Byte vs Character, File class, Buffered streams, Serialization, try-with-resources.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Serialization and deserialization with transient, static, serialVersionUID.
3. File class operations: create, delete, list, rename.

### Programs to Practice
1. ✅ **File operations (create, delete, list)** - appeared 2021, 2022, 2024
2. ✅ **File copy (byte streams)** - appeared 2023, 2025
3. ✅ **Read file line by line (BufferedReader)** - appeared 2022, 2023, 2024
4. ✅ **Serialization/Deserialization** - appeared 2021, 2022, 2024, 2025
5. ✅ **Object serialization steps** - appeared 2021, 2022, 2024, 2025

---

## 11.9 Summary of Unit 11

| Topic | Key Points |
|-------|------------|
| **Streams** | Sequence of data; Input (read) / Output (write) |
| **Byte Streams** | InputStream/OutputStream; binary data; FileInputStream, BufferedInputStream |
| **Character Streams** | Reader/Writer; text data; FileReader, BufferedReader |
| **File Class** | Path representation; create, delete, list, rename; no streams |
| **Buffered Streams** | Performance boost; BufferedInputStream, BufferedReader (readLine!) |
| **Data Streams** | DataInputStream/DataOutputStream; primitive types |
| **Serialization** | Object → byte stream; implements Serializable; ObjectOutputStream/ObjectInputStream |
| **transient** | Skip field in serialization |
| **serialVersionUID** | Version control for serialization |
| **Try-with-resources** | Auto-close AutoCloseable resources (Java 7+) |
| **Exceptions** | IOException hierarchy; FileNotFoundException, EOFException |

---

## 11.10 Quick Reference: Stream Selection

```java
// Binary files (images, PDF, etc.)
FileInputStream / FileOutputStream
BufferedInputStream / BufferedOutputStream

// Text files
FileReader / FileWriter
BufferedReader / BufferedWriter  (USE readLine()!)

// Primitive types to/from file
DataInputStream / DataOutputStream

// Object serialization
ObjectOutputStream.writeObject(obj)
ObjectInputStream.readObject()

// Console input
BufferedReader br = new BufferedReader(new InputStreamReader(System.in))
String line = br.readLine()

// Encoding specific
new InputStreamReader(byteStream, "UTF-8")
new OutputStreamWriter(byteStream, "UTF-8")
```