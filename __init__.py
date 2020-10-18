from flask import *
import json

import model.model as model

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    user = request.form['name']
    resp = make_response(render_template('bienvenida.html', name = user))
    resp.set_cookie('userID',user)
    return resp

@app.route('/proceso', methods = ['GET','POST'])
def proceso():
    user = request.form['name']
    with open('data/preguntas.json','r') as f:
        pj = json.load(f)
    resp = make_response(render_template('proceso.html', 
                           name = user, 
                           preguntas = pj))
    resp.set_cookie('userID',user)
    return resp

@app.route('/predict', methods = ['POST','GET'])
def predict():
    user = request.cookies.get('userID')
    result = model.prediction(request.form)
    response = render_template('resultado.html', 
                               concedido = result,
                               name = user)
    return response

if __name__ == '__main__':
   app.debug = True
   app.run()
