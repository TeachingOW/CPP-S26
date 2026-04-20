# C++ Code Examples

This directory contains code examples organized by topic to help students learn C++ concepts through practical implementations.

## Directory Structure

### Basic Examples (`basic/`)
**Description:** Fundamental C++ programs demonstrating basic syntax and concepts.

**Files:**
- `c1.cpp` - Basic C++ example
- `chello.cpp` - Hello World and basic I/O
- `pointers.cpp` - Pointer fundamentals and usage

**Topics:** Basic syntax, I/O, pointers, memory

---

### File Handling (`file-handling/`)
**Description:** Examples demonstrating file I/O operations in C++.

**Files:**
- `filematcher.cpp` - File matching implementation (v1)
- `filematcher2.cpp` - Enhanced file matcher (v2)
- `filematcher3.cpp` - Advanced file matcher (v3)

**Topics:** File I/O, string processing, pattern matching

**Related Lectures:** Lecture 12, 13

---

### BMP Image Processing (`bmp/`)
**Description:** Working with BMP image format - reading, modifying, and creating bitmap images.

**Files:**
- `bmp.hpp` - BMP file handling header
- `test.cpp` - BMP test program
- `grad.cpp` - Gradient generation
- `progressbar.cpp` - Progress bar visualization
- `progressbar2.cpp` - Enhanced progress bar
- `argtest.cpp` - Command-line argument handling
- Sample BMP files: `a.bmp`, `out.bmp`, `rect.bmp`

**Topics:** Binary files, image processing, structs, file formats

**Related:** [Assignment 2](https://github.com/TeachingOW/CPP-S26/tree/main/assignments/assignment-02), [Assignment 2.5](https://github.com/TeachingOW/CPP-S26/tree/main/assignments/assignment-02.5)

---

### Algorithms (`algorithms/`)
**Description:** Implementation of various algorithms and problem-solving techniques.

**Files:**
- `sudoku.cpp` - Sudoku solver implementation

**Topics:** Backtracking, recursion, constraint satisfaction

**External:** [Sudoku Solver Repository](https://github.com/TeachingOW/Sudoku-Solver)

---

### Lecture Code (`lectures/`)
**Description:** Code examples from specific lectures.

**Files:**
- `lec6_2.cpp` - Lecture 6 example 2
- `lec6_3.cpp` - Lecture 6 example 3

**Topics:** Various (see lecture notes)

---

### Exam Review (`exam_review/`)
**Description:** Review materials and example problems for exams.

**Files:**
- `review.md` - Exam review notes and sample problems

---

## Compilation Instructions

### For Most Examples (Linux/macOS)
```bash
g++ -std=c++11 -o output filename.cpp
./output
```

### For Most Examples (Windows)
```bash
g++ -std=c++11 -o output.exe filename.cpp
output.exe
```

### For BMP Examples
```bash
cd bmp
g++ -std=c++11 -o test test.cpp
./test
```

### Compilation Flags Explained
- `-std=c++11` - Use C++11 standard (or later: c++14, c++17, c++20)
- `-o` - Specify output file name
- `-Wall` - Enable all warnings (recommended for learning)
- `-g` - Include debugging information

---

## How to Use These Examples

1. **Start with basics:** Begin with examples in `basic/` directory
2. **Read the code:** Understand what each line does before running
3. **Modify and experiment:** Change values, add features, break things!
4. **Compile frequently:** Compile early and often to catch errors
5. **Use debugging tools:** Learn to use `gdb` or IDE debuggers

---

## Related Materials

- **Topics:** [topics/](https://github.com/TeachingOW/CPP-S26/tree/main/topics) - Concept explanations
- **Assignments:** [assignments/](https://github.com/TeachingOW/CPP-S26/tree/main/assignments) - Graded projects
- **Practice Problems:** [practice-problems/](https://github.com/TeachingOW/CPP-S26/tree/main/practice-problems) - Additional practice
- **Lectures:** [lectures/](https://github.com/TeachingOW/CPP-S26/tree/main/lectures) - Lecture notes and schedules

---

## External Code Repositories

- [Sudoku Solver](https://github.com/TeachingOW/Sudoku-Solver)
- [BMP Image Processing Quick start](https://github.com/TeachingOW/CPPF25-Assignment2)
- [SimdJson Quickstart](https://github.com/TeachingOW/simdjson-quickstart)
- [Unit Test Examples](https://github.com/TeachingOW/CPP-Unittest)

---

## Tips for Learning from Code Examples

1. **Don't just copy-paste:** Type the code yourself to build muscle memory
2. **Experiment:** Modify the code to see what happens
3. **Debug:** When something breaks, figure out why
4. **Comment:** Add your own comments explaining what you learned
5. **Extend:** Add new features to existing examples

---

## Compilation Best Practices

- Always use a recent C++ standard (C++11 or later)
- Enable compiler warnings to catch potential issues
- Test with different inputs and edge cases
- Use version control (git) for your own code
- Keep code organized and well-commented

---

**Need Help?** Check the [resources/](https://github.com/TeachingOW/CPP-S26/tree/main/resources) directory for books, cheat sheets, and external learning materials.
