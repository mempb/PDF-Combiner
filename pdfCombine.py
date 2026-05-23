import sys
from pathlib import Path

try:
    from pypdf import PdfWriter, PdfReader
except ImportError:
    sys.exit("pypdf not installed. Run: pip install pypdf")


def combine_pdfs(path1: str, path2: str, output: str) -> None:
    writer = PdfWriter()
    for path in (path1, path2):
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Saved: {output}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combine_pdfs.py file1.pdf file2.pdf [output.pdf]")
        sys.exit(1)

    pdf1, pdf2 = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else "combined.pdf"

    for p in (pdf1, pdf2):
        if not Path(p).exists():
            sys.exit(f"File not found: {p}")

    combine_pdfs(pdf1, pdf2, out)
