#!/usr/bin/env python3
import argparse
from pathlib import Path

from pptx_to_json import parse_pptx
from json_to_html_slides import build_html


def normalize_whitespace(text: str) -> str:
    lines = [line.strip() for line in (text or "").splitlines()]
    out = []
    prev_blank = False
    for line in lines:
        blank = line == ""
        if blank and prev_blank:
            continue
        out.append(line)
        prev_blank = blank
    return "\n".join(out).strip()


def slide_to_doc(deck_name: str, slide: dict) -> dict:
    slide_number = slide.get("slide_number")
    title = (slide.get("title") or "").strip() or f"Slide {slide_number}"
    paragraphs = []
    for block in slide.get("text_blocks", []):
        t = normalize_whitespace(block.get("text") or "")
        if t:
            paragraphs.append(t)
    content = normalize_whitespace(slide.get("full_text") or "")
    if not paragraphs and content:
        paragraphs = [content]
    return {
        "deck_name": deck_name,
        "slide_number": slide_number,
        "title": title,
        "paragraphs": paragraphs,
        "content": content,
    }


def is_short_doc(doc: dict) -> bool:
    content = doc.get("content", "")
    paras = doc.get("paragraphs", [])
    return len(content) < 180 and len(paras) <= 3


def should_combine(prev_doc: dict, next_doc: dict) -> bool:
    if prev_doc.get("deck_name") != next_doc.get("deck_name"):
        return False
    if not (is_short_doc(prev_doc) and is_short_doc(next_doc)):
        return False

    prev_title = (prev_doc.get("title") or "").strip().lower()
    next_title = (next_doc.get("title") or "").strip().lower()
    if prev_title == next_title:
        return True
    if "cont" in next_title or "continued" in next_title:
        return True
    if next_title.isdigit() or next_title == f"slide {next_doc.get('slide_number')}".lower():
        return True
    return False


def combine_docs(docs: list[dict]) -> list[dict]:
    combined = []
    i = 0
    while i < len(docs):
        cur = dict(docs[i])
        if i + 1 < len(docs) and should_combine(cur, docs[i + 1]):
            nxt = docs[i + 1]
            merged_paragraphs = list(cur.get("paragraphs", [])) + list(nxt.get("paragraphs", []))
            cur["paragraphs"] = merged_paragraphs
            cur["content"] = normalize_whitespace("\n\n".join(merged_paragraphs))
            cur["title"] = cur.get("title") or nxt.get("title")
            cur["slide_number"] = f"{cur.get('slide_number')}+{nxt.get('slide_number')}"
            i += 2
        else:
            i += 1
        combined.append(cur)
    return combined


def build_documents_from_pptx(inputs: list[Path]) -> dict:
    docs = []
    for pptx_path in inputs:
        deck = parse_pptx(pptx_path)
        deck_name = deck.get("deck_name", pptx_path.stem)
        for slide in deck.get("slides", []):
            docs.append(slide_to_doc(deck_name, slide))
    docs = combine_docs(docs)
    return {
        "document_type": "slide_documents",
        "deck_count": len({d["deck_name"] for d in docs}),
        "document_count": len(docs),
        "documents": docs,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PPTX files directly to revised HTML slides.")
    parser.add_argument("inputs", nargs="+", help="PPTX files or directories")
    parser.add_argument("-o", "--output", default="slides/html/all-slides.html")
    args = parser.parse_args()

    pptx_files: list[Path] = []
    for item in args.inputs:
        p = Path(item)
        if p.is_dir():
            pptx_files.extend(sorted(p.glob("*.pptx")))
        elif p.is_file() and p.suffix.lower() == ".pptx":
            pptx_files.append(p)

    seen = set()
    ordered = []
    for p in pptx_files:
        if p in seen:
            continue
        seen.add(p)
        ordered.append(p)

    data = build_documents_from_pptx(ordered)
    html_text = build_html(data, " + ".join(p.name for p in ordered))

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html_text, encoding="utf-8")
    print(f"Wrote {out_path} ({data['document_count']} revised source slides before html splitting)")


if __name__ == "__main__":
    main()
