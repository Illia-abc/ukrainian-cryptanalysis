import os


CURRENT_DIR = os.path.dirname(__file__)

NGRAM_FILES = {
    4: os.path.join(
        CURRENT_DIR,
        "uk",
        "quadrams.txt"
    )
}


def load_ngrams(n):

    if n not in NGRAM_FILES:
        raise ValueError(
            "Підтримується тільки 4-грама"
        )

    ngrams = {}

    with open(
        NGRAM_FILES[n],
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            if not line.strip():
                continue

            key = line[:n]
            count = line[n:].strip()

            if len(key) != n:
                continue

            ngrams[key] = int(count)

    return ngrams