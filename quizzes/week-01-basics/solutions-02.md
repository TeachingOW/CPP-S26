# Solutions: Quiz 2 - Variables and Operators

---

## Answer Key

### Section 1: Multiple Choice

**Question 1:** B) `2ndValue`

**Explanation:** Variable names in C++ cannot start with a digit. They must begin with a letter (a-z, A-Z) or an underscore (_). After the first character, they can contain letters, digits, and underscores. `_count`, `myVariable`, and `total_sum` are all valid because they start with a letter or underscore.

**Common Mistakes:** Students sometimes think underscores are not allowed at all, or that numbers can appear anywhere.

**Reference:** C++ naming conventions - Week 1

---

**Question 2:** B) 4 bytes

**Explanation:** On most modern 32-bit and 64-bit systems, an `int` is 4 bytes (32 bits), which can represent values from approximately -2 billion to +2 billion. However, the C++ standard only guarantees that `int` is at least 16 bits (2 bytes). The actual size can be checked using `sizeof(int)`.

**Common Mistakes:** Assuming it's always the same across all systems.

**Best Practice:** Use `<cstdint>` types like `int32_t` or `int64_t` when you need specific sizes.

---

**Question 3:** B) `2`

**Explanation:** This is integer division. When both operands are integers, C++ performs integer division, which discards the fractional part (truncates toward zero). `5 / 2` gives `2`, not `2.5`. To get `2.5`, at least one operand must be a floating-point type: `5.0 / 2` or `5 / 2.0` or `static_cast<double>(5) / 2`.

**Common Mistakes:** Expecting decimal results from integer division - this is one of the most common beginner mistakes!

**Reference:** Operator behavior with different types

---

**Question 4:** D) `()` (parentheses)

**Explanation:** Parentheses have the highest precedence in C++. They are evaluated first, allowing you to override the default operator precedence. The general order is: parentheses, unary operators, multiplication/division, addition/subtraction, comparison, logical, assignment.

**Common Mistakes:** Not knowing that you can always use parentheses to make expressions clearer, even when not strictly necessary.

---

**Question 5:** B) Makes the variable unchangeable after initialization

**Explanation:** The `const` keyword declares a constant variable that cannot be modified after initialization. Any attempt to change a `const` variable results in a compilation error. This is useful for defining values that shouldn't change, like `const double PI = 3.14159;`. It's a compile-time check that helps prevent bugs.

**Common Mistakes:** Forgetting to initialize `const` variables at declaration (which causes an error).

**Reference:** Constants and `const` keyword

---

### Section 2: True/False

**Question 6:** F (False)

**Explanation:** In C++, local variables are NOT automatically initialized. `int x;` declares an uninitialized variable containing whatever value (garbage) was previously in that memory location. This is a major source of bugs! You should always initialize variables: `int x = 0;` or `int x{0};`. Global and static variables ARE initialized to 0 by default.

**Common Mistakes:** Assuming uninitialized variables are 0 - this causes unpredictable bugs.

**Best Practice:** Always initialize variables when you declare them.

**Reference:** Variable initialization rules

---

**Question 7:** F (False)

**Explanation:** `++x` (prefix) increments BEFORE using the value, while `x++` (postfix) increments AFTER using the value. In isolation (`++x;` or `x++;`), they have the same effect, but in expressions they differ:
```cpp
int x = 5;
int a = ++x;  // a = 6, x = 6
int x = 5;
int b = x++;  // b = 5, x = 6
```

**Common Mistakes:** Not understanding the difference between prefix and postfix operators.

**Best Practice:** Prefer prefix `++x` when the expression value doesn't matter, as it's sometimes more efficient.

---

**Question 8:** F (False)

**Explanation:** The modulus operator `%` works only with integer types (`int`, `long`, etc.), not with floating-point types (`float`, `double`). If you need the remainder of floating-point division, use the `fmod()` function from `<cmath>`. Attempting to use `%` with floats results in a compilation error.

