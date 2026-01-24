# Grading Rubric for C++ Quizzes

## Overview

This document defines the grading criteria for all C++ quizzes in CPP-S26. Consistent grading ensures fairness and helps students understand expectations.

---

## General Grading Principles

### Core Values

1. **Consistency**: Same types of errors receive similar deductions across all quizzes
2. **Fairness**: Partial credit is awarded for demonstrating understanding
3. **Clarity**: Grading criteria are transparent and explained
4. **Learning-Focused**: Feedback helps students improve

### Partial Credit Philosophy

- **Effort Matters**: Attempting a question with reasonable approach earns partial credit
- **Syntax vs Logic**: Logical understanding weighted more heavily than syntax perfection
- **Show Your Work**: Students showing reasoning receive more credit even if answer is wrong
- **Minor Errors**: Small mistakes don't result in zero points

---

## Point Allocation by Question Type

### 1. Multiple Choice Questions (2 points each)

| Criteria | Points | Description |
|----------|--------|-------------|
| Correct answer | 2 | Full credit |
| Incorrect answer | 0 | No partial credit for MC |
| No answer | 0 | Blank receives zero |

**Notes**:
- Multiple choice questions are all-or-nothing
- If student circles two answers, both must be correct for credit
- Crossed out answers should be ignored if one clear answer remains

---

### 2. True/False Questions (1 point each)

| Criteria | Points | Description |
|----------|--------|-------------|
| Correct answer | 1 | Full credit |
| Incorrect answer | 0 | No partial credit |
| No answer | 0 | Blank receives zero |

**Notes**:
- No partial credit for True/False
- If student writes both T and F, mark as incorrect unless one is clearly crossed out

---

### 3. Code Output Prediction (2-3 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| Exact output correct | 3 | Perfect match including whitespace |
| Output mostly correct | 2 | Minor formatting issues (spacing, newline) |
| Wrong output, correct concept | 1 | Shows understanding but incorrect calculation |
| Compilation error correctly identified | 3 | If code doesn't compile |
| Completely incorrect | 0 | No understanding demonstrated |

**Common Deductions**:
- Missing newline: -0.5 points
- Extra space: -0.5 points
- Wrong order but correct values: -1 point
- Off-by-one error: -1 point

**Examples**:

✅ **Full Credit**:
```
Expected: "5 10"
Student: "5 10"
```

✅ **Full Credit**:
```
Expected: Compilation error (missing semicolon)
Student: "Compilation error" or "Won't compile"
```

⚠️ **Partial Credit (2 points)**:
```
Expected: "5 10\n"
Student: "5 10" (missing newline but values correct)
```

⚠️ **Partial Credit (1 point)**:
```
Expected: "6" (from ++x where x=5)
Student: "5" (used x++ mentally instead)
Shows understanding of increment but wrong operator
```

---

### 4. Bug Finding Questions (3-5 points)

#### Point Distribution
- **Identifying bugs**: 60% of points
- **Fixing bugs**: 30% of points
- **Explaining bugs**: 10% of points

| Criteria | Points (5 pt question) | Description |
|----------|--------|-------------|
| All bugs found and fixed correctly | 5 | Perfect |
| Most bugs found (≥75%), correctly fixed | 4 | One bug missed |
| Half bugs found, mostly fixed | 3 | Multiple bugs missed |
| Some bugs found, partial fixes | 2 | Recognized issues exist |
| Minimal effort or incorrect identification | 1 | Some attempt made |
| No answer or completely wrong | 0 | No understanding |

**Common Bug Patterns & Deductions**:

| Bug Type | If Missed | If Found but Not Fixed |
|----------|-----------|------------------------|
| Memory leak (missing delete) | -1.5 | -0.5 |
| Missing virtual destructor | -1.5 | -0.5 |
| Dangling pointer | -1.5 | -0.5 |
| Array index out of bounds | -1 | -0.5 |
| Missing const | -0.5 | -0.5 |
| Semicolon or syntax error | -0.5 | 0 |

**Example Grading**:

Code with 3 bugs: memory leak, missing virtual destructor, off-by-one error

✅ **5 points**: All three bugs identified and fixed with explanation
✅ **4 points**: Two critical bugs fixed (memory leak + virtual destructor), missed off-by-one
✅ **3 points**: Found all bugs but only fixed two correctly
✅ **2 points**: Found only the memory leak and attempted to fix
✅ **1 point**: Mentioned "memory issue" but couldn't identify specific bug
❌ **0 points**: No attempt or completely unrelated changes

---

### 5. Code Completion Questions (3-5 points)

| Criteria | Points (5 pt question) | Description |
|----------|--------|-------------|
| Perfect solution | 5 | Compiles, works correctly, good style |
| Working solution, minor issues | 4 | Works but has style or minor syntax issues |
| Mostly correct logic | 3 | Core logic right, implementation issues |
| Partial implementation | 2 | Started correctly but incomplete |
| Shows some understanding | 1 | Wrong approach but relevant code |
| No answer or unrelated code | 0 | No understanding |

