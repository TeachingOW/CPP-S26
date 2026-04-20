# Slide Update Recommendations

This document provides recommendations for updating the course PowerPoint slides to include modern C++ features and improve content organization.

## Current Slide Decks

1. **cpp-part1.pptx** - C++ Fundamentals (Weeks 1-6)
2. **cpp-part2.pptx** - Advanced C++ and OOP (Weeks 7-14)

---

## Priority Updates

### High Priority Topics to Add

#### 1. Template Specialization
**Slide Location:** cpp-part2.pptx (Templates section)

**Content to Add:**
- Introduction to template specialization
- Full template specialization
- Partial template specialization
- Use cases and examples
- Performance considerations

**Sample Code:**
```cpp
// Full specialization
template<typename T>
class Container { /* generic implementation */ };

template<>
class Container<bool> { /* specialized for bool */ };

// Partial specialization
template<typename T>
class Container<T*> { /* specialized for pointers */ };
```

---

#### 2. lvalue, rvalue, and Move Semantics
**Slide Location:** cpp-part2.pptx (New section after Rule of Three)

**Content to Add:**
- Value categories: lvalue vs rvalue
- Move constructors
- Move assignment operators
- std::move utility
- std::forward and perfect forwarding
- Rule of Five (extend Rule of Three)

**Visual Aids:**
- Memory diagrams showing move vs copy
- Performance comparison charts
- Step-by-step move operation visualization

**Sample Code:**
```cpp
class MyClass {
public:
    // Move constructor
    MyClass(MyClass&& other) noexcept 
        : data(std::move(other.data)) {
        other.data = nullptr;
    }
    
    // Move assignment
    MyClass& operator=(MyClass&& other) noexcept {
        if (this != &other) {
            delete data;
            data = other.data;
            other.data = nullptr;
        }
        return *this;
    }
private:
    int* data;
};
```

---

#### 3. Smart Pointers (Expanded)
**Slide Location:** cpp-part2.pptx (Memory Management section)

**Current Status:** Basic coverage exists  
**Improvements Needed:**
- More detailed `unique_ptr` examples
- Shared ownership with `shared_ptr`
- Weak references with `weak_ptr`
- Custom deleters
- Performance implications
- When to use which type

**Content to Add:**

**unique_ptr:**
```cpp
auto ptr = std::make_unique<int>(42);
// Automatic cleanup, no copies, movable
```

**shared_ptr:**
```cpp
auto ptr1 = std::make_shared<int>(42);
auto ptr2 = ptr1;  // Reference count = 2
// Automatic cleanup when last reference goes away
```

**weak_ptr:**
```cpp
std::shared_ptr<int> shared = std::make_shared<int>(42);
std::weak_ptr<int> weak = shared;
// Doesn't affect reference count
```

**Visual Aids:**
- Reference counting diagrams
- Memory ownership charts
- Decision tree: which smart pointer to use

---

#### 4. Scoped Enums (enum class)
**Slide Location:** cpp-part2.pptx (Types and enumerations section)

**Content to Add:**
- Problems with traditional enums
- Scoped enum syntax
- Type safety benefits
- No implicit conversions
- Scope resolution

**Comparison:**
```cpp
// Traditional enum (unscoped)
enum Color { black, white, red };
Color c = black;  // No scope needed
int value = black;  // Implicit conversion

// Scoped enum (enum class)
enum class Color { black, white, red };
Color c = Color::black;  // Scope required
// int value = Color::black;  // Error! No implicit conversion

auto white = false;  // OK - white doesn't pollute namespace
```

---

### Medium Priority Updates

#### 5. Lambda Expressions (Enhanced)
**Slide Location:** cpp-part2.pptx (Lambda section)

**Improvements:**
- More complex capture examples
- Generic lambdas (auto parameters)
- Mutable lambdas
- Return type deduction
- Common use cases with STL algorithms

---

#### 6. C++11/14/17/20 Feature Overview
**Slide Location:** cpp-part2.pptx (New section or expanded existing)

**Topics to Cover:**

**C++11:**
- auto and decltype
- nullptr
- Range-based for loops
- constexpr
- Uniform initialization
- Move semantics
- Lambda expressions
- Smart pointers

**C++14:**
- Generic lambdas
- Return type deduction for functions
- Binary literals
- std::make_unique

**C++17:**
- Structured bindings
- if/switch with initializers
- std::optional
- std::variant
- std::string_view
- Fold expressions

**C++20 (Preview):**
- Concepts
- Ranges
- Coroutines
- Modules

---

#### 7. Virtual Functions and Polymorphism (Enhanced)
**Slide Location:** cpp-part2.pptx (OOP/Polymorphism section)

**Add Example from Course Outline:**
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
    b.hi();  // Polymorphic call
}

