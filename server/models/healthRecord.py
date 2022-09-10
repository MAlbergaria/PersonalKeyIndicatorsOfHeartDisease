import numpy as np
import pandas as pd

from utils.entity import Entity


class HealthRecord(Entity):

    def __init__(self, bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health, diff_walking,
                 sex, age_category, race, diabetic, physical_activity, gen_health, sleep_time, asthma, 
                 kidney_disease, skin_cancer, heart_disease=None, id=None) -> None:
        super().__init__(id)
        self.bmi = bmi
        self.smoking = smoking
        self.alcohol_drinking = alcohol_drinking
        self.stroke = stroke
        self.physical_health = physical_health
        self.mental_health = mental_health
        self.diff_walking = diff_walking
        self.sex = sex
        self.age_category = age_category
        self.race = race
        self.diabetic = diabetic
        self.physical_activity = physical_activity
        self.gen_health = gen_health
        self.sleep_time = sleep_time
        self.asthma = asthma
        self.kidney_disease = kidney_disease
        self.skin_cancer = skin_cancer
        self.heart_disease = heart_disease


    def convert_for_classifier(self, bin_encoder, min_max_scaler):
        health_record_dict = self.to_json()
        
        yes_no_fields = ["smoking", "alcohol_drinking", "stroke", "diff_walking", 
                         "physical_activity", "asthma", "kidney_disease", "skin_cancer"]

        for field in yes_no_fields:
            health_record_dict[field] = bin_encoder.transform([health_record_dict[field]])[0]

        health_record_dict["sex"] = 0 if health_record_dict["sex"] == "Female" else 1

        continuous_fields = ["bmi", "physical_health", "mental_health", "sleep_time"]
        scale_array = np.array([health_record_dict["bmi"], health_record_dict["physical_health"], 
                       health_record_dict["mental_health"], health_record_dict["sleep_time"]]).reshape(1, -1)

        cont_fields_scaled = min_max_scaler.transform(scale_array)

        for field in continuous_fields:
            health_record_dict[field] = cont_fields_scaled[0][continuous_fields.index(field)]     

        categorical_dict = {'age_category':['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'],
                   'race': ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'],
                   'diabetic': ['No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'],
                   'gen_health': ['Excellent', 'Fair', 'Good', 'Poor', 'Very good']}

        for field in categorical_dict:
            values = categorical_dict[field]
            index = values.index(health_record_dict[field])
            array = np.zeros([len(values)], dtype = int)
            array[index] = 1
            health_record_dict[field] = array

        classifier_input = [health_record_dict['bmi'], health_record_dict['smoking'], health_record_dict['alcohol_drinking'],
                            health_record_dict['stroke'], health_record_dict['physical_health'], health_record_dict['mental_health'],
                            health_record_dict['diff_walking'], health_record_dict['sex'], health_record_dict['physical_activity'],
                            health_record_dict['sleep_time'], health_record_dict['asthma'], health_record_dict['kidney_disease'],
                            health_record_dict['skin_cancer']]

        classifier_input = classifier_input + health_record_dict['age_category'].tolist() + health_record_dict['race'].tolist() + \
                           health_record_dict['diabetic'].tolist() + health_record_dict['gen_health'].tolist()

        return [classifier_input]
