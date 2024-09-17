GLOF Prediction Demo Model
Welcome to the demo model for Glacial Lake Outburst Flood (GLOF) Prediction, a project developed as part of the Smart India Hackathon (SIH) 2024. This demo serves as a preliminary step toward creating a reliable early warning system aimed at predicting the occurrence of GLOFs. The project leverages satellite data and machine learning to provide predictive insights for potential flood events.

Project Overview
Glacial Lake Outburst Floods (GLOFs) are sudden releases of water from a dammed glacial lake, which can cause catastrophic downstream flooding. To mitigate this threat, we are building a system that analyzes environmental and satellite data to predict such events before they happen. This demo showcases the model’s early-stage performance using real-world satellite data.

Dataset Information
For this demo, we are using satellite data sourced from NASA's Earthdata platform. Since the dataset is large and can't be directly hosted on GitHub, we provide a link for you to download it manually.

Download Dataset
The dataset used for the model can be accessed and downloaded from the following link:

https://search.earthdata.nasa.gov/search/granules?p=C2559919423-NSIDC_ECS&pg[0][v]=f&pg[0][gsk]=-start_date&fdc=National%20Snow%20and%20Ice%20Data%20Center%20Distributed%20Active%20Archive%20Center%20(NSIDC%20DAAC)!National%20Snow%20and%20Ice%20Data%20Center%20(NSIDC)&tl=1726568564.497!3!!
You will need to download the specific .h5 file from this collection:

ATL03_20240731235234_06802403_006_01.h5
This file contains the satellite data required to train the prediction model. The code in this repository will guide you through processing the data.

Repository Contents
datasets.pynb: This Jupyter notebook is the core of our demo. It contains all the code needed to preprocess the data, train the model, and evaluate the results.
Note: We haven’t included the .csv file in this repository due to its large size. However, the notebook includes steps for extracting the necessary data from the .h5 file and generating your own .csv file.
Model Overview
Algorithm: We are using a Random Forest Classifier to make predictions about whether a GLOF is likely to occur.
Classification: The model predicts whether a GLOF will occur (1) or not (0).
Metrics: The performance of the model is evaluated using Accuracy, Precision, Recall, and F1-score to give a complete view of how well it handles predictions.
