# PDF Combiner

A simple local PDF combiner because PDF combining websites are awful. Make with Claude Code.

## Requirements

- Python 3.7+
- [pypdf](https://pypi.org/project/pypdf/)

## Installation

```bash
pip install pypdf
```

## Usage

```bash
python pdfCombine.py <file1.pdf> <file2.pdf> [output.pdf]
```

- `file1.pdf` — first PDF (required)
- `file2.pdf` — second PDF, appended after the first (required)
- `output.pdf` — name of the combined file (optional, defaults to `combined.pdf`)

## Examples

```bash
# Output saved as combined.pdf
python pdfCombine.py resume.pdf cover_letter.pdf

# Output saved as application.pdf
python pdfCombine.py resume.pdf cover_letter.pdf application.pdf
```
