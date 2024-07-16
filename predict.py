from sklearn.linear_model import LogisticRegression
import pandas as pd

from sardinas_patterson import sardinas_patterson
import algo as algo
import importlib
importlib.reload(algo)


def predict_langage(model: LogisticRegression, l: set):
    f = algo.extract_feature(l)
    # print(f)
    res = model.predict(pd.DataFrame([f]).values)[0]
    return res == 1

def predict_list(model: LogisticRegression, langages: list):
    feats = list()
    for l in langages:
        feats.append(algo.extract_feature(l))
    return model.predict(pd.DataFrame(feats).values) 

def predict(model: LogisticRegression, lang: str):
    l = set(lang.split(';'))
    prediction = predict_langage(model, l)
    sardinas = sardinas_patterson(l)
    res = dict()
    res['pred'] = 1 if prediction else 0 
    res['verdict'] = 1 if sardinas else 0
    return res
