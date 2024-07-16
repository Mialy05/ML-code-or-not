import joblib
from predict import predict, predict_langage
from sardinas_patterson import sardinas_patterson


langages = [
    {'0100011', '011011', '001', '0110000', '0101110', '101', '0000011', '00101', '00110'},
    {'0101000', '0100', '1100011', '0110', '10111', '01', '0110110', '110101'},
    {'000001', '1', '100000', '1011100', '000000'},
    {'10100', '10010', '11100', '10'},
    {'00', '0000', '1000001'},
    {'0', '000', '11000'},
    {'1011101', '10101', '1011', '0111011'},
    {'1101', '000', '00'},
    {'1101011', '010001', '1010', '10000', '0'},
    {'00001', '000', '00', '1100011', '1100101'},
    {'001', '110110', '110', '10'},
    {'00', '10', '01011', '10011', '10111'},
    {'111001', '10011', '00', '0000', '0000111'}
]
#
ok = 0
model = joblib.load('./models/model_90_6.mu')
for langage in langages :
    prediction = predict_langage(model, langage)
    # #
    sardinas = sardinas_patterson(langage)

    if(sardinas == prediction) :
        ok = ok +1
    print('L:', langage, ' S: ', sardinas, ' P: ', prediction)

print('ok ', ok, ' / ', len(langages))
