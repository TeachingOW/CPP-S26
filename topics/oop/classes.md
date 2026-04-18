# Classes in  C++

This tutorial covers C++ object-oriented types and related OOP features with practical examples.
Examples follow common C++ style-guide conventions (for example, no `using namespace std;` and explicit `std::` qualification).
It also includes exception-handling concepts (adapted from `Exception.md`) as they apply to object design.

## 1. `class` vs `struct`

In C++, `class` and `struct` are almost the same. The key difference is the default access level.

- `class`: members are `private` by default
- `struct`: members are `public` by default

```cpp
#include <iostream>

class student_type {
    int id; // private by default
public:
    student_type(int value) : id(value) {}
    int getId() const { return id; }
};

struct student_record {
    int id; // public by default
};

int main() {
    student_type a(101);
    std::cout << a.getId() << "\n";

    student_record b{202};
    std::cout << b.id << "\n";
}
```

Use `struct` for simple data types and `class` for encapsulated behavior-heavy types (common convention, not a rule).

## 2. Access Specifiers: `public`, `private`, `protected`

- `public`: accessible anywhere the object is visible
- `private`: accessible only inside the same class (and friends)
- `protected`: accessible in the class and derived classes

```cpp
#include <iostream>

class account {
private:
    double balance;

protected:
    int accountId;

public:
    account(int id, double initial) : balance(initial), accountId(id) {}

    void deposit(double amount) {
        if (amount > 0) balance += amount;
    }

    double getBalance() const { return balance; }
};

class savings_account : public account {
public:
    savings_account(int id, double initial) : account(id, initial) {}

    void printId() const {
        std::cout << "account ID: " << accountId << "\n"; // protected: OK
        // std::cout << balance; // private: not accessible
    }
};
```

## 3. Basic Class Example

```cpp
#include <iostream>
#include <string>

class rectangle {
private:
    double width;
    double height;

public:
    rectangle(double w, double h) : width(w), height(h) {}

    double area() const {
        return width * height;
    }

    void resize(double w, double h) {
        width = w;
        height = h;
    }
};

int main() {
    rectangle r(4.0, 2.5);
    std::cout << "Area: " << r.area() << "\n";
    r.resize(10, 3);
    std::cout << "Area: " << r.area() << "\n";
}
```

## 4. Constructors and Destructors

Note: In C++, the correct term is **destructor** (not "deconstructor").

### 4.1 Default Constructor

A default constructor can be called with no arguments.

```cpp
#include <iostream>

class point {
public:
    int x;
    int y;

    point() : x(0), y(0) {} // default constructor
    point(int xVal, int yVal) : x(xVal), y(yVal) {}
};

int main() {
    point p1;        // default constructor
    point p2(3, 4);  // parameterized constructor
    std::cout << p1.x << "," << p1.y << "\n";
    std::cout << p2.x << "," << p2.y << "\n";
}
```

### 4.2 Destructor

Destructors are used for cleanup. A class can only have one destructor.

```cpp
#include <iostream>

class logger {
public:
    logger() { std::cout << "logger created\n"; }
    ~logger() { std::cout << "logger destroyed\n"; }
};

int main() {
    logger log;
    std::cout << "Inside main\n";
}
```

## 5. Copy Constructor, Assignment Operator, and Rule of Three

If your class manages a resource manually (dynamic memory, file handle, socket, etc.), you usually need:

- destructor
- copy constructor
- copy assignment operator

### 5.1 Copy Constructor

The copy constructor creates a new object from an existing object.

```cpp
#include <iostream>
#include <string>

class string_box {
private:
    std::string data;

public:
    explicit string_box(std::string text = "") : data(text) {}

    // Copy constructor
    string_box(const string_box& other) {
        data = other.data;
    }

    void print() const {
        std::cout << data << "\n";
    }
};

int main() {
    string_box a("hello");
    string_box b = a; // copy constructor
    a.print();
    b.print();
}
```

### 5.2 Assignment Operator

