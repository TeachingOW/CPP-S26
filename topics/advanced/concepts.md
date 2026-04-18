---
layout: default
title: Concepts
---

<h1>Concepts (C++20)</h1>

<p>
Concepts let you express template requirements directly in code,
which improves diagnostics and documents intent.
</p>

<h2>Built-in Concepts</h2>

<pre><code class="language-cpp">#include &lt;concepts&gt;

template &lt;std::integral T&gt;
T add_one(T v) {
  return v + 1;
}</code></pre>

<h2>Custom Concepts</h2>

<pre><code class="language-cpp">template &lt;typename T&gt;
concept Addable = requires(T a, T b) {
  { a + b } -&gt; std::same_as&lt;T&gt;;
};

template &lt;Addable T&gt;
T add(T a, T b) {
  return a + b;
}</code></pre>

<h2>Where Concepts Help Most</h2>
<ul>
  <li>Template-heavy codebases</li>
  <li>Public generic APIs</li>
  <li>Constraining algorithm input types</li>
</ul>

> [!NOTE]
> Concepts reduce cryptic template error messages by failing at the constraint boundary.
