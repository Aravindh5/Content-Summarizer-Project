# Content Summarizer project
In this project,
I've summarized the review of the audience and other details given by our users based on the business requirements.

# Phases of the Project
# Six Phases of Developing ML-Engineering End-to-End Pipeline
Here, I explain each and every phase of the project.

# Phase 1: 
Data Ingestion Phase -> Based on the project requirements, we have to adjust the input data configurations in this 
phase.

# Phase 2: 
Data Validation Phase -> The Ingested Data should be validated, unwanted data should be removed, and 
overall data should be reviewed to move the pipeline into the next phase.

# Phase 3: 
Data Transformation Phase -> Based on the project requirements, the parameters which are given by 
data scientists are executed in this phase. This phase includes the feature engineering.

# Phase 4
Model Training Phase -> After Ingestion, Validation and Transformation, we have to perform the training.
In this phase, we have to decide the training algorithm, training place (Sage Maker, Vertex AI, EC2, etc.,).
Depends on the cloud provider and project requirements, we have to decide the configuration.

# Phase 5
Model Monitoring Phase -> Once the model has been trained, we have to monitor the performance of the trained model.
Using this phase, we can decide whether the trained model is feasible for production.

# Phase 6
Prediction -> In this phase, we can create a REST APIs and get the results from the trained model.

# Each Phase's workflow
In each and every phase, we have to do the following 8 steps.
At first do the following steps in the research file (folder) for each phase and then make the functions available 
for production

# 1. Update config.yaml
# 2. Update params.yaml
# 3. Update entity
# 4. Update the configuration Manager in src config
# 5. Update the components
# 6. Update the pipeline
# 7. Update the main.py
# 8. Update the app.py

## How to run?
# STEPS:

# Clone the repository

```bash
https://github.com/Aravindh5/Content-Summarizer-Project.git
```
# STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.9 -y
```

```bash
conda activate summary
```


# STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```


```bash
open up you local host and port
```


```bash
Author: Aravindh
Designation: AI/ML Engineer
Email: Ktaravindh005@gmail.com
```


## GCP-CICD-Deployment-with-GitHub-Actions

## 1. Login to Google Cloud Console.

## 2. Create a Service Account for Deployment
# IAM Role and Permissions:

    Grant the service account specific access:
        Google Compute Engine (GCE) access for creating and managing virtual machines.
        Google Container Registry (GCR) access to store Docker images.
    Description: 
        Define the purpose of the service account, emphasizing deployment tasks.

# Policy:

    roles/compute.instanceAdmin: Grants permissions to create and manage Compute Engine instances.
    roles/storage.admin: Provides full control over Cloud Storage resources for Docker image storage.

## 3. Create a Google Container Registry (GCR) Repository
    Save the Registry URI: Store the URI (gcr.io/project-id/repository-name) for later use.

## 4. Create a Compute Engine Instance (Ubuntu)

## 5. Connect to the Compute Engine Instance and Install Docker

# Update and upgrade existing packages (optional)
```bash    
sudo apt-get update -y
sudo apt-get upgrade -y
```

# Install Docker
```bash    
sudo apt-get install -y docker.io
```

# Add current user to the docker group
```bash    
sudo usermod -aG docker $(whoami)
```

# Restart the Compute Engine Instance:
```bash
sudo reboot
```

## 6. Configure Compute Engine as a Self-Hosted Runner
    Follow GitHub Actions documentation to set up a self-hosted runner on the Compute Engine instance.

## 7. Set Up GitHub Secrets
    In your GitHub repository settings, navigate to Secrets and add the following environment variables:
        GCP_PROJECT_ID: YOUR GOOGLE CLOUD PROJECT ID.
        GCP_SERVICE_KEY: Base64-encoded JSON key file for the service account.
        GCR_REGION: Region where your GCR repository is located (e.g., us-central1).
