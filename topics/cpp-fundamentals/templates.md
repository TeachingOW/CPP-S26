# C/C++ Templates

Templates in C/C++ allow us to define generic functions and classes that work with any data type. They enable code reusability and type safety while maintaining high performance.

## Why Use Templates?
- **Code Reusability**: Write generic code that works with multiple data types.
- **Type Safety**: Ensures correctness at compile-time.
- **Performance**: Eliminates the need for runtime type checking.

## Function Templates
A function template allows a function to operate on different data types without rewriting it.

### Example: Function Template for Maximum Value
```cpp
#include <iostream>
using namespace std;

// Template function to find maximum of two values
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    cout << "Max of 10 and 20: " << findMax(10, 20) << endl;
    cout << "Max of 5.5 and 2.2: " << findMax(5.5, 2.2) << endl;
    return 0;
}
```

## Class Templates
A class template allows us to define a blueprint for a class that can work with any data type.

### Example: Class Template for a Simple Pair
```cpp
#include <iostream>
using namespace std;

// Template class for a pair of values
template <typename T1, typename T2>
class Pair {
private:
    T1 first;
    T2 second;
public:
    Pair(T1 f, T2 s) : first(f), second(s) {}
    void display() {
        cout << "(" << first << ", " << second << ")" << endl;
    }
};

int main() {
    Pair<int, double> p1(10, 20.5);
    p1.display(); // Output: (10, 20.5)
    
    Pair<string, int> p2("Alice", 30);
    p2.display(); // Output: (Alice, 30)
    return 0;
}
```

## Template Specialization
Sometimes, we need a specific implementation of a template for a certain type.

### Example: Specialization for `char*`
```cpp
#include <iostream>
#include <cstring>
using namespace std;

// General template
template <typename T>
T findMax(T a, T b) {
    return (a > b) ? a : b;
}

// Specialization for char*
template <>
const char* findMax<const char*>(const char* a, const char* b) {
    return (strcmp(a, b) > 0) ? a : b;
}

int main() {
    cout << "Max of Hello and World: " << findMax("Hello", "World") << endl;
    return 0;
}
```

## Non-Type Template Parameters (Number Templates)
Templates can also accept non-type parameters, such as integers, at compile time. This is useful for fixed-size data structures and compile-time constants.

### Example: Fixed-Size Array with a Number Template
```cpp
#include <iostream>
using namespace std;

// Template with a non-type (number) parameter
template <typename T, int N>
class FixedArray {
private:
    T data[N];
public:
    FixedArray() {
        for (int i = 0; i < N; i++) data[i] = T{};
    }
    T& operator[](int index) { return data[index]; }
    int size() const { return N; }
};

int main() {
    FixedArray<int, 5> arr;
    arr[0] = 10;
    arr[1] = 20;
    cout << "Size: " << arr.size() << endl;   // Output: 5
    cout << "arr[0]: " << arr[0] << endl;     // Output: 10
    return 0;
}
```

The size `N` is a **compile-time constant** — the array lives on the stack and no dynamic allocation is needed.

### Example: Power Function Template (typename base, constant int exponent)

A function template where the **base type** (`T`) is a typename and the **exponent** is a compile-time constant integer:

```cpp
#include <iostream>
using namespace std;

// T  = type of the base (int, double, float, ...)
// Exp = exponent — must be known at compile time
template <typename T, int Exp>
T power(T base) {
    T result = 1;
    for (int i = 0; i < Exp; i++) {
        result *= base;
    }
    return result;
}

int main() {
    cout << power<int, 3>(2)      << endl; // 2^3  = 8
    cout << power<double, 4>(1.5) << endl; // 1.5^4 = 5.0625
    cout << power<float, 0>(99.9) << endl; // anything^0 = 1
    return 0;
}
```

Key points:
- `T` can be any numeric type (`int`, `double`, `float`, …).
- `Exp` is baked in at **compile time** — a different function is generated for each exponent value used.
- Calling `power<double, 4>(1.5)` is equivalent to writing `1.5 * 1.5 * 1.5 * 1.5` with the loop fully known to the compiler.

### Example: Compile-Time Power (struct / template metaprogramming)
```cpp
template <int Base, int Exp>
struct Power {
    static const int value = Base * Power<Base, Exp - 1>::value;
};

template <int Base>
struct Power<Base, 0> {
    static const int value = 1;
};

int main() {
    cout << Power<2, 10>::value << endl; // Output: 1024
    return 0;
}
```

The entire calculation happens at **compile time** — no runtime cost.

## Best Practices for Templates
- Use meaningful names for template parameters (e.g., `typename T1, T2`).
- Avoid unnecessary template instantiations to reduce compilation time.
- Consider template specialization for edge cases.

## Conclusion
C++ templates provide a powerful way to write reusable and efficient code. Function templates and class templates help achieve type safety and code flexibility, while specialization allows fine-tuning for specific needs.