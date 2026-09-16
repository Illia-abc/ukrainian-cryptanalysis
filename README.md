# Ukrainian Cryptanalysis

A Python project for automatic cryptanalysis and decryption of Ukrainian texts.

The project is based on [cryptanalysis](https://github.com/DominicBreuker/cryptanalysis) by DominicBreuker and adapted to work with the Ukrainian alphabet and Ukrainian language statistics.

## Features

At the current stage, the project supports automatic cryptanalysis of the **simple substitution cipher**.

The program:

1. Loads Ukrainian 4-gram statistics.
2. Scores text based on how closely it matches natural Ukrainian language.
3. Searches for a substitution key.
4. Produces the best candidate plaintexts.
5. Displays the score and substitution key for each candidate.

## Project Structure

```text
project/
│
├── README.md
├── main.py
│
├── breaking/
│   └── substitution.py
│
├── score/
│   └── ngram.py
│
└── data/
    ├── uk.py
    └── uk/
        └── quadrams.txt
```

### File Description

**`main.py`** — the main entry point. It contains the ciphertext, loads the n-gram statistics, runs the cryptanalysis and prints the results.

**`breaking/substitution.py`** — implements the cryptanalysis algorithm for the simple substitution cipher.

**`score/ngram.py`** — contains the `NgramScorer` class used to score text based on n-gram frequencies.

**`data/uk.py`** — loads Ukrainian n-gram statistics from the data file.

**`data/uk/quadrams.txt`** — contains Ukrainian 4-grams and their frequency counts.

## Ukrainian 4-Grams

The program uses **4-gram statistics** to evaluate candidate plaintexts.

A 4-gram is a sequence of four characters. For example:

```text
текст
стра
  аб
абв 
```

Spaces are also included because they provide useful information about word boundaries.

The statistics file is generated from a Ukrainian word list and word-frequency data.

During generation, two spaces are added before and after each word:

```python
word = "  " + word + "  "
```

This allows the program to generate 4-grams that contain word boundaries.

## Text Scoring

The `NgramScorer` processes the text as a sequence of overlapping 4-grams.

If a 4-gram exists in the statistical model, its log probability is added to the total score. Unknown 4-grams receive a small penalty.

A **higher score** means that the candidate text is statistically closer to Ukrainian language patterns.

Because logarithms of probabilities are used, the scores are usually negative. Therefore:

```text
-5590 > -6327
```

means that `-5590` is the better score.

## Why Does the Program Output 5 Variants?

The following code is used in `main.py`:

```python
results = breaker.guess(
    ciphertext,
    n=5
)
```

The `n=5` parameter tells the program to return the **5 best candidates** found during the search.

The algorithm does not actually understand Ukrainian language like a human. It evaluates candidates mathematically using 4-gram statistics, so some candidates can be correct while others can be incorrect.

For example, during testing the program produced:

```text
Variant 1
Score: -5590.593
```

and:

```text
Variant 2
Score: -5590.593
```

Both variants produced the same readable plaintext:

```text
Довбиш був багатий чоловік; він жив на самому кінці села...
```

Variants 3–5 had significantly lower scores and contained incorrect words.

This is related to the search algorithm: it can find several locally good substitution keys, but not every candidate is necessarily the correct decryption.

If only the best candidate is required, change:

```python
n=5
```

to:

```python
n=1
```

## Fixing Ukrainian 4-Gram Loading

During development, the following error occurred:

```text
ValueError: Усі n-грами повинні мати однакову довжину
```

The problem was caused by using:

```python
line.strip().split()
```

when reading the statistics file.

This does not work correctly for our data because some 4-grams contain spaces. For example:

```text
  аб
```

Using `strip()` removes the leading spaces.

The loader was therefore changed to treat the first `n` characters of each line as the n-gram:

```python
key = line[:n]
count = line[n:].strip()
```

This preserves spaces inside 4-grams and ensures that all loaded n-grams have the correct length.

## Running the Project

Install the required Python dependencies first.

Then run the program from the project root:

```powershell
python main.py
```

The program will load the Ukrainian 4-gram statistics, start the search and print the best candidate decryptions.

## Example Output

```text
Завантаження українських 4-грам...
Починаю пошук...

======================================================================
НАЙКРАЩІ РЕЗУЛЬТАТИ
======================================================================

--- Варіант 1 ---
Score: -5590.593

Довбиш був багатий чоловік; він жив на самому кінці села...
```

The program also prints the substitution key:

```text
а -> ч | б -> х | в -> ш | ...
```

The left side represents a ciphertext character, while the right side represents the corresponding plaintext character.

## Future Improvements

The project can be extended with support for additional classical ciphers and cryptanalysis methods, including:

* Caesar cipher;
* Vigenère cipher;
* simple substitution cipher;
* additional cryptanalysis algorithms;
* different n-gram models.

The main goal of the project is to explore the practical application of statistical cryptanalysis to the Ukrainian language.
