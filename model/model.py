import random
import json

def prediction(form):
    print('=== DATA FOR PREDICTION ===')
    print(json.dumps(form,indent=2))
    result = bool(random.getrandbits(1))
    print('For now, return random prediction:',result)
    return result
