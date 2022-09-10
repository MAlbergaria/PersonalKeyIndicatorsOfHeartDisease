from dependency_injector import containers, providers
from pathlib import Path

import joblib

from infra.database import Database
from infra.repositories.predictionsRepository import PredictionsRepository
from services.healthRecordService import HealthRecordService
from utils.utils import get_project_root


class Container(containers.DeclarativeContainer):
    
    __project_root: Path = get_project_root()
    config = providers.Configuration(yaml_files=[str(__project_root / "config.yml")])

    wiring_config = containers.WiringConfiguration(modules=["interfaces.controllers.healthRecordController"])

    #=#=#=#=#=#=#=#=#=#=#=# DATABASES #=#=#=#=#=#=#=#=#=#=#=#

    """ mysql_database = providers.Singleton(
        Database,
        config.databases.mysql_database.cnxn(),
        [config.databases.mysql_database.driver(), 
        config.databases.mysql_database.server(),
        config.databases.mysql_database.db_name(),
        config.databases.mysql_database.uid(),
        config.databases.mysql_database.password()]
    ) """

    mysql_database = providers.Singleton(
        Database,
        "DRIVER={?}; SERVER=?; DATABASE=?; UID=?; PASSWORD=?;",
        ["MySQL ODBC 8.0 ANSI Driver",
        "localhost",
        "results",
        "root",
        "root"]
    )

    #=#=#=#=#=#=#=#=#=#=#=# MODEL AND ENCODERS #=#=#=#=#=#=#=#=#=#=#=#

    classifier = joblib.load(r"models\classifier.pickle")
    bin_encoder = joblib.load(r"models\binary_encoder.pickle")
    min_max_scaler = joblib.load(r"models\min_max_scaler.pickle")

    #=#=#=#=#=#=#=#=#=#=#=# REPOSITORIES AND SERVICES #=#=#=#=#=#=#=#=#=#=#=#

    predictions_repository = providers.Factory(
        PredictionsRepository,
        mysql_database
    )

    health_record_service = providers.Factory(
        HealthRecordService,
        predictions_repository,
        classifier,
        bin_encoder,
        min_max_scaler
    )

    