Assignment copies into an already-existing object.

```cpp
#include <iostream>
#include <string>

class string_box {
private:
    std::string data;

public:
    explicit string_box(std::string text = "") : data(text) {}
    string_box(const string_box& other) : data(other.data) {}

    string_box& operator=(const string_box& other) {
        data = other.data;
        return *this;
    }

    void print() const {
        std::cout << data << "\n";
    }
};

int main() {
    string_box a("one");
    string_box b("two");
    b = a; // assignment operator
    b.print();
}
```

## 6. Inheritance and Access Modes

Inheritance lets one class reuse and extend another.

### 6.1 Public Inheritance

Represents an "is-a" relationship.

```cpp
#include <iostream>

class animal {
public:
    void eat() const { std::cout << "animal eating\n"; }
};

class dog : public animal {
public:
    void bark() const { std::cout << "Woof!\n"; }
};

int main() {
    dog d;
    d.eat();  // inherited public stays public
    d.bark();
}
```

### 6.2 Private Inheritance

Inherited public/protected members become `private` inside the derived class.

```cpp
#include <iostream>

class engine {
public:
    void start() const { std::cout << "engine started\n"; }
};

class car : private engine {
public:
    void drive() {
        start(); // OK inside car
        std::cout << "car driving\n";
    }
};

int main() {
    car c;
    c.drive();
    // c.start(); // error: start is private in car
}
```

### 6.3 Protected Inheritance

Inherited public/protected members become `protected` in the derived class.

```cpp
#include <iostream>

class device {
public:
    void powerOn() const { std::cout << "device on\n"; }
};

class phone : protected device {
public:
    void boot() {
        powerOn(); // OK (now protected in phone)
    }
};
```

## 7. Calling the Correct Methods (Overriding, Hiding, and Qualification)

This is a common source of confusion. There are multiple "correct method" rules in C++:

### 7.1 Non-virtual methods are chosen by static type

```cpp
#include <iostream>

class base {
public:
    void speak() const { std::cout << "base::speak\n"; }
};

class derived : public base {
public:
    void speak() const { std::cout << "derived::speak\n"; } // hides base::speak
};

int main() {
    derived d;
    base& ref = d;

    d.speak(); // derived::speak
    ref.speak(); // base::speak (not virtual)
}
```

### 7.2 Virtual methods are chosen by dynamic type (runtime polymorphism)

```cpp
#include <iostream>

class base {
public:
    virtual void speak() const { std::cout << "base::speak\n"; }
    virtual ~base() = default;
};

class derived : public base {
public:
    void speak() const override { std::cout << "derived::speak\n"; }
};

int main() {
    derived d;
    base& ref = d;
    ref.speak(); // derived::speak
}
```

### 7.3 Calling a hidden base method explicitly

Use scope resolution (`base::method`) when needed.

```cpp
#include <iostream>

class base {
public:
    void show() const { std::cout << "base::show\n"; }
};

class derived : public base {
public:
    void show() const {
        std::cout << "derived::show\n";
        base::show(); // explicitly call base version
    }
};
```

## 8. Abstract Classes and Virtual Functions

An abstract class has at least one pure virtual function (`= 0`) and cannot be instantiated.

```cpp
#include <iostream>

class shape {
public:
    virtual double area() const = 0; // pure virtual
    virtual void draw() const = 0;
    virtual ~shape() = default;      // virtual destructor for polymorphic base
};

class circle : public shape {
private:
    double r;
public:
    circle(double radius) : r(radius) {}

    double area() const override { return 3.14159 * r * r; }
    void draw() const override { std::cout << "Drawing circle\n"; }
};

int main() {
    // shape s; // error: abstract class
    circle c(5.0);
    shape& s = c;
    s.draw();
    std::cout << s.area() << "\n";
}
```

## 9. Multiple Inheritance

C++ allows a class to inherit from more than one base class.

