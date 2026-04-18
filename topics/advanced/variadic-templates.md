---
layout: default
title: Variadic Templates — C++
---

<h1>Variadic Templates — C++</h1>

<h2>What are Variadic Templates?</h2>
<p>Introduced in C++11, variadic templates accept <strong>any number of type arguments</strong>. They power <code>std::tuple</code>, <code>std::make_unique</code>, <code>std::forward</code>, and many other standard library facilities.</p>

<hr>

<h2>Parameter Pack Syntax</h2>
<pre><code>template &lt;typename... Args&gt;   // template parameter pack
void print_all(Args... args); // function parameter pack

// sizeof... gets the count
template &lt;typename... Args&gt;
constexpr std::size_t count() { return sizeof...(Args); }</code></pre>

<hr>

<h2>Pack Expansion</h2>
<p>Appending <code>...</code> expands a pack in the appropriate context:</p>
<pre><code>template &lt;typename... Args&gt;
void forward_all(Args&amp;&amp;... args) {
    some_func(std::forward&lt;Args&gt;(args)...); // expands both packs
}</code></pre>

<hr>

<h2>Recursive Variadic Templates</h2>
<p>Classic C++11 pattern: base case + recursive case:</p>
<pre><code>// Base case
void print() {}

// Recursive case
template &lt;typename T, typename... Rest&gt;
void print(T first, Rest... rest) {
    std::cout &lt;&lt; first &lt;&lt; " ";
    print(rest...);   // recurse with remaining args
}
// Usage: print(1, "hello", 3.14);</code></pre>

> [!NOTE]
> C++17 fold expressions replace most recursive variadic templates with shorter, clearer code.

<hr>

<h2>Fold Expressions (C++17)</h2>
<p>Fold expressions collapse a pack using a binary operator in a single expression:</p>
<pre><code>// Unary right fold: (args op ...)
template &lt;typename... Args&gt;
auto sum(Args... args) { return (args + ...); }

// Unary left fold: (... op args)
template &lt;typename... Args&gt;
auto sum_left(Args... args) { return (... + args); }

// Binary fold with initial value
template &lt;typename... Args&gt;
auto sum_with_init(Args... args) { return (0 + ... + args); }

// Print with fold
template &lt;typename... Args&gt;
void print_all(Args&amp;&amp;... args) {
    ((std::cout &lt;&lt; args &lt;&lt; " "), ...);
}</code></pre>

<hr>

<h2>sizeof...(Args)</h2>
<pre><code>template &lt;typename... Args&gt;
void show_count(Args... args) {
    std::cout &lt;&lt; "Pack has " &lt;&lt; sizeof...(args) &lt;&lt; " elements\n";
}</code></pre>

<hr>

<h2>Common Use Cases</h2>
<p>Perfect forwarding wrapper:</p>
<pre><code>template &lt;typename T, typename... Args&gt;
std::unique_ptr&lt;T&gt; make(Args&amp;&amp;... args) {
    return std::unique_ptr&lt;T&gt;(new T(std::forward&lt;Args&gt;(args)...));
}</code></pre>

> [!TIP]
> This pattern is exactly how <code>std::make_unique</code> and <code>std::make_shared</code> are implemented in the standard library.

<hr>

<h2>Variadic Template Instantiation</h2>
<div class="mermaid">
flowchart TD
  A["print(1, hello, 3.14)"] --> B["Instantiate print(int, string, double)"]
  B --> C["Print 1, call print(hello, 3.14)"]
  C --> D["Instantiate print(string, double)"]
  D --> E["Print hello, call print(3.14)"]
  E --> F["Instantiate print(double)"]
  F --> G["Print 3.14, call print()"]
  G --> H["Base case: print() - done"]
</div>

<h2>Fold Expression Types</h2>
<div class="mermaid">
flowchart LR
  A["Fold Expressions (C++17)"] --> B["Unary Right Fold"]
  A --> C["Unary Left Fold"]
  A --> D["Binary Right Fold"]
  A --> E["Binary Left Fold"]
  B --> B1["(args op ...)"]
  C --> C1["(... op args)"]
  D --> D1["(args op ... op init)"]
  E --> E1["(init op ... op args)"]
</div>

<hr>

<h2>Summary Table</h2>
<table>
  <thead>
    <tr><th>Feature</th><th>Syntax</th><th>C++ Version</th><th>Use case</th></tr>
  </thead>
  <tbody>
    <tr><td>Parameter pack</td><td><code>typename... Args</code></td><td>C++11</td><td>Accept any number of types</td></tr>
    <tr><td>Pack expansion</td><td><code>args...</code></td><td>C++11</td><td>Expand pack in expression</td></tr>
    <tr><td><code>sizeof...</code></td><td><code>sizeof...(Args)</code></td><td>C++11</td><td>Count pack elements</td></tr>
    <tr><td>Recursive variadic</td><td>base + recursive fn</td><td>C++11</td><td>Process each element</td></tr>
    <tr><td>Unary fold</td><td><code>(args op ...)</code></td><td>C++17</td><td>Reduce pack with operator</td></tr>
    <tr><td>Binary fold</td><td><code>(init op ... op args)</code></td><td>C++17</td><td>Reduce with initial value</td></tr>
  </tbody>
</table>
