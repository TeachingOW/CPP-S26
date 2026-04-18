---
layout: default
title: Rule of Five — C++
---

<h1>Rule of Three/Five — C++</h1>

<h2>From Rule of Three to Rule of Five</h2>

<p>
The <strong>Rule of Three</strong> (C++98) says: if a class defines any one of these, it must define <strong>all three</strong>:
</p>

<ol>
  <li><strong>Destructor</strong></li>
  <li><strong>Copy constructor</strong></li>
  <li><strong>Copy assignment operator</strong></li>
</ol>

<p>
Modern C++ (C++11 and later) adds <strong>move semantics</strong>, extending this to the <strong>Rule of Five</strong>:
</p>

<ol>
  <li><strong>Destructor</strong></li>
  <li><strong>Copy constructor</strong></li>
  <li><strong>Copy assignment operator</strong></li>
  <li><strong>Move constructor</strong> <em>(C++11)</em></li>
  <li><strong>Move assignment operator</strong> <em>(C++11)</em></li>
</ol>


>[!NOTE]
>See also: <a href="https://www.youtube.com/watch?v=bvCEqS4S0sg">Rule of Three (video)</a> and <a href="https://www.youtube.com/watch?v=St0MNEU5b0o">Move Semantics (video)</a>


<div class="mermaid">
flowchart TD
  A["Class manages dynamic resource"]
  B["Destructor"]
  C["Copy constructor"]
  D["Copy assignment operator"]
  E["Move constructor (C++11)"]
  F["Move assignment operator (C++11)"]
  G["All 5 must handle memory correctly"]

  A --> B
  A --> C
  A --> D
  A --> E
  A --> F
  B --> G
  C --> G
  D --> G
  E --> G
  F --> G
</div>

---

<h2>Why It Matters</h2>

<p>These member functions <strong>initialize</strong> and <strong>manage</strong> an object's owned resources.</p>
<p>Improper handling leads to:</p>

<ul>
  <li>🔴 <strong>Double deletion</strong></li>
  <li>🔴 <strong>Memory leaks</strong></li>
  <li>🔴 <strong>Dangling pointers</strong></li>
  <li>🔴 <strong>Unnecessary copies (performance)</strong></li>
</ul>

<div class="mermaid">
flowchart LR
  X["Constructor allocates (new)"] --> Y["Destructor deallocates (delete)"]
  Y --> Z["Copy: duplicate safely"]
  Z --> M["Move: transfer ownership (no copy)"]
  M --> X
</div>


---

<h2>Example Class: <code>MaybeInt</code></h2>

<p>A class that may or may not own an integer in dynamic memory.</p>

<pre><code class="language-cpp">class MaybeInt {
 public:
  MaybeInt() : value_(nullptr) {}
  MaybeInt(int value) : value_(new int(value)) {}

  // 1. Destructor
  ~MaybeInt() { delete value_; }

  // 2. Copy constructor — deep copy
  MaybeInt(const MaybeInt&amp; other) {
    value_ = other.value_ ? new int(*other.value_) : nullptr;
  }

  // 3. Copy assignment operator — deep copy
  MaybeInt&amp; operator=(const MaybeInt&amp; other) {
    if (this != &amp;other) {
      delete value_;
      value_ = other.value_ ? new int(*other.value_) : nullptr;
    }
    return *this;
  }

  // 4. Move constructor — transfer ownership
  MaybeInt(MaybeInt&amp;&amp; other) noexcept : value_(other.value_) {
    other.value_ = nullptr;   // leave source in valid empty state
  }

  // 5. Move assignment operator — transfer ownership
  MaybeInt&amp; operator=(MaybeInt&amp;&amp; other) noexcept {
    if (this != &amp;other) {
      delete value_;
      value_ = other.value_;
      other.value_ = nullptr; // leave source in valid empty state
    }
    return *this;
  }

 private:
  int* value_;
};
</code></pre>

<div class="mermaid">
classDiagram
class MaybeInt {
    - int* value_
    + MaybeInt()
    + MaybeInt(int value)
    + ~MaybeInt()
    + MaybeInt(MaybeInt const-ref other)
    + operator=(MaybeInt const-ref other) MaybeInt-ref
    + MaybeInt(MaybeInt rref other)
    + operator=(MaybeInt rref other) MaybeInt-ref
}
</div>

