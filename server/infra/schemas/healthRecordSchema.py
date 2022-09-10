from marshmallow import Schema, fields

class HealthRecordSchema(Schema):

    id = fields.Int(dump_only=True)
    bmi = fields.Float()
    smoking = fields.String()
    alcohol_drinking = fields.String()
    stroke = fields.String()
    physical_health = fields.Float()
    mental_health = fields.Float()
    diff_walking = fields.String()
    sex = fields.String()
    age_category = fields.String()
    race = fields.String()
    diabetic = fields.String()
    physical_activity = fields.String()
    gen_health = fields.String()
    sleep_time = fields.Float()
    asthma = fields.String()
    kidney_disease = fields.String()
    skin_cancer = fields.String()
    heart_disease = fields.String(dump_only=True)


    """ {
        "age_category": "55-59",
        "alcohol_drinking": "No",
        "asthma": "Yes",
        "bmi": 16.6,
        "diabetic": "Yes",
        "diff_walking": "No",
        "gen_health": "Very good",
        "heart_disease": "No",
        "id": 1,
        "kidney_disease": "No",
        "mental_health": 30.0,
        "physical_activity": "Yes",
        "physical_health": 3.0,
        "race": "White",
        "sex": "Female",
        "skin_cancer": "Yes",
        "sleep_time": 5.0,
        "smoking": "Yes",
        "stroke": "No"
    } """