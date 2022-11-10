from fano import *

alfa_file = open('alfabet.txt', 'r', encoding='utf-8')


def readalfa(file):
    if direct_fano(lid_fano()) and reverse_fano(lid_fano()):

        alfa = file.readlines()
        dict_alfa = {}
        for i in range(len(alfa)):
            alfa[i] = alfa[i].split()
        for j in alfa:
            dict_alfa[j[0]] = j[1]
        return dict_alfa
    else:
        raise ValueError


if __name__ == '__main__':
    print(readalfa(alfa_file))