---

<h2>Bug Example — Shallow Copy (No Rule of Three/Five)</h2>

<pre><code class="language-cpp">int main() {
  MaybeInt a(7);
  MaybeInt b(a); // Copy constructor (shallow without Rule of Five)
  MaybeInt c;
  c = a;         // Copy assignment (shallow without Rule of Five)
  return 0;      // Both a and b delete the same pointer!
}
</code></pre>

<h3>🔗 Interactive Visualization</h3>

<p>👉 <a href="https://pythontutor.com/render.html#code=class%20MaybeInt%20%7B%0A%20public%3A%0A%20%20MaybeInt%28%29%20%3A%20value_%28nullptr%29%20%7B%7D%0A%20%20MaybeInt%28int%20value%29%20%3A%20value_%28new%20int%28value%29%29%20%7B%7D%0A%0A%20%20~MaybeInt%28%29%20%7B%0A%20%20%20%20if%20%28value_%20!%3D%20nullptr%29%20%7B%0A%20%20%20%20%20%20delete%20value_%3B%0A%20%20%20%20%7D%0A%20%20%7D%0A%0A%20private%3A%0A%20%20int*%20value_%3B%0A%7D%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20MaybeInt%20a%287%29%3B%0A%20%20MaybeInt%20b%28a%29%3B%20//%20Copy%20constructor%20%28shallow%29%0A%20%20MaybeInt%20c%3B%0A%20%20c%20%3D%20a%3B%20%20%20%20%20%20%20%20%20//%20Copy%20assignment%20%28shallow%29%0A%20%20return%200%3B%0A%7D&cumulative=false&curInstr=12&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp_g%2B%2B9.3.0&rawInputLstJSON=%5B%5D&textReferences=false" target="_blank" rel="noopener">View shallow-copy bug in Python Tutor</a></p>

---

<h2>Animation — Copy Problem (Shallow Copy / Double Delete)</h2>

<div id="pointer-animation1">
  <canvas id="pointerCanvas1" width="620" height="370" style="border:1px solid #ccc; border-radius:6px; display:block;"></canvas>
</div>

