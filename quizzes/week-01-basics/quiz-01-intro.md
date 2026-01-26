# Quiz 1: Introduction to C++

---

## Quiz Information

| **Field** | **Details** |
|-----------|-------------|
| **Week** | Week 1 |
| **Topic** | C++ Basics - Program Structure & I/O |
| **Duration** | 15 minutes |
| **Total Points** | 30 points |
| **Difficulty** | 🟢 Easy |

---

## Instructions

### Before You Begin
1. Write your name at the top of this page
2. Read all questions before starting
3. Budget your time wisely - approximately 1 minute per question
4. Show your work for partial credit

### During the Quiz
- ✅ You **MAY** use: Pen/pencil
- ❌ You **MAY NOT** use: Notes, textbook, calculator, phone, computer
- Write legibly - illegible answers may not receive credit

---

## Questions

### Section 1: Multiple Choice (2 points each)

**Question 1:** Which header file is required for input/output operations in C++?

A) `<stdio.h>`  
B) `<iostream>`  
C) `<cstdio>`  
D) `<input.h>`

**Answer:** _______

---

**Question 2:** What is the correct way to declare the main function in C++?

A) `void main()`  
B) `int main()`  
C) `main()`  
D) `void main(void)`

**Answer:** _______

---

**Question 3:** Which statement is used to output data to the console in C++?

A) `printf`  
B) `print`  
C) `cout`  
D) `console.log`

**Answer:** _______

---

**Question 4:** What does the `using namespace std;` directive do?

A) Creates a new namespace called std  
B) Allows use of std library components without std:: prefix  
C) Imports all C++ libraries  
D) Declares a standard variable

**Answer:** _______

---

**Question 5:** What is the file extension for C++ source files?

A) `.c`  
B) `.cpp` or `.cc`  
C) `.java`  
D) `.cs`

**Answer:** _______

---

### Section 2: True/False (1 point each)

**Question 6:** C++ is case-sensitive, meaning `Variable` and `variable` are different identifiers.

**Answer:** _______ (T/F)

---

**Question 7:** Single-line comments in C++ start with `//`.

**Answer:** _______ (T/F)

---

**Question 8:** Every C++ program must have exactly one `main()` function.

**Answer:** _______ (T/F)

---

**Question 9:** The statement `cout << "Hello";` requires a semicolon at the end.

**Answer:** _______ (T/F)

---

**Question 10:** C++ comments can be nested (multi-line comments inside multi-line comments).

**Answer:** _______ (T/F)

---

### Section 3: Code Output Prediction (3 points each)

**Question 11:** What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello" << " " << "World!";
    return 0;
}
```

**Output:** _______________________

---

**Question 12:** What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "C++" << endl;
    cout << "Programming";
    return 0;
}
```

**Output:** _______________________

---

**Question 13:** What is the exact output of this program?

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    cout << "The value is: " << x;
    return 0;
}
```

**Output:** _______________________

---

### Section 4: Short Answer (4 points each)

**Question 14:** Explain the compilation process in C++. List the main steps from source code to executable.

**Your Answer:**
```




```

---

**Question 15:** What is the purpose of `return 0;` in the main function? What does the return value indicate?

**Your Answer:**
```




```

---

## Bonus Question (Optional - 2 points extra credit)

🌟 **Challenge:** Why does C++ require `#include <iostream>` while C uses `#include <stdio.h>`? What's the difference between `.h` and no extension?

**Answer:**
```




```

---

## Honor Code Statement

I affirm that I have neither given nor received any unauthorized assistance on this quiz.

**Signature:** _________________________ **Date:** _____________

---

## Quick Reference

### Common C++ Program Structure
```cpp
#include <iostream>      // Preprocessor directive
using namespace std;     // Namespace (optional)

int main() {             // Main function
    // Your code here
    return 0;            // Exit status
}
```

### Comments
```cpp
// Single-line comment
/* Multi-line
   comment */
```

### Basic Output
```cpp
cout << "text";          // Output text
cout << variable;        // Output variable
cout << "a" << "b";      // Chain outputs
cout << endl;            // Newline
```
