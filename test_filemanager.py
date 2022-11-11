from read_text import d_d
from deshifr import *
from main_fano import readalfa
from fano import *
from console import *
import os
import shutil


data = open('Data.txt', 'r', encoding='utf-8').readlines()
alfa_file = open('alfabet.txt', 'r', encoding='utf-8')
shifr = open('shifr.txt', 'r', encoding='utf-8')

def test_d_d():
    assert type(d_d(data)) == dict

def test_desh():
    assert (desh(shifr, readalfa(alfa_file))) == "Python the best ! "

def test_readalfa():
    alfa_file = open('alfabet.txt', 'r', encoding='utf-8')
    assert (readalfa(alfa_file)) == {'000001': 'Python', '000010': 'best', '000011': 'the', '000100': '!'}
    assert type(readalfa(alfa_file)) == dict
def test_fano():
    assert reverse_fano(lid_fano()) == True
    assert type(direct_fano(lid_fano())) == bool
    assert lid_fano() == ['000001', '000011', '000010', '000100']
    assert type(lid_fano()) == list

def test_console():
    assert copy_folder('shifr.txt', 'shifr_new.txt') == 'shifr_new.txt'
    assert viewer() == ['.git', '.idea', '.pytest_cache', 'venv', '__pycache__']

