---
layout: default
title: Range-Based For Loops — C++
---

<h1>Range-Based For Loops — C++</h1>

<h2>Syntax</h2>
<pre><code>for (declaration : range_expression) { statement }
// Example:
std::vector&lt;int&gt; v = {1, 2, 3, 4, 5};
for (auto x : v) { std::cout &lt;&lt; x &lt;&lt; "\n"; }</code></pre>

<hr>

<h2>How It Works — Lowering to Iterators</h2>
<p>The compiler transforms <code>for (auto x : range)</code> into:</p>
<pre><code>{
    auto&amp;&amp; __range = range;
    auto __begin = begin(__range);
    auto __end   = end(__range);
    for (; __begin != __end; ++__begin) {
        auto x = *__begin;
        // body
    }
}</code></pre>

<hr>

<h2>Works With</h2>
<ul>
  <li>C-style arrays: <code>int arr[] = {1,2,3};</code></li>
  <li>STL containers: <code>std::vector</code>, <code>std::list</code>, <code>std::map</code>, etc.</li>
  <li><code>std::initializer_list</code></li>
  <li>Custom types: must provide <code>begin()</code> and <code>end()</code> (member or ADL free functions)</li>
</ul>

<pre><code>// Custom type example
struct Range {
    int* begin() { return data; }
    int* end()   { return data + size; }
    int data[4] = {10, 20, 30, 40};
    int size = 4;
};
Range r;
for (auto v : r) { /* ... */ }</code></pre>

<hr>

<h2>Value vs Reference vs Const Reference</h2>
<pre><code>std::vector&lt;std::string&gt; names = {"Alice", "Bob", "Carol"};

for (auto name : names)         // COPY — safe but expensive
for (auto&amp; name : names)        // REFERENCE — modify allowed, no copy
for (const auto&amp; name : names)  // CONST REF — safe, no copy (preferred for read)</code></pre>

<blockquote>[!TIP]
Prefer <code>const auto&amp;</code> for read-only iteration over containers holding non-trivial types — it avoids copies entirely.
</blockquote>

<hr>

<h2>Structured Bindings with Range-For (C++17)</h2>
<pre><code>std::map&lt;std::string, int&gt; scores = {{"Alice", 95}, {"Bob", 87}};
for (auto&amp; [name, score] : scores) {
    std::cout &lt;&lt; name &lt;&lt; ": " &lt;&lt; score &lt;&lt; "\n";
}</code></pre>

<hr>

<h2>Modifying Elements</h2>
<p>Must use <code>auto&amp;</code>:</p>
<pre><code>std::vector&lt;int&gt; v = {1, 2, 3, 4};
for (auto&amp; x : v) { x *= 2; }  // v is now {2, 4, 6, 8}</code></pre>

<hr>

<h2>Index Tracking Workaround</h2>
<p>Range-for has no built-in index. Options:</p>
<pre><code>// Manual counter
int i = 0;
for (const auto&amp; x : v) { std::cout &lt;&lt; i &lt;&lt; ": " &lt;&lt; x &lt;&lt; "\n"; ++i; }

// C++23 enumerate (ranges::views::enumerate)
// for (auto [i, x] : std::views::enumerate(v)) { ... }</code></pre>

<blockquote>[!NOTE]
C++23 introduces <code>std::views::enumerate</code> which provides index-value pairs directly in a range-for loop.
</blockquote>

<hr>

<h2>Range-for Expansion</h2>
<div class="mermaid">
flowchart TD
  A["for (auto x : range)"] --> B["auto range = range_expr"]
  B --> C["auto begin = begin(range)"]
  C --> D["auto end = end(range)"]
  D --> E{"begin != end?"}
  E -->|"Yes"| F["auto x = *begin"]
  F --> G["Execute body"]
  G --> H["++begin"]
  H --> E
  E -->|"No"| I["Loop ends"]
</div>

<h2>Which Loop Form to Choose</h2>
<div class="mermaid">
flowchart TD
  A["Range-for loop"] --> B{"Need to modify elements?"}
  B -->|"Yes"| C["for (auto&amp; x : range)"]
  B -->|"No"| D{"Elements expensive to copy?"}
  D -->|"Yes"| E["for (const auto&amp; x : range)"]
  D -->|"No"| F["for (auto x : range)"]
</div>

<hr>

<h2>Summary Table</h2>
<table>
  <thead>
    <tr><th>Syntax</th><th>Use case</th><th>Modifies?</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td><code>for (auto x : v)</code></td><td>Small/cheap types, read only</td><td>No</td><td>Makes a copy each iteration</td></tr>
    <tr><td><code>for (auto&amp; x : v)</code></td><td>Any type, modify elements</td><td>Yes</td><td>Direct reference to element</td></tr>
    <tr><td><code>for (const auto&amp; x : v)</code></td><td>Any type, read only</td><td>No</td><td>Most efficient for read-only</td></tr>
    <tr><td><code>for (auto&amp; [k,v] : map)</code></td><td>Key-value containers</td><td>Yes</td><td>C++17 structured binding</td></tr>
    <tr><td><code>for (const auto&amp; [k,v] : map)</code></td><td>Key-value containers, read</td><td>No</td><td>C++17 structured binding</td></tr>
  </tbody>
</table>
