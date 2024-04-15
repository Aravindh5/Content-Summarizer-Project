# Content Summarizer project
In this project,
I've summarized the review of the audience and other details given by our users based on the business requirements.

# Phases of the Project
# Six Phases of Developing ML-Engineering End-to-End Pipeline
Here, I have explained each and every phase of the project.

# Phase 1: 
Data Ingestion Phase -> Based on the project requirements, we have to adjust the input data configurations in this phase.

# Phase 2: 
Data Validation Phase -> The Ingested Data should be validated, unwanted data should be removed, and 
overall data should be reviewed to move the pipeline into the next phase.

# Phase 3: 
Data Transformation Phase -> Based on the project requirements, the parameters which are given by 
data scientists are executed in this phase. This phase includes the feature engineering.

# Phase 4
Model Training Phase -> After Ingestion, Validation and Transformation, we have to perform the training.
In this phase, we have to decide the training algorithm, training place (Sage Maker, Vertex AI, etc.,).
Depends on the cloud provider and project requirements, we have to decide the configuration.

# Phase 5
Model Monitoring Phase -> Once the model has been trained, we have to monitor the performance of the trained model.
Using this phase, we can decide whether the trained model is feasible for production.

# Phase 6
Prediction -> In this phase, we can create a REST APIs and get the results from the trained model.

# Each Phase's workflow
In each and every phase, we have to do the following 9 steps.
At first do the following steps in the research file (folder) for each phase and then make the functions available for production

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration Manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py
