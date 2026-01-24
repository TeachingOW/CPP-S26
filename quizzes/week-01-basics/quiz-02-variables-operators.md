# Quiz 2: Variables and Operators

---

## Quiz Information

| **Field** | **Details** |
|-----------|-------------|
| **Week** | Week 1 |
| **Topic** | Variables, Data Types & Operators |
| **Duration** | 20 minutes |
| **Total Points** | 35 points |
| **Difficulty** | 🟢 Easy to 🟡 Medium |

---

## Instructions

### Before You Begin
1. Write your name at the top of this page
2. Read all questions before starting
3. Budget your time wisely - approximately 1.5 minutes per question
4. Show your work for partial credit

### During the Quiz
- ✅ You **MAY** use: Pen/pencil
- ❌ You **MAY NOT** use: Notes, textbook, calculator, phone, computer
- Write legibly - illegible answers may not receive credit

---

## Questions

### Section 1: Multiple Choice (2 points each)

**Question 1:** 🟢 Which of the following is NOT a valid variable name in C++?

A) `_count`  
B) `2ndValue`  
C) `myVariable`  
D) `total_sum`

**Answer:** _______

---

**Question 2:** 🟢 What is the size of an `int` on most modern 32-bit and 64-bit systems?

A) 2 bytes  
B) 4 bytes  
C) 8 bytes  
D) Depends on the compiler

**Answer:** _______

---

**Question 3:** 🟡 What is the result of `5 / 2` in C++?

A) `2.5`  
B) `2`  
C) `3`  
D) Compilation error

**Answer:** _______

---

**Question 4:** 🟡 Which operator has the highest precedence?

A) `+` (addition)  
B) `*` (multiplication)  
C) `=` (assignment)  
D) `()` (parentheses)

**Answer:** _______

---

**Question 5:** 🟢 What does the `const` keyword do when applied to a variable?

A) Makes the variable global  
B) Makes the variable unchangeable after initialization  
C) Allocates the variable on the heap  
D) Makes the variable private

**Answer:** _______

---

### Section 2: True/False (1 point each)

**Question 6:** 🟢 In C++, `int x;` automatically initializes `x` to 0.

**Answer:** _______ (T/F)

---

**Question 7:** 🟢 The operators `++x` and `x++` always produce the same result in an expression.

**Answer:** _______ (T/F)

---

**Question 8:** 🟢 The modulus operator `%` can be used with floating-point numbers.

**Answer:** _______ (T/F)

---

**Question 9:** 🟡 The statement `int x = 5, y = 10, z;` declares three integers and initializes all of them.

**Answer:** _______ (T/F)

---

**Question 10:** 🟡 Type casting with `(int)` is preferred over `static_cast<int>()` in modern C++.

**Answer:** _______ (T/F)

---

### Section 3: Code Output Prediction (3 points each)

**Question 11:** 🟡 What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    int y = x++;
    cout << x << " " << y;
    return 0;
}
```

**Output:** _______________________

---

**Question 12:** 🟡 What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10;
    int b = 3;
    cout << a / b << " " << a % b;
    return 0;
}
```

**Output:** _______________________

---

**Question 13:** 🔴 What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 5;
    x += ++x;
    cout << x;
    return 0;
}
```

**Output:** _______________________

---

### Section 4: Code Completion (4 points each)

**Question 14:** 🟡 Complete this program to swap two variables without using a temporary variable (using arithmetic operations):

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;
    
    // Your code here (3 lines)
    
    
    
    
    cout << "a = " << a << ", b = " << b;
    return 0;
}
```

**Your Answer:**
```cpp




```

---

**Question 15:** 🟡 Complete the variable declarations with appropriate data types:

```cpp
_______ age = 25;                    // Whole number
_______ price = 19.99;               // Decimal number
_______ grade = 'A';                 // Single character
_______ isStudent = true;            // Boolean value
_______ PI = 3.14159;                // Constant decimal
```

**Your Answer:**
```cpp






```

---

## Bonus Question (Optional - 3 points extra credit)

🌟 **Challenge:** Explain the difference between `5 / 2`, `5.0 / 2`, and `5 / 2.0`. What is the output of each expression and why?

**Answer:**
```




```

---

## Honor Code Statement

I affirm that I have neither given nor received any unauthorized assistance on this quiz.

**Signature:** _________________________ **Date:** _____________

---

## Quick Reference

### Common Data Types
```cpp
int      // Integer: 42, -10
double   // Floating-point: 3.14, -0.5
float    // Single precision: 3.14f
char     // Character: 'A', 'x'
bool     // Boolean: true, false
string   // String: "hello" (requires #include <string>)
```

### Operators
```cpp
// Arithmetic: +, -, *, /, %
// Assignment: =, +=, -=, *=, /=, %=
// Increment/Decrement: ++, --
// Comparison: ==, !=, <, >, <=, >=
// Logical: &&, ||, !
```

### Operator Precedence (High to Low)
1. `()` - Parentheses
2. `++ --` - Increment/Decrement
3. `* / %` - Multiplication, Division, Modulus
4. `+ -` - Addition, Subtraction
5. `< > <= >=` - Comparison
6. `== !=` - Equality
7. `&&` - Logical AND
8. `||` - Logical OR
9. `=` - Assignment
