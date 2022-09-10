from dependency_injector.wiring import inject, Provide
from flask import request
from flask_restful import Resource
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from itsdangerous import json

from container import Container
from models.healthRecord import HealthRecord
from infra.schemas.healthRecordSchema import HealthRecordSchema
from services.healthRecordService import HealthRecordService
from utils.utils import make_error_message


class AddHealthRecordAPI(MethodResource, Resource):

    @inject
    def __init__(self, health_record_service: HealthRecordService = Provide[Container.health_record_service]) -> None:
        super().__init__()
        self.health_record_service = health_record_service

    @doc(description='Returns heart disease prediction.', 
         tags=['Predict heart disease'])
    @use_kwargs(HealthRecordSchema, location=('json'))
    @marshal_with(HealthRecordSchema)
    def post(self, **kwargs):
        try:
            json_data = request.json
        

            health_record = HealthRecord(json_data["bmi"], json_data["smoking"], json_data["alcohol_drinking"], json_data["stroke"],
                                     json_data["physical_health"], json_data["mental_health"], json_data["diff_walking"], json_data["sex"],
                                     json_data["age_category"], json_data["race"], json_data["diabetic"], json_data["physical_activity"],
                                     json_data["gen_health"], json_data["sleep_time"], json_data["asthma"], json_data["kidney_disease"],
                                     json_data["skin_cancer"])

            response = self.health_record_service.predict_heart_disease(health_record).to_json()
        except:
            response = make_error_message("Error predicting heart disease", status=500)

        return response


class AllHealthRecordAPI(MethodResource, Resource):

    @inject
    def __init__(self, health_record_service: HealthRecordService = Provide[Container.health_record_service]) -> None:
        super().__init__()
        self.health_record_service = health_record_service

    @doc(description='Returns list of all heart disease predictions (health records).', 
         tags=['Get all predictions'])
    @marshal_with(HealthRecordSchema(many=True))
    def get(self):
        return [health_record.to_json() for health_record in self.health_record_service.get_all_health_records()]