#!/usr/bin/env python3
import argparse
import html
import json
import re
from pathlib import Path


CPP_KEYWORDS = {
    "class",
    "struct",
    "public",
    "private",
    "protected",
    "virtual",
    "override",
    "const",
    "return",
    "if",
    "else",
    "for",
    "while",
    "switch",
    "case",
    "break",
    "continue",
    "try",
    "catch",
    "throw",
    "new",
    "delete",
    "using",
    "namespace",
    "include",
    "int",
    "double",
    "float",
    "char",
    "bool",
    "void",
    "std",
    "template",
    "typename",
    "auto",
    "static",
}


def is_code_like(text: str) -> bool:
    if not text:
        return False
    lines = [ln for ln in text.splitlines() if ln.strip()]
    if not lines:
        return False
    score = 0
    markers = ["#include", "int main(", "std::", "{", "}", ";", "cout", "cin", "::"]
    for m in markers:
        if m in text:
            score += 1
    codey_lines = 0
    for ln in lines:
        s = ln.strip()
        if s.endswith(";") or s.endswith("{") or s.endswith("}") or re.match(r"^(if|for|while|class|struct)\b", s):
            codey_lines += 1
    if codey_lines >= max(2, len(lines) // 3):
        score += 2
    return score >= 3


def split_document(doc: dict) -> list[dict]:
    paragraphs = [p for p in (doc.get("paragraphs") or []) if str(p).strip()]
    if not paragraphs and doc.get("content"):
        paragraphs = [doc["content"]]

    chunks: list[list[str]] = []
    current: list[str] = []
    current_chars = 0
    current_code = False
    current_code_blocks = 0

    def flush() -> None:
        nonlocal current, current_chars, current_code, current_code_blocks
        if current:
            chunks.append(current)
        current = []
        current_chars = 0
        current_code = False
        current_code_blocks = 0

    for para in paragraphs:
        para = str(para).strip()
        para_is_code = is_code_like(para)
        para_chars = len(para)

        max_chars = 760 if para_is_code else 900
        max_blocks = 4 if para_is_code else 8

        # Split very long single blocks by lines so one HTML slide does not overflow.
        if para_chars > max_chars * 1.25:
            flush()
            lines = para.splitlines() or [para]
            line_buf: list[str] = []
            line_chars = 0
            line_limit = 18 if para_is_code else 28
            char_limit = max_chars
            for line in lines:
                extra = len(line) + 1
                if line_buf and (len(line_buf) >= line_limit or line_chars + extra > char_limit):
                    chunks.append(["\n".join(line_buf)])
                    line_buf = []
                    line_chars = 0
                line_buf.append(line)
                line_chars += extra
            if line_buf:
                chunks.append(["\n".join(line_buf)])
            continue

        should_flush = False
        if current:
            if len(current) >= max_blocks:
                should_flush = True
            if current_chars + para_chars > max_chars:
                should_flush = True
            if current_code != para_is_code:
                # Allow a short text preamble to stay with one code block.
                if not (not para_is_code and current_code_blocks == 1 and current_chars < 820):
                    if not (para_is_code and len(current) <= 2 and current_chars < 220 and current_chars + para_chars < 880):
                        if current_chars > 250 or para_chars > 250:
                            should_flush = True
        if should_flush:
            flush()

        current.append(para)
        current_chars += para_chars
        if para_is_code:
            current_code_blocks += 1
        current_code = para_is_code if len(current) == 1 else current_code and para_is_code

    flush()

    if not chunks:
        chunks = [[]]

    parts = []
    for i, chunk in enumerate(chunks, start=1):
        part_doc = dict(doc)
        part_doc["paragraphs"] = chunk
        part_doc["content"] = "\n\n".join(chunk)
        part_doc["_part"] = i
        part_doc["_part_total"] = len(chunks)
        parts.append(part_doc)
    return parts


def highlight_cpp(code: str) -> str:
    token_re = re.compile(
        r'//.*?$|"(?:\\.|[^"\\])*"|\b\d+(?:\.\d+)?\b|\b[A-Za-z_][A-Za-z0-9_]*\b',
        re.MULTILINE,
    )
    pieces = []
    last = 0
    for m in token_re.finditer(code):
        if m.start() > last:
            pieces.append(html.escape(code[last:m.start()]))
        tok = m.group(0)
        if tok.startswith("//"):
            pieces.append(f'<span class="cm">{html.escape(tok)}</span>')
        elif tok.startswith('"'):
            pieces.append(f'<span class="str">{html.escape(tok)}</span>')
        elif re.fullmatch(r"\d+(?:\.\d+)?", tok):
            pieces.append(f'<span class="num">{tok}</span>')
        elif tok in CPP_KEYWORDS:
            pieces.append(f'<span class="kw">{tok}</span>')
        else:
            pieces.append(html.escape(tok))
        last = m.end()
    if last < len(code):
        pieces.append(html.escape(code[last:]))
    return "".join(pieces)


def classify_blocks(paragraphs: list[str]) -> list[tuple[str, str]]:
    blocks = []
    for p in paragraphs:
        text = str(p)
        if is_code_like(text):
            blocks.append(("code", text))
            continue
        if "\n" in text:
            lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
            bulletish = sum(1 for ln in lines if re.match(r"^([-*]|\d+[.)])\s+", ln))
            if lines and bulletish >= max(2, len(lines) // 2):
                blocks.append(("list", "\n".join(lines)))
                continue
            # Many slide paragraphs are extracted as newline-separated statements without bullets.
            if len(lines) >= 4 and all(len(ln) <= 140 for ln in lines) and not any(is_code_like(ln) for ln in lines):
                blocks.append(("list_plain", "\n".join(lines)))
                continue
        blocks.append(("text", text))
    return blocks


def render_slide(doc: dict, index: int, total: int) -> str:
    deck = html.escape(str(doc.get("deck_name", "")))
    slide_number_raw = str(doc.get("slide_number", ""))
    slide_number = html.escape(slide_number_raw)
    title_text = str(doc.get("title", "") or f"Slide {slide_number_raw}")
    part = doc.get("_part", 1)
    part_total = doc.get("_part_total", 1)
    title = html.escape(title_text + (f" (Part {part}/{part_total})" if part_total > 1 else ""))
    paragraphs = [str(p) for p in (doc.get("paragraphs") or [])]
    blocks = classify_blocks(paragraphs)

    content_blocks = []
    code_only = bool(blocks) and all(kind == "code" for kind, _ in blocks)
    short_slide = sum(len(b[1]) for b in blocks) < 120 and len(blocks) <= 2
    for kind, raw in blocks:
        if kind == "code":
            content_blocks.append(f'<pre class="code"><code>{highlight_cpp(raw)}</code></pre>')
        elif kind in {"list", "list_plain"}:
            items = []
            for line in raw.splitlines():
                if kind == "list":
                    line = re.sub(r"^([-*]|\d+[.)])\s+", "", line)
                items.append(f"<li>{html.escape(line)}</li>")
            content_blocks.append("<ul>" + "".join(items) + "</ul>")
        else:
            text = html.escape(raw).replace("\n", "<br>")
            content_blocks.append(f"<p>{text}</p>")

    classes = ["slide"]
    if code_only:
        classes.append("slide-code")
    if short_slide:
        classes.append("slide-short")

    return f"""
    <section class="{' '.join(classes)}" data-index="{index}">
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
    expanded_docs = []
    for doc in docs:
        expanded_docs.extend(split_document(doc))
    slides_html = "\n".join(render_slide(doc, i, len(expanded_docs)) for i, doc in enumerate(expanded_docs))
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
      --code-bg: #151922;
      --code-ink: #eef4ff;
      --code-muted: #9cb2d6;
      --kw: #80d4ff;
      --num: #ffd580;
      --str: #9ff0a8;
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
      min-height: min(76vh, 820px);
      padding: 28px 32px;
      border-radius: 18px;
      background: var(--card);
      border: 1px solid var(--border);
      box-shadow: 0 10px 35px rgba(0,0,0,0.08);
    }}
    .slide.slide-short .slide-content {{
      font-size: clamp(1.25rem, 2vw, 1.8rem);
      display: grid;
      align-content: center;
      min-height: 52vh;
    }}
    .slide.slide-short .slide-content p {{
      margin-bottom: 18px;
    }}
    .slide.slide-code {{
      background:
        linear-gradient(180deg, #fffdf8 0 30%, #fbf8f1 100%);
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
      line-height: 1.45;
      max-height: 66vh;
      overflow: auto;
      padding-right: 6px;
      display: grid;
      gap: 10px;
      align-content: start;
    }}
    .slide-content p {{
      margin: 0;
      white-space: normal;
      overflow-wrap: anywhere;
    }}
    .slide-content ul {{
      margin: 0;
      padding-left: 1.2rem;
      display: grid;
      gap: 8px;
    }}
    .slide-content li {{
      line-height: 1.35;
    }}
    pre.code {{
      margin: 0;
      padding: 14px 16px;
      border-radius: 12px;
      background: var(--code-bg);
      color: var(--code-ink);
      border: 1px solid #263147;
      box-shadow: inset 0 1px 0 rgba(255,255,255,0.04);
      overflow: auto;
    }}
    pre.code code {{
      font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
      font-size: clamp(0.9rem, 1.1vw, 1rem);
      line-height: 1.45;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    .kw {{ color: var(--kw); font-weight: 600; }}
    .num {{ color: var(--num); }}
    .str {{ color: var(--str); }}
    .cm {{ color: var(--code-muted); font-style: italic; }}
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
        <input id="jumpInput" type="number" min="1" max="{len(expanded_docs)}" value="1">
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
    expanded_count = sum(len(split_document(doc)) for doc in data.get("documents", []))
    print(f"Wrote {output_path} ({expanded_count} html slides from {len(data.get('documents', []))} source slides)")


if __name__ == "__main__":
    main()
