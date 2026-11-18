# Unit 12: Java API / Collections

## Unit Overview
This unit covers the Collections Framework hierarchy, Date class, Set interface (HashSet, TreeSet, LinkedHashSet), Map interface (HashMap, TreeMap, Hashtable), List interface (ArrayList, LinkedList, Vector), and Stack class.

---

## 12.1 Collections Framework Overview

### Definition
> The **Collections Framework** is a unified architecture for representing and manipulating collections of objects. It provides interfaces, implementations, and algorithms.

### Benefits
- ✅ Reduces programming effort (ready-to-use data structures)
- ✅ Increases performance (optimized implementations)
- ✅ Interoperability (standard interfaces)
- ✅ Easy to learn/use (consistent API)

### Core Interfaces (java.util)

```
                    Iterable
                       │
                    Collection
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
       List           Set           Queue
        │              │              │
  ┌─────┴─────┐  ┌────┴────┐  ┌──────┴──────┐
  ▼           ▼  ▼         ▼  ▼             ▼
ArrayList  Vector  HashSet  TreeSet  PriorityQueue
LinkedList          LinkedHashSet          ArrayDeque
```

```
Map (Interface)
    │
    ├──────────────────┐
    ▼                  ▼
HashMap             TreeMap
    │
    ▼
Hashtable (legacy)
```

---

## 12.2 Collection Interface Methods

| Method | Description |
|--------|-------------|
| `boolean add(E e)` | Add element |
| `boolean addAll(Collection<? extends E> c)` | Add all |
| `boolean remove(Object o)` | Remove element |
| `boolean removeAll(Collection<?> c)` | Remove all in collection |
| `boolean retainAll(Collection<?> c)` | Keep only elements in collection |
| `void clear()` | Remove all elements |
| `boolean contains(Object o)` | Check if contains |
| `boolean containsAll(Collection<?> c)` | Check if contains all |
| `int size()` | Number of elements |
| `boolean isEmpty()` | Check if empty |
| `Iterator<E> iterator()` | Get iterator |
| `Object[] toArray()` | Convert to array |
| `<T> T[] toArray(T[] a)` | Convert to typed array |

---

## 12.3 Iterator Interface

### Methods
```java
boolean hasNext()        // More elements?
E next()                 // Next element
void remove()            // Remove last returned (optional)
default void forEachRemaining(Consumer<? super E> action)  // Java 8+
```

### Usage Pattern
```java
Collection<String> coll = new ArrayList<>();
coll.add("A"); coll.add("B"); coll.add("C");

Iterator<String> it = coll.iterator();
while (it.hasNext()) {
    String s = it.next();
    System.out.println(s);
    // it.remove();  // Safe removal during iteration
}
```

### Enhanced For Loop (Uses Iterator internally)
```java
for (String s : coll) {
    System.out.println(s);
}
```

---

## 12.4 List Interface

### Characteristics
- **Ordered**: Elements have position (index)
- **Allows duplicates**
- **Indexed access**: get(index), set(index, element)

### Implementations

| Class | Description | Best For |
|-------|-------------|----------|
| `ArrayList` | Dynamic array; fast random access | Frequent reads, infrequent inserts |
| `LinkedList` | Doubly linked list; fast inserts/deletes | Frequent inserts/deletes at ends |
| `Vector` | Synchronized ArrayList (legacy) | Thread-safe (use Collections.synchronizedList) |

### Common List Methods
```java
void add(int index, E element)        // Insert at index
boolean addAll(int index, Collection<? extends E> c)
E get(int index)                      // Get by index
E set(int index, E element)           // Replace at index
int indexOf(Object o)                 // First occurrence
int lastIndexOf(Object o)             // Last occurrence
ListIterator<E> listIterator()        // Bidirectional iterator
ListIterator<E> listIterator(int index)
E remove(int index)                   // Remove by index
List<E> subList(int from, int to)     // View [from, to)
```

### ArrayList Example
```java
List<String> list = new ArrayList<>();
list.add("A");           // [A]
list.add("B");           // [A, B]
list.add(1, "C");        // [A, C, B]
list.get(1);             // "C"
list.set(1, "D");        // [A, D, B]
list.remove(1);          // [A, B]
list.size();             // 2
```

### Vector (Legacy)
```java
Vector<String> v = new Vector<>();
v.addElement("A");       // Legacy method
v.insertElementAt("B", 0);
v.capacity();            // Current capacity
v.ensureCapacity(50);    // Increase capacity
```

---

## 12.5 Stack Class

### Characteristics
- Extends `Vector`
- **LIFO** (Last In, First Out)
- Synchronized (thread-safe)

### Methods
```java
E push(E item)           // Push onto stack
E pop()                  // Remove and return top
E peek()                 // Return top without removing
boolean empty()          // Check if empty
int search(Object o)     // 1-based position from top
```

### Example
```java
Stack<Integer> stack = new Stack<>();
stack.push(10);
stack.push(20);
stack.push(30);

System.out.println(stack.peek());    // 30
System.out.println(stack.pop());     // 30
System.out.println(stack.pop());     // 20
System.out.println(stack.search(10)); // 1 (1-based from top)
```

