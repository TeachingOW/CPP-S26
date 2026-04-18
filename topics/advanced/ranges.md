---
layout: default
title: Ranges
---

<h1>Ranges (C++20)</h1>

<p>
Ranges provide composable, lazy operations over sequences.
You can build pipelines with views and then consume them efficiently.
</p>

<h2>Pipeline Example</h2>

<pre><code class="language-cpp">#include &lt;iostream&gt;
#include &lt;ranges&gt;
#include &lt;vector&gt;

int main() {
  std::vector&lt;int&gt; data{1, 2, 3, 4, 5, 6};

  auto result = data
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * 10; });

  for (int n : result) {
    std::cout &lt;&lt; n &lt;&lt; " ";
  }
}</code></pre>

<h2>Common Views</h2>
<ul>
  <li><code>std::views::filter</code></li>
  <li><code>std::views::transform</code></li>
  <li><code>std::views::take</code></li>
  <li><code>std::views::drop</code></li>
</ul>

<h2>Benefits</h2>
<ul>
  <li>Readable data-flow style</li>
  <li>Lazy evaluation</li>
  <li>Fewer temporary containers</li>
</ul>

> [!TIP]
> Prefer ranges for transformation pipelines; use classic loops when mutation-heavy control flow is clearer.
