---
layout: default
title: Scoped Enums
---

<h1>Scoped Enums (enum class)</h1>

<p>
Scoped enums were introduced in C++11 to provide type-safe enumerations with controlled scope.
They avoid implicit conversions to integers and prevent name collisions.
</p>

<h2>Unscoped vs Scoped</h2>

<pre><code class="language-cpp">enum ColorOld { Red, Green, Blue };       // unscoped

enum class Color { Red, Green, Blue };    // scoped

enum class Status : int { Ok = 0, Error = 1 };</code></pre>

<h2>Key Differences</h2>
<ul>
  <li><code>enum class</code> members are scoped: <code>Color::Red</code></li>
  <li>No implicit conversion to <code>int</code></li>
  <li>Underlying type can be specified explicitly</li>
</ul>

<h2>Converting to Integer</h2>

<pre><code class="language-cpp">Color c = Color::Green;
int x = static_cast&lt;int&gt;(c);</code></pre>

<h2>Why Use Scoped Enums</h2>
<ul>
  <li>Improved type safety</li>
  <li>Cleaner APIs</li>
  <li>Fewer accidental bugs from implicit conversions</li>
</ul>

> [!NOTE]
> Prefer <code>enum class</code> in modern C++ unless you specifically need legacy unscoped behavior.
