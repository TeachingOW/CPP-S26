# Quiz 3: Conditionals

---

## Quiz Information

| **Field** | **Details** |
|-----------|-------------|
| **Week** | Week 2 |
| **Topic** | Conditional Statements (if, else, switch) |
| **Duration** | 20 minutes |
| **Total Points** | 36 points |
| **Difficulty** | 🟢 Easy to 🟡 Medium |

---

## Instructions

### Before You Begin
1. Write your name at the top of this page
2. Read all questions before starting
3. Budget your time wisely
4. Show your work for partial credit

### During the Quiz
- ✅ You **MAY** use: Pen/pencil
- ❌ You **MAY NOT** use: Notes, textbook, calculator, phone, computer

---

## Questions

### Section 1: Multiple Choice (2 points each)

**Question 1:** 🟢 Which of the following is the correct syntax for an if statement?

A) `if x == 5 { }`  
B) `if (x == 5) { }`  
C) `if [x == 5] { }`  
D) `if x == 5 then { }`

**Answer:** _______

---

**Question 2:** 🟢 What is the output when `x = 10`?

```cpp
if (x > 5)
    cout << "A";
else
    cout << "B";
```

A) `A`  
B) `B`  
C) `AB`  
D) Nothing

**Answer:** _______

---

**Question 3:** 🟡 What is the correct operator for logical AND in C++?

A) `and`  
B) `&`  
C) `&&`  
D) `||`

**Answer:** _______

---

**Question 4:** 🟡 In a switch statement, what happens if you forget the `break` statement?

A) Compilation error  
B) Fall-through to next case  
C) Program crashes  
D) Automatic break is assumed

**Answer:** _______

---

**Question 5:** 🟡 Which statement is equivalent to `if (x != 0)`?

A) `if (x)`  
B) `if (!x)`  
C) `if (x == 0)`  
D) `if (x = 0)`

**Answer:** _______

---

### Section 2: True/False (1 point each)

**Question 6:** 🟢 The else clause is always required when using an if statement.

**Answer:** _______ (T/F)

---

**Question 7:** 🟢 In C++, `0` is considered false and any non-zero value is considered true.

**Answer:** _______ (T/F)

---

**Question 8:** 🟡 The statement `if (x = 5)` checks if x equals 5.

**Answer:** _______ (T/F)

---

**Question 9:** 🟡 A switch statement can work with floating-point numbers.

**Answer:** _______ (T/F)

---

**Question 10:** 🟡 You can have multiple else if blocks between an if and else.

**Answer:** _______ (T/F)

---

### Section 3: Code Output Prediction (3 points each)

**Question 11:** 🟡 What is the output?

```cpp
int x = 15;
if (x > 20)
    cout << "A";
else if (x > 10)
    cout << "B";
else
    cout << "C";
```

**Output:** _______________________

---

**Question 12:** 🔴 What is the output?

```cpp
int day = 2;
switch(day) {
    case 1: cout << "Mon";
    case 2: cout << "Tue";
    case 3: cout << "Wed";
    default: cout << "Other";
}
```

**Output:** _______________________

---

**Question 13:** 🔴 What is the output?

```cpp
int x = 5, y = 10;
if (x < 10 && y++ > 9)
    cout << y;
else
    cout << x;
```

**Output:** _______________________

---

### Section 4: Bug Finding (5 points each)

**Question 14:** 🟡 Find and fix ALL bugs in this code:

```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    
    if (score >= 90);
        cout << "A";
    else if (score >= 80)
        cout << "B";
    else
        cout << "C";
    
    return 0;
}
```

**Bugs Found:**
1. _________________________________
2. _________________________________

**Fixed Code:**
```cpp




```

---

### Section 5: Code Completion (4 points each)

**Question 15:** 🟡 Complete this code to check if a number is positive, negative, or zero:

```cpp
int num;
cin >> num;

// Your code here






```

**Your Answer:**
```cpp






```

---

## Bonus Question (Optional - 3 points extra credit)

🌟 **Challenge:** Write a single expression using the ternary operator (`? :`) that returns the maximum of three numbers `a`, `b`, and `c`.

**Answer:**
```cpp




```

---

## Honor Code Statement

I affirm that I have neither given nor received any unauthorized assistance on this quiz.

**Signature:** _________________________ **Date:** _____________

---

## Quick Reference

### Conditional Operators
```cpp
==  // Equal to
!=  // Not equal to
<   // Less than
>   // Greater than
<=  // Less than or equal to
>=  // Greater than or equal to
```

### Logical Operators
```cpp
&&  // AND
||  // OR
!   // NOT
```

### If-Else Syntax
```cpp
if (condition) {
    // code
} else if (condition) {
    // code
} else {
    // code
}
```

### Switch Syntax
```cpp
switch (variable) {
    case value1:
        // code
        break;
    case value2:
        // code
        break;
    default:
        // code
}
```

### Ternary Operator
```cpp
result = (condition) ? value_if_true : value_if_false;
```
