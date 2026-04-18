---
layout: default
title: std::optional, std::variant, std::any — C++
---

<h1><code>std::optional</code>, <code>std::variant</code>, <code>std::any</code> — C++</h1>

<h2>std::optional&lt;T&gt; (C++17)</h2>
<p>Represents a value that may or may not be present — a nullable value without pointers.</p>
<pre><code>#include &lt;optional&gt;

std::optional&lt;int&gt; find_age(const std::string&amp; name) {
    if (name == "Alice") return 30;
    return std::nullopt;
}

auto age = find_age("Alice");
if (age.has_value()) {
    std::cout &lt;&lt; age.value() &lt;&lt; "\n";  // 30
}
std::cout &lt;&lt; age.value_or(0) &lt;&lt; "\n"; // 30 or 0 if empty

// C++23 monadic operations
auto doubled = age.transform([](int v){ return v * 2; }); // optional&lt;int&gt;{60}</code></pre>

<blockquote>[!TIP]
Use <code>value_or(default)</code> to safely extract a value from an <code>optional</code> without risking <code>std::bad_optional_access</code>.
</blockquote>

<hr>

<h2>std::variant&lt;T1,T2,...&gt; (C++17)</h2>
<p>A type-safe union — holds exactly one value from a fixed set of types at any time.</p>
<pre><code>#include &lt;variant&gt;

std::variant&lt;int, double, std::string&gt; v;
v = 42;                                    // holds int
v = 3.14;                                  // holds double
v = std::string("hello");                  // holds string

// Check which type
if (std::holds_alternative&lt;std::string&gt;(v)) {
    std::cout &lt;&lt; std::get&lt;std::string&gt;(v) &lt;&lt; "\n";
}

// std::visit with overloaded lambda
std::visit([](auto&amp;&amp; val) {
    std::cout &lt;&lt; val &lt;&lt; "\n";
}, v);</code></pre>

<p>Overloaded visitor pattern:</p>
<pre><code>// Helper to create a visitor from multiple lambdas
template&lt;class... Ts&gt;
struct overloaded : Ts... { using Ts::operator()...; };

std::visit(overloaded{
    [](int i)               { std::cout &lt;&lt; "int: "    &lt;&lt; i &lt;&lt; "\n"; },
    [](double d)            { std::cout &lt;&lt; "double: " &lt;&lt; d &lt;&lt; "\n"; },
    [](const std::string&amp; s){ std::cout &lt;&lt; "string: " &lt;&lt; s &lt;&lt; "\n"; }
}, v);</code></pre>

<blockquote>[!NOTE]
<code>std::get&lt;T&gt;(v)</code> throws <code>std::bad_variant_access</code> if the variant does not hold type <code>T</code>. Use <code>std::get_if&lt;T&gt;(&amp;v)</code> for a non-throwing pointer-based access.
</blockquote>

<hr>

<h2>std::any (C++17)</h2>
<p>Type-erased container — can hold any copyable value, type checked at runtime.</p>
<pre><code>#include &lt;any&gt;

std::any a = 42;
a = std::string("hello");
a = 3.14;

// Access (throws std::bad_any_cast if wrong type)
try {
    double d = std::any_cast&lt;double&gt;(a);
    std::cout &lt;&lt; d &lt;&lt; "\n";
} catch (const std::bad_any_cast&amp; e) {
    std::cerr &lt;&lt; "wrong type\n";
}

// Safe access via pointer
if (auto* p = std::any_cast&lt;double&gt;(&amp;a)) {
    std::cout &lt;&lt; *p &lt;&lt; "\n";
}</code></pre>

<blockquote>[!WARNING]
<code>std::any</code> involves heap allocation and runtime type checks. Prefer <code>std::variant</code> when the set of types is known at compile time.
</blockquote>

<hr>

<h2>When to Use Each</h2>
<ul>
  <li><strong><code>optional&lt;T&gt;</code></strong>: when a value might be absent (nullable return values, optional parameters)</li>
  <li><strong><code>variant&lt;T1,T2&gt;</code></strong>: when a value must be one of a known set of types (tagged union, state machines)</li>
  <li><strong><code>any</code></strong>: when the type is truly unknown at compile time (plugin systems, scripting bridges)</li>
</ul>

<hr>

<h2>optional Lifecycle</h2>
<div class="mermaid">
flowchart LR
  A["std::nullopt (empty)"] -->|"assign value"| B["has_value() == true"]
  B -->|"value()"| C["Access T"]
  B -->|"reset()"| A
  A -->|"value_or(def)"| D["Returns default"]
  B -->|"value_or(def)"| C
</div>

<h2>variant Visitor Pattern</h2>
<div class="mermaid">
flowchart TD
  A["std::variant holds value"] --> B["std::visit(visitor, v)"]
  B --> C{"Runtime type check"}
  C -->|"is int"| D["Call visitor(int)"]
  C -->|"is double"| E["Call visitor(double)"]
  C -->|"is string"| F["Call visitor(string)"]
</div>

<h2>Decision Tree</h2>
<div class="mermaid">
flowchart TD
  A["Need nullable or multi-type value?"] --> B{"Known fixed set of types?"}
  B -->|"Yes, one optional value"| C{"Can be absent?"}
  C -->|"Yes"| D["Use std::optional"]
  C -->|"No"| E["Use direct type"]
  B -->|"Yes, multiple types"| F["Use std::variant"]
  B -->|"No, any type"| G["Use std::any"]
</div>

<hr>

<h2>Summary Table</h2>
<table>
  <thead>
    <tr><th>Type</th><th>Header</th><th>Use case</th><th>Type safety</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td><code>std::optional&lt;T&gt;</code></td><td><code>&lt;optional&gt;</code></td><td>Nullable single value</td><td>Compile-time</td><td>C++17; monadic ops C++23</td></tr>
    <tr><td><code>std::variant&lt;Ts...&gt;</code></td><td><code>&lt;variant&gt;</code></td><td>One of N known types</td><td>Compile-time</td><td>C++17; use <code>std::visit</code></td></tr>
    <tr><td><code>std::any</code></td><td><code>&lt;any&gt;</code></td><td>Any copyable value</td><td>Runtime</td><td>C++17; slower, use sparingly</td></tr>
  </tbody>
</table>
