from difflib import SequenceMatcher
import math
from random import randint
import statistics

from pandas import DataFrame
import sardinas_patterson as sp
import importlib
importlib.reload(sp)
# from Levenshtein import distance



ALPHABET = ['0', '1']

def random_word(minLength: int = 1, maxLength: int = 7):
    length = randint(minLength, maxLength)
    w = ''
    for i in range(0, length):
        w += ALPHABET[randint(0, len(ALPHABET) - 1)]
    return w

def random_langage(minWord: int = 1, maxWord: int = 10):
    count = randint(minWord, maxWord)
    langage = set()
    i = 0
    while(i < count):
        w = random_word()
        if(w not in langage):
            langage.add(w)
            i += 1
    return langage

def generate_code(nbr_code: int):
    code = set()
    lastLen = 0
    while(len(code) < nbr_code):
        print('code ', len(code), '/', nbr_code)
        l = random_langage()
        s = sp.sardinas_patterson(l)
        if(len(l) != lastLen and s == True):
           code.add(';'.join(list(l)))
           lastLen = len(l)
    return code

def generate_tsy_code(nbr: int):
    tsy_code = set()
    lastLen = 0
    while(len(tsy_code) < nbr):
        print('tsy_code ', len(tsy_code), '/', nbr)
        l = random_langage()
        s = sp.sardinas_patterson(l)
        if(len(l) != lastLen and s == False):
            tsy_code.add(';'.join(list(l)))
            lastLen = len(l)
    return tsy_code

def generate_data(nbr: int):
    langs = list()
    while(len(langs) < nbr):
        l = random_langage()
        s = sp.sardinas_patterson(l)
        lang = list(l)
    
        if(s == False):
            lang.append('0')
        else:
            lang.append('1')
        langs.append(lang)
        print('generating ', len(langs), '/', nbr)
    return langs
        
def generate_dataset(code_file: str, no_code_file: str, nbr_code: int = 100, nbr_no_code: int = 100):
    code = generate_code(nbr_code)
    no_code = generate_tsy_code(nbr_no_code)
    with open(code_file, 'w+') as f:
        f.write('\n'.join(list(code)))    
    with open(no_code_file, 'w+') as f:
        f.write('\n'.join(list(no_code)))




# def score(w1: str, w2: str):
#     s = 0
#     len_w1 = len(w1)
#     len_w2 = len(w2)
#     for i in range(len_w1):
#         if(i < len_w2):
#             if(w1[i] == w2[i]):
#                 s += 1   
#         else:
#             break
#     s = s/(len_w1 + len_w2)
#     coeff = 0
#     if(len_w1 == len_w2):
#         coeff = 1
#     # if(len_w1 < len_w2):
#     #     coeff = len_w1/len_w2
#     # if(len_w1 > len_w2):
#     #     coeff = len_w2/len_w1
#     # return s * coeff
#     return s + coeff

def score(w1: str, w2: str):
    return SequenceMatcher(None, w1, w2).ratio()
   

def similarity_score(l: set):
    l = list(l)
    for i in range(len(l)):
        word_score = []
        for j in range(len(l)):
            if( i != j):
                word_score.append(score(l[i], l[j]))
    if(len(word_score) == 0):
        return 1
    return statistics.mean(word_score)
    
def residuels(l: set):
    res = list()
    for mot in l:
        res.append([r for r in list(sp.residuel(l, mot)) if len(r) > 0])      
    return res

def format_to_set(df: DataFrame):
    l = list()
    for c in df.values:
        l.append(set(c[0].split(';')))
    return l

def entropie_lang(l: set):
    n = len(l)
    if(n == 0):
        return 0
    prob = 1 / n
    return -n * prob * math.log2(prob)

def extract_feature(l: set):
    len_words = [len(w) for w in l]
    feat = dict()

    # feat['len'] = len(l)
    feat['dev_len'] = statistics.pstdev(len_words)
    feat['med_len'] = statistics.median(len_words)
    feat['min_length'] = min(len_words)
    feat['max_length'] = max(len_words)
    m = len([ len_words.count(s) for s in set(len_words) if len_words.count(s) > 1])
    feat['same_len'] = m
    words = ''.join([w for w in l])
    
    feat['stat_0'] = words.count('0')/len(words)
    feat['stat_1'] = words.count('1')/len(words)
    
    sans_suffix = 0 
    for r in residuels(l):
        if(len(r) == 0):
            sans_suffix += 1
    
    q = sp.quotient(list(l), list(l))
    feat['suf'] = len([u for u in q if u != ''])
    # feat['suf'] = len(q)
    feat['tsisy_suf'] = sans_suffix/len(l)
    
   
    feat['entropie'] = entropie_lang(l)
    feat['sim'] = similarity_score(l)
    
    return feat
