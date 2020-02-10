"""
Ejemplo de enviar imagen usando una API KEY

Python 3.6

Vaico
JCA
"""
from time import strftime, localtime
from os import path

import cv2 as cv

from auxfunc.Sender import Sender

# Usar el número de alguien incluyendo el indicativo
# Esto posibilita ver las predicciones en la página web
OBSERVER = ''# número celular con indicativo +57
API_KEY =  '' # solo para pruebas de estudiantes
API =  ""

# Dirección de la imagen local a predecir
IM_FILEPATH = path.join('assets', 'test_im.jpg')
MODEL = 'detector-free' # Nombre del modelo a usar para predecir la imagen enviada

def main():
    print(' - Sending image for predictions')
    date = strftime("%Y-%m-%d_%H:%M:%S", localtime()) # No cambiar formato de la fecha
    im = cv.imread(IM_FILEPATH)

    payload = {
        'task': 'predict',
        'place': 'Unknown',
        'observer': OBSERVER,
        'date': date,
        'frame': im,
        'model': MODEL,
    }

    my_sender = Sender(API, API_KEY)
    res = my_sender.send_request(payload)

    if res.status_code == 200:
        response_payload = res.json()
        print('Objetos encontrados: {}'.format(response_payload['predictions']))


if __name__ == '__main__':
    main()