<script>
(function() {
  var canvas = document.getElementById('pointerCanvas1');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');

  var step = 0;

  var stack = [
    {name: 'a::value_', x: 50, y: 60,  target: null},
    {name: 'b::value_', x: 50, y: 110, target: null},
    {name: 'c::value_', x: 50, y: 160, target: null}
  ];

  var heap       = {name: '7',       x: 320, y: 110, invalid: false, visible: false};
  var nullptrPos = {name: 'nullptr', x: 370, y: 230, visible: false};
  var showDoubleDelete = false;

  var steps = [
    "Initial state — no pointers set",
    "MaybeInt a(7) — a::value_ points to heap(7)",
    "MaybeInt b(a) — shallow copy: b::value_ points to same heap(7)",
    "MaybeInt c    — c::value_ = nullptr",
    "c = a         — shallow: c::value_ points to same heap(7)",
    "Destructor for a — deletes heap(7), now invalid",
    "Destructor for b — tries to delete same heap! Double delete!"
  ];

  function drawArrow(fromX, fromY, toX, toY, color) {
    ctx.beginPath();
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(toX, toY);
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.stroke();
    var angle = Math.atan2(toY - fromY, toX - fromX);
    ctx.beginPath();
    ctx.moveTo(toX, toY);
    ctx.lineTo(toX - 10 * Math.cos(angle - 0.4), toY - 10 * Math.sin(angle - 0.4));
    ctx.lineTo(toX - 10 * Math.cos(angle + 0.4), toY - 10 * Math.sin(angle + 0.4));
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
  }

  function drawBox(x, y, w, h, fill, text) {
    ctx.fillStyle = fill;
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.strokeRect(x, y, w, h);
    ctx.fillStyle = '#000';
    ctx.font = '13px monospace';
    ctx.fillText(text, x + 4, y + 15);
  }

  function drawPointer(obj) {
    drawBox(obj.x, obj.y, 80, 22, '#87CEFA', obj.name);
    if (obj.target) {
      var color = (obj.target === nullptrPos) ? 'red' : '#333';
      drawArrow(obj.x + 80, obj.y + 11, obj.target.x, obj.target.y + 11, color);
    }
  }

  function drawHeap() {
    if (heap.visible) {
      drawBox(heap.x, heap.y, 80, 22, heap.invalid ? '#FF6347' : '#90EE90',
              heap.invalid ? 'freed' : heap.name);
    }
    if (nullptrPos.visible) {
      drawBox(nullptrPos.x, nullptrPos.y, 70, 22, '#FFD700', 'nullptr');
    }
  }

  function drawStep() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = '#555';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('Stack', 50, 40);
    ctx.fillText('Heap', 320, 40);

    ctx.fillStyle = '#000';
    ctx.font = '14px sans-serif';
    ctx.fillText('Step ' + step + ': ' + steps[step], 10, 20);

    drawHeap();
    stack.forEach(drawPointer);

    if (showDoubleDelete) {
      ctx.fillStyle = 'red';
      ctx.font = 'bold 16px sans-serif';
      ctx.fillText('Double Delete!', heap.x + 90, heap.y + 15);
    }

    ctx.fillStyle = '#E0E0E0';
    ctx.strokeStyle = '#666';
    ctx.lineWidth = 1;
    ctx.fillRect(150, 300, 80, 30);
    ctx.strokeRect(150, 300, 80, 30);
    ctx.fillStyle = '#000';
    ctx.font = '14px sans-serif';
    ctx.fillText('Prev', 175, 320);

    ctx.fillStyle = '#E0E0E0';
    ctx.strokeStyle = '#666';
    ctx.fillRect(270, 300, 80, 30);
    ctx.strokeRect(270, 300, 80, 30);
    ctx.fillStyle = '#000';
    ctx.fillText('Next', 295, 320);
  }

  function applyStep(n) {
    stack.forEach(function(s) { s.target = null; });
    heap.invalid = false; heap.visible = false;
    nullptrPos.visible = false;
    showDoubleDelete = false;
    for (var i = 1; i <= n; i++) {
      if (i === 1) { stack[0].target = heap; heap.visible = true; }
      else if (i === 2) { stack[1].target = heap; }
      else if (i === 3) { stack[2].target = nullptrPos; nullptrPos.visible = true; }
      else if (i === 4) { stack[2].target = heap; }
      else if (i === 5) { heap.invalid = true; }
      else if (i === 6) { showDoubleDelete = true; }
    }
    drawStep();
  }

  canvas.addEventListener('click', function(e) {
    var rect = canvas.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    if (x >= 150 && x <= 230 && y >= 300 && y <= 330) {
      if (step > 0) { step--; applyStep(step); }
    } else if (x >= 270 && x <= 350 && y >= 300 && y <= 330) {
      if (step < 6) { step++; applyStep(step); }
    }
  });

  applyStep(0);
})();
</script>

---

<h2>Move Semantics — What and Why</h2>

<p>
<strong>Copying</strong> duplicates data. <strong>Moving</strong> transfers ownership — the source is left in a valid but empty state.
This is especially important for performance when returning objects from functions or inserting into containers.
</p>

<pre><code class="language-cpp">MaybeInt a(42);
MaybeInt b = std::move(a);  // Move constructor: b now owns the int, a.value_ == nullptr
</code></pre>

<div class="mermaid">
flowchart LR
  A["a::value_ points to heap(42)"] -->|"std::move(a)"| B["Move constructor called"]
  B --> C["b::value_ now owns heap(42)"]
  B --> D["a::value_ set to nullptr"]
</div>

<h3>Copy vs. Move Comparison</h3>

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th>Source after</th>
      <th>Memory allocated</th>
      <th>Performance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Copy constructor / assignment</td>
      <td>Unchanged (still owns data)</td>
      <td>New allocation (<code>new</code>)</td>
      <td>Slower (deep copy)</td>
    </tr>
    <tr>
      <td>Move constructor / assignment</td>
      <td>Emptied (<code>nullptr</code>)</td>
      <td>No allocation (pointer transfer)</td>
      <td>Fast (pointer swap)</td>
    </tr>
  </tbody>
</table>

---

<h2>Animation — Move Semantics</h2>