---

## 12.6 Set Interface

### Characteristics
- **No duplicates** (uses equals())
- **Unordered** (except SortedSet implementations)
- **At most one null**

### Implementations

| Class | Ordering | Null Allowed | Performance |
|-------|----------|--------------|-------------|
| `HashSet` | No guarantee | Yes (one) | O(1) - fastest |
| `LinkedHashSet` | Insertion order | Yes (one) | O(1) |
| `TreeSet` | Sorted (natural/comparator) | No | O(log n) |

### HashSet
```java
Set<String> set = new HashSet<>();
set.add("A");
set.add("B");
set.add("A");  // Duplicate ignored
set.add(null); // Allowed once

// Internally uses HashMap
// Iteration order unpredictable
```

### LinkedHashSet
```java
Set<String> set = new LinkedHashSet<>();
set.add("C");
set.add("A");
set.add("B");
// Iteration: C, A, B (insertion order preserved)
```

### TreeSet (SortedSet)
```java
Set<Integer> set = new TreeSet<>();
set.add(50);
set.add(10);
set.add(30);
// Iteration: 10, 30, 50 (sorted)

Set<String> set2 = new TreeSet<>(Comparator.reverseOrder());
set2.add("A"); set2.add("C"); set2.add("B");
// Iteration: C, B, A (custom order)
```

### TreeSet Methods
```java
E first()                    // Lowest element
E last()                     // Highest element
E lower(E e)                 // Strictly less than
E higher(E e)                // Strictly greater than
E floor(E e)                 // Less than or equal
E ceiling(E e)               // Greater than or equal
E pollFirst()                // Remove and return first
E pollLast()                 // Remove and return last
NavigableSet<E> descendingSet()  // Reverse order view
Iterator<E> descendingIterator()
```

---

## 12.7 Map Interface

