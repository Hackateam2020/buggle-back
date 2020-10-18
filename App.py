from flask import *
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

@app.route('/proceso', methods = ['GET'])
def proceso():
    user = request.cookies.get('user')
    return render_template('proceso.html', name = user)

@app.route('/predict', methods = ['POST','GET'])
def predict():
    print('=== /predict/ ===')
    print(str(request))
    return 'Not implemented'

if __name__ == '__main__':
   app.debug = True
   app.run()
