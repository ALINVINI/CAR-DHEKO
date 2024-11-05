Car Dekho Project: Used Car Price Prediction
Project Overview

This project aims to predict the prices of used cars using a machine learning pipeline that includes data cleaning, visualization, model training, and hyperparameter tuning. The project uses a dataset of 8,400 data points and features such as fuel type, body type, mileage, engine, and more to develop an effective predictive model.
Table of Contents

    Project Overview
    Data Description
    Data Cleaning
    Data Visualization
    Machine Learning Models
    Hyperparameter Tuning
    Model Evaluation
    Results
    Conclusion
    Future Work

Data Description

The dataset consists of 8,400 data points with features including:

    Fuel Type (ft)
    Body Type (bt)
    Kilometers Driven (km)
    Transmission
    Owner Number (ownerNo)
    Model
    Model Year
    Mileage
    Engine
    Seats
    City

Data Cleaning

To ensure high-quality data for model training, the following data cleaning steps were performed:

    Handling Missing Values: Imputed missing data using appropriate techniques (e.g., mean, median, or mode imputation).
    Removing Duplicates: Identified and removed duplicate entries.
    Outlier Detection: Analyzed distributions and handled outliers using statistical methods to reduce noise.
    Feature Encoding: Categorical features were encoded using one-hot encoding or label encoding where applicable.
    Scaling: Numerical features were standardized using StandardScaler to improve model performance.

Data Visualization

Data visualization played a key role in understanding data distribution and relationships between features:

    Correlation Heatmap: Displayed correlations among numerical features.
    Box Plots: Highlighted outliers and distribution for continuous variables.
    Histograms and Bar Charts: Showed the frequency distribution of categorical features.
    Scatter Plots: Illustrated relationships between features such as Mileage, Engine size, and Price.

Machine Learning Models:

Multiple machine learning models were implemented and evaluated:

    Linear Regression
    Decision Tree Regressor
    Random Forest Regressor
    Gradient Boosting Regressor
    XGBoost Regressor

Hyperparameter Tuning:

To optimize model performance, hyperparameter tuning was carried out using techniques like GridSearchCV

Model Evaluation:

Model Performance Summary

Model	R-squared Accuracy

Linear Regression	92%
Decision Tree Regressor	83%
Random Forest Regressor	91%
Gradient Boosting Regressor	90%
XGBoost Regressor	94%

Results: 
Though XGBoost shows greater accuracy,I opted for Linear regression based on the following criteria,

1. Simplicity and Interpretability
2. Computational Efficiency
3. Generalizability
4. Maintenance and Scalability
5. Client Priorities
6. Robustness to Outliers
    

Conclusion

The project successfully built a robust pipeline for predicting the price of used cars, with the LINEAR REGRESSION MODEL showing the best results after hyperparameter tuning.Deployed the model using Streamlit for user-friendly interaction.

Future Work:

    Integrate additional features like car condition and service history.
    
    Explore deep learning techniques for further improvements.
