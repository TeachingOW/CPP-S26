# C++ Course Outline and Planning

This document outlines topics to cover, problems to assign, and resources to incorporate into the C++ course.

## Core C++ Topics to Cover

### 1. Template Specialization
**Priority:** High  
**Description:** Full and partial template specialization techniques  
**Prerequisites:** Templates, generics  
**Resources:**
- See [topics/cpp-fundamentals/templates.md](topics/cpp-fundamentals/templates.md)
- Add examples in [code-examples/](https://github.com/TeachingOW/CPP-S26/tree/main/code-examples)

---

### 2. lvalue, rvalue, and Move Semantics
**Priority:** High  
**Description:** Understanding value categories and move semantics in modern C++  
**Topics to Cover:**
- lvalue vs rvalue
- Move constructors
- Move assignment operators  
- std::move and std::forward
- Perfect forwarding

**Prerequisites:** Rule of Three, references, pointers  
**Related Topics:** Rule of Five

---

### 3. Smart Pointers
**Priority:** High  
**Description:** Modern C++ memory management with smart pointers  
**Coverage:**
- `std::unique_ptr` - Exclusive ownership
- `std::shared_ptr` - Shared ownership  
- `std::weak_ptr` - Non-owning references
- Custom deleters
- Performance considerations

**Prerequisites:** Pointers, RAII, destructors  
**Resources:**
- See [topics/advanced/smartpointers.md](topics/advanced/smartpointers.md)

---

### 4. Scoped Enums (enum class)
**Priority:** Medium  
**Description:** Type-safe enumerations in modern C++  

**Example:**
```cpp
// Traditional enum (unscoped)
enum Color { black, white, red };

// Scoped enum (enum class)
enum class Color { black, white, red };
Color c = Color::red;  // Requires scope resolution

auto white = false;  // OK - white is now scoped
```

**Advantages:**
- Type safety
- No implicit conversions
- Scoped names (avoid naming conflicts)

---

### 5. Member vs Non-Member Functions
**Priority:** Medium  
**Description:** When to use member functions vs non-member functions  
**Topics:**
- Friend functions
- Operator overloading best practices
- Interface design principles

**Example:**
```cpp
struct Base {
    virtual void hi() { cout << "a"; }
};

struct Derived : Base {
    void hi() override { cout << "b"; }
};

void foo(Base &b) {
    b.hi();  // Polymorphic call
}

int main() {
    Derived x;
    foo(x);  // Outputs: b
    Base y;
    foo(y);  // Outputs: a
}
```

---

## LeetCode Problems to Assign

### Dynamic Programming
1. [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/description/)
   - **Difficulty:** Medium
   - **Topics:** DP, recursion, memoization

2. [Ways to Express an Integer as Sum of Powers](https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/)
   - **Difficulty:** Medium
   - **Topics:** DP, backtracking

---

### Design Problems
3. [Design a Text Editor](https://leetcode.com/problems/design-a-text-editor/description/?envType=problem-list-v2&envId=design)
   - **Difficulty:** Hard
   - **Topics:** Data structures, string manipulation
   - **Skills:** Class design, implementation

4. [Design an ATM Machine](https://leetcode.com/problems/design-an-atm-machine/description/?envType=problem-list-v2&envId=design)
   - **Difficulty:** Medium
   - **Topics:** OOP, design patterns
   - **Skills:** State management, operations

5. [Finding MK Average](https://leetcode.com/problems/finding-mk-average/description/?envType=problem-list-v2&envId=design)
   - **Difficulty:** Hard
   - **Topics:** Data structures, design
   - **Skills:** Efficient data structure design

6. [Design Parking System](https://leetcode.com/problems/design-parking-system/description/?envType=problem-list-v2&envId=design)
   - **Difficulty:** Easy
   - **Topics:** OOP basics, simple design
   - **Skills:** Class design fundamentals

7. [Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/?envType=problem-list-v2&envId=design)
   - **Difficulty:** Hard
   - **Topics:** Intervals, data structures
   - **Skills:** Complex data structure design

---

### Already Assigned
8. **Design Circular Queue** (Lecture 10/22)
   - [LeetCode Link](https://leetcode.com/problems/design-circular-queue/)
   - **Status:** Completed in class

---

## Video Resources

### Primary Course Videos
- **[C++ Programming Playlist](https://www.youtube.com/playlist?list=PLvv0ScY6vfd8j-tlhYVPYgiIyXduu6m-L)**
  - Main course lecture recordings
  - Follow chronologically

### Supplementary Videos
- **[Mike Shah's C++ Course](https://www.youtube.com/watch?v=LGOgNqkRMs0&list=PLvv0ScY6vfd8j-tlhYVPYgiIyXduu6m-L&index=1)**
  - Additional explanations
  - Alternative teaching approach

- **[Additional C++ Resources](https://www.youtube.com/playlist?list=PLvv0ScY6vfd-fxDQiicYsjqAhJqZkkRH-)**
  - Advanced topics
  - Special subjects

---

## Code Examples to Add

### 1. Virtual Functions and Polymorphism
**Priority:** High

```cpp
#include <iostream>
using namespace std;

struct Base {
    virtual void hi() { cout << "a"; }
};

struct Derived : Base {
    void hi() override { cout << "b"; }
};

void foo(Base &b) {
    b.hi();
}

int main() {
    Derived x;
    foo(x);    // Outputs: b (polymorphic)
    Base y;
    foo(y);    // Outputs: a
}
```

**Location:** `code-examples/oop/virtual-functions.cpp`

---

### 2. Move Semantics Example
**Priority:** High

```cpp
#include <utility>
#include <vector>

class MyClass {
    std::vector<int> data;
public:
    // Move constructor
    MyClass(MyClass&& other) noexcept 
        : data(std::move(other.data)) {}
    
    // Move assignment
    MyClass& operator=(MyClass&& other) noexcept {
        data = std::move(other.data);
        return *this;
    }
};
```

**Location:** `code-examples/advanced/move-semantics.cpp`

---

### 3. Smart Pointer Examples
**Priority:** High

```cpp
#include <memory>

void uniquePtrExample() {
    auto ptr = std::make_unique<int>(42);
    // Automatic cleanup
}

void sharedPtrExample() {
    auto ptr1 = std::make_shared<int>(42);
    auto ptr2 = ptr1;  // Reference count = 2
}
```

**Location:** `code-examples/advanced/smart-pointers.cpp`

---

## Books and References

### Recommended Reading
1. **Scott Meyers Books**
   - Effective C++
   - More Effective C++
   - Effective Modern C++

2. **Bjarne Stroustrup**
   - The C++ Programming Language
   - Programming: Principles and Practice Using C++

---

## Course Structure Recommendations

### Week 1-4: Fundamentals
- Basic syntax, data types
- Control structures
- Functions and parameters
- Arrays and pointers

### Week 5-8: Object-Oriented Programming
- Classes and objects
- Constructors and destructors
- Inheritance
- Polymorphism
- Rule of Three

### Week 9-12: Advanced Topics
- Templates
- STL (containers, algorithms, iterators)
- Smart pointers
- Move semantics
- Exception handling

### Week 13-15: Modern C++ and Projects
- C++11/14/17 features
- Design patterns
- Final project work
- Code review and best practices

---

## Topics for Future Expansion

### C++11/14/17/20 Features
- constexpr
- auto and decltype
- Range-based for loops
- Lambda improvements
- Variadic templates
- std::optional, std::variant, std::any
- Concepts (C++20)
- Ranges (C++20)
- Modules (C++20)

### Advanced Topics
- Multithreading and concurrency
- Template metaprogramming
- Compile-time programming
- Memory models
- Custom allocators

### Practical Skills
- Build systems (CMake, Make)
- Debugging techniques
- Profiling and optimization
- Unit testing frameworks
- Version control best practices

---

## Implementation Notes

### Slide Updates Needed
- Add template specialization examples
- Include move semantics diagrams
- Expand smart pointer coverage
- Add scoped enum examples
- Include more C++11/14/17 features

See [slides/SLIDE_UPDATES.md](slides/SLIDE_UPDATES.md) for detailed recommendations.

### Assignment Ideas
- LRU Cache implementation (already assigned)
- Custom smart pointer implementation
- Template-based data structures
- Move-aware container class
- Design pattern implementations

---

**Last Updated:** January 2026  
**Course:** CPP-S26  
**Maintainer:** Course Instructor
