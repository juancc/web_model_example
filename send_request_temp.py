"""
Ejemplo de enviar imagen usando una API KEY

Python 3.6

Vaico
JCA
"""
from time import strftime, localtime, time
from os import path

import cv2 as cv

from auxfunc.Sender import Sender

# Usar el número de alguien incluyendo el indicativo
# Esto posibilita ver las predicciones en la página web
STAGE = 'dev'

SERVER = {
    "prod":{
        "api": 'https://1x06civnj2.execute-api.us-east-2.amazonaws.com/DummyStage/newdata/fromstream',
        'key': 'TmEpgrNEOC8KS8FNYKB6zmKnqagJmMC2mW0F6ky0'
        },
    'dev':{
        'key':'SbdzW13c8E8mLkf9NEkk14a2o3hh5nN04hXo7spM',
        'api': ' https://j8wmps8gr0.execute-api.us-east-2.amazonaws.com/testing/newdata/fromstream'
        }
}



# OBSERVER = '+573155582556'  # Número celular con indicativo +57
OBSERVER = '+573207748138'  # Número celular con indicativo +57
# SENDER = 'jarbel16@eafit.edu.co'
SENDER = 'backend1@vaico.com.co'
# Dirección de la imagen local a predecir
#IM_FILEPATH = path.join('assets', 'test_im.jpg')
IM_FILEPATH = '/home/juanc/5eb8334b-a41f-4436-a311-87a7493b3a2c.jpeg'
MODEL = 'SURA-alturas' # Nombre del modelo a usar para predecir la imagen enviada

def main():
    api = SERVER[STAGE]['api']
    key = SERVER[STAGE]['key']
    
    print(' - Sending image for predictions on {}'.format(STAGE))
    date = strftime("%Y-%m-%d_%H:%M:%S", localtime()) # No cambiar formato de la fecha
    im = cv.imread(IM_FILEPATH)

    payload = {
        'task': 'predict-cloud',
        'place': 'local-test',
        'observer': OBSERVER,
        'date': date,
        'frame': im,
        'model': MODEL,
        'sender': SENDER
    }

    my_sender = Sender(api, key)
    start = time()
    res = my_sender.send_request(payload)
    if res.status_code == 200:
        response_payload = res.json()
        print(response_payload)
        print('Objetos encontrados: {}'.format(response_payload['predictions']))
    duration = time() - start
    print('Duration: {}s'.format(duration))

if __name__ == '__main__':
    main()
