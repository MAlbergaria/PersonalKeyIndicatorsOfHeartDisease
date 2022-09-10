from models.healthRecord import HealthRecord


class PredictionsRepository():

    def __init__(self, database) -> None:
        self.__cursor = database.cursor


    def __db_health_record_to_object(self, row):
        return HealthRecord(id=row[0], bmi=float(row[1]), smoking=row[2], alcohol_drinking=row[3], stroke=row[4], 
                            physical_health=float(row[5]), mental_health=float(row[6]), diff_walking=row[7], sex=row[8],
                            age_category=row[9], race=row[10], diabetic=row[11], physical_activity=row[12],
                            gen_health=row[13], sleep_time=float(row[14]), asthma=row[15], kidney_disease=row[16],
                            skin_cancer=row[17], heart_disease=row[18])


    def __get_health_records(self, query):
        self.__cursor.execute(query)

        health_records = []
        for row in self.__cursor:
            health_records.append(self.__db_health_record_to_object(row))

        return health_records


    def add_health_record(self, health_record: HealthRecord):
        query = "INSERT INTO HealthRecord (bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health, \
                                           diff_walking, sex, age_category, race, diabetic, physical_activity, \
						                    gen_health, sleep_time, asthma, kidney_disease, skin_cancer, heart_disease) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        values = (health_record.bmi, health_record.smoking, health_record.alcohol_drinking, health_record.stroke, 
                  health_record.physical_health, health_record.mental_health, health_record.diff_walking, health_record.sex,
                  health_record. age_category, health_record.race, health_record.diabetic, health_record.physical_activity,
                  health_record.gen_health, health_record.sleep_time, health_record.asthma, health_record.kidney_disease,
                  health_record.skin_cancer, health_record.heart_disease)
                  
        self.__cursor.execute(query, *values)
        self.__cursor.execute("SELECT @@IDENTITY")

        for row in self.__cursor:
            health_record.id = int(row[0])

        self.__cursor.commit()

        return health_record

    
    def get_all_health_records(self):
        query = "SELECT * FROM HealthRecord"

        return self.__get_health_records(query)
