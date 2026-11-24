"""The Long Roast: one satirical sentence about lawmakers and the file
they cannot convert. Writes it to /output/entry.txt."""

from pathlib import Path

LINE = "The senator who chairs the committee on artificial intelligence just emailed his staff a file called FINAL_final_v7 and asked them to turn it into a PDF, then went back to writing the law that will govern the machines that do it in a single click."


def main() -> None:
    # Gate: the entry must be 1-320 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 320 or not LINE.strip():
        raise ValueError("entry line must be 1-320 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
