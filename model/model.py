import pandas as pd
import pickle

filename = 'model/prediction_model'
loaded_model = pickle.load(open(filename,'rb'))

dicto = {'gender_type':0, 'birth_date':1990, 'income_monthly_amount': 1000, 'deudas_banca': 0, 'banca_movil': 1, 'Sunat':0}
ended = pd.DataFrame(data=dicto,index=[0])
predict = loaded_model.predict(ended)
print(f'Según nuestros datos tu solicitud ha sido: {predict}')
