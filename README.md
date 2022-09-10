# README.md

This repository contains a example of a project based on [Kaggle's Personal Key Indicators of Heart Disease](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease).

# Repository structure and contents # 

**Models (folder):**
* Notebook for the pre-processing of the dataset and training and evaluation of the models.
* Pickle file of the saved models, encoders and scalers (Run notebook to generate necessary pickle files).

**Server (folder):**
* REST API (based on Flask) for doing inference with the trained model and saving results into a database.
* REST API specifications.

**SQL (folder):**
* SQL file for the creation of the MySQL table that stores the inference results, along with the personal key indicators of heart disease.

**Webapp (folder) (To Do):**
* Web application (based on Dash) to interact with the REST API.

  