### Characteristics
- **Key-Value pairs**
- **Unique keys** (no duplicate keys)
- **Values can be duplicated**
- **Not a Collection** (doesn't extend Collection)

### Implementations

| Class | Ordering | Null Keys | Null Values | Thread-Safe |
|-------|----------|-----------|-------------|-------------|
| `HashMap` | No guarantee | Yes (one) | Yes | No |
| `LinkedHashMap` | Insertion order | Yes | Yes | No |
| `TreeMap` | Sorted by key | No | Yes | No |
| `Hashtable` | No guarantee | No | No | Yes (legacy) |
| `ConcurrentHashMap` | No guarantee | No | No | Yes (modern) |

### Common Map Methods
```java
V put(K key, V value)              // Add/replace
V get(Object key)                  // Get by key
V remove(Object key)               // Remove by key
boolean containsKey(Object key)    // Check key
boolean containsValue(Object value) // Check value
int size()                         // Number of entries
boolean isEmpty()
void clear()
Set<K> keySet()                    // View of keys
Collection<V> values()             // View of values
Set<Map.Entry<K,V>> entrySet()     // View of key-value pairs
V getOrDefault(K key, V default)   // Java 8+
V putIfAbsent(K key, V value)      // Java 8+
void forEach(BiConsumer<? super K,? super V> action)  // Java 8+
```

### HashMap Example
```java
Map<Integer, String> map = new HashMap<>();
map.put(1, "Alice");
map.put(2, "Bob");
map.put(3, "Charlie");

String name = map.get(2);          // "Bob"
map.remove(1);                     // Remove key 1

// Iteration
for (Map.Entry<Integer, String> entry : map.entrySet()) {
    System.out.println(entry.getKey() + " -> " + entry.getValue());
}

// Java 8+
map.forEach((k, v) -> System.out.println(k + " -> " + v));
```

### TreeMap (SortedMap)
```java
Map<String, Integer> map = new TreeMap<>();
map.put("Zebra", 3);
map.put("Apple", 1);
map.put("Banana", 2);
// Iteration: Apple=1, Banana=2, Zebra=3 (sorted by key)

Map<String, Integer> desc = new TreeMap<>(Comparator.reverseOrder());
// Iteration: Zebra=3, Banana=2, Apple=1
```

---

## 12.8 HashMap vs Hashtable

| Aspect | HashMap | Hashtable |
|--------|---------|-----------|
| **Synchronization** | No | Yes (all methods) |
| **Null Keys** | Allowed (one) | Not allowed |
| **Null Values** | Allowed | Not allowed |
| **Iteration** | Fail-fast iterator | Enumerator (not fail-fast) |
| **Performance** | Faster | Slower (sync overhead) |
| **Legacy** | Java 2+ | Java 1.0 |

> Use `ConcurrentHashMap` for thread-safe Map in modern Java.

---

## 12.9 Date Class (java.util.Date)

### Constructors
```java
Date()                          // Current date/time
Date(long millis)               // Milliseconds since Jan 1, 1970
```

### Important Methods
```java
boolean after(Date when)        // This after when?
boolean before(Date when)       // This before when?
int compareTo(Date anotherDate) // Compare: 0=equal, <0=before, >0=after
Object clone()                  // Copy
boolean equals(Object obj)      // Compare
long getTime()                  // Milliseconds since epoch
void setTime(long time)         // Set time
String toString()               // String representation
```

### Deprecated Methods (Avoid)
```java
getYear(), getMonth(), getDate(), getHours(), getMinutes(), getSeconds()
// Use Calendar or java.time (Java 8+) instead
```

### Example
```java
import java.util.Date;
import java.text.SimpleDateFormat;

public class DateDemo {
    public static void main(String[] args) {
        Date now = new Date();
        System.out.println("Current: " + now);
        System.out.println("Millis: " + now.getTime());
        
        Date d1 = new Date(1599117817589L);
        System.out.println("Date: " + d1);
        
        int cmp = now.compareTo(d1);
        if (cmp > 0) System.out.println("Now is later");
        else if (cmp < 0) System.out.println("Now is earlier");
        else System.out.println("Same time");
        
        // Formatting
        SimpleDateFormat sdf = new SimpleDateFormat("E yyyy.MM.dd 'at' hh:mm:ss a zzz");
        System.out.println("Formatted: " + sdf.format(now));
    }
}
```

### SimpleDateFormat Patterns
| Pattern | Description | Example |
|---------|-------------|---------|
| `yyyy` | Year (4 digits) | 2024 |
| `MM` | Month (01-12) | 07 |
| `dd` | Day of month | 15 |
| `HH` | Hour (0-23) | 14 |
| `hh` | Hour (1-12) | 02 |
| `mm` | Minutes | 30 |
| `ss` | Seconds | 45 |
| `a` | AM/PM | PM |
| `E` | Day name | Tue |
| `zzz` | Time zone | IST |

---

## 12.10 Important Exam Questions (from PYQ Analysis)

### High Priority

**2-Mark Questions:**
1. Difference between ArrayList and Vector.
2. Difference between HashSet and TreeSet.
3. Difference between HashMap and Hashtable.
4. Difference between List and Set.
5. Difference between Set and Map.
6. What is Iterator? Methods.
7. What is Stack? Methods.
8. Date class methods: after, before, compareTo.
9. What is Collections Framework?

**5-Mark Questions:**
1. Explain Collection hierarchy with diagram.
2. Explain ArrayList vs LinkedList vs Vector.
3. Explain HashSet, LinkedHashSet, TreeSet with examples.
4. Explain HashMap, TreeMap, Hashtable.
5. Explain Iterator and ListIterator.
6. Write program: Date comparison using after/before/compareTo.
7. Write program: HashMap with employee ID and name.
8. Explain Stack class with push/pop/peek.

**10-Mark Questions:**
1. **Explain Collection Framework: List, Set, Map interfaces and their implementations with examples.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Compare all Set implementations. Compare all Map implementations.
3. Date class with formatting. Vector vs Stack.

### Programs to Practice
1. ✅ **HashSet/TreeSet demo** - appeared 2021, 2023, 2024
2. ✅ **HashMap/TreeMap demo** - appeared 2021, 2022, 2023, 2024, 2025
3. ✅ **Vector vs Stack** - appeared 2023
4. ✅ **Date comparison (after, before, compareTo)** - appeared 2021, 2022, 2023, 2024
5. ✅ **Collection traversal using Iterator** - appeared 2023, 2024

---

## 12.11 Summary of Unit 12

| Topic | Key Points |
|-------|------------|
| **Collections Framework** | Unified architecture; interfaces + implementations + algorithms |
| **Collection Interface** | Root (except Map); add, remove, contains, size, iterator |
| **Iterator** | hasNext(), next(), remove(); fail-fast |
| **List** | Ordered, indexed, duplicates; ArrayList, LinkedList, Vector |
| **Set** | No duplicates; HashSet (fast), LinkedHashSet (order), TreeSet (sorted) |
| **Map** | Key-Value; unique keys; HashMap, LinkedHashMap, TreeMap, Hashtable |
| **Stack** | LIFO; extends Vector; push, pop, peek, search |
| **Date** | Milliseconds since epoch; after, before, compareTo, getTime; SimpleDateFormat |
| **Performance** | HashSet/HashMap O(1); TreeSet/TreeMap O(log n); ArrayList fast random access |

---

## 12.12 Quick Reference: Choosing Collection

```java
// Need duplicates + order + index access
List<String> list = new ArrayList<>();

// Need unique + fast lookup + no order
Set<String> set = new HashSet<>();

// Need unique + insertion order
Set<String> set = new LinkedHashSet<>();

// Need unique + sorted
Set<String> set = new TreeSet<>();

// Need key-value + fast lookup
Map<K,V> map = new HashMap<>();

// Need key-value + insertion order
Map<K,V> map = new LinkedHashMap<>();

// Need key-value + sorted by key
Map<K,V> map = new TreeMap<>();

// Need thread-safe List
List<String> list = Collections.synchronizedList(new ArrayList<>());

// Need thread-safe Map
Map<K,V> map = new ConcurrentHashMap<>();

// Need LIFO stack
Deque<String> stack = new ArrayDeque<>();  // Preferred over Stack
```