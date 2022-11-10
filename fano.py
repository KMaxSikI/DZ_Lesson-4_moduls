def lid_fano():


    kod = open('shifr.txt', 'r', encoding='utf-8')

    kod_str = kod.read()
    fano = []
    for i in range(0, len(kod_str), 6):
        f = kod_str[i:i + 6].split()
        fano.extend(f)
    return fano


def direct_fano(fano):
    counter = 0

    for n in fano:
        for j in fano:
            if len(n) <= len(j):
                if not j.startswith(n):
                    continue
                else:
                    counter += 1
            else:
                continue

    return counter == len(fano)


def reverse_fano(fano):
    counter = 0

    for n in fano:
        for j in fano:
            if len(n) <= len(j):
                if not j.endswith(n):
                    continue
                else:
                    counter += 1
            else:
                continue

    return counter == len(fano)

