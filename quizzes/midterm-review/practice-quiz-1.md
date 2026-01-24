# Practice Quiz 1: Midterm Review

---

## Quiz Information

| **Field** | **Details** |
|-----------|-------------|
| **Coverage** | Weeks 1-6 (C++ Basics through OOP Advanced) |
| **Purpose** | Midterm Exam Preparation |
| **Duration** | 50 minutes |
| **Total Points** | 100 points |
| **Difficulty** | 🟡 Medium to 🔴 Hard (Comprehensive) |

---

## Instructions

### Purpose of This Practice Quiz
This practice quiz simulates the format and difficulty of the actual midterm exam. Use it to:
- Identify knowledge gaps
- Practice time management
- Build confidence for the midterm
- Review key concepts from Weeks 1-6

### Before You Begin
1. Set a timer for 50 minutes
2. Find a quiet place without distractions
3. Have scratch paper ready
4. Read all instructions carefully

### During the Quiz
- ✅ You **MAY** use: Pen/pencil, scratch paper
- ❌ You **MAY NOT** use: Notes, textbook, IDE, internet, calculator
- Simulate real exam conditions
- Show all work for partial credit

---

## Questions

### Part 1: Multiple Choice (2 points each, 20 questions = 40 points)

**Question 1:** 🟢 Which of the following correctly includes the C++ I/O library?

A) `#include <stdio.h>`  
B) `#include <iostream>`  
C) `#include <io.h>`  
D) `import iostream`

**Answer:** _______

---

**Question 2:** 🟢 What is the result of `10 / 3` in C++?

A) `3.33`  
B) `3`  
C) `4`  
D) `3.0`

**Answer:** _______

---

**Question 3:** 🟡 What is the output of the following code?

```cpp
int x = 5;
cout << ++x << " " << x++;
```

A) `5 5`  
B) `6 6`  
C) `6 7`  
D) `6 6` (then x becomes 7)

**Answer:** _______

---

**Question 4:** 🟡 Which loop is guaranteed to execute at least once?

A) `for` loop  
B) `while` loop  
C) `do-while` loop  
D) All loops execute at least once

**Answer:** _______

---

**Question 5:** 🟡 What is the correct way to declare a pointer to an integer?

A) `int ptr;`  
B) `int *ptr;`  
C) `pointer<int> ptr;`  
D) `int &ptr;`

**Answer:** _______

---

**Question 6:** 🟡 What does the `delete` operator do in C++?

A) Removes a file from disk  
B) Frees dynamically allocated memory  
C) Deletes a variable from the stack  
D) Removes a function from memory

**Answer:** _______

---

**Question 7:** 🔴 Which correctly defines a class in C++?

A) `class MyClass ( int x; )`  
B) `Class MyClass { int x; }`  
C) `class MyClass { public: int x; };`  
D) `class MyClass { int x }`

**Answer:** _______

---

**Question 8:** 🔴 What is the purpose of a constructor?

A) To destroy an object when it goes out of scope  
B) To initialize an object when it is created  
C) To declare a new class  
D) To inherit from a parent class

**Answer:** _______

---

**Question 9:** 🔴 What does the `virtual` keyword enable in C++?

A) Makes a function private  
B) Enables runtime polymorphism  
C) Creates a virtual machine  
D) Makes memory allocation virtual

**Answer:** _______

---

**Question 10:** 🟡 What is the scope of a variable declared inside a function?

A) Global scope  
B) File scope  
C) Local scope (function scope)  
D) Class scope

**Answer:** _______

---

**Question 11-20:** [Additional questions covering operators, control structures, functions, pointers, arrays, classes, inheritance, and polymorphism]

---

### Part 2: True/False (1 point each, 10 questions = 10 points)

**Question 21:** 🟢 In C++, local variables are automatically initialized to 0.

**Answer:** _______ (T/F)

---

**Question 22:** 🟢 The `break` statement exits a loop immediately.

**Answer:** _______ (T/F)

---

**Question 23:** 🟡 A pointer can be reassigned to point to different variables.

**Answer:** _______ (T/F)

---

**Question 24:** 🟡 A class automatically gets a default constructor if you don't define any constructors.

**Answer:** _______ (T/F)

---

**Question 25:** 🔴 Derived classes can access private members of their base class.

**Answer:** _______ (T/F)

---

[Questions 26-30 continue...]

---

### Part 3: Code Output Prediction (3 points each, 6 questions = 18 points)

**Question 31:** 🟡 What is the exact output?

```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *ptr = arr + 2;
    cout << *ptr << " " << *(ptr + 1);
    return 0;
}
```

**Output:** _______________________

---

**Question 32:** �� What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() { cout << "Base"; }
};

class Derived : public Base {
public:
    void show() { cout << "Derived"; }
};

int main() {
    Base *ptr = new Derived();
    ptr->show();
    delete ptr;
    return 0;
}
```

**Output:** _______________________

---

[Questions 33-36 continue...]

---

### Part 4: Bug Finding (6 points each, 3 questions = 18 points)

**Question 37:** 🔴 Find ALL bugs in this code and fix them:

```cpp
#include <iostream>
using namespace std;

class Rectangle {
    int width, height;
public:
    Rectangle(int w, int h) {
        width = w;
        height = h;
    }
    
    int getArea() {
        return width * height
    }
};

int main() {
    Rectangle *r = new Rectangle(10, 5);
    cout << r->getArea();
}
```

**Bugs Found:**
1. _________________________________
2. _________________________________
3. _________________________________

**Fixed Code:**
```cpp




```

---

[Questions 38-39 continue...]

---

### Part 5: Short Answer / Code Writing (7 points each, 2 questions = 14 points)

**Question 40:** 🔴 Write a function that takes an array of integers and its size, and returns the largest element.

```cpp
// Your function here






```

---

**Question 41:** 🔴 Explain the difference between pass-by-value and pass-by-reference in C++. When should you use each?

**Answer:**
```




```

---

## Bonus Question (5 points)

🌟 **Challenge:** Implement a simple linked list node class and a function to insert a node at the beginning of the list.

```cpp




```

---

## Study Tips

- Review all quiz solutions from weeks 1-6
- Practice writing code by hand
- Understand concepts, don't just memorize
- Time yourself on practice problems
- Focus on weak areas

---

**Review solutions in solutions-practice-1.md after completing**
