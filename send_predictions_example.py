"""
Ejemplo de enviar imagen y predicciones usando una API KEY

Python 3.6

Vaico
JCA
"""
from time import strftime, localtime
from os import path
from uuid import getnode as get_mac

import cv2 as cv

from auxfunc.Sender import Sender

# Usar el número de alguien incluyendo el indicativo
# Esto posibilita ver las predicciones en la página web
MAC = get_mac()  # Observer
API_KEY = 'ZXLbQDOTDyauiZTIHVbtg7KSojUvDUtk1wCGkMmZ'  # Leer archivo de credentials.ods
API = 'https://j8wmps8gr0.execute-api.us-east-2.amazonaws.com/testing/newdata/fromstream'  # Leer archivo de credentials.ods

# Dirección de la imagen local a predecir
IM_FILEPATH = path.join('assets', 'test_im.jpg')


def main():
    print(' - Sending image for predictions')
    date = strftime("%Y-%m-%d_%H:%M:%S", localtime()) # No cambiar formato de la fecha
    im = cv.imread(IM_FILEPATH)

    # Lista de diccionarios con las predicciones
    # la obtienen pasando la imagen por el modelo y por cada uno de los objetos de la respuesta con Object._asdict()
    # Este es un ejemplo de como deben lucir las predicciones
    preds = [
        {'label': 'tie',
         'score': '0.42',
         'boundbox': {'xmin': 248, 'ymin': 221, 'xmax': 260, 'ymax': 269}
         }
    ]
    payload = {
        'sender': 'node',
        'observer': MAC,
        'date': date,
        'frame': im,
        'predictions': preds,
    }

    my_sender = Sender(API, API_KEY)
    res = my_sender.send_request(payload)

    if res.status_code == 200:
        response_payload = res.json()
        print(res)


if __name__ == '__main__':
    main()