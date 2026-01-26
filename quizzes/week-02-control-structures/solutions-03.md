# Solutions: Quiz 3 - Conditionals

---

## Answer Key

### Section 1: Multiple Choice

**Question 1:** B) `if (x == 5) { }`

**Explanation:** C++ requires the condition to be enclosed in parentheses `()` and uses curly braces `{}` for the code block. This is standard syntax inherited from C.

**Common Mistakes:** Using brackets `[]` from other languages, or forgetting parentheses.

---

**Question 2:** A) `A`

**Explanation:** Since `x = 10` and `10 > 5` is true, the if branch executes, printing "A". The else branch is skipped.

---

**Question 3:** C) `&&`

**Explanation:** The logical AND operator in C++ is `&&`. The single `&` is bitwise AND, `and` is an alternative keyword (rarely used), and `||` is OR.

**Common Mistakes:** Using single `&` which performs bitwise operations, not logical.

---

**Question 4:** B) Fall-through to next case

**Explanation:** Without `break`, execution continues to the next case (fall-through). This is sometimes intentional but often a bug.

**Common Mistakes:** Forgetting break statements leads to unexpected behavior.

---

**Question 5:** A) `if (x)`

**Explanation:** In C++, any non-zero value is true, and zero is false. So `if (x)` is equivalent to `if (x != 0)`. Option B `if (!x)` checks if x is zero, C checks equality, and D is assignment (not comparison).

**Common Mistakes:** Confusing `if (x)` with `if (x == 1)`.

---

### Section 2: True/False

**Question 6:** F (False)

**Explanation:** The else clause is optional. You can have a standalone if statement without else.

---

**Question 7:** T (True)

**Explanation:** In C++, 0 is false, and any non-zero value (1, -1, 100, etc.) is considered true. This is fundamental to how conditions work.

---

**Question 8:** F (False)

**Explanation:** **CRITICAL MISTAKE!** `if (x = 5)` is assignment, not comparison. It assigns 5 to x, then evaluates to true (since 5 is non-zero). The correct comparison is `if (x == 5)`. This is one of the most common and dangerous bugs!

**Warning:** Many compilers issue warnings about this. Always use `-Wall` flag.

---

**Question 9:** F (False)

**Explanation:** Switch statements work only with integral types (int, char, enum) and strings (C++11 with some limitations). They do not work with floating-point types (float, double).

---

**Question 10:** T (True)

**Explanation:** You can chain multiple else if blocks: `if () {...} else if () {...} else if () {...} else {...}`

---

### Section 3: Code Output Prediction

**Question 11:** `B`

**Explanation:** 
- First condition: `15 > 20` is false
- Second condition: `15 > 10` is true, so "B" is printed
- The else is not reached

---

**Question 12:** `TueWedOther`

**Explanation:** Classic fall-through bug! Since there are no break statements:
- Matches case 2, prints "Tue"
- Falls through to case 3, prints "Wed"  
- Falls through to default, prints "Other"
- Output: `TueWedOther`

**Common Mistakes:** Expecting just "Tue" - forgetting about fall-through.

---

**Question 13:** `11`

**Explanation:** This demonstrates short-circuit evaluation:
- Condition: `x < 10 && y++ > 9`
- First part: `5 < 10` is true
- Second part must be evaluated: `y++ > 9` checks if 10 > 9 (true), then increments y to 11
- Condition is true, so output is y which is now 11

**Key Concept:** The `&&` operator uses short-circuit evaluation - if left side is false, right side isn't evaluated.

---

### Section 4: Bug Finding

**Question 14:** 

**Bugs Found:**
1. Semicolon after if condition: `if (score >= 90);`
2. This creates an empty statement, causing the code block to execute regardless

**Fixed Code:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int score = 85;
    
    if (score >= 90)  // Removed semicolon
        cout << "A";
    else if (score >= 80)
        cout << "B";
    else
        cout << "C";
    
    return 0;
}
```

**Explanation:** The semicolon creates a null statement, so the if only controls that empty statement. The cout << "A" always executes, causing the else to be a syntax error.

---

### Section 5: Code Completion

**Question 15:** Sample Answer:

```cpp
if (num > 0) {
    cout << "Positive";
} else if (num < 0) {
    cout << "Negative";
} else {
    cout << "Zero";
}
```

**Grading:** Award full credit for correct logic, even if exact wording differs.

---

### Bonus Question

**Sample Answer:**
```cpp
int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
```

**Explanation:** Nested ternary operators:
- First checks if a > b
- If true, returns max of a and c
- If false, returns max of b and c

**Alternative (more readable):**
```cpp
int max = (a > b && a > c) ? a : (b > c ? b : c);
```

---

## Grading Rubric

| Section | Total Possible |
|---------|----------------|
| Multiple Choice (Q1-5) | 10 points |
| True/False (Q6-10) | 5 points |
| Code Output (Q11-13) | 9 points |
| Bug Finding (Q14) | 5 points |
| Code Completion (Q15) | 4 points |
| **Total** | **33 points** |
| Bonus | 3 points |

## Common Student Errors

1. **Assignment vs. Comparison** - Using `=` instead of `==`
2. **Semicolon after if** - `if (condition);` creates null statement
3. **Forgetting break in switch** - Causes fall-through
4. **Logical operators** - Using `&` instead of `&&`

---

*Last Updated: Week 2, Quiz 3*
