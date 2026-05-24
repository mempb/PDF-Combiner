import sys
from pathlib import Path
from pypdf import PdfWriter, PdfReader

# Merges all input PDFs in order into a single output file
def combine_pdfs(inputs: list[str], output: str) -> None:
    writer = PdfWriter()
    for path in inputs:
        # Read each input PDF and append its pages to the writer
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    # Write the combined result to the output file
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Saved: {output}")

if __name__ == "__main__":
    # Display usage if help command passed, or incorrect usage
    if (len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help")) or len(sys.argv) < 4:
        print("Usage: python combine.py file1.pdf file2.pdf [file3.pdf ...] output.pdf")
        sys.exit(0)

    # Last argument is the output file, everything before is input files
    *inputs, combined = sys.argv[1:]

    # Check for valid files
    for p in inputs:
        if not Path(p).exists():
            sys.exit(f"File not found: {p}")

    combine_pdfs(inputs, combined)
