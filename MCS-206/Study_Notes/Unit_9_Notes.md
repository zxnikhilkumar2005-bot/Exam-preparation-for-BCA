# Unit 9: Multithreading

## Unit Overview
This unit covers multithreading concepts, Java thread model, thread creation (Thread class and Runnable interface), thread life cycle, thread priorities, synchronization, inter-thread communication, thread state management, daemon threads, volatile keyword, and thread interruption.

---

## 9.1 Multithreading Basics

### Topic Introduction
Multithreading allows concurrent execution of multiple parts of a program for maximum CPU utilization.

### Multitasking Types

| Type | Description | Memory | Example |
|------|-------------|--------|---------|
| **Process-based** (Multiprocessing) | Multiple programs running simultaneously | Separate memory spaces (heavyweight) | Browser + Word + Music player |
| **Thread-based** (Multithreading) | Multiple threads within one program | Shared memory space (lightweight) | Web server handling requests |

### Thread vs Process
```
Process (Heavyweight)
├── Stack
├── Heap
├── Variable Space
└── Code Space

Thread (Lightweight) - Shares process memory
├── Own Stack
├── Own PC Register
└── Own Thread State
```

### Advantages of Multithreading
- ✅ Better CPU utilization
- ✅ Responsive applications
- ✅ Resource sharing (memory, files)
- ✅ Lightweight (less overhead than processes)
- ✅ Parallel execution on multi-core CPUs

---

## 9.2 Java Thread Model

### Thread Components
| Component | Description |
|-----------|-------------|
| **CPU** | Thread class encapsulates virtual CPU |
| **Data** | May/may not be shared between threads |
| **Code** | Shared by multiple threads, independent of data |

### Thread States (Life Cycle)

In Java, threads have **6 standard states** (from `Thread.State` enum):

```
                    ┌─────────┐
                    │  NEW    │  (Thread object created, not started)
                    └────┬────┘
                         │ start()
                         ▼
                    ┌─────────────┐
                    │  RUNNABLE   │  (Ready to run OR currently executing)
                    │             │  (Includes READY + RUNNING from OS view)
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
    ┌──────────┐    ┌──────────────┐    ┌─────────────┐
    │ BLOCKED  │    │   WAITING    │    │TIMED_WAITING│
    │          │    │              │    │             │
    │ Waiting  │    │ wait()       │    │ sleep()     │
    │ for lock │    │ join()       │    │ wait(time)  │
    └────┬─────┘    └──────┬───────┘    └──────┬──────┘
         │                 │                   │
         │           notify/notifyAll    timeout/
         │           lock acquired       notify
         └─────────────┬───────────────────┘
                       │
                       ▼
                  ┌──────────┐
                  │TERMINATED│  (run() completes normally or with exception)
                  └──────────┘
```

### State Descriptions

| State | Description | How Entered |
|-------|-------------|-------------|
| **NEW** | Thread created but not started | `new Thread()` |
| **RUNNABLE** | Ready to run or executing; waiting for CPU | `start()` called; returns from BLOCKED/WAITING/TIMED_WAITING |
| **BLOCKED** | Waiting for monitor lock (synchronized) | Trying to enter `synchronized` block/method |
| **WAITING** | Waiting indefinitely for another thread | `wait()`, `join()` (no timeout) |
| **TIMED_WAITING** | Waiting with specified timeout | `sleep()`, `wait(time)`, `join(time)` |
| **TERMINATED** | Thread completed execution | `run()` returns or throws exception |

> **Key Point**: Java's `RUNNABLE` combines OS-level "Ready" and "Running" states. There is **no separate RUNNING state** in Java API.

---

## 9.3 Creating Threads

### Two Ways to Create Threads

| Method | Description | Preferred? |
|--------|-------------|------------|
| **1. Extend Thread class** | Subclass Thread, override `run()` | No (limits inheritance) |
| **2. Implement Runnable** | Implement `run()` in separate class | **Yes** (flexible, OOP-friendly) |

### 9.3.1 Thread Class

#### Constructors
```java
Thread()
Thread(String name)
Thread(Runnable target)
Thread(Runnable target, String name)
```