**Common Mistakes:** Trying to use `%` with doubles when calculating remainders.

**Correct Alternative:** `#include <cmath>` and use `fmod(5.5, 2.0)`

---

**Question 9:** F (False)

**Explanation:** This statement declares three integers but only initializes `x` and `y`. Variable `z` is declared but uninitialized (contains garbage). To initialize all three: `int x = 5, y = 10, z = 0;` or better yet, use separate lines for clarity.

**Common Mistakes:** Assuming all variables in a multi-declaration are initialized.

**Best Practice:** Initialize all variables explicitly, or use separate declaration lines.

---

**Question 10:** F (False)

**Explanation:** Modern C++ prefers C++-style casts like `static_cast<int>()` over C-style casts like `(int)`. C++-style casts are safer, more explicit about intent, and easier to search for in code. They also provide compile-time checking. C-style casts can perform dangerous conversions that C++ casts would reject.

**Common Mistakes:** Using C-style casts out of habit from C programming.

**Best Practice:** Always use `static_cast`, `dynamic_cast`, `const_cast`, or `reinterpret_cast` in C++.

---

### Section 3: Code Output Prediction

**Question 11:** `6 5`

**Explanation:** This demonstrates postfix increment `x++`:
1. `int x = 5;` - x is 5
2. `int y = x++;` - y gets the CURRENT value of x (5), THEN x is incremented to 6
3. Output shows x (6) then y (5)

**Trace:**
- Initial: x = 5
- After `y = x++`: x = 6, y = 5
- Output: `6 5`

**Common Mistakes:** 
- Getting the order wrong
- Thinking both variables would be 6

**Comparison:** If it were `int y = ++x;` (prefix), the output would be `6 6`.

---

**Question 12:** `3 1`

**Explanation:** Integer division and modulus:
- `10 / 3` = 3 (integer division, discards remainder)
- `10 % 3` = 1 (remainder when 10 is divided by 3)

10 ÷ 3 = 3 with remainder 1, so output is `3 1`

**Common Mistakes:** 
- Getting decimal result for division
- Confusing what modulus returns

**Key Concept:** `a / b` gives quotient, `a % b` gives remainder (both for integers)

---

**Question 13:** `11` (Note: Undefined Behavior!)

**Explanation:** **WARNING:** This code has undefined behavior! The expression `x += ++x` modifies `x` twice without a sequence point, which violates C++ standards. Different compilers may produce different results. 

Most likely behavior:
- `++x` increments x from 5 to 6
- `x += 6` adds 6 to x, making it 12
- But some compilers might give 11 or other values

**Common Mistakes:** Writing expressions that modify a variable multiple times.

**Best Practice:** Never modify a variable more than once in a single expression. Write:
```cpp
x = x + 1;  // or ++x;
x = x + x;
```

**Important:** This question tests understanding of undefined behavior, which students should avoid!

---

### Section 4: Code Completion

**Question 14:** Swap without temporary variable

**Sample Answer:**
```cpp
a = a + b;   // a = 30, b = 20
b = a - b;   // a = 30, b = 10
a = a - b;   // a = 20, b = 10
```

**Explanation:** This is a classic programming trick:
1. `a = a + b` - a becomes the sum (30)
2. `b = a - b` - b becomes original a (30 - 20 = 10)
3. `a = a - b` - a becomes original b (30 - 10 = 20)

**Alternative Solutions:**
```cpp
// Using XOR (works only with integers)
a = a ^ b;
b = a ^ b;
a = a ^ b;

// Using multiplication/division (watch for overflow!)
a = a * b;
b = a / b;
a = a / b;
```

**Common Mistakes:** 
- Not following the exact sequence
- Attempting to use a temporary variable (defeats the purpose)

**Real World:** In practice, use a temporary variable for clarity! This is just a teaching exercise.

---

