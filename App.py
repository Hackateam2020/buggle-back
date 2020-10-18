from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods = ['POST','GET'])
def login():
    form_name = request.form['name']
    return render_template('bienvenida.html', name = form_name)

@app.route('/proceso', methods = ['GET'])
def proceso():
    return render_template('proceso.html')

@app.route('/predict', methods = ['POST','GET'])
def predict():
    print('=== /predict/ ===')
    print(str(request))
    return 'Not implemented'

if __name__ == '__main__':
   app.debug = True
   app.run()
