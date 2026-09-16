from collections import Counter
from wordfreq import iter_wordlist, zipf_frequency


ALPHABET = set(
    "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
)


quadgrams = Counter()


for i, word in enumerate(
    iter_wordlist("uk")
):

    if i >= 100000:
        break

    word = word.lower()

    if not word:
        continue

    if not all(
        char in ALPHABET
        for char in word
    ):
        continue

    frequency = zipf_frequency(
        word,
        "uk"
    )

    if frequency <= 0:
        continue

    weight = max(
        1,
        int(10 ** frequency)
    )

    word = "  " + word + "  "

    for j in range(
        len(word) - 3
    ):

        quad = word[j:j + 4]

        quadgrams[quad] += weight


with open(
    "data/uk/quadrams.txt",
    "w",
    encoding="utf-8"
) as file:

    for quad, count in quadgrams.most_common():

        file.write(
            f"{quad} {count}\n"
        )


print(
    f"Готово. 4-грам: {len(quadgrams)}"
)