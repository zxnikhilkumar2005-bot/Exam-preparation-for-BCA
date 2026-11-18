# Unit 12: Java API / Collections

## Unit Overview
This unit covers the Collections Framework hierarchy, Date class, Set interface (HashSet, TreeSet, LinkedHashSet), Map interface (HashMap, TreeMap, Hashtable), List interface (ArrayList, LinkedList, Vector), Stack class, Queue interface, Comparable vs Comparator, Collections utility class, and Iterator/ListIterator.

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

> **Exam Note**: The Collection hierarchy (Collection → List/Set/Queue → implementations) is a **frequent 10-mark question** (appeared 2023, 2024, 2025). Be ready to draw the diagram and explain each interface.

---

## 12.2 Queue Interface

### Characteristics
- **Ordered** (typically FIFO - First In, First Out)
- **Allows duplicates**
- **Additional operations**: insertion at tail, removal from head

### Implementations

| Class | Description | Best For |
|-------|-------------|----------|
| `PriorityQueue` | Elements ordered by priority (natural/comparator) | Processing by priority, not FIFO |
| `ArrayDeque` | Resizable array, double-ended queue | Fast FIFO queue or stack (preferred over Stack) |
| `LinkedList` | Also implements Queue/Deque | When you need both List and Queue |

### Queue Methods (Additional to Collection)
```java
E add(E e)                    // Insert, throws exception if full
boolean offer(E e)            // Insert, returns false if full
E remove()                    // Remove head, throws if empty
E poll()                      // Remove head, returns null if empty
E element()                   // Peek head, throws if empty
E peek()                      // Peek head, returns null if empty
```

### Deque Methods (Double-Ended Queue)
```java
void addFirst(E e)            // Insert at front
void addLast(E e)             // Insert at end
boolean offerFirst(E e)       // Insert at front, safe
boolean offerLast(E e)        // Insert at end, safe
E removeFirst()               // Remove from front
E removeLast()                // Remove from end
E pollFirst()                 // Remove from front, safe
E pollLast()                  // Remove from end, safe
E getFirst()                  // Peek front
E getLast()                   // Peek end
E peekFirst()                 // Peek front, safe
E peekLast()                  // Peek end, safe
```

### Example
```java
// PriorityQueue - sorted by natural order
Queue<Integer> pq = new PriorityQueue<>();
pq.offer(30); pq.offer(10); pq.offer(20);
while (!pq.isEmpty()) System.out.print(pq.poll() + " ");  // 10 20 30

// ArrayDeque - preferred for Stack/Queue (non-synchronized, faster)
Deque<String> deque = new ArrayDeque<>();
deque.push("A");    // Stack behavior
deque.push("B");
System.out.println(deque.pop());   // B

deque.offerLast("C"); // Queue behavior
deque.offerLast("D");
System.out.println(deque.pollFirst()); // C
```

> **Exam Note**: `ArrayDeque` is **preferred over Stack** (not synchronized, faster). `PriorityQueue` does **NOT allow null** elements.

---

## 12.3 Collection Interface Methods

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

## 12.4 Iterator and ListIterator Interface

### Iterator Methods
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

### ListIterator (Bidirectional Iterator for Lists)
```java
boolean hasNext()         // Forward: more elements?
E next()                  // Forward: next element
int nextIndex()           // Index of next element
boolean hasPrevious()     // Backward: more elements?
E previous()              // Backward: previous element
int previousIndex()       // Index of previous element
void remove()             // Remove last returned by next/previous
void set(E e)             // Replace last returned element
void add(E e)             // Insert before next element
```

### ListIterator Example
```java
List<String> list = new ArrayList<>(Arrays.asList("A", "B", "C"));
ListIterator<String> li = list.listIterator();

while (li.hasNext()) {
    System.out.println(li.next());  // A B C
}

// Now iterate backward
while (li.hasPrevious()) {
    System.out.println(li.previous());  // C B A
}

// Modify during iteration
li = list.listIterator();
li.next();              // A
li.set("X");            // [X, B, C]
li.add("Y");            // [X, Y, B, C]
```

> **Exam Note**: `ListIterator` is a **frequent 5-10 mark question** (appeared 2023, 2024). Know differences from Iterator: bidirectional, can add/set, has index methods.

---

## 12.5 List Interface

