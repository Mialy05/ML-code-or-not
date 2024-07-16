# residuel de L % u
def residuel(L: list, u: str):
    residus = set()
    for mot in L:
        if(str(mot).startswith(u)):
            residus.add(str(mot).removeprefix(u))
    return residus
        
# quotient de L % M
def quotient(L: list, M: list):
    q = set()
    for mot in M:
        q = q.union(residuel(L, mot))
    return q        

def est_ensemble_vide(L: set):
    return len(L) == 0

# conditions d'arret:
# raha misy mot vide anaty Ln => tsy code
# raha Ln ensemble vide => code
# raha efa nisy ilay Ln => code
def sardinas_patterson(L: set):
    langs = list()
    langs.append(L)
    Ln: set = quotient(L, L).difference({''})
    i = 1
    while(len(Ln.intersection({''})) == 0 and est_ensemble_vide(Ln) == False and Ln not in langs ):
        langs.append(Ln)
        Ln = quotient(langs[-1], L).union(quotient(L, langs[-1]))
        i+=1
    # if(Ln in langs):
        # print('Périodique L', i, Ln)
    # langs.append(Ln)
    if( len(Ln.intersection({''})) > 0) :
        # print('nisy mot vide L', i)
        return False
    # if(len(Ln) == 0):
        # print('Ensemble vide L', i)
    # print(langs)
    return True
   

def alea(L: set):
    liste = list(L)
    # print(liste)
    # while(len(liste) > 0):
    i = 0
    while(i < len(liste)):
        liste = liste[i:]
        if(sardinas_patterson(set(liste)) == False):
            for j in range(i, len(liste)):
                liste = liste[liste[i], liste[j], liste[j:]]
        i+=1
    print(liste)
    return

# tableau de tableau
def delete_doublon(tab: list):
    if(len(tab) == 0):
        return tab
    sets = [set(tab[0])]
    for t in tab:
        if(set(t) not in sets):
            sets.append(set(t))
    return [list(s) for s in sets]

# combinaison: tableau de tableau
def generate_combinaison(tab: list, length: int, combinaison: list = [], step: int = 0):
    if(step == length):
        return combinaison
    if(len(combinaison) == 0):
        return generate_combinaison(tab, length, [ [t] for t in tab], step+1)
    tmp = list()
    for t in tab:
        for c in combinaison:
            if(t not in c):
                u = list(c)
                u.append(t)
                if(u not in tmp):
                    tmp.append(u)
    return generate_combinaison(tab, length, delete_doublon(tmp),  step+1)
                