int main() {
    Derived x;
    foo(x);  // Outputs: b
    Base y;
    foo(y);  // Outputs: a
}
```

**Visual Aids:**
- Virtual table (vtable) diagrams
- Polymorphic call resolution
- Override vs overload

---

### Low Priority Improvements

#### 8. Exception Handling (Enhanced)
- Exception safety guarantees
- RAII and exception safety
- noexcept specifier
- Custom exception classes

#### 9. Const Correctness
- const member functions
- const references
- const pointers vs pointer to const
- mutable keyword

#### 10. Type Traits and SFINAE
- Basic type traits
- Compile-time type checking
- SFINAE basics
- Concepts as modern alternative

---

## Organizational Recommendations

### Slide Numbering
- Use consistent numbering scheme
- Add slide numbers to all slides
- Include total slide count

### Section Organization

**Recommended Structure for cpp-part1.pptx:**
1. Introduction and Setup
2. Basic Syntax and Types
3. Control Structures
4. Functions
5. Arrays and Pointers
6. References

**Recommended Structure for cpp-part2.pptx:**
1. OOP Fundamentals
2. Constructors and Destructors
3. Rule of Three/Five
4. Inheritance
5. Polymorphism
6. Templates
7. STL
8. Modern C++ Features
9. Move Semantics
10. Smart Pointers

---

## Visual Design Guidelines

### Consistency
- Use consistent fonts across all slides
- Maintain color scheme
- Standardize code block formatting
- Use similar diagram styles

### Code Examples
- Syntax highlighting for readability
- Line numbers for reference
- Comments for explanation
- Clear, concise examples

### Diagrams
- Memory layouts for pointer concepts
- Class hierarchy diagrams for inheritance
- Flowcharts for algorithms
- UML diagrams where appropriate

### Best Practices
- One concept per slide (where possible)
- Avoid text walls
- Use bullet points effectively
- Include visual aids
- Provide real-world examples

---

## Code Examples to Incorporate

### From Repository
- [code-examples/basic/pointers.cpp](../code-examples/basic/pointers.cpp)
- [code-examples/file-handling/](https://github.com/TeachingOW/CPP-S26/tree/main/code-examples/file-handling)
- [code-examples/bmp/](https://github.com/TeachingOW/CPP-S26/tree/main/code-examples/bmp)
- Examples from lecture Gists

### To Create
- Move semantics demonstrations
- Smart pointer usage patterns
- Template specialization examples
- Modern C++ feature showcases

---

## Interactive Elements

### Recommendations
- Add quiz slides for key concepts
- Include "Try it yourself" exercises
- Provide links to online compilers (godbolt.org, compiler explorer)
- Reference course GitHub repository
- Link to video demonstrations

---

## Accessibility

### Guidelines
- High contrast text and backgrounds
- Readable font sizes (minimum 18pt for body text)
- Alt text for images
- Clear diagram labels
- Avoid relying solely on color coding

---

## Version Control

### Recommendations
- Version number on title slide
- Change log in notes section
- Date of last update
- Track major revisions

**Format:** `v[Major].[Minor].[Patch] - YYYY-MM-DD`

Example: `v2.1.0 - 2026-01-24`

---

## Testing and Validation

### Before Finalizing Updates
- [ ] All code examples compile
- [ ] Code examples demonstrate intended concepts
- [ ] Diagrams are clear and accurate
- [ ] Links work correctly
- [ ] Slides flow logically
- [ ] No spelling/grammar errors
- [ ] Technical accuracy verified
- [ ] Peer review completed

---

## Implementation Priority

### Phase 1 (High Priority)
1. Add move semantics section
2. Expand smart pointers coverage
3. Add template specialization
4. Include scoped enums

### Phase 2 (Medium Priority)
1. Enhance lambda expression coverage
2. Add C++11/14/17 feature overview
3. Improve polymorphism examples
4. Update visual consistency

### Phase 3 (Low Priority)
1. Add exception safety content
2. Include const correctness section
3. Add type traits basics
4. Improve accessibility

---

## Resources for Slide Creation

### Reference Materials
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/)
- [cppreference.com](https://en.cppreference.com/)
- Scott Meyers' Effective C++ books
- Course [COURSE_OUTLINE.md](../COURSE_OUTLINE.md)

### Tools
- [Mermaid](https://mermaid.js.org/) for diagrams
- [Carbon](https://carbon.now.sh/) for code screenshots
- [Python Tutor](https://pythontutor.com/cpp.html) for visualizations
- [Compiler Explorer](https://godbolt.org/) for assembly comparisons

---

**Last Updated:** January 2026  
**Next Review:** Start of next semester  
**Maintainer:** Course Instructor

**Note:** These are recommendations. Actual implementation should be discussed with the teaching team.
