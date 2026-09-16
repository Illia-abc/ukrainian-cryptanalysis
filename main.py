from breaking.substitution import SubstitutionBreak
from score.ngram import NgramScorer
from data.uk import load_ngrams


ciphertext = """Очмєкв єзм єсясґкж ачечмдп; мдг їкм гс фсичиз пдгшд фцес, ґси, оц яекєчпкж ьл мбчокм з едф мзхупки пекгчи. М фсичиз пзґпз ґчяч ьлз єекрсм исецгупкж Очмєквдм фґсмчачп. Гсо фґсмпчи фґчьес Очмєквцмс бсґс, мфь м ацлцвгьб. Чо мзекшд єзеч мкогч ґдеупк плсж єдечт фґдгк х фдгцвгдик омцлкис. Язфґд мкфчпд мквгд хчмфди хсплкмсек чо мзекшд мдпгс ж фґдгк, гсац язфґкж едф. Псліч жвчм ічисецгупз, фпчфс ічяеьосйак гс Очмєквдм омдл. Іцлцо гки єекфгзм мзяче єдечт фґдгк, ідоіцлцхсгкж мгкхз ацлмчгчй ілкхуєчй; хсачлгдек ачлгчй іеьичй чоакгцгд омцлд х чомдлпсик, ічисеучмсгкик ьфгч-фкгучй юслєчй х ацлмчгчй мзхупчй физїпчй гсмплзяк. Очмєквцмс бсґс єзес гчмс, мцекпс, очєлц мвкґс, х акисекик мдпгсик. Пчеч мдпчг мкфдек мдпчггкшд, ічисеучмсгд ьфгч-фкгучй юслєчй."""


print("Завантаження українських 4-грам...")

ngrams = load_ngrams(4)

scorer = NgramScorer(ngrams)

breaker = SubstitutionBreak(
    scorer,
    seed=42
)

print("Починаю пошук...")
print()

breaker.optimise(
    ciphertext,
    n=20
)

print()
print("=" * 70)
print("НАЙКРАЩІ РЕЗУЛЬТАТИ")
print("=" * 70)

results = breaker.guess(
    ciphertext,
    n=5
)

for i, (plaintext, score, key) in enumerate(
    results,
    1
):

    print()
    print(f"--- Варіант {i} ---")
    print(f"Score: {score:.3f}")
    print(plaintext)
    print()
    print("Ключ:")

    alphabet = (
        "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    )

    for cipher, plain in zip(
        alphabet,
        key
    ):
        print(
            f"{cipher} -> {plain}",
            end=" | "
        )

    print()