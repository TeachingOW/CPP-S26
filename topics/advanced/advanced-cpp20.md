---
layout: default
title: Advanced C++20 Features
---

<h1>Advanced C++20 Features</h1>

<p>
C++20 introduced major language and library improvements that make templates safer,
ranges easier to compose, and large projects easier to organize.
</p>

<h2>Core Features Covered</h2>
<ul>
  <li><strong>Concepts</strong>: constrain templates with clear requirements</li>
  <li><strong>Ranges</strong>: compose lazy views and algorithms declaratively</li>
  <li><strong>Modules</strong>: replace most header/include usage with faster, cleaner boundaries</li>
</ul>

<h2>Quick Example</h2>

<pre><code class="language-cpp">#include &lt;concepts&gt;
#include &lt;ranges&gt;
#include &lt;vector&gt;

template &lt;std::integral T&gt;
T square(T x) { return x * x; }

int main() {
  std::vector&lt;int&gt; v{1, 2, 3, 4, 5};
  auto evenSquares = v
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * n; });
}</code></pre>

<h2>Recommended Learning Order</h2>
<ol>
  <li>Concepts</li>
  <li>Ranges</li>
  <li>Modules</li>
</ol>

> [!TIP]
> Concepts and ranges are useful immediately in application code; modules are most impactful at project scale.
