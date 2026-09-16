from math import log10


class NgramScorer:

    def __init__(self, ngrams):
        self.ngrams = ngrams
        self._identify_ngram_length()
        self._calculate_log_probs()

    def _identify_ngram_length(self):
        lengths = {len(key) for key in self.ngrams}

        if len(lengths) != 1:
            raise ValueError(
                "Усі n-грами повинні мати однакову довжину"
            )

        self.n = lengths.pop()

    def _calculate_log_probs(self, alpha=0.01):

        total = sum(self.ngrams.values())

        for key in self.ngrams:
            self.ngrams[key] = log10(
                float(self.ngrams[key]) / total
            )

        self.alpha = log10(alpha / total)

    def score(self, text, split_by=None, ignore=""):

        if ignore:
            for char in ignore:
                text = text.replace(char, "")

        if split_by is not None:
            return sum(
                self._score(part)
                for part in text.split(split_by)
            )

        return self._score(text)

    def _score(self, text):

        score = 0

        for i in range(len(text) - self.n + 1):

            current = text[i:i + self.n]

            if current in self.ngrams:
                score += self.ngrams[current]
            else:
                score += self.alpha

        return score