---
layout: default
title: Template Specialization
---

<h1>Template Specialization</h1>

<p>
Template specialization lets you provide custom behavior for specific template arguments.
Use it when the generic implementation is not correct or not optimal for a known type.
</p>

<h2>Full Specialization</h2>
<p>Full specialization replaces the primary template for an exact type.</p>

<pre><code class="language-cpp">#include &lt;iostream&gt;

template &lt;typename T&gt;
struct Printer {
  static void print(const T&amp; value) {
    std::cout &lt;&lt; "generic: " &lt;&lt; value &lt;&lt; "\n";
  }
};

template &lt;&gt;
struct Printer&lt;bool&gt; {
  static void print(bool value) {
    std::cout &lt;&lt; (value ? "true" : "false") &lt;&lt; "\n";
  }
};</code></pre>

<h2>Partial Specialization</h2>
<p>Partial specialization customizes only part of a template argument pattern.</p>

<pre><code class="language-cpp">#include &lt;memory&gt;

template &lt;typename T&gt;
struct TypeInfo {
  static constexpr const char* name = "value type";
};

template &lt;typename T&gt;
struct TypeInfo&lt;T*&gt; {
  static constexpr const char* name = "raw pointer";
};

template &lt;typename T&gt;
struct TypeInfo&lt;std::unique_ptr&lt;T&gt;&gt; {
  static constexpr const char* name = "unique pointer";
};</code></pre>

<h2>Guidelines</h2>
<ul>
  <li>Prefer overloads or concepts first when behavior differs by operation.</li>
  <li>Use specialization when behavior differs by type representation.</li>
  <li>Keep specializations close to the primary template for readability.</li>
</ul>

> [!TIP]
> Full specialization matches one exact type. Partial specialization matches a family of types.
