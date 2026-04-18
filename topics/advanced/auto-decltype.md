---
layout: default
title: auto and decltype — C++
---

<h1><code>auto</code> and <code>decltype</code> — C++</h1>

<h2>auto — Type Deduction (C++11)</h2>
<p><code>auto</code> tells the compiler to deduce the type from the initializer. Reduces verbosity and keeps code in sync with type changes.</p>

<p>Variable examples:</p>
<pre><code>auto x = 42;            // int
auto pi = 3.14;         // double
auto s = std::string{"hello"}; // std::string
auto it = vec.begin();  // std::vector&lt;int&gt;::iterator</code></pre>

<p>Return type deduction (C++14):</p>
<pre><code>auto add(int a, int b) { return a + b; } // return type: int</code></pre>

<p>Structured bindings (C++17):</p>
<pre><code>std::pair&lt;int, std::string&gt; p{1, "one"};
auto [num, name] = p;   // num: int, name: std::string</code></pre>

<hr>

<h2>decltype — Type Introspection</h2>
<p><code>decltype(expr)</code> yields the type of an expression <strong>without evaluating it</strong>.</p>

<pre><code>int x = 0;
decltype(x) y = 5;        // y is int
decltype(x + 0.0) z = 1.5; // z is double

std::vector&lt;int&gt; v;
decltype(v)::iterator it = v.begin(); // vector&lt;int&gt;::iterator</code></pre>

<p><code>decltype(auto)</code> (C++14) — deduces type including references and cv-qualifiers:</p>
<pre><code>int x = 42;
int&amp; ref = x;
decltype(auto) a = ref;  // a is int&amp; (reference preserved)
auto b = ref;            // b is int (reference stripped)</code></pre>

<hr>

<h2>Trailing Return Types</h2>
<p>Used when the return type depends on parameter types:</p>
<pre><code>template &lt;typename A, typename B&gt;
auto multiply(A a, B b) -&gt; decltype(a * b) {
    return a * b;
}</code></pre>

<hr>

<h2>auto in Lambdas (C++14 Generic Lambdas)</h2>
<pre><code>auto greet = [](auto name) {
    return std::string("Hello, ") + name;
};
greet("world");   // works with any string-like type</code></pre>

<hr>

<h2>Common Pitfalls</h2>
<p><code>auto</code> strips references and cv-qualifiers:</p>
<pre><code>const int&amp; cref = x;
auto a = cref;       // a is int (not const int&amp;!)
auto&amp; b = cref;      // b is const int&amp; (reference preserved)
const auto&amp; c = cref; // c is const int&amp;</code></pre>

> [!WARNING]
> When using <code>auto</code> with references or const-qualified types, always add <code>&amp;</code> or <code>const auto&amp;</code> to preserve those qualifiers.

<hr>

<h2>auto Type Deduction Flow</h2>
<div class="mermaid">
flowchart TD
  A["auto x = expr"] --> B{"Is expr a reference?"}
  B -->|"Yes"| C["Strip reference"]
  C --> D{"Has cv-qualifiers?"}
  B -->|"No"| D
  D -->|"Yes"| E["Strip cv-qualifiers"]
  D -->|"No"| F["Deduce base type"]
  E --> F
  F --> G["x has deduced type"]
</div>

<h2>decltype vs auto Decision</h2>
<div class="mermaid">
flowchart TD
  A["Need to capture a type"] --> B{"Preserve references and cv?"}
  B -->|"Yes"| C["Use decltype(auto)"]
  B -->|"No"| D{"Have initializer expression?"}
  D -->|"Yes"| E["Use auto"]
  D -->|"No"| F{"Have an expression to inspect?"}
  F -->|"Yes"| G["Use decltype(expr)"]
  F -->|"No"| H["Use explicit type"]
</div>

<hr>

<h2>Summary Table</h2>
<table>
  <thead>
    <tr><th>Feature</th><th>Syntax</th><th>What it deduces</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td><code>auto</code> variable</td><td><code>auto x = expr;</code></td><td>Type of expr (strips ref/cv)</td><td>C++11</td></tr>
    <tr><td><code>auto</code> return</td><td><code>auto fn() { ... }</code></td><td>Return expression type</td><td>C++14</td></tr>
    <tr><td>Structured binding</td><td><code>auto [a,b] = pair;</code></td><td>Member types</td><td>C++17</td></tr>
    <tr><td><code>decltype(expr)</code></td><td><code>decltype(x+1) v;</code></td><td>Exact type of expression</td><td>No evaluation</td></tr>
    <tr><td><code>decltype(auto)</code></td><td><code>decltype(auto) x = expr;</code></td><td>Type preserving ref and cv</td><td>C++14</td></tr>
    <tr><td>Trailing return</td><td><code>auto f() -&gt; decltype(...)</code></td><td>Expression-dependent return</td><td>C++11</td></tr>
  </tbody>
</table>
