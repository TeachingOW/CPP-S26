# Solutions: Quiz 4 - Loops

---

## Answer Key and Detailed Explanations

### Section 1: Multiple Choice

**Question 1:** C) `do-while` loop

**Explanation:** A do-while loop checks its condition AFTER executing the loop body, guaranteeing at least one execution even if the condition is initially false. For loops and while loops check the condition before execution, so they may never execute if the condition starts as false.

**Common Mistakes:** Confusing the order of execution between different loop types.

---

**Question 2:** B) Exits the loop completely

**Explanation:** The `break` statement immediately terminates the loop and transfers control to the first statement after the loop. It's useful for early loop termination when a certain condition is met.

**Common Mistakes:** Confusing `break` with `continue`.

---

**Question 3:** B) 5 times

**Explanation:** The loop executes with i = 0, 1, 2, 3, 4 (five iterations). When i becomes 5, the condition `i < 5` is false, and the loop terminates.

**Trace:**
- i=0: executes, i++, i=1
- i=1: executes, i++, i=2
- i=2: executes, i++, i=3
- i=3: executes, i++, i=4
- i=4: executes, i++, i=5
- i=5: condition false, loop ends

**Common Mistakes:** Off-by-one errors - thinking it executes 4 or 6 times.

---

**Question 4:** B) `break` exits loop, `continue` skips to next iteration

**Explanation:** `break` immediately exits the entire loop, while `continue` skips the remaining code in the current iteration and proceeds to the next iteration. Both are important for loop control flow.

**Example:**
```cpp
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;  // Skip printing 2
    if (i == 4) break;     // Exit before printing 4
    cout << i;             // Prints: 0, 1, 3
}
```

---

**Question 5:** C) `for` loop

**Explanation:** For loops are ideal when the number of iterations is known in advance because they keep initialization, condition, and increment together in one line, making the code more readable and less error-prone.

**Best Practice:** Use for loops for counting, while loops for unknown iterations, and do-while when you need at least one execution.

---

### Section 2: True/False

**Question 6:** F (False)

**Explanation:** All three parts of a for loop (initialization; condition; increment) are optional! You can write `for (;;)` to create an infinite loop. However, omitting parts should be done carefully and intentionally.

**Example:**
```cpp
int i = 0;
for (; i < 10; i++)  // Initialization outside
for (int i = 0; ; i++)  // No condition (infinite unless broken)
for (int i = 0; i < 10;)  // Manual increment inside loop
```

---

**Question 7:** T (True)

**Explanation:** Since 1 is non-zero and C++ treats non-zero as true, `while(1)` creates an infinite loop. The same effect can be achieved with `while(true)`. You must use `break` or `return` to exit such loops.

**Common Use:** Infinite loops with break conditions are common in game loops, servers, and event handlers.

---

**Question 8:** F (False)

**Explanation:** In a do-while loop, the condition is checked AFTER the body executes, not before. This is the key difference from a while loop. The syntax is:
```cpp
do {
    // code
} while (condition);
```

**Common Mistakes:** Forgetting the semicolon after the while condition in do-while loops.

---

**Question 9:** T (True)

**Explanation:** You can declare and initialize multiple variables in a for loop: `for (int i = 0, j = 10; i < j; i++, j--)`. This is useful for algorithms that need multiple counters moving in opposite directions.

**Example:** Checking if a string is a palindrome.

---

**Question 10:** T (True)

**Explanation:** In nested loops, `break` only exits the immediately enclosing loop. To exit multiple nested loops, you need multiple breaks, a goto statement, or a flag variable.

**Example:**
```cpp
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j == 1) break;  // Only exits inner loop
        cout << i << "," << j << " ";
    }
}
// Output: 0,0 1,0 2,0
```

---

### Section 3: Code Output Prediction

**Question 11:** `1 2 3 `

**Explanation:** The loop executes three times (i = 1, 2, 3), printing each value followed by a space. Note the trailing space after 3.

**Trace:**
- i=1: prints "1 "
- i=2: prints "2 "
- i=3: prints "3 "
- i=4: condition false, loop ends

---

**Question 12:** `0123`

**Explanation:** 
- Loop prints 0, 1, 2 while i < 3
- After loop, i is 3 (the condition that failed)
- Final cout prints 3
- Total output: `0123` (no spaces)

