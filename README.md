GLOF Prediction Demo Model
Welcome to the Glacial Lake Outburst Flood (GLOF) Prediction Demo Model repository. This project is developed as part of the Smart India Hackathon (SIH) 2024, with the goal of predicting potential GLOFs using satellite data and machine learning. GLOFs can have devastating impacts, so early warning systems like this are vital for mitigating risks.

This repository includes two separate demonstration models, showcasing different approaches to GLOF prediction using machine learning techniques.

Project Overview
Glacial Lake Outburst Floods (GLOFs) occur when a dam formed by a glacier fails, releasing vast amounts of water downstream, causing significant damage. Our system analyzes environmental and satellite data to predict such events, giving authorities time to act. This demo represents our initial step in building an accurate early warning system.

Dataset Information
The primary dataset for this project is sourced from NASA's Earthdata platform, containing crucial satellite data required for model training and prediction. Due to the large size of this dataset, we are providing a link for users to download it manually.

Dataset Link:
You can download the dataset from NASA Earthdata using the following link: https://search.earthdata.nasa.gov/search/granules?p=C2559919423-NSIDC_ECS&pg[0][v]=f&pg[0][gsk]=-start_date&fdc=National%20Snow%20and%20Ice%20Data%20Center%20Distributed%20Active%20Archive%20Center%20(NSIDC%20DAAC)!National%20Snow%20and%20Ice%20Data%20Center%20(NSIDC)&tl=1726571921.749!3!!

Please download the specific .h5 file required for this project:

File: ATL03_20240731235234_06802403_006_01.h5
This file contains the satellite data necessary for training and testing the model in datasets.pynb file.
Repository Contents
1. datasets.pynb
This Jupyter Notebook demonstrates a more comprehensive approach to GLOF prediction using a larger dataset. It contains:

Code for data preprocessing, model training, and evaluation.
Instructions to help you extract necessary data from the .h5 file and generate your own .csv file, which can be used for training the model.
The model uses a Random Forest Classifier to predict whether a GLOF is likely to occur (1) or not (0).
Performance metrics like Accuracy, Precision, Recall, and F1-score are included to evaluate the model.
2. main.py
This Python script serves as a lightweight demonstration model, offering a simpler version of GLOF prediction with a small dataset. The script uses a pre-generated .csv file (outputt.csv). Key features include:

Random Forest Classifier used to make predictions based on latitude and longitude data.
Ability to input latitude and longitude interactively for real-time prediction.
The model outputs whether there is a risk of a GLOF at the given location.
3. outputt.csv
The .csv file, containing processed data for the training of the model in main.py
Model Overview
Algorithm:
Both models use the Random Forest Classifier to predict GLOF risks.
Classification:
The models predict binary outcomes: 1 (GLOF risk) or 0 (No GLOF risk).
Evaluation Metrics:
Accuracy: Measures the overall correctness of the model.
Precision: Identifies the percentage of true positive GLOF predictions.
Recall: Captures the sensitivity of the model in identifying GLOF events.
F1-score: Combines precision and recall for a balanced evaluation.
