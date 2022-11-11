

from main_fano import readalfa

alfa_file = open('alfabet.txt', 'r', encoding='utf-8')
shifr = open('shifr.txt', 'r', encoding='utf-8')

def desh(fshif, dict_alf):
    shifr_str = fshif.read()
    open_sifr = ''
    fano = []
    for i in range(0, len(shifr_str), 6):
        f = shifr_str[i:i+6].split()
        fano.extend(f)
        open_sifr += dict_alf.get(shifr_str[i:i+6]) + " "
    return open_sifr

print(desh(shifr, readalfa(alfa_file)))