### Characteristics
- **Ordered**: Elements have position (index)
- **Allows duplicates**
- **Indexed access**: get(index), set(index, element)

### Implementations

| Class | Description | Best For |
|-------|-------------|----------|
| `ArrayList` | Dynamic array; fast random access O(1) | Frequent reads, infrequent inserts |
| `LinkedList` | Doubly linked list; fast inserts/deletes O(1) at ends | Frequent inserts/deletes at ends |
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

### ArrayList vs Vector vs LinkedList - Quick Comparison

| Feature | ArrayList | Vector | LinkedList |
|---------|-----------|--------|------------|
| **Synchronized** | No | Yes | No |
| **Data Structure** | Dynamic Array | Dynamic Array | Doubly Linked List |
| **Random Access** | O(1) | O(1) | O(n) |
| **Insert/Delete at End** | O(1) amortized | O(1) amortized | O(1) |
| **Insert/Delete at Middle** | O(n) | O(n) | O(n) |
| **Memory Overhead** | Low | Low | High (node objects) |
| **Legacy** | No | Yes (Java 1.0) | No |
| **Growth Strategy** | 1.5x | 2x | N/A |

> **Exam Note**: "ArrayList vs Vector" is a **classic 2-5 mark question** (appeared 2021, 2023, 2024). Key difference: Vector is synchronized, ArrayList is not. Use `Collections.synchronizedList()` for thread-safe ArrayList.

---

## 12.6 Stack Class

### Characteristics
- Extends `Vector`
- **LIFO** (Last In, First Out)
- Synchronized (thread-safe) - **legacy class**

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

### Modern Alternative: ArrayDeque (Preferred)
```java
// Use ArrayDeque instead of Stack (non-synchronized, faster, implements Deque)
Deque<Integer> stack = new ArrayDeque<>();
stack.push(10);
stack.push(20);
stack.push(30);

System.out.println(stack.peek());   // 30
System.out.println(stack.pop());    // 30
System.out.println(stack.pop());    // 20

// Also works as Queue
stack.offerLast(40);
System.out.println(stack.pollFirst()); // 10
```

> **Exam Note**: "Vector vs Stack" appeared as a **10-mark question in Dec 2023**. Stack extends Vector (synchronized). Modern code should use `ArrayDeque` which implements `Deque` interface - faster, not synchronized, supports both stack and queue operations.

---

## 12.7 Set Interface

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

### TreeSet Methods (NavigableSet)
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

### Comparable vs Comparator (Critical for TreeSet/TreeMap)

| Aspect | Comparable | Comparator |
|--------|------------|------------|
| **Package** | java.lang | java.util |
| **Method** | `int compareTo(T o)` | `int compare(T o1, T o2)` |
| **Use Case** | Natural ordering (single sort) | Multiple/custom sort orders |
| **Modification** | Must modify class | External class (no modification) |
| **Sort Method** | `Collections.sort(list)` | `Collections.sort(list, comparator)` |

```java
// Comparable - Natural ordering (implement in class)
class Student implements Comparable<Student> {
    int id; String name;
    public int compareTo(Student s) {
        return this.id - s.id;  // Sort by ID ascending
    }
}

// Comparator - Custom ordering (external)
class NameComparator implements Comparator<Student> {
    public int compare(Student s1, Student s2) {
        return s1.name.compareTo(s2.name);
    }
}

// Usage with TreeSet
Set<Student> set1 = new TreeSet<>();                    // Uses Comparable
Set<Student> set2 = new TreeSet<>(new NameComparator()); // Uses Comparator
Set<Student> set3 = new TreeSet<>(Comparator.comparing(Student::getName)); // Java 8+
```

> **Exam Note**: "Comparable vs Comparator" is listed as **Low Priority but asked in exams** (Unit 12 PYQ). TreeSet/TreeMap require elements to implement Comparable OR provide a Comparator. Null not allowed in TreeSet.

> **Exam Note**: "HashSet vs TreeSet" and "HashSet & TreeSet utility" appeared in **2023, 2024, 2025, 2026** (5-10 marks). Know: HashSet = O(1), unordered, allows null; TreeSet = O(log n), sorted, no null, needs Comparable/Comparator.

---

## 12.8 Map Interface