```cpp
#include <iostream>

class printer {
public:
    void print() const { std::cout << "Printing...\n"; }
};

class scanner {
public:
    void scan() const { std::cout << "Scanning...\n"; }
};

class all_in_one : public printer, public scanner {
public:
    void fax() const { std::cout << "Faxing...\n"; }
};

int main() {
    all_in_one x;
    x.print();
    x.scan();
    x.fax();
}
```

## 10. Virtual Inheritance (Diamond Problem)

Virtual inheritance is used to avoid duplicate base subobjects in a diamond hierarchy.

```cpp
#include <iostream>
#include <string>

class person {
public:
    std::string name;
    person(std::string n = "Unknown") : name(n) {}
    void identify() const { std::cout << "I am " << name << "\n"; }
};

class student : virtual public person {
public:
    student(std::string n = "student") : person(n) {}
};

class teacher : virtual public person {
public:
    teacher(std::string n = "teacher") : person(n) {}
};

class teaching_assistant : public student, public teacher {
public:
    teaching_assistant(std::string n)
        : person(n), student(n), teacher(n) {}
};

int main() {
    teaching_assistant ta("Alex");
    ta.identify(); // only one person subobject
    std::cout << ta.name << "\n"; // no ambiguity
}
```

Important rule:

- In virtual inheritance, the **most derived class** is responsible for constructing the virtual base (`person` in this example).

## 11. `friend`

`friend` gives a function or another class access to private/protected members.
Use it sparingly because it weakens encapsulation.

```cpp
#include <iostream>

class box {
private:
    int value;

public:
    box(int v) : value(v) {}

    friend void printBox(const box& b);
};

void printBox(const box& b) {
    std::cout << "box value = " << b.value << "\n"; // friend access
}

int main() {
    box b(42);
    printBox(b);
}
```

Friend class example:

```cpp
class engine;

class mechanic {
public:
    void inspect(const engine& e);
};

class engine {
private:
    int serial = 1234;
    friend class mechanic;
};

void mechanic::inspect(const engine& e) {
    // Allowed because mechanic is a friend of engine
    // std::cout << e.serial << "\n";
}
```

## 12. Operator Overloading

Operator overloading lets user-defined types behave like built-in types where appropriate.

### 12.1 Overloading `+` and `<<`

```cpp
#include <iostream>

class vector2d {
public:
    double x, y;

    vector2d(double xVal = 0, double yVal = 0) : x(xVal), y(yVal) {}

    vector2d operator+(const vector2d& other) const {
        return vector2d(x + other.x, y + other.y);
    }
};

std::ostream& operator<<(std::ostream& os, const vector2d& v) {
    os << "(" << v.x << ", " << v.y << ")";
    return os;
}

int main() {
    vector2d a(1, 2), b(3, 4);
    vector2d c = a + b;
    std::cout << c << "\n";
}
```

### 12.2 Overloading `[]` (with const and non-const versions)

```cpp
#include <iostream>
#include <stdexcept>

class int_array {
private:
    int data[3]{10, 20, 30};

public:
    int& operator[](int index) {
        if (index < 0 || index >= 3) throw std::out_of_range("Index out of range");
        return data[index];
    }

    const int& operator[](int index) const {
        if (index < 0 || index >= 3) throw std::out_of_range("Index out of range");
        return data[index];
    }
};
```

## 13. `static` Members and Methods

`static` members belong to the class itself, not to each object instance.

### 13.1 `static` Member Function

A `static` member function can be called without creating an object.
It does not have access to `this`, so it can only use:

- its parameters
- local variables
- other `static` members

```cpp
#include <iostream>

class math_utils {
public:
    static int square(int x) {
        return x * x;
    }
};

int main() {
    std::cout << math_utils::square(5) << "\n"; // call using class name
}
```

### 13.2 `static` Data Member (with `static` Method)

```cpp
#include <iostream>

class student {
private:
    static int count; // shared by all student objects

public:
    student() { ++count; }

    static int getCount() {
        return count;
    }
};

int student::count = 0; // definition (usually in a .cpp file)

int main() {
    student a;
    student b;
    std::cout << "Students created: " << student::getCount() << "\n";
}
```

