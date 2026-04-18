---
layout: default
title: Modules
---

<h1>Modules (C++20)</h1>

<p>
Modules are a modern alternative to the traditional header/include model.
They improve build scalability and reduce accidental macro leakage.
</p>

<h2>Basic Syntax</h2>

<pre><code class="language-cpp">// math.ixx
export module math;

export int add(int a, int b) {
  return a + b;
}</code></pre>

<pre><code class="language-cpp">// main.cpp
import math;
#include &lt;iostream&gt;

int main() {
  std::cout &lt;&lt; add(2, 3) &lt;&lt; "\n";
}</code></pre>

<h2>Why Modules</h2>
<ul>
  <li>Faster incremental builds in large projects</li>
  <li>Better encapsulation of internal declarations</li>
  <li>Cleaner dependency boundaries</li>
</ul>

<h2>Practical Note</h2>
<p>
Compiler and build-system support is improving, but setup differs across toolchains.
For course assignments, headers are still fine unless module support is explicitly required.
</p>

> [!WARNING]
> Module support can be compiler-version and build-tool specific. Always verify flags and toolchain docs.
