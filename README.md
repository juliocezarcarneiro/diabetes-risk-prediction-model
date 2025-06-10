# Early Diabetes Risk Prediction Model

## 📌 Overview
This project develops a machine learning model to predict an individual's risk of diabetes using health indicator data from the CDC’s Behavioral Risk Factor Surveillance System (BRFSS). The model aims to support early intervention and healthcare planning by identifying high-risk individuals.

## 🎯 Goals
- Predict diabetes risk using classification models (Logistic Regression, Random Forest, XGBoost).
- Evaluate model performance using metrics like accuracy, precision, recall, and F1-score.
- Identify key health factors contributing to diabetes risk.
- Deploy the final model as an interactive app using Gradio.

## 📊 Dataset
- **Source**: [Diabetes Health Indicators Dataset (Kaggle)](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
- **Records**: 253,680 survey responses
- **Target**: `Diabetes_binary`
- **Features**: BMI, physical activity, smoking, alcohol consumption, high blood pressure, cholesterol, age category, sex, etc.


## 🛠️ Tools and Technologies
- Python: pandas, numpy, scikit-learn, matplotlib, seaborn, XGBoost
- Visualization: Plotly, Tableau
- Deployment: Gradio
- Development Environment: Jupyter Notebook, Google Colab

## 📝 Evaluation Metrics and Finding
- Random Forest Classification Model:
No Diabetes (0) - precision = 0.93, recall =  0.95 
Diabetes (1)- precision = 0.82 , recall = 0.76
-  Overall model accuracy is 91%
- The model effectively identifies key health indicators contributing to diabetes risk, enabling personalized risk assessment.
- The interactive app allows users to input their health information and receive immediate, actionable diabetes risk scores.
- This approach supports early detection and promotes proactive health management.

## 🚀 Future Enhancements
- Integrate additional features (e.g., dietary patterns, medication).
- Improve deployment with cloud-based hosting.
- Explore more advanced models or ensemble methods.

## 👥 Authors
Anqa Javed, Humaira Enayetullah, Julio Carneiro, Shahab Eshghifard  
*University of Toronto Data Analytics Bootcamp*

## 📌 References
- [Kaggle Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)