#### Common Methods
| Method | Description |
|--------|-------------|
| `start()` | Starts thread (calls `run()`) |
| `run()` | Entry point for thread execution |
| `sleep(millis)` | Pauses current thread |
| `getName()` | Returns thread name |
| `setName(name)` | Sets thread name |
| `getPriority()` | Returns priority (1-10) |
| `setPriority(p)` | Sets priority |
| `isAlive()` | Returns true if thread running |
| `join()` | Waits for thread to die |
| `currentThread()` | Returns current thread reference |

### 9.3.2 Method 1: Extend Thread Class

```java
class MyThread extends Thread {
    private String name;
    
    MyThread(String name) {
        super(name);  // Set thread name
    }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(getName() + ": " + i);
            try { Thread.sleep(100); } catch (InterruptedException e) {}
        }
    }
}

public class ThreadDemo {
    public static void main(String[] args) {
        MyThread t1 = new MyThread("Thread-1");
        MyThread t2 = new MyThread("Thread-2");
        
        t1.start();  // MUST call start(), NOT run()!
        t2.start();
        
        System.out.println("Main thread finished");
    }
}
```

### 9.3.3 Method 2: Implement Runnable Interface

```java
class MyRunnable implements Runnable {
    private String name;
    
    MyRunnable(String name) { this.name = name; }
    
    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            System.out.println(name + ": " + i);
            try { Thread.sleep(100); } catch (InterruptedException e) {}
        }
    }
}

public class RunnableDemo {
    public static void main(String[] args) {
        Thread t1 = new Thread(new MyRunnable("Runnable-1"));
        Thread t2 = new Thread(new MyRunnable("Runnable-2"));
        
        t1.start();
        t2.start();
    }
}
```

### Comparison: Thread vs Runnable

| Aspect | Extend Thread | Implement Runnable |
|--------|---------------|-------------------|
| **Inheritance** | Can't extend other class | Can extend another class |
| **Flexibility** | Less flexible | More flexible |
| **Sharing** | Each thread = separate object | Same Runnable shared |
| **Preferred** | No | **Yes** |

### 9.3.4 Lambda Expression (Java 8+)
```java
// Modern approach - Runnable is a Functional Interface
Thread t = new Thread(() -> {
    for (int i = 1; i <= 5; i++) {
        System.out.println("Lambda Thread: " + i);
        try { Thread.sleep(100); } catch (InterruptedException e) {}
    }
});
t.start();
```

### 9.3.5 ThreadGroup (Legacy)
- Groups threads for bulk operations (deprecated, use ExecutorService instead)
- `ThreadGroup` methods: `activeCount()`, `enumerate()`, `interrupt()`

---

## 9.4 Thread Life Cycle Details

### State Transitions
```java
Thread t = new Thread();     // NEW
t.start();                   // NEW → RUNNABLE
// Scheduler assigns CPU     // RUNNABLE → RUNNING
Thread.sleep(1000);          // RUNNING → TIMED_WAITING
t.join();                    // RUNNING → WAITING
// I/O or lock wait          // RUNNING → BLOCKED
// run() completes           // RUNNING → TERMINATED
```

### Getting Thread State
```java
Thread.State state = t.getState();
// Returns: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED
```

---

## 9.5 Thread Priority

### Priority Constants
```java
Thread.MIN_PRIORITY   // 1
Thread.NORM_PRIORITY  // 5 (default)
Thread.MAX_PRIORITY   // 10
```

### Setting Priority
```java
Thread t = new Thread(runnable);
t.setPriority(8);  // Higher priority
t.setPriority(Thread.MAX_PRIORITY);
```

### Priority Scheduling
- **Preemptive**: Higher priority thread preempts lower
- **Same priority**: Round-robin (time-slicing)
- **Not guaranteed**: OS-dependent behavior

```java
class PriorityDemo implements Runnable {
    String name;
    PriorityDemo(String n) { name = n; }
    
    public void run() {
        System.out.println(name + " priority: " + Thread.currentThread().getPriority());
    }
}

public class Test {
    public static void main(String[] args) {
        Thread t1 = new Thread(new PriorityDemo("High"), "High");
        Thread t2 = new Thread(new PriorityDemo("Low"), "Low");
        
        t1.setPriority(Thread.MAX_PRIORITY);
        t2.setPriority(Thread.MIN_PRIORITY);
        
        t1.start();
        t2.start();
    }
}
```

