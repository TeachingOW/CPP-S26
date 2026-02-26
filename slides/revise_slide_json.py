#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def normalize_whitespace(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    cleaned = []
    prev_blank = False
    for line in lines:
        blank = line == ""
        if blank and prev_blank:
            continue
        cleaned.append(line)
        prev_blank = blank
    return "\n".join(cleaned).strip()


def revise_deck_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    deck_name = data.get("deck_name", path.stem)
    source_file = data.get("source_file")
    slides = data.get("slides", [])

    documents = []
    for slide in slides:
        slide_number = slide.get("slide_number")
        title = (slide.get("title") or "").strip() or f"Slide {slide_number}"
        full_text = normalize_whitespace(slide.get("full_text") or "")
        paragraphs = []
        for block in slide.get("text_blocks", []):
            text = normalize_whitespace(block.get("text") or "")
            if text:
                paragraphs.append(text)

        documents.append(
            {
                "doc_id": f"{deck_name}-slide-{slide_number}",
                "deck_name": deck_name,
                "slide_number": slide_number,
                "title": title,
                "paragraphs": paragraphs,
                "content": full_text,
            }
        )

    return {
        "source_json": str(path),
        "source_pptx": source_file,
        "deck_name": deck_name,
        "document_type": "slide_documents",
        "document_count": len(documents),
        "documents": documents,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Revise deck JSON files into slide-document JSON files.")
    parser.add_argument("inputs", nargs="+", help="JSON files or directories")
    parser.add_argument("-o", "--output-dir", default="slides/json_revised", help="Output directory")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    json_files: list[Path] = []
    for item in args.inputs:
        p = Path(item)
        if p.is_dir():
            json_files.extend(sorted(p.glob("*.json")))
        elif p.is_file() and p.suffix.lower() == ".json":
            json_files.append(p)

    seen = set()
    for jf in json_files:
        if jf in seen:
            continue
        seen.add(jf)
        revised = revise_deck_json(jf)
        out_path = output_dir / f"{jf.stem}.slide-docs.json"
        out_path.write_text(json.dumps(revised, indent=2, ensure_ascii=True), encoding="utf-8")
        print(f"Wrote {out_path} ({revised['document_count']} documents)")


if __name__ == "__main__":
    main()