**Trace:**
- i=0: prints "0", i++
- i=1: prints "1", i++
- i=2: prints "2", i++
- i=3: condition false, exit loop
- prints i (3)

---

**Question 13:** `013`

**Explanation:**
- i=0: prints 0
- i=1: prints 1
- i=2: continue skips the print statement
- i=3: prints 3
- i=4: break exits loop before printing
- Output: `013`

**Trace:**
- i=0: no skip, no break, prints 0
- i=1: no skip, no break, prints 1
- i=2: continue executed, skips print
- i=3: no skip, no break, prints 3
- i=4: break executed, exits loop

**Common Mistakes:** Forgetting that continue skips remaining code but loop continues.

---

### Section 4: Code Completion

**Question 14:** Sample Solutions

**Solution 1 (for loop):**
```cpp
for (int i = 1; i <= n; i++) {
    sum += i;
}
```

**Solution 2 (while loop):**
```cpp
int i = 1;
while (i <= n) {
    sum += i;
    i++;
}
```

**Solution 3 (do-while):**
```cpp
if (n > 0) {
    int i = 1;
    do {
        sum += i;
        i++;
    } while (i <= n);
}
```

**Grading:**
- Correct logic: 3 points
- Proper syntax: 1 point
- Handles edge cases: 1 point

**Mathematical Note:** The sum can also be calculated using the formula: `sum = n * (n + 1) / 2`

---

**Question 15:** Sample Solution

```cpp
for (int i = 1; i <= 10; i++) {
    cout << num << " x " << i << " = " << (num * i) << endl;
}
```

**Expected Output (for num=5):**
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

**Grading:**
- Correct loop structure: 2 points
- Correct multiplication: 2 points
- Proper formatting: 1 point

---

### Bonus Question Solution

**Sample Answer:**
```cpp
for (int i = 1; i <= 5; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "*";
    }
    cout << endl;
}
```

**Explanation:** 
- Outer loop controls rows (1-5)
- Inner loop prints stars, number of stars equals row number
- Each row ends with endl

**Alternative using single loop:**
```cpp
string stars = "";
for (int i = 1; i <= 5; i++) {
    stars += "*";
    cout << stars << endl;
}
```

**Grading (5 points):**
- Correct nested loop structure: 2 points
- Correct star printing: 2 points
- Proper newlines: 1 point

---

## Grading Rubric

| Section | Points per Question | Total Possible |
|---------|---------------------|----------------|
| Multiple Choice (Q1-5) | 2 points | 10 points |
| True/False (Q6-10) | 1 point | 5 points |
| Code Output (Q11-13) | 3 points | 9 points |
| Code Completion (Q14) | 5 points | 5 points |
| Code Completion (Q15) | 5 points | 5 points |
| **Total** | | **34 points** |
| Bonus | 5 points | 5 points |

---

## Common Student Errors

1. **Off-by-one errors** - Getting loop bounds wrong (< vs <=)
2. **Infinite loops** - Forgetting to increment/update loop variable
3. **Continue vs break confusion** - Using wrong control statement
4. **Missing semicolon** - Especially after do-while condition
5. **Nested loop confusion** - Losing track of which variable belongs to which loop

## Loop Selection Guide

### Use FOR when:
- Number of iterations is known
- Need a counter variable
- Iterating over a range

### Use WHILE when:
- Number of iterations is unknown
- Waiting for a condition
- Reading until EOF

### Use DO-WHILE when:
- Need at least one execution
- Menu-driven programs
- Input validation loops

## Best Practices

1. **Initialize loop variables** - Always initialize before using
2. **Avoid modifying loop counter** - Don't change loop variable inside loop body
3. **Use meaningful variable names** - `i, j, k` only for simple loops
4. **Keep it simple** - Complex loop conditions are error-prone
5. **Comment nested loops** - Make it clear what each loop does

---

## Additional Practice

### Easy
1. Sum of even numbers from 1 to n
2. Print numbers in reverse
3. Find factorial of a number

### Medium
4. Check if a number is prime
5. Print Fibonacci sequence
6. Count digits in a number

### Hard
7. Print Pascal's triangle
8. Find all prime numbers up to n (Sieve)
9. Print diamond pattern

---

*Last Updated: Week 2, Quiz 4*
*Review this material if you scored below 70%*
