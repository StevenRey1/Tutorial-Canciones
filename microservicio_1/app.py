from microservicio_1 import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery
from microservicio_1.celery_config import make_celery

app = create_app('default')
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)
celery = make_celery(app)
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

@celery.task(name="tabla.registrar")
def registrar_puntaje(cancion_json):
    pass

class VistaPuntuacion(Resource):

    def post(self, id_cancion):
        content = requests.get('http://127.0.0.1:5000/cancion/{}'.format(id_cancion))
        
        
        if content.status_code == 404:
            return content.json(),404
        else:
            cancion = content.json()
            
            cancion["puntaje"] = request.json["puntaje"]
            print(cancion)
            args = (cancion,)
            registrar_puntaje.apply_async(args)
            return json.dumps(cancion)

api.add_resource(VistaPuntuacion, '/cancion/<int:id_cancion>/puntuar')
