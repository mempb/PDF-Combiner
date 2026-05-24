# PDF Combiner

A simple command-line tool to merge multiple PDFs into one, because PDF combining websites are awful.

## Requirements

- Python 3.10+
- [pypdf](https://pypi.org/project/pypdf/)

## Installation

```bash
pip install pypdf
```

## Usage

```bash
python combine.py <file1.pdf> <file2.pdf> [file3.pdf ...] <output.pdf>
```

- `file1.pdf` — first PDF (required)
- `file2.pdf` — second PDF, appended after the first (required)
- `file3.pdf ...` — any number of additional PDFs (optional)
- `output.pdf` — name of the combined file (required)

## Examples

```bash
# Combine two PDFs
python combine.py pdf1.pdf pdf2.pdf mypdf.pdf

# Combine three or more PDFs
python combine.py pdf1.pdf pdf2.pdf pdf3.pdf mypdf.pdf
```

## Help

```bash
python combine.py --help
```
