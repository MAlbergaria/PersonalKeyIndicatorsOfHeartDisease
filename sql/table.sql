DROP TABLE HealthRecord;

CREATE TABLE HealthRecord (
	id 	INT	NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bmi DECIMAL(5, 2) NOT NULL,
    smoking VARCHAR(3) NOT NULL,
    alcohol_drinking VARCHAR(3) NOT NULL, 
    stroke VARCHAR(3) NOT NULL, 
    physical_health DECIMAL(5, 2) NOT NULL, 
    mental_health DECIMAL(5, 2) NOT NULL,
    diff_walking VARCHAR(3) NOT NULL, 
    sex VARCHAR(10) NOT NULL,
    age_category VARCHAR(30) NOT NULL,
    race VARCHAR(30) NOT NULL,
    diabetic VARCHAR(30) NOT NULL,
    physical_activity VARCHAR(30) NOT NULL, 
    gen_health VARCHAR(15) NOT NULL,
    sleep_time DECIMAL(5, 2) NOT NULL,
    asthma VARCHAR(3) NOT NULL,
    kidney_disease VARCHAR(3) NOT NULL,
    skin_cancer VARCHAR(3) NOT NULL,
    heart_disease VARCHAR(3) NOT NULL
);