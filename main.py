from pathlib import Path

TEXT = "Opened the fridge for a snack; now we're both waiting for the leftovers to make the first move."


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