Use `static` methods for utility behavior, factories, counters, or logic that belongs to the class concept but not to one specific object.

## 14. Templates: Function Templates and Class Templates

Templates let you write generic code that works with many types.

### 14.1 Function Template

```cpp
#include <iostream>

template <typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << maximum(3, 7) << "\n";
    std::cout << maximum(2.5, 1.2) << "\n";
}
```

### 14.2 Class Template

```cpp
#include <iostream>

template <typename T>
class box {
private:
    T value;

public:
    explicit box(T v) : value(v) {}
    T get() const { return value; }
};

int main() {
    box<int> a(10);
    box<double> b(3.14);
    std::cout << a.get() << "\n";
    std::cout << b.get() << "\n";
}
```

### 14.3 Why Template Code Is Usually Kept in One Header File

For templates, the compiler usually needs to see the **full definition** at the point where the template is used (instantiated).

- If you put only the declaration in a header and the definition in a `.cpp` file, other `.cpp` files may not see the definition
- That often causes linker errors such as `undefined reference`
- Keeping template declaration + definition in the same header makes the definition visible everywhere the template is used

Common pattern:

- `my_template.h` (or `.hpp`): contains both template declarations and definitions

Advanced exception:

- You *can* separate template definitions if you use **explicit instantiation**, but that is more advanced and usually not needed in beginner/intermediate code

## 15. Exceptions 

Classes and exceptions are tightly connected in C++ because of resource management and polymorphism.

### 15.1 Basics: `try`, `throw`, `catch`

- `try`: wrap code that may fail
- `throw`: signal an error
- `catch`: handle the error

```cpp
#include <iostream>
#include <stdexcept>

class bank_account {
private:
    double balance;

public:
    bank_account(double initial) : balance(initial) {
        if (initial < 0) {
            throw std::invalid_argument("Initial balance cannot be negative");
        }
    }

    void withdraw(double amount) {
        if (amount > balance) {
            throw std::runtime_error("Insufficient funds");
        }
        balance -= amount;
    }
};

int main() {
    try {
        bank_account acc(100);
        acc.withdraw(150);
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
}
```

### 15.2 Standard Exceptions and `what()`

As described in `Exception.md`, standard exceptions derive from `std::exception`, and `what()` is virtual.
That means when you catch by `const std::exception&`, the derived `what()` message is preserved.

```cpp
#include <stdexcept>
#include <iostream>

class invalid_grade : public std::runtime_error {
public:
    invalid_grade() : std::runtime_error("Grade must be between 0 and 100") {}
};

class grade_book {
public:
    void setGrade(int g) {
        if (g < 0 || g > 100) throw invalid_grade();
    }
};

int main() {
    try {
        grade_book gb;
        gb.setGrade(150);
    } catch (const std::exception& e) {
        std::cout << e.what() << "\n";
    }
}
```

### 15.3 Stack Unwinding and Destructors (RAII)

When an exception is thrown, local objects are destroyed automatically during stack unwinding.
This is why destructors and RAII are so important.

```cpp
#include <iostream>
#include <stdexcept>

class guard {
public:
    guard() { std::cout << "Acquire resource\n"; }
    ~guard() { std::cout << "Release resource\n"; }
};

void risky() {
    guard g;
    throw std::runtime_error("Something failed");
}

int main() {
    try {
        risky();
    } catch (const std::exception& e) {
        std::cout << "Caught: " << e.what() << "\n";
    }
}
```

Key takeaway:

- Prefer classes that manage resources in constructors/destructors (RAII)
- Throw exceptions for runtime errors
- Catch exceptions by `const` reference (`const std::exception&`)

## 16. Common Mistakes and Best Practices

### Mistakes

- Forgetting a virtual destructor in a polymorphic base class
- Catching exceptions by value instead of `const` reference
- Returning references to local variables
- Using `friend` too much
- Writing shallow copies for resource-owning classes
- Hiding base methods accidentally (without `virtual` / `override`)

