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
- Python: Pandas, Numpy, Scikit-learn, Matplotlib, Seaborn, XGBoost
- Visualization: Plotly, Tableau
- Deployment: Gradio
- Development Environment: Jupyter Notebook, Google Colab

## 📈 Results & Insights
- Best model: Random Forest Classifier with 91% accuracy
- Class-wise performance:
  - Class 0 (No Diabetes): Precision = 0.93 | Recall = 0.95
  - Class 1 (Diabetes): Precision = 0.82 | Recall = 0.76
- Key Predictive Features to indentify risk of diabetes:
  - BMI
  - Age category
  - General health status
  - Income level
  - High blood pressure
- The model identifies individuals at risk of diabetes based on lifestyle and health attributes, promoting personalized risk management and preventive care.

##  🧪 Deployment
- The trained model is deployed using Gradio.
- Users can input their health information and receive a diabetes risk level (Low/High) prediction.
🔗 Try the live demo

## 🚀 Future Enhancements
- Integrate additional features (e.g., dietary patterns, genetics, medication).
- Improve deployment with cloud-based hosting.
- Explore more advanced models or ensemble methods.

## 👥 Authors
Anqa Javed, Humaira Enayetullah, Julio Carneiro, Shahab Eshghifard  
*University of Toronto Data Analytics Bootcamp*

## 📌 References
- [Kaggle Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)


**Live access**
-[Demo](https://juliocarneiro-diabetes-risk-predictor.hf.space/)
-[Tableau](https://public.tableau.com/app/profile/shahab.eshghifard/viz/Book1_17491728312230/ExploringDiabetesRiskFactors)
