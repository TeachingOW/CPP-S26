#!/usr/bin/env python3
import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}

SLIDE_PATH_RE = re.compile(r"ppt/slides/slide(\d+)\.xml$")


def slide_sort_key(name: str) -> int:
    m = SLIDE_PATH_RE.search(name)
    return int(m.group(1)) if m else 10**9


def shape_text(shape: ET.Element) -> str:
    parts = []
    for paragraph in shape.findall(".//a:p", NS):
        runs = []
        for text_node in paragraph.findall(".//a:t", NS):
            if text_node.text:
                runs.append(text_node.text)
        line = " ".join(runs).strip()
        if line:
            parts.append(line)
    return "\n".join(parts).strip()


def placeholder_type(shape: ET.Element) -> str | None:
    ph = shape.find("./p:nvSpPr/p:nvPr/p:ph", NS)
    if ph is None:
        return None
    return ph.attrib.get("type", "body")


def parse_pptx(pptx_path: Path) -> dict:
    slides = []
    with zipfile.ZipFile(pptx_path) as zf:
        slide_names = sorted(
            [name for name in zf.namelist() if SLIDE_PATH_RE.match(name)],
            key=slide_sort_key,
        )

        for index, slide_name in enumerate(slide_names, start=1):
            root = ET.fromstring(zf.read(slide_name))
            text_blocks = []
            title = None

            for shape in root.findall(".//p:sp", NS):
                text = shape_text(shape)
                if not text:
                    continue

                ph_type = placeholder_type(shape)
                if ph_type in {"title", "ctrTitle"} and not title:
                    title = text

                text_blocks.append(
                    {
                        "placeholder_type": ph_type,
                        "text": text,
                    }
                )

            if not title and text_blocks:
                title = text_blocks[0]["text"].splitlines()[0].strip()

            slides.append(
                {
                    "slide_number": index,
                    "title": title,
                    "text_blocks": text_blocks,
                    "full_text": "\n\n".join(block["text"] for block in text_blocks),
                }
            )

    return {
        "source_file": str(pptx_path),
        "deck_name": pptx_path.stem,
        "slide_count": len(slides),
        "slides": slides,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PPTX files to JSON documents.")
    parser.add_argument("inputs", nargs="+", help="PPTX files or directories containing PPTX files")
    parser.add_argument(
        "-o",
        "--output-dir",
        default="slides/json",
        help="Directory to write JSON files (default: slides/json)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    pptx_files: list[Path] = []
    for item in args.inputs:
        path = Path(item)
        if path.is_dir():
            pptx_files.extend(sorted(path.glob("*.pptx")))
        elif path.suffix.lower() == ".pptx" and path.exists():
            pptx_files.append(path)

    seen = set()
    for pptx_file in pptx_files:
        if pptx_file in seen:
            continue
        seen.add(pptx_file)
        doc = parse_pptx(pptx_file)
        out_path = output_dir / f"{pptx_file.stem}.json"
        out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=True), encoding="utf-8")
        print(f"Wrote {out_path} ({doc['slide_count']} slides)")


if __name__ == "__main__":
    main()