<div id="move-animation">
  <canvas id="moveCanvas" width="620" height="370" style="border:1px solid #ccc; border-radius:6px; display:block;"></canvas>
</div>

<script>
(function() {
  var canvas = document.getElementById('moveCanvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var step = 0;

  var stepLabels = [
    "Initial state",
    "MaybeInt a(42) — a::value_ points to heap(42)",
    "MaybeInt b = std::move(a) — move constructor called",
    "b::value_ takes ownership of heap(42)",
    "a::value_ set to nullptr (source emptied)",
    "Destructor for a — deletes nullptr (safe, no-op)",
    "Destructor for b — deletes heap(42) (only one delete!)"
  ];

  var aBox = {label: 'a::value_', x: 50,  y: 80};
  var bBox = {label: 'b::value_', x: 50,  y: 140};
  var heap = {label: '42',        x: 340, y: 110};
  var nullP = {label: 'nullptr',  x: 360, y: 220};

  // [aTarget, bTarget, heapVisible, nullVisible, note]
  var states = [
    [null,  null,  false, false, ''],
    [heap,  null,  true,  false, ''],
    [heap,  null,  true,  false, 'Moving...'],
    [heap,  heap,  true,  false, ''],
    [nullP, heap,  true,  true,  'a emptied'],
    [null,  heap,  true,  true,  'a destroyed (nullptr, safe)'],
    [null,  null,  false, false, 'b destroyed — heap freed correctly']
  ];

  function drawBox(x, y, w, h, fill, text) {
    ctx.fillStyle = fill;
    ctx.fillRect(x, y, w, h);
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.strokeRect(x, y, w, h);
    ctx.fillStyle = '#000';
    ctx.font = '13px monospace';
    ctx.fillText(text, x + 4, y + 15);
  }

  function drawArrow(fromX, fromY, toX, toY, color) {
    ctx.beginPath();
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(toX, toY);
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.stroke();
    var angle = Math.atan2(toY - fromY, toX - fromX);
    ctx.beginPath();
    ctx.moveTo(toX, toY);
    ctx.lineTo(toX - 10 * Math.cos(angle - 0.4), toY - 10 * Math.sin(angle - 0.4));
    ctx.lineTo(toX - 10 * Math.cos(angle + 0.4), toY - 10 * Math.sin(angle + 0.4));
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
  }

  function drawScene() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    var state = states[step];
    var aTarget    = state[0];
    var bTarget    = state[1];
    var heapVisible = state[2];
    var nullVisible = state[3];
    var note        = state[4];

    ctx.fillStyle = '#555';
    ctx.font = 'bold 13px sans-serif';
    ctx.fillText('Stack', 50, 55);
    ctx.fillText('Heap', 340, 55);

    ctx.fillStyle = '#000';
    ctx.font = '14px sans-serif';
    ctx.fillText('Step ' + step + ': ' + stepLabels[step], 10, 22);
    if (note) {
      ctx.fillStyle = '#0077b6';
      ctx.fillText('-> ' + note, 10, 40);
    }

    drawBox(aBox.x, aBox.y, 90, 22, '#87CEFA', aBox.label);
    drawBox(bBox.x, bBox.y, 90, 22, '#87CEFA', bBox.label);
    if (heapVisible) drawBox(heap.x, heap.y, 70, 22, '#90EE90', heap.label);
    if (nullVisible) drawBox(nullP.x, nullP.y, 70, 22, '#FFD700', nullP.label);

    if (aTarget === heap)  drawArrow(aBox.x + 90, aBox.y + 11, heap.x,  heap.y  + 11, '#333');
    if (aTarget === nullP) drawArrow(aBox.x + 90, aBox.y + 11, nullP.x, nullP.y + 11, 'red');
    if (bTarget === heap)  drawArrow(bBox.x + 90, bBox.y + 11, heap.x,  heap.y  + 11, '#00a86b');

    ctx.fillStyle = '#E0E0E0';
    ctx.strokeStyle = '#666';
    ctx.lineWidth = 1;
    ctx.fillRect(150, 330, 80, 30);
    ctx.strokeRect(150, 330, 80, 30);
    ctx.fillStyle = '#000';
    ctx.font = '14px sans-serif';
    ctx.fillText('Prev', 175, 350);

    ctx.fillStyle = '#E0E0E0';
    ctx.strokeStyle = '#666';
    ctx.fillRect(270, 330, 80, 30);
    ctx.strokeRect(270, 330, 80, 30);
    ctx.fillStyle = '#000';
    ctx.fillText('Next', 295, 350);
  }

  canvas.addEventListener('click', function(e) {
    var rect = canvas.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    if (x >= 150 && x <= 230 && y >= 330 && y <= 360) {
      if (step > 0) { step--; drawScene(); }
    } else if (x >= 270 && x <= 350 && y >= 330 && y <= 360) {
      if (step < states.length - 1) { step++; drawScene(); }
    }
  });

  drawScene();
})();
</script>

