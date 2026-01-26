# Quiz 4: Loops

---

## Quiz Information

| **Field** | **Details** |
|-----------|-------------|
| **Week** | Week 2 |
| **Topic** | Loop Structures (for, while, do-while) |
| **Duration** | 20 minutes |
| **Total Points** | 38 points |
| **Difficulty** | 🟢 Easy to 🔴 Hard |

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

**Question 1:** 🟢 Which loop is guaranteed to execute at least once?

A) `for` loop  
B) `while` loop  
C) `do-while` loop  
D) None of the above

**Answer:** _______

---

**Question 2:** 🟢 What does the `break` statement do in a loop?

A) Skips the current iteration  
B) Exits the loop completely  
C) Restarts the loop  
D) Pauses the loop

**Answer:** _______

---

**Question 3:** 🟡 How many times does this loop execute?

```cpp
for (int i = 0; i < 5; i++) {
    cout << i;
}
```

A) 4 times  
B) 5 times  
C) 6 times  
D) Infinite

**Answer:** _______

---

**Question 4:** 🟡 What is the difference between `break` and `continue`?

A) No difference  
B) `break` exits loop, `continue` skips to next iteration  
C) `continue` exits loop, `break` skips to next iteration  
D) Both exit the loop

**Answer:** _______

---

**Question 5:** 🟡 Which loop structure is best for iterating a known number of times?

A) `while` loop  
B) `do-while` loop  
C) `for` loop  
D) All are equally good

**Answer:** _______

---

### Section 2: True/False (1 point each)

**Question 6:** 🟢 A `for` loop must have all three parts (initialization; condition; increment).

**Answer:** _______ (T/F)

---

**Question 7:** 🟢 The statement `while(1)` creates an infinite loop.

**Answer:** _______ (T/F)

---

**Question 8:** 🟡 In a `do-while` loop, the condition is checked before the loop body executes.

**Answer:** _______ (T/F)

---

**Question 9:** 🟡 You can use multiple variables in a `for` loop initialization.

**Answer:** _______ (T/F)

---

**Question 10:** 🟡 A `break` statement only exits the innermost loop in nested loops.

**Answer:** _______ (T/F)

---

### Section 3: Code Output Prediction (3 points each)

**Question 11:** 🟡 What is the output?

```cpp
for (int i = 1; i <= 3; i++) {
    cout << i << " ";
}
```

**Output:** _______________________

---

**Question 12:** 🔴 What is the output?

```cpp
int i = 0;
while (i < 3) {
    cout << i;
    i++;
}
cout << i;
```

**Output:** _______________________

---

**Question 13:** 🔴 What is the output?

```cpp
for (int i = 0; i < 5; i++) {
    if (i == 2)
        continue;
    if (i == 4)
        break;
    cout << i;
}
```

**Output:** _______________________

---

### Section 4: Code Completion (5 points each)

**Question 14:** 🟡 Complete this code to calculate the sum of numbers from 1 to n:

```cpp
int n = 10;
int sum = 0;

// Your loop here






cout << "Sum = " << sum;
```

**Your Answer:**
```cpp






```

---

**Question 15:** 🔴 Complete this code to print a multiplication table for a given number:

```cpp
int num = 5;

// Your code here (print 5 x 1 = 5, 5 x 2 = 10, etc. up to 10)






```

**Your Answer:**
```cpp






```

---

## Bonus Question (Optional - 5 points extra credit)

🌟 **Challenge:** Write a nested loop to print this pattern:
```
*
**
***
****
*****
```

**Answer:**
```cpp






```

---

## Honor Code Statement

I affirm that I have neither given nor received any unauthorized assistance on this quiz.

**Signature:** _________________________ **Date:** _____________

---

## Quick Reference

### For Loop
```cpp
for (initialization; condition; increment) {
    // code
}
```

### While Loop
```cpp
while (condition) {
    // code
}
```

### Do-While Loop
```cpp
do {
    // code
} while (condition);
```

### Loop Control
```cpp
break;      // Exit loop
continue;   // Skip to next iteration
```

### Common Patterns
```cpp
// Count up
for (int i = 0; i < n; i++)

// Count down
for (int i = n; i > 0; i--)

// Step by 2
for (int i = 0; i < n; i += 2)

// Infinite loop
while (true)
for (;;)
```