### Characteristics
- **Key-Value pairs**
- **Unique keys** (no duplicate keys)
- **Values can be duplicated**
- **Not a Collection** (doesn't extend Collection)

### Implementations

| Class | Ordering | Null Keys | Null Values | Thread-Safe |
|-------|----------|-----------|-------------|-------------|
| `HashMap` | No guarantee | Yes (one) | Yes | No |
| `LinkedHashMap` | Insertion order | Yes (one) | Yes | No |
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

### HashMap Internal Working (Important for Interviews/Exams)
- **Array of buckets** (Node<K,V>[])
- **Hash function**: `hash(key) = key.hashCode() ^ (key.hashCode() >>> 16)`
- **Index**: `(n - 1) & hash` where n = table size (power of 2)
- **Collision handling**: LinkedList (Java 7) → TreeNode/Red-Black Tree (Java 8+ when bucket size > 8)
- **Load factor**: 0.75 (resize when size > capacity * 0.75)
- **Default capacity**: 16

> **Exam Note**: "HashMap, TreeMap, Hashtable" explanation appeared as **10-mark question** (2021, 2022, 2023, 2024, 2025). "HashSet & HashMap role" appeared in **June 2025 Q5(c)** as 5-mark short note. Know: HashMap = O(1), unsorted, allows 1 null key; TreeMap = O(log n), sorted by key, no null keys; Hashtable = synchronized legacy class.

## 12.9 HashMap vs Hashtable

| Aspect | HashMap | Hashtable |
|--------|---------|-----------|
| **Synchronization** | No | Yes (all methods) |
| **Null Keys** | Allowed (one) | Not allowed |
| **Null Values** | Allowed | Not allowed |
| **Iteration** | Fail-fast iterator | Enumerator (not fail-fast) |
| **Performance** | Faster | Slower (sync overhead) |
| **Legacy** | Java 2+ | Java 1.0 |
| **Superclass** | AbstractMap | Dictionary |
| **Fail-fast** | Yes (Iterator) | No (Enumeration) |

> Use `ConcurrentHashMap` for thread-safe Map in modern Java (segment-level locking, better performance).

### HashMap vs LinkedHashMap vs TreeMap

| Feature | HashMap | LinkedHashMap | TreeMap |
|---------|---------|---------------|---------|
| **Ordering** | None | Insertion order | Sorted (key) |
| **Null Keys** | 1 allowed | 1 allowed | Not allowed |
| **Null Values** | Allowed | Allowed | Allowed |
| **Performance** | O(1) | O(1) | O(log n) |
| **Interface** | Map | Map | SortedMap, NavigableMap |
| **Implementation** | Hash table | Hash table + linked list | Red-Black Tree |

---

## 12.10 Date Class (java.util.Date)

### Constructors
```java
Date()                          // Current date/time
Date(long millis)               // Milliseconds since Jan 1, 1970 (epoch)
```

### Important Methods
```java
boolean after(Date when)        // This after when?
boolean before(Date when)       // This before when?
int compareTo(Date anotherDate) // Compare: 0=equal, <0=before, >0=after
Object clone()                  // Copy
boolean equals(Object obj)      // Compare (checks time equality)
long getTime()                  // Milliseconds since epoch
void setTime(long time)         // Set time
String toString()               // String representation (e.g., "Tue Jul 15 14:30:45 IST 2024")
int hashCode()                  // Hash code
```

### Deprecated Methods (Avoid - Use Calendar or java.time instead)
```java
getYear(), getMonth(), getDate(), getHours(), getMinutes(), getSeconds()
setYear(), setMonth(), setDate(), setHours(), setMinutes(), setSeconds()
toLocaleString(), toGMTString(), parse(String)
```

### Example - Date Comparison (Frequent 5-mark program)
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
        
        // Using after/before
        if (now.after(d1)) System.out.println("Now is after d1");
        if (now.before(d1)) System.out.println("Now is before d1");
        
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

> **Exam Note**: "Date class compareTo, after, before" appeared in **2021, 2022, 2023, 2024** (5 marks). "Date class with formatting" appeared in **2021, 2023, 2024, 2025** (10 marks). Must know: compareTo returns int, after/before return boolean, getTime returns long. Deprecated methods should not be used.

---

## 12.11 Collections Utility Class (java.util.Collections)

### Important Static Methods
```java
// Sorting
static <T extends Comparable<? super T>> void sort(List<T> list)
static <T> void sort(List<T> list, Comparator<? super T> c)

// Searching (list must be sorted)
static <T> int binarySearch(List<? extends T> list, T key)
static <T> int binarySearch(List<? extends T> list, T key, Comparator<? super T> c)

// Reversing/Shuffling
static void reverse(List<?> list)
static void shuffle(List<?> list)
static void shuffle(List<?> list, Random rnd)

// Rotating/Swapping
static void rotate(List<?> list, int distance)
static void swap(List<?> list, int i, int j)

// Min/Max
static <T extends Object & Comparable<? super T>> T min(Collection<? extends T> coll)
static <T> T min(Collection<? extends T> coll, Comparator<? super T> comp)
static <T extends Object & Comparable<? super T>> T max(Collection<? extends T> coll)
static <T> T max(Collection<? extends T> coll, Comparator<? super T> comp)

// Synchronized Wrappers (Thread-Safe)
static <T> Collection<T> synchronizedCollection(Collection<T> c)
static <T> List<T> synchronizedList(List<T> list)
static <K,V> Map<K,V> synchronizedMap(Map<K,V> m)
static <K,V> SortedMap<K,V> synchronizedSortedMap(SortedMap<K,V> m)
static <T> Set<T> synchronizedSet(Set<T> s)
static <T> SortedSet<T> synchronizedSortedSet(SortedSet<T> s)

// Unmodifiable Views (Read-only)
static <T> Collection<T> unmodifiableCollection(Collection<? extends T> c)
static <T> List<T> unmodifiableList(List<? extends T> list)
static <K,V> Map<K,V> unmodifiableMap(Map<? extends K,? extends V> m)
static <T> Set<T> unmodifiableSet(Set<? extends T> s)

// Other
static <T> void fill(List<? super T> list, T obj)
static int frequency(Collection<?> c, Object o)
static boolean disjoint(Collection<?> c1, Collection<?> c2)
```

### Example
```java
List<Integer> list = Arrays.asList(30, 10, 50, 20, 40);

Collections.sort(list);              // [10, 20, 30, 40, 50]
Collections.reverse(list);           // [50, 40, 30, 20, 10]
Collections.shuffle(list);           // Random order

int index = Collections.binarySearch(list, 30);  // Requires sorted list
System.out.println(Collections.max(list));       // 50
System.out.println(Collections.min(list));       // 10

// Thread-safe wrapper
List<String> syncList = Collections.synchronizedList(new ArrayList<>());

// Read-only view
List<String> unmodifiable = Collections.unmodifiableList(list);
// unmodifiable.add("X");  // UnsupportedOperationException
```

> **Exam Note**: Collections class utility methods (sort, binarySearch, reverse, synchronized wrappers) are important for 5-mark questions.

## 12.12 Summary of Unit 12

| Topic | Key Points |
|-------|------------|
| **Collections Framework** | Unified architecture; interfaces + implementations + algorithms |
| **Collection Interface** | Root (except Map); add, remove, contains, size, iterator |
| **Iterator / ListIterator** | hasNext(), next(), remove(); ListIterator adds bidirectional, add, set, index |
| **List** | Ordered, indexed, duplicates; ArrayList, LinkedList, Vector |
| **Queue/Deque** | FIFO/LIFO; PriorityQueue (sorted), ArrayDeque (fast, preferred over Stack) |
| **Set** | No duplicates; HashSet (fast), LinkedHashSet (order), TreeSet (sorted) |
| **Map** | Key-Value; unique keys; HashMap, LinkedHashMap, TreeMap, Hashtable, ConcurrentHashMap |
| **Stack** | LIFO; extends Vector; push, pop, peek, search (legacy; use ArrayDeque) |
| **Date** | Milliseconds since epoch; after, before, compareTo, getTime; SimpleDateFormat |
| **Collections Utility** | sort, binarySearch, reverse, shuffle, synchronized/unmodifiable wrappers |
| **Comparable vs Comparator** | Natural ordering vs custom ordering; required for TreeSet/TreeMap |
| **Performance** | HashSet/HashMap O(1); TreeSet/TreeMap O(log n); ArrayList fast random access |

---

## 12.13 Quick Reference: Choosing Collection

```java
// Need duplicates + order + index access
List<String> list = new ArrayList<>();

// Need unique + fast lookup + no order
Set<String> set = new HashSet<>();

// Need unique + insertion order
Set<String> set = new LinkedHashSet<>();

// Need unique + sorted (natural/comparator)
Set<String> set = new TreeSet<>();

// Need key-value + fast lookup
Map<K,V> map = new HashMap<>();

// Need key-value + insertion order
Map<K,V> map = new LinkedHashMap<>();

// Need key-value + sorted by key
Map<K,V> map = new TreeMap<>();

// Need FIFO Queue
Queue<String> queue = new ArrayDeque<>();  // or LinkedList

// Need Priority Queue (sorted)
Queue<Integer> pq = new PriorityQueue<>();

// Need thread-safe List
List<String> list = Collections.synchronizedList(new ArrayList<>());

// Need thread-safe Map
Map<K,V> map = new ConcurrentHashMap<>();

// Need LIFO stack (modern)
Deque<String> stack = new ArrayDeque<>();  // Preferred over Stack

// Need synchronized Set
Set<String> set = Collections.synchronizedSet(new HashSet<>());

// Need read-only view
List<String> roList = Collections.unmodifiableList(list);
Map<K,V> roMap = Collections.unmodifiableMap(map);
```

---

## 12.14 Important Exam Questions (from PYQ Analysis - Dec 2021 to June 2026)

### HIGH PRIORITY (Appeared 4+ times)

**2-Mark Questions:**
1. Difference between ArrayList and Vector. (2021, 2023, 2024)
2. Difference between HashSet and TreeSet. (2023, 2024, 2025, 2026)
3. Difference between HashMap and Hashtable. (2021, 2023, 2024, 2025)
4. Difference between List and Set.
5. Difference between Set and Map.
6. What is Iterator? Methods.
7. What is Stack? Methods.
8. Date class methods: after, before, compareTo. (2021, 2022, 2023, 2024)
9. What is Collections Framework?

**5-Mark Questions:**
1. Explain Collection hierarchy with diagram. (2023, 2024, 2025 - 10 marks)
2. Explain ArrayList vs LinkedList vs Vector.
3. Explain HashSet, LinkedHashSet, TreeSet with examples. (2023, 2024, 2025, 2026)
4. Explain HashMap, TreeMap, Hashtable. (2021, 2022, 2023, 2024, 2025)
5. Explain Iterator and ListIterator. (2023, 2024)
6. Write program: Date comparison using after/before/compareTo. (2021, 2022, 2023, 2024)
7. Write program: HashMap with employee ID and name. (2021, 2022, 2023, 2024, 2025)
8. Explain Stack class with push/pop/peek.
9. Explain Vector vs Stack with methods. (Dec 2023 - 10 marks)

**10-Mark Questions:**
1. **Explain Collection Framework: List, Set, Map interfaces and their implementations with examples.** (Appeared 2021, 2022, 2023, 2024, 2025)
2. Compare all Set implementations. Compare all Map implementations.
3. Date class with formatting. Vector vs Stack. (Dec 2023, Dec 2024)
4. HashSet vs HashMap, TreeSet vs HashSet, Set vs Map differentiations. (June 2023 - 10 marks)

### Programs to Practice (High Yield)
1. ✅ **HashSet/TreeSet demo** - appeared 2021, 2023, 2024
2. ✅ **HashMap/TreeMap demo** - appeared 2021, 2022, 2023, 2024, 2025
3. ✅ **Vector vs Stack** - appeared 2023
4. ✅ **Date comparison (after, before, compareTo)** - appeared 2021, 2022, 2023, 2024
5. ✅ **Collection traversal using Iterator** - appeared 2023, 2024
6. ✅ **ArrayDeque as Stack/Queue** - modern replacement
7. ✅ **TreeSet with Comparable/Comparator** - for custom sorting
8. ✅ **Collections.sort, binarySearch, reverse** - utility methods

### Short Notes (5 marks each - appears in Q5 frequently)
- HashSet & HashMap role (June 2025 Q5c)
- TreeSet & HashSet utility (Dec 2025 Q5d)
- Collection API + Date class (Dec 2024 Q3a)
- HashSet constructors (Dec 2024 Q3b)
- Iterators and ListIterators
- Comparable vs Comparator