---

<h2>Interactive Python Tutor — All Five Functions</h2>

<p>Click the link below to step through all five special member functions in Python Tutor:</p>

<p>👉 Open in Python Tutor (all 5 functions)</a></p>
<a href="
https://pythontutor.com/visualize.html#code=%23include%20%3Cutility%3E%0A%0Aclass%20MaybeInt%20%7B%0A%20public%3A%0A%20%20MaybeInt%28%29%20%3A%20value_%28nullptr%29%20%7B%7D%0A%20%20MaybeInt%28int%20v%29%20%3A%20value_%28new%20int%28v%29%29%20%7B%7D%0A%0A%20%20~MaybeInt%28%29%20%7B%20delete%20value_%3B%20%7D%0A%0A%20%20MaybeInt%28const%20MaybeInt%26%20o%29%20%7B%0A%20%20%20%20value_%20%3D%20o.value_%20%3F%20new%20int%28*o.value_%29%20%3A%20nullptr%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%26%20operator%3D%28const%20MaybeInt%26%20o%29%20%7B%0A%20%20%20%20if%20%28this%20!%3D%20%26o%29%20%7B%0A%20%20%20%20%20%20delete%20value_%3B%0A%20%20%20%20%20%20value_%20%3D%20o.value_%20%3F%20new%20int%28*o.value_%29%20%3A%20nullptr%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%20*this%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%28MaybeInt%26%26%20o%29%20noexcept%20%3A%20value_%28o.value_%29%20%7B%0A%20%20%20%20o.value_%20%3D%20nullptr%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%26%20operator%3D%28MaybeInt%26%26%20o%29%20noexcept%20%7B%0A%20%20%20%20if%20%28this%20!%3D%20%26o%29%20%7B%0A%20%20%20%20%20%20delete%20value_%3B%0A%20%20%20%20%20%20value_%20%3D%20o.value_%3B%0A%20%20%20%20%20%20o.value_%20%3D%20nullptr%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%20*this%3B%0A%20%20%7D%0A%0A%20private%3A%0A%20%20int*%20value_%3B%0A%7D%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20MaybeInt%20a%287%29%3B%0A%20%20MaybeInt%20b%28a%29%3B%0A%20%20MaybeInt%20c%3B%0A%20%20c%20%3D%20a%3B%0A%20%20MaybeInt%20d%28std%3A%3Amove%28a%29%29%3B%0A%20%20MaybeInt%20e%3B%0A%20%20e%20%3D%20std%3A%3Amove%28b%29%3B%0A%20%20return%200%3B%0A%7D&curInstr=6&mode=display&origin=opt-frontend.js&py=cpp_g%2B%2B9.3.0"> Open in Python Tutor  </a>

