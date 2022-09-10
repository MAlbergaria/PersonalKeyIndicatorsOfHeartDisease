from .controllers.healthRecordController import *


class Routes():

    def __init__(self, api) -> None:
        self.setupHealthRecordControllerRoutes(api)


    def setupHealthRecordControllerRoutes(self, api, base_url="/predict") -> None:
        # Predict Heart Disease (Add to database)
        api.add_resource(AddHealthRecordAPI, base_url + "/")
        # Get all health records (predictions)
        api.add_resource(AllHealthRecordAPI, base_url + "/")