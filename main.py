from pathlib import Path

TEXT = "I came for leftovers, stayed for the quiet. The cheese understands me."


def main():
    try:
        output = Path("/output")
        output.mkdir(parents=True, exist_ok=True)
    except OSError:
        output = Path("output")
        output.mkdir(parents=True, exist_ok=True)
    try:
        (output / "entry.txt").write_text(TEXT, encoding="utf-8")
    except OSError:
        output = Path("output")
        output.mkdir(parents=True, exist_ok=True)
        (output / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
