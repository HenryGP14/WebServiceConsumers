import requests
import json


def generate_request(url, params={}):
    headers = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(params), headers=headers)
    if response.status_code == 200:
        return response.json()


def get_LgVacun(params={}):
    respuesta = generate_request("https://webservicesvacunacion.herokuapp.com/vacunacion/consultar-lugar/", params)
    print(respuesta)
    if respuesta:
        resultJSON = respuesta.get("consulta")
        return resultJSON
    return ""
