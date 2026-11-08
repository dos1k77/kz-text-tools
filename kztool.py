"""Kazakh / Russian / English text tools: stats, summarize, translate, simplify."""
import argparse
import sys

import llm
from textstats import stats

LANGS = {"kk": "Kazakh", "ru": "Russian", "en": "English"}


def read_input(path):
    """Read text from a file, or from stdin if no file is given."""
    if path:
        with open(path, encoding="utf-8") as f:
            return f.read()
    if sys.stdin.isatty():
        print("Paste text, then press Ctrl+D (Ctrl+Z + Enter on Windows):", file=sys.stderr)
    return sys.stdin.read()


def build_prompt(command, text, lang="kk"):
    """Build the LLM instruction for a command."""
    name = LANGS[lang]
    tasks = {
        "summarize": f"Summarize the following text in 3-5 short bullet points. Write in {name}.",
        "translate": f"Translate the following text into {name}. Output only the translation.",
        "simplify": f"Rewrite the following text in simple, easy-to-understand {name}, "
                    "as if explaining to a school student. Keep the meaning.",
    }
    return f"{tasks[command]}\n\nText:\n{text}"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    for name, help_ in [
        ("stats", "word count, reading time, top words (offline)"),
        ("summarize", "short bullet-point summary"),
        ("translate", "translate to another language"),
        ("simplify", "rewrite in simpler words"),
    ]:
        p = sub.add_parser(name, help=help_)
        p.add_argument("file", nargs="?", help="text file (default: stdin)")
        if name != "stats":
            p.add_argument("--lang", choices=LANGS, default="kk",
                           help="output language (default: kk)")

    args = ap.parse_args()
    text = read_input(args.file).strip()
    if not text:
        raise SystemExit("No text provided.")

    if args.command == "stats":
        s = stats(text)
        print(f"Characters : {s['characters']}")
        print(f"Words      : {s['words']}")
        print(f"Sentences  : {s['sentences']}")
        print(f"Reading    : ~{s['reading_minutes']} min")
        print("Top words  : " + ", ".join(f"{w} ({n})" for w, n in s["top_words"]))
        return

    try:
        print(llm.ask(build_prompt(args.command, text, args.lang)))
    except llm.LLMError as e:
        raise SystemExit(f"Error: {e}")


if __name__ == "__main__":
    main()
