# KZ Text Tools

A command-line toolkit for working with Kazakh, Russian and English text:

| Command     | What it does                                   | Needs API key |
|-------------|------------------------------------------------|---------------|
| `stats`     | words, sentences, reading time, top words      | no            |
| `summarize` | short bullet-point summary                     | yes           |
| `translate` | translate between Kazakh / Russian / English   | yes           |
| `simplify`  | rewrite text in simpler words                  | yes           |

Built with **only the Python standard library**.

## Setup

1. Get a free API key at <https://aistudio.google.com/apikey> (only needed
   for `summarize`, `translate`, `simplify`).
2. Copy `.env.example` to `.env` and paste the key.

## Usage

```bash
python kztool.py stats sample.txt
python kztool.py summarize sample.txt --lang kk
python kztool.py translate sample.txt --lang en
python kztool.py simplify sample.txt --lang kk

# you can also pipe text in
echo "Hello world" | python kztool.py translate --lang kk
```

## Files

- `kztool.py` – command-line interface and prompt building
- `textstats.py` – offline text statistics
- `llm.py` – small Gemini API client
- `tests/` – unit tests (run offline)

## Tests

```bash
python -m unittest -v
```

## Ideas for improvement

- Add a `keywords` command
- Support PDF / web page input
- Detect the input language automatically
- Package it so it installs with `pip install .`

> Never commit your `.env` file (it is in `.gitignore`).