**Question 15:** Variable declarations with data types

**Sample Answer:**
```cpp
int age = 25;                    // Whole number
double price = 19.99;            // Decimal number
char grade = 'A';                // Single character
bool isStudent = true;           // Boolean value
const double PI = 3.14159;       // Constant decimal
```

**Explanation:** 
- `int` - integers (whole numbers)
- `double` - floating-point (decimals), more precise than `float`
- `char` - single character (use single quotes)
- `bool` - true or false
- `const` - makes the variable read-only

**Common Mistakes:**
- Using `float` when `double` is more appropriate
- Using double quotes for `char` (should be single quotes)
- Forgetting `const` for PI

**Reference:** Data types covered in Week 1

---

### Bonus Question

**Answer:** The three expressions give different results due to type conversion:

1. **`5 / 2`** = `2` - Both operands are integers, so integer division is performed, truncating the result to 2.

2. **`5.0 / 2`** = `2.5` - The first operand is a double, so the integer 2 is promoted to 2.0, and floating-point division is performed, giving 2.5.

3. **`5 / 2.0`** = `2.5` - The second operand is a double, so the integer 5 is promoted to 5.0, and floating-point division is performed, giving 2.5.

**Key Concept:** In mixed-type operations, the narrower type is promoted to the wider type. Integer is narrower than double, so integers are promoted to doubles when mixed.

**Operator Precedence:** Division is left-to-right associative, but type promotion happens during evaluation.

---

## Grading Rubric

| Section | Points per Question | Total Possible |
|---------|---------------------|----------------|
| Multiple Choice (Q1-5) | 2 points | 10 points |
| True/False (Q6-10) | 1 point | 5 points |
| Code Output (Q11-13) | 3 points | 9 points |
| Code Completion (Q14-15) | 4 points | 8 points |
| **Total** | | **32 points** |
| Bonus | 3 points | 3 points |

### Partial Credit Guidelines

**Code Output Questions (3 points each):**
- Exact correct output: 3 points
- Minor formatting error: 2 points
- Shows understanding but wrong result: 1 point
- No understanding: 0 points

**Code Completion Questions (4 points each):**
- Correct, working solution: 4 points
- Minor syntax error but correct logic: 3 points
- Partial solution showing some understanding: 2 points
- Minimal effort: 1 point
- No attempt or completely wrong: 0 points

---

## Common Student Errors Summary

1. **Integer division surprise** - Expecting 2.5 from `5 / 2`
2. **Uninitialized variables** - Assuming they're automatically 0
3. **Prefix vs postfix** - Confusing `++x` and `x++`
4. **Type casting** - Using C-style casts instead of `static_cast`
5. **Modulus with floats** - Trying to use `%` with doubles
6. **Variable naming** - Starting names with digits

## Tips for Students

1. **Always initialize variables** - Don't rely on default values
2. **Use parentheses** - Make expressions clear even if not required
3. **Watch for integer division** - Cast to double when needed: `static_cast<double>(a) / b`
4. **Test boundary cases** - What happens with 0? Negative numbers?
5. **Compile frequently** - Catch errors early
6. **Use meaningful names** - `totalScore` is better than `ts`

## Important Concepts

### Type Promotion Rules
- `int` → `long` → `float` → `double`
- Mixed operations promote to wider type
- Be careful with integer division!

### Operator Precedence (Memorize!)
1. `()` Parentheses
2. `++ --` (postfix)
3. `++ -- !` (prefix, unary)
4. `* / %`
5. `+ -`
6. `< > <= >=`
7. `== !=`
8. `&&`
9. `||`
10. `=` (and compound assignments)

---

## Additional Resources

- **C++ Reference:** https://en.cppreference.com/w/cpp/language/operator_precedence
- **Practice:** Try predicting output before running code
- **Tool:** Use `sizeof()` to check type sizes on your system

---

*Last Updated: Week 1, Quiz 2*
