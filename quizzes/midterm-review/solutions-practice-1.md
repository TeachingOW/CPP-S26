# Solutions: Practice Quiz 1 - Midterm Review

---

## Answer Key and Explanations

### Part 1: Multiple Choice

**Question 1:** B) `#include <iostream>`
**Explanation:** Standard C++ uses `<iostream>` for I/O, not the C-style `<stdio.h>`.

**Question 2:** B) `3`
**Explanation:** Integer division truncates the decimal part. 10/3 = 3 remainder 1.

**Question 3:** D) `6 6` (then x becomes 7)
**Explanation:** `++x` increments first (x=6), prints 6. Then `x++` prints current value (6) then increments to 7.

**Question 4:** C) `do-while` loop
**Explanation:** do-while checks condition AFTER executing, guaranteeing at least one iteration.

**Question 5:** B) `int *ptr;`
**Explanation:** The asterisk (*) declares a pointer to int.

**Question 6:** B) Frees dynamically allocated memory
**Explanation:** delete releases memory allocated with new.

**Question 7:** C) `class MyClass { public: int x; };`
**Explanation:** Classes need semicolon after closing brace. Public members are accessible outside class.

**Question 8:** B) To initialize an object when it is created
**Explanation:** Constructors set up initial object state.

**Question 9:** B) Enables runtime polymorphism
**Explanation:** Virtual functions allow derived classes to override base class methods with dynamic dispatch.

**Question 10:** C) Local scope (function scope)
**Explanation:** Variables declared in functions are local to that function.

---

### Part 2: True/False

**Question 21:** F (False) - Local variables are NOT automatically initialized.

**Question 22:** T (True) - break exits the loop immediately.

**Question 23:** T (True) - Pointers can be reassigned.

**Question 24:** T (True) - Compiler provides default constructor if you don't define any.

**Question 25:** F (False) - Private members are NOT accessible in derived classes (use protected instead).

---

### Part 3: Code Output

**Question 31:** `3 4`
**Explanation:** arr+2 points to third element (3). ptr+1 points to fourth element (4).

**Question 32:** `Derived`
**Explanation:** Virtual function enables runtime polymorphism, calling Derived's version.

---

### Part 4: Bug Finding

**Question 37 Bugs:**
1. Missing semicolon after `return width * height`
2. Memory leak - need `delete r;` before return
3. Consider making destructor virtual if this will be a base class

**Fixed Code:**
```cpp
#include <iostream>
using namespace std;

class Rectangle {
    int width, height;
public:
    Rectangle(int w, int h) : width(w), height(h) {}
    
    int getArea() {
        return width * height;  // Added semicolon
    }
};

int main() {
    Rectangle *r = new Rectangle(10, 5);
    cout << r->getArea();
    delete r;  // Fixed memory leak
    return 0;
}
```

---

### Part 5: Code Writing

**Question 40:** Sample Solution

```cpp
int findMax(int arr[], int size) {
    if (size <= 0) return 0;  // Handle edge case
    
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}
```

**Question 41:** Pass-by-value vs Pass-by-reference

**Answer:** Pass-by-value creates a copy of the argument (safe but slower for large objects). Pass-by-reference passes the actual variable (faster, allows modification). Use pass-by-value for small types and when you don't want to modify the original. Use pass-by-reference for large objects or when you need to modify the original.

---

## Performance Guidelines

- 70-100: Well prepared for midterm
- 50-69: Review weak areas before exam
- Below 50: Schedule additional study sessions

**Focus areas for improvement:**
- If struggling with Q1-10: Review C++ basics
- If struggling with Q11-20: Review OOP concepts
- If struggling with code output: Practice tracing execution
- If struggling with bug finding: Practice debugging

---

*Review corresponding course materials for questions you missed*