**Grading Criteria Breakdown**:

| Aspect | Points | Notes |
|--------|--------|-------|
| Correct logic/algorithm | 2.5 | Most important aspect |
| Compilable code | 1.0 | Must be syntactically correct |
| Proper style | 0.5 | Readable, follows conventions |
| Edge cases handled | 1.0 | Null checks, boundary conditions |

**Common Deductions**:
- Missing return statement: -1 point
- Syntax error that prevents compilation: -1 point
- Incorrect data type: -0.5 points
- Poor variable names: -0.5 points
- Missing edge case handling: -1 point
- Inefficient but working solution: -0.5 points

**Example Grading**:

Task: "Complete a function to find maximum of two numbers"

```cpp
// Perfect Solution (5 points)
template<typename T>
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

// Good Solution (4 points) - works but no template
int maximum(int a, int b) {
    return (a > b) ? a : b;
}

// Acceptable Solution (3 points) - works, verbose
int maximum(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

// Partial Credit (2 points) - logic right, syntax error
int maximum(int a, int b) {
    return (a > b) ? a  // missing : b;
}

// Minimal Credit (1 point) - wrong but shows some understanding
int maximum(int a, int b) {
    return a + b;  // Wrong but attempted to return something
}
```

---

### 6. Short Answer Questions (3-5 points)

| Criteria | Points (4 pt question) | Description |
|----------|--------|-------------|
| Complete, accurate answer | 4 | All key points covered clearly |
| Good answer, minor omission | 3 | Most key points covered |
| Partial understanding | 2 | Some correct information |
| Minimal understanding | 1 | One correct point or concept |
| No answer or completely wrong | 0 | No understanding demonstrated |

**Key Point Rubric**:

Most short answer questions have 3-4 key points. Award points as follows:

| Key Points Covered | Points (out of 4) |
|-------------------|-------------------|
| All 4 key points | 4 |
| 3 key points | 3 |
| 2 key points | 2 |
| 1 key point | 1 |
| 0 key points | 0 |

**Example Question & Grading**:

> "Explain when and why you would use a virtual destructor."

**Key Points to Cover**:
1. Used when class has virtual functions / used polymorphically
2. Ensures derived class destructors are called
3. Prevents memory leaks in inheritance hierarchies
4. Required for proper cleanup of derived class resources

**Sample Answers**:

✅ **4 points**:
> "A virtual destructor is needed when a class is used polymorphically through base class pointers. It ensures that when you delete a base class pointer pointing to a derived object, the derived class destructor is called first, then the base class destructor. This prevents memory leaks by properly cleaning up derived class resources."
(Covers all 4 points clearly)

✅ **3 points**:
> "Virtual destructors ensure that the correct destructor is called in an inheritance hierarchy. Without it, only the base class destructor would be called, potentially causing memory leaks."
(Covers points 2, 3, partially 1)

✅ **2 points**:
> "Virtual destructors are used with inheritance to make sure derived classes clean up properly."
(Covers points 2 partially)

✅ **1 point**:
> "Virtual destructors are used with inheritance."
(Mentions inheritance connection but no explanation)

❌ **0 points**:
> "Virtual destructors delete memory."
(Incorrect/confused understanding)

---

### 7. Design Questions (5-10 points)

| Criteria | Points (10 pt question) | Description |
|----------|--------|-------------|
| Excellent design | 9-10 | Correct, elegant, follows best practices |
| Good design | 7-8 | Correct, minor style issues |
| Adequate design | 5-6 | Works but has design flaws |
| Partial design | 3-4 | Started but incomplete or flawed |
| Minimal attempt | 1-2 | Shows some relevant knowledge |
| No answer | 0 | No attempt |

**Grading Breakdown** (10-point question):

| Aspect | Points | Description |
|--------|--------|-------------|
| Correct functionality | 4 | Does what's required |
| Proper encapsulation | 2 | Access specifiers used correctly |
| Good design choices | 2 | Follows OOP principles |
| Code quality | 1 | Readable, well-organized |
| Documentation/explanation | 1 | Clear comments or explanation |

**Common Deductions**:
- Missing access specifiers: -1 point
- Public member variables (should be private): -1 point
- Missing necessary methods (getters/setters): -1 point
- Poor naming conventions: -0.5 points
- Missing const correctness: -0.5 points
- No constructor when needed: -1 point
- No explanation of design: -1 point

---

### 8. Code Tracing Questions (3 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| All values correct | 3 | Perfect trace |
| Most values correct (≥80%) | 2 | One or two errors |
| Some values correct (≥50%) | 1 | Multiple errors but showing effort |
| Mostly incorrect | 0 | No understanding |

**Deduction Guidelines**:
- Each incorrect value: -0.5 points
- If error propagates logically from earlier error: -0.5 total (not per row)

---

### 9. Conceptual Questions (2-3 points)

Similar to multiple choice - typically all or nothing unless requiring explanation.

---

## Common Mistake Deductions

### Syntax Errors

