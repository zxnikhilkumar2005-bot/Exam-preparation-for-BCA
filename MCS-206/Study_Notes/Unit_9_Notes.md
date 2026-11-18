# Unit 9: Multithreading

## Unit Overview
This unit covers multithreading concepts, Java thread model, thread creation (Thread class and Runnable interface), thread life cycle, thread priorities, synchronization, inter-thread communication, and thread state management.

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

```
                    ┌─────────┐
                    │  NEW    │  (Thread object created)
                    └────┬────┘
                         │ start()
                         ▼
                    ┌─────────┐
                    │ RUNNABLE│  (Ready to run, waiting for CPU)
                    └────┬────┘
                         │ Gets CPU
                         ▼
              ┌──────────┴──────────┐
              ▼                     ▼
       ┌─────────────┐        ┌─────────────┐
       │  RUNNING    │        │  BLOCKED    │
       │ (Executing) │        │ (Waiting for│
       └──────┬──────┘        │  I/O, lock) │
              │               └──────┬──────┘
              │                      │
       ┌──────┴──────┐               │
       ▼             ▼               │
 sleep(),        I/O complete,     │
 wait(),         lock acquired     │
 yield()                        │
       │             │             │
       └─────────────┴─────────────┘
                         │
                         ▼
                    ┌─────────┐
                    │  DEAD   │  (run() completes)
                    └─────────┘
```

### State Descriptions

| State | Description |
|-------|-------------|
| **NEW** | Thread created but not started (`new Thread()`) |
| **RUNNABLE** | Ready to run, waiting for scheduler |
| **RUNNING** | Currently executing on CPU |
| **BLOCKED** | Waiting for I/O, lock, or resource |
| **WAITING** | Waiting indefinitely (`wait()`, `join()`) |
| **TIMED_WAITING** | Waiting with timeout (`sleep()`, `wait(time)`) |
| **TERMINATED** | `run()` completed or exception |

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

---

## 9.9 Thread Issues and Solutions

| Issue | Description | Solution |
|-------|-------------|----------|
| **Race Condition** | Multiple threads access shared data | Synchronization |
| **Deadlock** | Threads wait for each other's locks | Lock ordering, timeout |
| **Starvation** | Low-priority thread never gets CPU | Fair scheduling, priority aging |
| **Livelock** | Threads actively respond but make no progress | Random backoff |

### Deadlock Example
```java
// Thread 1: locks A, needs B
// Thread 2: locks B, needs A → DEADLOCK!

// Solution: Always acquire locks in same order
synchronized(lockA) {
    synchronized(lockB) { ... }
}
```

### Deprecated Methods (Avoid)
| Method | Reason |
|--------|--------|
| `stop()` | Leaves objects in inconsistent state |
| `suspend()` | Can cause deadlock |
| `resume()` | Counterpart to suspend |

---

## 9.10 Important Exam Questions (from PYQ Analysis)

### High Priority (CRITICAL - Appeared 9/10 years)

**2-Mark Questions:**
1. Difference between process and thread.
2. What is multithreading? Advantages.
3. Two ways to create thread. Which preferred?
4. Thread life cycle states.
5. What is synchronization? Why needed?
6. Difference between `wait()` and `sleep()`.
7. What is `isAlive()` and `join()`?
8. What is deadlock? How to avoid?
9. Difference between `notify()` and `notifyAll()`.
10. What is thread priority? Constants.

**5-Mark Questions:**
1. Explain thread creation with Thread class and Runnable interface.
2. Explain thread life cycle with diagram.
3. Explain synchronization with example.
4. Explain inter-thread communication (wait/notify).
5. Explain `isAlive()` and `join()` with program.
6. Explain thread priority with example.
7. Write producer-consumer program using synchronization.

**10-Mark Questions:**
1. **What is multithreading? Explain thread creation, life cycle, synchronization, and inter-thread communication with programs.** (Appeared 2021, 2022, 2023, 2024, 2025, 2026)
2. Explain synchronization in detail. Thread issues (deadlock, race condition) and solutions.
3. Thread creation methods comparison. Producer-consumer problem.

### Programs to Practice
1. ✅ **Thread creation (Thread class + Runnable)** - appeared 2021, 2022, 2023, 2025
2. ✅ **Thread priority + isAlive()** - appeared 2021, 2023, 2025
3. ✅ **Synchronization (Producer-Consumer or Counter)** - appeared 2022, 2023, 2025, 2026
4. ✅ **Thread life cycle diagram** - appeared 2021, 2022, 2023, 2024, 2025, 2026
5. ✅ **Inter-thread communication** - appeared 2023, 2026

---

## 9.11 Summary of Unit 9

| Topic | Key Points |
|-------|------------|
| **Multithreading** | Concurrent execution; shared memory; lightweight |
| **Creation** | Extend Thread OR implement Runnable (preferred) |
| **start() vs run()** | `start()` creates new thread; `run()` executes in current |
| **Life Cycle** | NEW → RUNNABLE → RUNNING → BLOCKED/WAITING → TERMINATED |
| **Priority** | 1-10 (MIN=1, NORM=5, MAX=10); preemptive scheduling |
| **Synchronization** | `synchronized` keyword; object lock; prevents race condition |
| **wait()/notify()** | Inter-thread communication; must be in synchronized block |
| **isAlive()** | Checks if thread running |
| **join()** | Waits for thread termination |
| **Deadlock** | Circular wait; avoid with lock ordering |
| **Deprecated** | `stop()`, `suspend()`, `resume()` - don't use |

---

## 9.12 Quick Reference: Thread Methods

```java
Thread t = new Thread(runnable, "MyThread");

t.start();              // Start thread
t.run();                // DON'T CALL DIRECTLY!
t.sleep(1000);          // Static: sleep current thread
t.getName();            // Get name
t.setName("NewName");   // Set name
t.getPriority();        // Get priority (1-10)
t.setPriority(8);       // Set priority
t.isAlive();            // Is running?
t.join();               // Wait for death
t.join(1000);           // Wait with timeout
Thread.currentThread(); // Get current thread
t.getState();           // Get state (NEW, RUNNABLE, etc.)
```