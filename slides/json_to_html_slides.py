#!/usr/bin/env python3
import argparse
import html
import json
from pathlib import Path


def render_slide(doc: dict, index: int, total: int) -> str:
    deck = html.escape(str(doc.get("deck_name", "")))
    slide_number = html.escape(str(doc.get("slide_number", "")))
    title = html.escape(str(doc.get("title", "") or f"Slide {slide_number}"))
    paragraphs = doc.get("paragraphs") or []
    content_blocks = []
    for p in paragraphs:
        text = html.escape(str(p))
        # preserve line breaks within extracted text blocks
        text = text.replace("\n", "<br>")
        content_blocks.append(f"<p>{text}</p>")
    if not content_blocks:
        text = html.escape(str(doc.get("content", ""))).replace("\n", "<br>")
        content_blocks.append(f"<p>{text}</p>")

    return f"""
    <section class="slide" data-index="{index}">
      <header class="slide-meta">
        <span class="deck">{deck}</span>
        <span class="num">Slide {slide_number}</span>
        <span class="count">{index + 1} / {total}</span>
      </header>
      <h1>{title}</h1>
      <div class="slide-content">
        {''.join(content_blocks)}
      </div>
    </section>
    """


def build_html(data: dict, source_name: str) -> str:
    docs = data.get("documents", [])
    slides_html = "\n".join(render_slide(doc, i, len(docs)) for i, doc in enumerate(docs))
    title = html.escape(f"Slides from {source_name}")
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #f6f2e9;
      --ink: #1f1a17;
      --muted: #6e635a;
      --accent: #0b6bcb;
      --card: #fffdf8;
      --border: #d8ccbf;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Georgia, "Times New Roman", serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 15% 15%, #fff7cf 0%, transparent 45%),
        radial-gradient(circle at 90% 10%, #dceeff 0%, transparent 38%),
        linear-gradient(180deg, #f8f4ec, #efe8db);
    }}
    .app {{
      min-height: 100vh;
      display: grid;
      grid-template-rows: auto 1fr auto;
      gap: 12px;
      padding: 14px;
    }}
    .topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 10px 12px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: rgba(255,255,255,0.72);
      backdrop-filter: blur(4px);
    }}
    .controls {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    button, input[type="number"] {{
      font: inherit;
      padding: 8px 10px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: white;
      color: var(--ink);
    }}
    button {{
      cursor: pointer;
    }}
    button:hover {{
      border-color: var(--accent);
    }}
    .viewport {{
      display: grid;
      place-items: center;
      min-height: 0;
    }}
    .slide {{
      display: none;
      width: min(1100px, 100%);
      min-height: min(72vh, 760px);
      padding: 28px 32px;
      border-radius: 18px;
      background: var(--card);
      border: 1px solid var(--border);
      box-shadow: 0 10px 35px rgba(0,0,0,0.08);
    }}
    .slide.active {{ display: block; }}
    .slide-meta {{
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      color: var(--muted);
      font-size: 0.95rem;
      margin-bottom: 10px;
    }}
    .slide-meta .deck {{
      color: var(--accent);
      font-weight: 600;
    }}
    h1 {{
      margin: 0 0 18px 0;
      font-size: clamp(1.4rem, 2.3vw, 2.2rem);
      line-height: 1.2;
    }}
    .slide-content {{
      font-size: clamp(1rem, 1.35vw, 1.2rem);
      line-height: 1.5;
      max-height: 60vh;
      overflow: auto;
      padding-right: 6px;
    }}
    .slide-content p {{
      margin: 0 0 12px 0;
      white-space: normal;
      overflow-wrap: anywhere;
    }}
    .footer {{
      color: var(--muted);
      font-size: 0.9rem;
      text-align: center;
    }}
    @media (max-width: 700px) {{
      .slide {{
        padding: 18px;
        min-height: 70vh;
      }}
      .topbar {{
        align-items: flex-start;
        flex-direction: column;
      }}
    }}
    @media (prefers-reduced-motion: no-preference) {{
      .slide.active {{
        animation: fadein .18s ease-out;
      }}
      @keyframes fadein {{
        from {{ opacity: 0; transform: translateY(4px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
    }}
  </style>
</head>
<body>
  <div class="app">
    <div class="topbar">
      <div><strong>{title}</strong></div>
      <div class="controls">
        <button id="prevBtn" type="button">Prev</button>
        <button id="nextBtn" type="button">Next</button>
        <label for="jumpInput">Go to:</label>
        <input id="jumpInput" type="number" min="1" max="{len(docs)}" value="1">
        <button id="jumpBtn" type="button">Jump</button>
      </div>
    </div>
    <main class="viewport" id="viewport">
      {slides_html}
    </main>
    <div class="footer">Keyboard: Left/Right arrows, Home, End</div>
  </div>
  <script>
    const slides = Array.from(document.querySelectorAll('.slide'));
    let current = 0;

    function show(index) {{
      if (!slides.length) return;
      current = Math.max(0, Math.min(index, slides.length - 1));
      slides.forEach((s, i) => s.classList.toggle('active', i === current));
      const jumpInput = document.getElementById('jumpInput');
      if (jumpInput) jumpInput.value = String(current + 1);
      window.location.hash = `slide-${{current + 1}}`;
    }}

    document.getElementById('prevBtn').addEventListener('click', () => show(current - 1));
    document.getElementById('nextBtn').addEventListener('click', () => show(current + 1));
    document.getElementById('jumpBtn').addEventListener('click', () => {{
      const n = Number(document.getElementById('jumpInput').value);
      if (!Number.isFinite(n)) return;
      show(n - 1);
    }});
    document.getElementById('jumpInput').addEventListener('keydown', (e) => {{
      if (e.key === 'Enter') document.getElementById('jumpBtn').click();
    }});

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === 'PageDown') show(current + 1);
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') show(current - 1);
      if (e.key === 'Home') show(0);
      if (e.key === 'End') show(slides.length - 1);
    }});

    const hash = window.location.hash.match(/slide-(\\d+)/);
    const startIndex = hash ? Number(hash[1]) - 1 : 0;
    show(startIndex);
  </script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert slide-document JSON to HTML slides.")
    parser.add_argument("input_json")
    parser.add_argument("-o", "--output", default="slides/html/all-slides.html")
    args = parser.parse_args()

    input_path = Path(args.input_json)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = json.loads(input_path.read_text(encoding="utf-8"))
    html_text = build_html(data, input_path.name)
    output_path.write_text(html_text, encoding="utf-8")
    print(f"Wrote {output_path} ({len(data.get('documents', []))} slides)")


if __name__ == "__main__":
    main()