<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=%23include%20%3Cutility%3E%0A%0Aclass%20MaybeInt%20%7B%0A%20public%3A%0A%20%20MaybeInt%28%29%20%3A%20value_%28nullptr%29%20%7B%7D%0A%20%20MaybeInt%28int%20v%29%20%3A%20value_%28new%20int%28v%29%29%20%7B%7D%0A%0A%20%20~MaybeInt%28%29%20%7B%20delete%20value_%3B%20%7D%0A%0A%20%20MaybeInt%28const%20MaybeInt%26%20o%29%20%7B%0A%20%20%20%20value_%20%3D%20o.value_%20%3F%20new%20int%28*o.value_%29%20%3A%20nullptr%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%26%20operator%3D%28const%20MaybeInt%26%20o%29%20%7B%0A%20%20%20%20if%20%28this%20!%3D%20%26o%29%20%7B%0A%20%20%20%20%20%20delete%20value_%3B%0A%20%20%20%20%20%20value_%20%3D%20o.value_%20%3F%20new%20int%28*o.value_%29%20%3A%20nullptr%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%20*this%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%28MaybeInt%26%26%20o%29%20noexcept%20%3A%20value_%28o.value_%29%20%7B%0A%20%20%20%20o.value_%20%3D%20nullptr%3B%0A%20%20%7D%0A%0A%20%20MaybeInt%26%20operator%3D%28MaybeInt%26%26%20o%29%20noexcept%20%7B%0A%20%20%20%20if%20%28this%20!%3D%20%26o%29%20%7B%0A%20%20%20%20%20%20delete%20value_%3B%0A%20%20%20%20%20%20value_%20%3D%20o.value_%3B%0A%20%20%20%20%20%20o.value_%20%3D%20nullptr%3B%0A%20%20%20%20%7D%0A%20%20%20%20return%20*this%3B%0A%20%20%7D%0A%0A%20private%3A%0A%20%20int*%20value_%3B%0A%7D%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20MaybeInt%20a%287%29%3B%0A%20%20MaybeInt%20b%28a%29%3B%0A%20%20MaybeInt%20c%3B%0A%20%20c%20%3D%20a%3B%0A%20%20MaybeInt%20d%28std%3A%3Amove%28a%29%29%3B%0A%20%20MaybeInt%20e%3B%0A%20%20e%20%3D%20std%3A%3Amove%28b%29%3B%0A%20%20return%200%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&curInstr=6&origin=opt-frontend.js&py=cpp_g%2B%2B9.3.0"> </iframe>
---

<h2>Summary Table — The Five Special Member Functions</h2>

<table>
  <thead>
    <tr>
      <th>Function</th>
      <th>Syntax</th>
      <th>Purpose</th>
      <th>Must Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Destructor</strong></td>
      <td><code>~T()</code></td>
      <td>Destroys object, frees resources</td>
      <td><code>delete</code></td>
    </tr>
    <tr>
      <td><strong>Copy constructor</strong></td>
      <td><code>T(const T&amp;)</code></td>
      <td>Creates a deep copy</td>
      <td><code>new</code></td>
    </tr>
    <tr>
      <td><strong>Copy assignment</strong></td>
      <td><code>T&amp; operator=(const T&amp;)</code></td>
      <td>Replaces content with deep copy</td>
      <td><code>delete</code> + <code>new</code></td>
    </tr>
    <tr>
      <td><strong>Move constructor</strong> <em>(C++11)</em></td>
      <td><code>T(T&amp;&amp;) noexcept</code></td>
      <td>Transfers ownership from rvalue</td>
      <td>Steal pointer, null source</td>
    </tr>
    <tr>
      <td><strong>Move assignment</strong> <em>(C++11)</em></td>
      <td><code>T&amp; operator=(T&amp;&amp;) noexcept</code></td>
      <td>Replaces content by ownership transfer</td>
      <td><code>delete</code> old, steal, null source</td>
    </tr>
  </tbody>
</table>

<blockquote>
[!TIP]
<strong>Rule of Zero:</strong> If you use smart pointers (<code>std::unique_ptr</code>, <code>std::shared_ptr</code>) or standard containers, you can often avoid writing any of these five functions yourself — the compiler-generated defaults will do the right thing.
</blockquote>

<h3>Rule of Zero — Prefer Smart Pointers</h3>

<pre><code class="language-cpp">#include &lt;memory&gt;

class MaybeInt {
 public:
  MaybeInt() = default;
  explicit MaybeInt(int v) : value_(std::make_unique&lt;int&gt;(v)) {}

  // No destructor, no copy/move — compiler-generated defaults are correct!

 private:
  std::unique_ptr&lt;int&gt; value_;
};
</code></pre>

<blockquote>
[!NOTE]
In modern C++, if you define <strong>any</strong> of the five special member functions, define <strong>all five</strong> — or use smart pointers (Rule of Zero) and define <strong>none</strong>.
</blockquote>
