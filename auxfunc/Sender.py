"""
Functions for cast and make an HTTP request to AWS API to store predictions

JCA
Vaico
"""
import base64
import json

import pickle

import cv2 as cv
import requests
from requests.exceptions import HTTPError
from sys import getsizeof



class Sender:
    def __init__(self, api_endpoint, api_key=None):
        self.API_ENDPOINT = api_endpoint
        self.API_KEY = api_key
        print('Sender API {}'.format(self.API_ENDPOINT))

    def pack_data(self, obs_data):
        """Add data, modify and encode data, to set ready to send"""
        obs_data['frame'] = self.im2json(obs_data['frame'])
        json_data = json.dumps(obs_data)
        print('Package size: {} Kilobyte'.format(getsizeof(json_data) / 1000))
        return json_data

    def send_request(self, frameData):
        """Send general request to server"""
        print('Sending request from: {}'.format(frameData['observer']))
        json_data = self.pack_data(frameData)
        headers = {"x-api-key": self.API_KEY}

        try:
            url = '{}/{}'.format(self.API_ENDPOINT, '')
            print('Wating server response...')
            response = requests.post(url, data=json_data, headers=headers)  # data-> body in http request
            # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
            raise HTTPError(http_err)
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
            raise Exception(err)
        else:
            print('Successfully sent package')
            return response

    def im2json(self, im):
        """Encode image to send"""
        _, imdata = cv.imencode('.JPG', im)
        im_str = base64.b64encode(imdata).decode('ascii')
        return im_str