| Error Type | Deduction |
|------------|-----------|
| Missing semicolon | -0.5 |
| Missing bracket/brace | -0.5 |
| Typo in keyword | -0.5 |
| Wrong bracket type [] vs {} | -0.5 |
| Multiple syntax errors | -1 (cap) |

### Logic Errors

| Error Type | Deduction |
|------------|-----------|
| Off-by-one error | -1 |
| Wrong operator (< vs <=) | -1 |
| Wrong loop type | -1.5 |
| Incorrect condition | -1 to -2 |
| Algorithm completely wrong | -3 to -5 |

### C++ Specific Errors

| Error Type | Deduction |
|------------|-----------|
| Memory leak | -1.5 |
| Dangling pointer | -1.5 |
| Missing const correctness | -0.5 |
| Wrong access specifier | -1 |
| Missing virtual | -1 |
| Incorrect template syntax | -1 |
| Wrong STL container | -1 |

### Style Issues (if style is graded)

| Issue | Deduction |
|-------|-----------|
| Poor variable names | -0.5 |
| No comments (when required) | -0.5 |
| Inconsistent formatting | -0.5 |
| Magic numbers | -0.5 |

---

## Special Circumstances

### Blank Answers

- **Policy**: Zero points unless question is optional
- **Exception**: If student runs out of time, instructor may give minimal credit (0.5-1 point) for previous demonstrated understanding

### Multiple Attempts at Same Question

- **Policy**: Grade the clearly marked final answer
- **If unclear**: Ask student to clarify or grade most complete attempt

### Code That Doesn't Compile

- **Major syntax errors**: Maximum 40% credit (shows logic understanding)
- **Minor syntax errors**: Maximum 80% credit
- **Single typo**: Maximum 90% credit

### Answers Exceeding Space Provided

- **Policy**: Grade all provided answer if on same page
- **If continues elsewhere**: Must be clearly marked with arrow/note

---

## Partial Credit Examples

### Example 1: Pointer Question (5 points)

**Question**: "Write code to dynamically allocate an array of 10 integers, initialize them to zero, and properly deallocate."

**Perfect Answer (5 points)**:
```cpp
int* arr = new int[10];
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}
delete[] arr;
arr = nullptr;
```

**Good Answer (4 points)**:
```cpp
int* arr = new int[10];
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}
delete[] arr;
// Missing: arr = nullptr (good practice but not required)
```

**Acceptable Answer (3 points)**:
```cpp
int* arr = new int[10];
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}
delete arr;  // WRONG: should be delete[]
```

**Partial Credit (2 points)**:
```cpp
int arr[10];  // WRONG: not dynamic allocation
for (int i = 0; i < 10; i++) {
    arr[i] = 0;
}
// Shows understanding of arrays and initialization
```

---

### Example 2: OOP Question (10 points)

**Question**: "Design a class `Rectangle` with private width and height, constructor, and method to calculate area."

**Excellent (10 points)**:
```cpp
class Rectangle {
private:
    double width;
    double height;
    
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double calculateArea() const {
        return width * height;
    }
    
    double getWidth() const { return width; }
    double getHeight() const { return height; }
};
```

**Good (8 points)**:
```cpp
class Rectangle {
private:
    double width;
    double height;
    
public:
    Rectangle(double w, double h) {
        width = w;
        height = h;
    }
    
    double calculateArea() {  // Missing const
        return width * height;
    }
};
// Missing getters but has core functionality
```

**Adequate (6 points)**:
```cpp
class Rectangle {
    double width;   // Missing access specifier
    double height;
    
public:
    Rectangle(double w, double h) {
        width = w;
        height = h;
    }
    
    double calculateArea() {
        return width * height;
    }
};
```

**Partial (3 points)**:
```cpp
class Rectangle {
    double width;
    double height;
    
    double calculateArea() {
        return width * height;
    }
};
// Missing constructor, access specifiers
// But shows basic class structure
```

---

## Grade Boundaries

### Standard Percentage Conversion

| Percentage | Letter Grade |
|------------|--------------|
| 93-100% | A |
| 90-92% | A- |
| 87-89% | B+ |
| 83-86% | B |
| 80-82% | B- |
| 77-79% | C+ |
| 73-76% | C |
| 70-72% | C- |
| 67-69% | D+ |
| 63-66% | D |
| 60-62% | D- |
| 0-59% | F |

---

## Instructor Guidelines

### Consistency Checks

- Review sample answers before grading
- Grade one question at a time across all quizzes
- Use rubric consistently
- Have second grader spot-check random sample

### Feedback Best Practices

- Mark specific errors, not just point deductions
- Provide brief explanation for major deductions
- Note what was done well
- Suggest resources for improvement

### Handling Disputes

- Allow 1 week for grade disputes
- Student must provide written explanation
- Re-grade entire quiz (grade can go up or down)
- Maintain consistent standards

---

## Revision History

| Date | Changes |
|------|---------|
| Spring 2026 | Initial rubric created |

---

**Questions about grading?** Contact the instructor during office hours.
