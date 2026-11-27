"""Text Statistics Analyzer: reports basic statistics about a text file."""
import sys


def count_stats(text):
    """Return line, word and character counts for the given text."""
    return {
        "lines": len(text.splitlines()),
        "words": len(text.split()),
        "characters": len(text),
    }


def format_report(stats):
    """Turn the statistics into a one-line report."""
    return f"Lines: {stats['lines']} | Words: {stats['words']}"


def main():
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <file>")
        return 1
    with open(sys.argv[1], encoding="utf-8") as handle:
        text = handle.read()
    print(format_report(count_stats(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
