import joblib
from algo import generate_dataset, residuels
from predict import predict, predict_langage
from sardinas_patterson import sardinas_patterson



# print(random_word())
# codeFile = open('./data/kely/code.csv', 'w+')
# tsyCodeFile = open('./data/kely/tsy_code.csv', 'w+')
# print(set('1;001;001101'.split(';')))

# print(extract_feature({'0011', '00111'}))
# print(sardinas_patterson({'1111101'}))

# model = joblib.load('./models/model_90_6.mu')
# print(predict(model, '11;111011'))
generate_dataset('./data/code.csv', './data/tsy_code.csv', 2500, 2500)
# print(sardinas_patterson(set(['100001', '110', '0', '000001'])))

  