### Best Practices

- Use `override` for overridden virtual functions
- Mark read-only methods `const`
- Prefer composition over inheritance unless there is a clear "is-a" relationship
- Use public inheritance for polymorphism
- Use RAII and standard library containers (`std::string`, `std::vector`) to avoid manual memory bugs
- If you implement one of destructor/copy constructor/copy assignment for resource management, consider the full Rule of Three (or Rule of Five in modern C++)

## 17. Splitting Code into Files and Compiling

As programs grow, put declarations and implementations in separate files.

Typical layout:

- Header file (`.h` / `.hpp`): class declaration
- Source file (`.cpp`): method definitions
- `main.cpp`: program entry point and usage

### 17.1 Example: `bank_account` split into files

`bank_account.h`

```cpp
#ifndef BANK_ACCOUNT_H
#define BANK_ACCOUNT_H

#include <stdexcept>

class bank_account {
public:
    explicit bank_account(double initial_balance = 0.0);

    void deposit(double amount);
    void withdraw(double amount);
    double balance() const;

private:
    double balance_;
};

#endif
```

`bank_account.cpp`

```cpp
#include "bank_account.h"

bank_account::bank_account(double initial_balance) : balance_(initial_balance) {
    if (initial_balance < 0.0) {
        throw std::invalid_argument("Initial balance cannot be negative");
    }
}

void bank_account::deposit(double amount) {
    if (amount > 0.0) {
        balance_ += amount;
    }
}

void bank_account::withdraw(double amount) {
    if (amount > balance_) {
        throw std::runtime_error("Insufficient funds");
    }
    balance_ -= amount;
}

double bank_account::balance() const {
    return balance_;
}
```

`main.cpp`

```cpp
#include <exception>
#include <iostream>

#include "bank_account.h"

int main() {
    try {
        bank_account acct(100.0);
        acct.deposit(50.0);
        acct.withdraw(25.0);
        std::cout << "Balance: " << acct.balance() << "\n";
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << "\n";
    }
}
```

### 17.2 How to Compile (with `g++`)

Compile all `.cpp` files together:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp bank_account.cpp -o app
```

Run:

```bash
./app
```

### 17.3 Separate Compilation (Object Files)

This is common in larger projects because only changed files need recompiling.

```bash
g++ -std=c++17 -Wall -Wextra -pedantic -c bank_account.cpp -o bank_account.o
g++ -std=c++17 -Wall -Wextra -pedantic -c main.cpp -o main.o
g++ main.o bank_account.o -o app
```

### 17.4 Header and Include Tips

- Put declarations in headers and definitions in `.cpp` files
- Use include guards (`#ifndef`, `#define`, `#endif`) or `#pragma once`
- Include only what you need
- Keep headers self-contained when possible
- Do not put non-`inline` function definitions in headers unless you understand linker behavior
- Template functions/classes are usually fully defined in headers so the compiler can instantiate them where they are used

### 17.5 Common Compile Errors

- `undefined reference to ...`
  Cause: a `.cpp` file was not compiled/linked, or a function was declared but not defined
- `multiple definition of ...`
  Cause: a non-`inline` definition was placed in a header included by multiple `.cpp` files
- `No such file or directory` (header)
  Cause: wrong include path or incorrect `#include`
- Method signature mismatch
  Cause: declaration in the header does not exactly match the definition in the source file

## 18. Practice Exercises

1. Create a `student` class with private members and public getters/setters.
2. Create an abstract base class `shape` and derive `rectangle` and `triangle`.
3. Implement a `matrix2x2` class with overloaded `+` and `<<`.
4. Build a diamond hierarchy with and without virtual inheritance and observe the difference.
5. Create a custom exception class for invalid user input and use it in a class method.

## 19. Related Notes

- `topics/oop/PillarsofOOP.md`
- `topics/advanced/ruleofFive.md`
