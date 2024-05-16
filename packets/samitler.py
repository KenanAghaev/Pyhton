def samitleri_al(cumle):
    samitler = set()
    for herf in cumle:
        if herf.lower() not in "aeiou" and herf.isalpha():
            samitler.add(herf.lower())

    return samitler
