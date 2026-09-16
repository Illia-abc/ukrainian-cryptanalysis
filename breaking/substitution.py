import random


ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"


class SubstitutionBreak:

    def __init__(self, scorer, seed=None):

        self.scorer = scorer
        self.candidates = []

        if seed is not None:
            random.seed(seed)

    def guess(self, text, n=3):

        if len(self.candidates) < n:
            raise ValueError(
                f"Спочатку потрібно отримати хоча б {n} кандидатів"
            )

        result = []

        for key, score in self.candidates[:n]:

            plaintext = self.decipher(text, key)

            result.append(
                (plaintext, score, key)
            )

        return result

    def optimise(self, text, n=20):

        for i in range(n):

            key, score = self.optimise_once(text)

            self.append_candidate(
                key,
                score
            )

            print(
                f"Ітерація {i + 1}: "
                f"score = {score:.3f} | "
                f"{self.decipher(text, key)[:50]}"
            )

    def append_candidate(self, key, score):

        self.candidates.append(
            (key, score)
        )

        self.candidates.sort(
            key=lambda x: x[1],
            reverse=True
        )

    def optimise_once(self, text):

        # Початковий випадковий ключ
        key = list(ALPHABET)
        random.shuffle(key)

        score = self.score_key(
            text,
            key
        )

        count = 0

        # Аналогічно оригінальному алгоритму:
        # якщо покращення немає 1000 разів поспіль —
        # вважаємо, що пошук завершено.
        while count < 1000:

            new_key = self.random_swap(key)

            new_score = self.score_key(
                text,
                new_key
            )

            if new_score > score:

                key = new_key
                score = new_score

                count = 0

            count += 1

        return key, score

    def random_swap(self, key):

        a, b = random.sample(
            range(len(ALPHABET)),
            2
        )

        new_key = list(key)

        new_key[a], new_key[b] = (
            new_key[b],
            new_key[a]
        )

        return new_key

    def score_key(self, text, key):

        return self.scorer.score(
            self.decipher(text, key)
        )

    def decipher(self, text, key):

        result = []

        translation = dict(
            zip(ALPHABET, key)
        )

        for char in text:

            lower = char.lower()

            if lower in translation:

                decoded = translation[lower]

                if char.isupper():
                    decoded = decoded.upper()

                result.append(decoded)

            else:
                result.append(char)

        return "".join(result)