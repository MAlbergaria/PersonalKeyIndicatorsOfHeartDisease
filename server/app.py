from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

from container import Container
from interfaces.routes import Routes
from interfaces.controllers.healthRecordController import *


# Create API
app = Flask(__name__)
api = Api(app)


# Dependency injector container
container = Container()
app.container = container


# Setup specifications
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Products',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)


# Setup API Resources\Routes
routes = Routes(api)


# Run API
if __name__ == '__main__':
    apis = [AddHealthRecordAPI, AllHealthRecordAPI]

    for api in apis:
        docs.register(api)

    app.run(debug=container.config.run.debug(), port=container.config.run.port())