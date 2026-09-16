from breaking.substitution import SubstitutionBreak
from score.ngram import NgramScorer
from data.uk import load_ngrams


ciphertext = """Ь фвніуйпй чщбвещ, ь чкїкї йьіг ьвплгейґ уйбщек хініочкчю хініоч: чй зфі Бвглд. Д акїйфєщ ев тіьпгвеел цйнд, цгйїйфєщ цігіавнк л чвб, фі єіагличю ущгпвек, цйїкндиою ев овбйчеи цщочінюещ оуіни. Д фканиою а фвню.— Чйфл фщбв ьв фщбйи, ду вбвьйедеук, фєкплчщичю евауйнй біеі. Чйфл аоі цгйцвфвя... Чвябел аігхекук нічдчю, гкчблшей цйїкчщишкою, фй йчгйпла, л пвоеі фіею; тлєкчю щ бйпкнвї фйгйпв, ч ьв еіи — бйашвьекз очіц... Д йфукфви алґ л ьпвфщи... айлочкещ бйд бвчк — ачлніекз цгййтгвь чляґ евфьакшвзейґ Бвглґ, жй очйґчю ев пгведї еіалфйбкї алула. Бйд бвчк — евґаелочю, чкїв єщгв л фйтглочю тіьбієев. (Сі д фйтггі цвб'дчви!). Л блз еібйєнкакз тлню, л бйд еіьейоев бщув чіцнличю щ нвбцвфл рвевчкьбщ цігіф скб цгіугвоекб цішвнюекб йтгвьйб."""


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