---
layout: default
title: constexpr — C++
---

<h1><code>constexpr</code> — C++</h1>

<h2>What is constexpr?</h2>
<p><code>constexpr</code> (C++11) tells the compiler to evaluate an expression at <strong>compile time</strong> if possible. It applies to variables and functions. C++20 added <code>consteval</code> (compile-time only) and <code>constinit</code> (constant initialization).</p>

<hr>

<h2>constexpr Variables</h2>
<p>Must be initialized with a constant expression. Examples:</p>
<pre><code>constexpr int max_size = 100;
constexpr double pi = 3.14159265358979;
constexpr int arr_size = max_size * 2; // composed constexpr</code></pre>

<hr>

<h2>constexpr Functions</h2>
<p>Can be evaluated at compile time (if all arguments are constant expressions) or at runtime (if not). C++11 had a strict single-return-statement rule; C++14 relaxed it; C++20 allows virtual functions.</p>
<pre><code>constexpr int square(int x) { return x * x; }
constexpr int s = square(5);  // compile-time: s == 25
int n = 7;
int r = square(n);             // runtime evaluation</code></pre>

<hr>

<h2>constexpr if (C++17)</h2>
<p><code>if constexpr</code> selects a branch <strong>at compile time</strong> based on a constant expression. The discarded branch is not instantiated — this enables generic code without SFINAE tricks.</p>
<pre><code>template &lt;typename T&gt;
auto process(T val) {
    if constexpr (std::is_integral_v&lt;T&gt;) {
        return val * 2;
    } else {
        return val + 0.5;
    }
}</code></pre>

> [!TIP]
> <code>if constexpr</code> replaces many SFINAE patterns and tag dispatch tricks that were common before C++17.

<hr>

<h2>consteval (C++20)</h2>
<p>Functions marked <code>consteval</code> are <strong>immediate functions</strong> — they MUST be called at compile time. A runtime call is a compile error.</p>
<pre><code>consteval int triple(int x) { return x * 3; }
constexpr int t = triple(4);  // OK: compile-time
// int n = 5; triple(n);       // ERROR: n is not constexpr</code></pre>

<hr>

<h2>constinit (C++20)</h2>
<p><code>constinit</code> ensures a variable is <strong>constant-initialized</strong> (initialized at program start, not at first use). It does NOT make the variable constant — the value can change later. Prevents the "static initialization order fiasco."</p>
<pre><code>constinit int global_counter = 0;   // constant-initialized
// global_counter = 42;              // OK: not const</code></pre>

> [!WARNING]
> <code>constinit</code> only guarantees the <em>initialization</em> is constant - the variable itself is still mutable unless also declared <code>const</code>.

<hr>

<h2>Keyword Overview</h2>
<div class="mermaid">
flowchart TD
  A["constexpr (C++11)"] --> B["constexpr variable"]
  A --> C["constexpr function"]
  A --> D["if constexpr (C++17)"]
  A --> E["consteval (C++20)"]
  A --> F["constinit (C++20)"]
</div>

<h2>constexpr Function Evaluation</h2>
<div class="mermaid">
flowchart TD
  A["Call constexpr function"] --> B{"All args constant?"}
  B -->|"Yes"| C["Compile-time evaluation"]
  B -->|"No"| D["Runtime evaluation"]
  C --> E["Result embedded in binary"]
  D --> F["Result computed at runtime"]
</div>

<hr>

<h2>Summary Table</h2>
<table>
  <thead>
    <tr><th>Keyword</th><th>C++ Version</th><th>Purpose</th><th>Requirement</th></tr>
  </thead>
  <tbody>
    <tr><td><code>constexpr</code> var</td><td>C++11</td><td>Compile-time constant</td><td>Must be initialized with constant expression</td></tr>
    <tr><td><code>constexpr</code> fn</td><td>C++11</td><td>Compile-time or runtime evaluation</td><td>Body must be constexpr-compatible</td></tr>
    <tr><td><code>if constexpr</code></td><td>C++17</td><td>Compile-time branch selection</td><td>Condition must be constant expression</td></tr>
    <tr><td><code>consteval</code></td><td>C++20</td><td>Force compile-time evaluation</td><td>Call site must be constant expression</td></tr>
    <tr><td><code>constinit</code></td><td>C++20</td><td>Constant initialization guarantee</td><td>Must have constant initializer</td></tr>
  </tbody>
</table>