---

## 9.5.1 Daemon Threads

### Concept
- **User Threads**: JVM waits for them to finish before exiting
- **Daemon Threads**: Background service threads; JVM exits when only daemon threads remain

### Usage
```java
Thread t = new Thread(runnable);
t.setDaemon(true);  // Must call BEFORE start()
t.start();
```

### Examples
- **GC (Garbage Collector)** - daemon thread
- **JIT Compiler** - daemon thread
- **Finalizer** - daemon thread

### Important Notes
- `setDaemon(true)` must be called **before** `start()`
- Default: `false` (user thread)
- Main thread is always a user thread
- If all user threads finish, JVM terminates all daemon threads immediately

---

## 9.5.2 Thread Interruption

### Methods
| Method | Description |
|--------|-------------|
| `interrupt()` | Sets interrupted flag; wakes up sleeping/waiting thread |
| `isInterrupted()` | Returns interrupted flag (doesn't clear it) |
| `Thread.interrupted()` | Static; returns and **clears** current thread's flag |

### Handling Interruption
```java
class InterruptibleTask implements Runnable {
    public void run() {
        try {
            while (!Thread.currentThread().isInterrupted()) {
                // Do work
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
            // Sleep threw InterruptedException - flag is cleared
            Thread.currentThread().interrupt(); // Restore flag if needed
        }
    }
}

// Usage
Thread t = new Thread(new InterruptibleTask());
t.start();
// Later...
t.interrupt();  // Request thread to stop
```

### Best Practice
- Check `Thread.interrupted()` or `isInterrupted()` in loops
- Don't swallow `InterruptedException` without restoring the flag
- Use interruption for cancellation, not `stop()` (deprecated)

---

## 9.6 Synchronization

### Problem: Race Condition
```java
class Counter {
    int count = 0;
    void increment() { count++; }  // Not atomic!
}

// Two threads calling increment() → count may be wrong
```

### Solution: Synchronized Keyword
```java
class Counter {
    int count = 0;
    
    // Synchronized method
    public synchronized void increment() {
        count++;
    }
    
    // Synchronized block (more granular)
    public void incrementBlock() {
        synchronized(this) {
            count++;
        }
    }
}
```

### Object Lock (Monitor)
- Every object has an **intrinsic lock** (monitor)
- `synchronized` acquires lock before entering
- Only one thread can hold lock at a time
- Other threads wait in **lock pool**

### Static vs Instance Synchronization
```java
class MyClass {
    // Instance lock (this)
    public synchronized void instanceMethod() { }
    
    public void instanceBlock() {
        synchronized(this) { }
    }
    
    // Class lock (MyClass.class)
    public static synchronized void staticMethod() { }
    
    public static void staticBlock() {
        synchronized(MyClass.class) { }
    }
}
```
- **Instance methods** lock on `this` (per object)
- **Static methods** lock on `Class` object (per class)

### 9.6.1 volatile Keyword

### Purpose
- Ensures **visibility** of changes across threads
- Does **NOT** provide atomicity or mutual exclusion
- Prevents compiler/JIT reordering optimizations

### When to Use
| Use Case | volatile Sufficient? |
|----------|---------------------|
| Single variable read/write | ✅ Yes |
| Compound actions (i++) | ❌ No - use synchronized/AtomicInteger |
| Multiple variables | ❌ No - use synchronized |

```java
class VolatileExample {
    volatile boolean flag = false;  // Visibility guaranteed
    int count = 0;                  // NOT thread-safe for count++
    
    public void stop() { flag = true; }
    public void run() { while (!flag) { count++; } }
}
```

### volatile vs synchronized
| Aspect | volatile | synchronized |
|--------|----------|--------------|
| **Visibility** | ✅ | ✅ |
| **Atomicity** | ❌ | ✅ |
| **Ordering** | ✅ | ✅ |
| **Locking** | None | Object monitor |
| **Performance** | Better (no blocking) | Overhead |

---

### Synchronization Example: Producer-Consumer
```java
class Buffer {
    int data;
    boolean hasData = false;
    
    public synchronized void put(int value) {
        while (hasData) {
            try { wait(); } catch (InterruptedException e) {}
        }
        data = value;
        hasData = true;
        notify();  // Wake up consumer
    }
    
    public synchronized int get() {
        while (!hasData) {
            try { wait(); } catch (InterruptedException e) {}
        }
        hasData = false;
        notify();  // Wake up producer
        return data;
    }
}

class Producer implements Runnable {
    Buffer buffer;
    Producer(Buffer b) { buffer = b; }
    
    public void run() {
        for (int i = 1; i <= 5; i++) {
            buffer.put(i);
            System.out.println("Produced: " + i);
        }
    }
}

class Consumer implements Runnable {
    Buffer buffer;
    Consumer(Buffer b) { buffer = b; }
    
    public void run() {
        for (int i = 1; i <= 5; i++) {
            int value = buffer.get();
            System.out.println("Consumed: " + value);
        }
    }
}

public class ProducerConsumer {
    public static void main(String[] args) {
        Buffer buffer = new Buffer();
        new Thread(new Producer(buffer)).start();
        new Thread(new Consumer(buffer)).start();
    }
}
```

---

## 9.7 Inter-Thread Communication

### Methods (from Object class)
| Method | Description |
|--------|-------------|
| `wait()` | Releases lock, waits until `notify()` |
| `wait(timeout)` | Waits with timeout |
| `notify()` | Wakes up ONE waiting thread |
| `notifyAll()` | Wakes up ALL waiting threads |

### Rules
- ✅ Must be called from **synchronized** context
- ✅ Current thread must **own the lock**
- ❌ Called outside synchronized → `IllegalMonitorStateException`

### Wait/Notify Flow
```
Thread A (Producer)                    Thread B (Consumer)
────────────────────                    ──────────────────
synchronized(buffer) {                 synchronized(buffer) {
    while (full) wait();                   while (empty) wait();
    produce();                             consume();
    notify();                              notify();
}                                        }
```

### 9.7.1 notify() vs notifyAll()

| Method | Behavior | Use When |
|--------|----------|----------|
| `notify()` | Wakes **one** arbitrary waiting thread | Only one thread can proceed (e.g., single consumer) |
| `notifyAll()` | Wakes **all** waiting threads | Multiple threads may need to re-check condition |

> **Best Practice**: Use `notifyAll()` unless you're certain only one thread should proceed. Using `notify()` with multiple waiters can cause "missed signals" if wrong thread wakes.

---

## 9.8 isAlive() and join()

### isAlive()
```java
Thread t = new Thread(runnable);
t.start();
if (t.isAlive()) {
    System.out.println("Thread is running");
}
```
- Returns `true` if thread started and not terminated

### join()
```java
Thread t1 = new Thread(runnable);
Thread t2 = new Thread(runnable);

t1.start();
t2.start();

t1.join();  // Main waits for t1 to finish
t2.join();  // Main waits for t2 to finish
System.out.println("Both threads finished");
```

#### Overloaded join()
```java
t.join();                    // Wait indefinitely
t.join(1000);                // Wait max 1000ms
t.join(1000, 500000);        // Wait max 1000ms + 500000ns
```

### 9.8.1 join() with isAlive() Pattern
```java
Thread t = new Thread(task);
t.start();

// Wait for thread with timeout
t.join(5000);  // Wait max 5 seconds
if (t.isAlive()) {
    System.out.println("Thread still running after timeout");
    t.interrupt();  // Request cancellation
} else {
    System.out.println("Thread completed normally");
}
```

---

## 9.9 Thread Issues and Solutions

| Issue | Description | Solution |
|-------|-------------|----------|
| **Race Condition** | Multiple threads access shared data | Synchronization, `volatile`, `Atomic*` classes |
| **Deadlock** | Circular wait for locks | Lock ordering, timeout, `tryLock()` |
| **Starvation** | Low-priority thread never gets CPU | Fair scheduling, priority aging |
| **Livelock** | Threads active but make no progress | Random backoff, queue-based coordination |

### Deadlock Example
```java
// Thread 1: locks A, needs B
// Thread 2: locks B, needs A → DEADLOCK!

// Solution: Always acquire locks in same order
synchronized(lockA) {
    synchronized(lockB) { ... }
}
```

### 9.9.1 Deadlock Prevention Strategies

1. **Lock Ordering**: Always acquire locks in consistent global order
2. **Lock Timeout**: Use `ReentrantLock.tryLock(timeout)` instead of `synchronized`
3. **Lock Hierarchy**: Assign numeric levels to locks, acquire only increasing
4. **Single Lock**: Coarse-grained locking (reduces concurrency but prevents deadlock)

```java
// Using tryLock with timeout (java.util.concurrent.locks.ReentrantLock)
Lock lockA = new ReentrantLock();
Lock lockB = new ReentrantLock();

public void transfer(Account from, Account to, int amount) {
    if (lockA.tryLock(1, TimeUnit.SECONDS)) {
        try {
            if (lockB.tryLock(1, TimeUnit.SECONDS)) {
                try {
                    // Safe transfer
                } finally { lockB.unlock(); }
            }
        } finally { lockA.unlock(); }
    }
}
```

### 9.9.2 Livelock Example
```java
// Two threads trying to avoid deadlock by yielding, but both yield simultaneously
// Result: Neither makes progress → LIVELOCK
while (true) {
    if (lockA.tryLock()) {
        try {
            if (lockB.tryLock()) {
                try { /* work */ } finally { lockB.unlock(); }
            }
        } finally { lockA.unlock(); }
    }
    // If couldn't get both, back off randomly
    Thread.sleep(random.nextInt(100));
}
```

### Deprecated Methods (Avoid)
| Method | Reason |
|--------|--------|
| `stop()` | Leaves objects in inconsistent state |
| `suspend()` | Can cause deadlock |
| `resume()` | Counterpart to suspend |

> **Why Deprecated**: These methods violate thread safety guarantees and can leave shared objects in corrupted state.

---

## 9.10 Important Exam Questions (from PYQ Analysis)

### High Priority (CRITICAL - Appeared 9/10 years)

**2-Mark Questions:**
1. Difference between process and thread.
2. What is multithreading? Advantages.
3. Two ways to create thread. Which preferred?
4. Thread life cycle states (6 states: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED).
5. What is synchronization? Why needed?
6. Difference between `wait()` and `sleep()`.
7. What is `isAlive()` and `join()`?
8. What is deadlock? How to avoid?
9. Difference between `notify()` and `notifyAll()`.
10. What is thread priority? Constants.
11. **What is daemon thread?** (New - asked in recent exams)
12. **Difference between `volatile` and `synchronized`?** (New - trending)

**5-Mark Questions:**
1. Explain thread creation with Thread class and Runnable interface (include lambda).
2. Explain thread life cycle with diagram.
3. Explain synchronization with example (method vs block).
4. Explain inter-thread communication (wait/notify/notifyAll).
5. Explain `isAlive()` and `join()` with program.
6. Explain thread priority with example.
7. Write producer-consumer program using synchronization.
8. **Explain daemon threads with example.**
9. **Explain thread interruption and `InterruptedException` handling.**

**10-Mark Questions:**
1. **What is multithreading? Explain thread creation, life cycle, synchronization, and inter-thread communication with programs.** (Appeared 2021, 2022, 2023, 2024, 2025, 2026)
2. Explain synchronization in detail. Thread issues (deadlock, race condition, livelock) and solutions.
3. Thread creation methods comparison. Producer-consumer problem.
4. **Complete multithreading: creation, life cycle, synchronization, wait/notify, deadlock, daemon threads.**

### Programs to Practice
1. ✅ **Thread creation (Thread class + Runnable + Lambda)** - appeared 2021, 2022, 2023, 2025
2. ✅ **Thread priority + isAlive()** - appeared 2021, 2023, 2025
3. ✅ **Synchronization (Producer-Consumer or Counter)** - appeared 2022, 2023, 2025, 2026
4. ✅ **Thread life cycle diagram** - appeared 2021, 2022, 2023, 2024, 2025, 2026
5. ✅ **Inter-thread communication (wait/notify)** - appeared 2023, 2026
6. ✅ **Daemon thread demo** - trending in recent exams
7. ✅ **Thread interruption handling** - trending

---

## 9.11 Summary of Unit 9

| Topic | Key Points |
|-------|------------|
| **Multithreading** | Concurrent execution; shared memory; lightweight |
| **Creation** | Extend Thread OR implement Runnable (preferred) OR Lambda (Java 8+) |
| **start() vs run()** | `start()` creates new thread; `run()` executes in current |
| **Life Cycle** | NEW → RUNNABLE → BLOCKED/WAITING/TIMED_WAITING → TERMINATED |
| **Priority** | 1-10 (MIN=1, NORM=5, MAX=10); preemptive scheduling |
| **Daemon Thread** | Background thread; JVM exits when only daemons remain |
| **Interruption** | `interrupt()`, `isInterrupted()`, `Thread.interrupted()` |
| **Synchronization** | `synchronized` keyword; object lock; prevents race condition |
| **volatile** | Visibility only; no atomicity; for single variables |
| **wait()/notify()** | Inter-thread communication; must be in synchronized block |
| **notify() vs notifyAll()** | notify = one thread; notifyAll = all waiting threads |
| **isAlive()** | Checks if thread running |
| **join()** | Waits for thread termination (with optional timeout) |
| **Deadlock** | Circular wait; avoid with lock ordering, timeout |
| **Livelock** | Active but no progress; avoid with random backoff |
| **Deprecated** | `stop()`, `suspend()`, `resume()` - don't use |

---

## 9.12 Quick Reference: Thread Methods

```java
Thread t = new Thread(runnable, "MyThread");

// Creation & Start
t.start();                      // Start thread (creates new call stack)
t.run();                        // DON'T CALL DIRECTLY! Runs in current thread
Thread.sleep(1000);             // Static: sleep current thread

// Thread Properties
t.getName();                    // Get name
t.setName("NewName");           // Set name
t.getPriority();                // Get priority (1-10)
t.setPriority(8);               // Set priority
t.setDaemon(true);              // Set as daemon (BEFORE start!)
t.isDaemon();                   // Check if daemon

// State & Control
t.isAlive();                    // Is running? (started & not terminated)
t.join();                       // Wait for death (indefinite)
t.join(1000);                   // Wait with timeout (ms)
t.join(1000, 500000);           // Wait with timeout (ms + ns)
Thread.currentThread();         // Get current thread reference
t.getState();                   // Get state: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED

// Interruption
t.interrupt();                  // Request interruption (sets flag, wakes wait/sleep)
t.isInterrupted();              // Check interrupted flag (doesn't clear)
Thread.interrupted();           // Static: check & CLEAR current thread's flag

// Synchronization (Object methods - call from synchronized context)
obj.wait();                     // Release lock, wait indefinitely
obj.wait(1000);                 // Wait with timeout
obj.notify();                   // Wake ONE waiting thread
obj.notifyAll();                // Wake ALL waiting threads

// Deprecated - AVOID
// t.stop();      // Unsafe - leaves objects corrupted
// t.suspend();   // Deadlock-prone
// t.resume();    // Counterpart to suspend
```

---

## 9.13 wait() vs sleep() vs join() vs yield() Comparison

| Method | Class | Releases Lock? | Purpose | Wakes On |
|--------|-------|----------------|---------|----------|
| `wait()` | Object | **Yes** | Inter-thread communication | `notify()` / `notifyAll()` / timeout |
| `wait(time)` | Object | **Yes** | Timed wait | `notify()` / timeout |
| `sleep()` | Thread | **No** | Pause execution | Timeout expires |
| `join()` | Thread | **No** | Wait for thread death | Target thread terminates / timeout |
| `yield()` | Thread | **No** | Hint scheduler to run others | Scheduler assigns CPU |

> **Critical**: `wait()`/`notify()` must be called from `synchronized` context (own the lock). `sleep()`/`yield()`/`join()` do NOT require synchronization.