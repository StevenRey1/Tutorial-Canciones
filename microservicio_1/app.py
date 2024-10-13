from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://redis:6379/0',
    CELERY_RESULT_BACKEND='redis://redis:6379/0'
)
celery = Celery(
    app.import_name,
    backend=app.config['CELERY_RESULT_BACKEND'],
    broker=app.config['CELERY_BROKER_URL']
)
celery.conf.update(app.config)
app_context = app.app_context()
app_context.push()
api = Api(app)
api.init_app(app)

@celery.task(name="tabla.registrar")
def registrar_puntaje(cancion_json):
    pass

class VistaPuntuacion(Resource):

    def post(self, id_cancion):
        content = requests.get('http://flaskr:8000/cancion/{}'.format(id_cancion))
        
        
        if content.status_code == 404:
            return content.json(),400
        else:
            cancion = content.json()
            
            cancion["puntaje"] = request.json["puntaje"]
            print(cancion)
            args = (cancion,)
            registrar_puntaje.apply_async(args)
            return json.dumps(cancion)

api.add_resource(VistaPuntuacion, '/cancion/<int:id_cancion>/puntuar')
