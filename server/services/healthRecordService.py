

class HealthRecordService():

    def __init__(self, predictions_repository, classifier, bin_encoder, min_max_scaler) -> None:
        self.predictions_repository = predictions_repository
        self.classifier = classifier
        self.bin_encoder = bin_encoder
        self.min_max_scaler = min_max_scaler

    
    def predict_heart_disease(self, health_record):
        health_record_classifier_input = health_record.convert_for_classifier(self.bin_encoder, self.min_max_scaler)
        heart_disease_prediction = self.classifier.predict(health_record_classifier_input)

        health_record.heart_disease = "No" if heart_disease_prediction == 0 else "Yes"

        return self.predictions_repository.add_health_record(health_record)


    def get_all_health_records(self):
        return self.predictions_repository.get_all_health_records()
    