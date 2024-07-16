import flask
from flask_cors import CORS, cross_origin
import joblib

from predict import predict


app = flask.Flask(__name__)
app.config['DEBUG'] = True
model = joblib.load('./models/model_91_7_latest.mu')
cors = CORS(app)

@cross_origin()
@app.route('/predict', methods=['GET'])
def predict_code():
    if('lang' in flask.request.args ):
        params = flask.request.args['lang']
        res = predict(model, params)
        return flask.jsonify(res)
    else:
        return flask.jsonify({'error': 'Veuillez fournir un langage'})


app.run()