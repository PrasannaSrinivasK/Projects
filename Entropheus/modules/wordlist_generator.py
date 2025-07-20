# modules/wordlist_generator.py
import itertools

LEET_MAP = {
    'a': ['a', '@', '4'], 'e': ['e', '3'], 'i': ['i', '1', '!'],
    'o': ['o', '0'], 's': ['s', '$', '5'], 't': ['t', '7']
}

YEARS = ['2024', '2025', '123', '007', '786']

def leetify(word):
    combos = [[LEET_MAP.get(c.lower(), [c]) for c in word]]
    return [''.join(x) for x in itertools.product(*combos[0])][:5]

def generate_wordlist(name, dob, pet):
    base_words = [name, dob, pet]
    combos = set()

    for w in base_words:
        combos.update(leetify(w))

    all_combo = set()
    for w1 in combos:
        for w2 in combos:
            all_combo.add(f"{w1}{w2}")
            for year in YEARS:
                all_combo.add(f"{w1}{w2}{year}")
                all_combo.add(f"{year}{w1}{w2}")

    return list(all_combo)[:5000]
