import pandas as pd
import pickle

filename = 'model/prediction_model'
loaded_model = pickle.load(open(filename,'rb'))

dicto = {'gender_type':0, 'birth_date':1990, 'income_monthly_amount': 1000, 'deudas_banca': 0, 'banca_movil': 1, 'Sunat':0}
# ended = pd.DataFrame(data=dicto,index=[0])
# predict = loaded_model.predict(ended)
# print(f'Según nuestros datos tu solicitud ha sido: {predict}')

def prediction(form):
    dicto['gender_type'] = form['género'] == 'masculino' and 1 or 0
    dicto['birth_date'] = int(form['año'])
    dicto['income_monthly_amount'] = int(form['ingresos'])
    dicto['deudas_banca'] = form['ingresos'] == 'si' and 0 or 1
    dicto['banca_movil'] = form['celular'] == 'si' and 0 or 1
    dicto['Sunat'] = form['deudasunat'] == 'si' and 0 or 1
    ended = pd.DataFrame(data=dicto, index=[0])
    result = loaded_model.predict(ended)
    return result[0] == 'Aprobado'
    
    
    
