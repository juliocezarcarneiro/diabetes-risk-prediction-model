![Early Diabetes Risk Prediction Model](assets/banner.svg)

# Early Diabetes Risk Prediction Model

**A Random Forest model trained on 253,680 CDC survey responses flags people at high diabetes risk with 91% accuracy, deployed as a live web app.**

![Python](https://img.shields.io/badge/Python-1F4E79?style=flat-square&logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1F4E79?style=flat-square&logo=scikitlearn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-1F4E79?style=flat-square) ![Tableau](https://img.shields.io/badge/Tableau-1F4E79?style=flat-square&logo=tableau&logoColor=white) ![Gradio](https://img.shields.io/badge/Gradio-1F4E79?style=flat-square)

**[Try the live demo](https://juliocarneiro-diabetes-risk-predictor.hf.space/)** · **[Tableau dashboard](https://public.tableau.com/app/profile/shahab.eshghifard/viz/Book1_17491728312230/ExploringDiabetesRiskFactors)** · **[Presentation (PDF)](Early%20Diabetes%20Risk%20Prediction%20Presentation.pdf)**

---

## Business problem

Diabetes is often diagnosed late, when prevention is harder and care is more expensive. Health planners need a simple way to identify people at higher risk from everyday health and lifestyle information, so they can focus screening and prevention.

## Approach

1. **Data:** CDC Behavioral Risk Factor Surveillance System (BRFSS) 2015, via Kaggle: 253,680 responses with BMI, activity, smoking, alcohol, blood pressure, cholesterol, age, sex and income.
2. **Clean and merge** the three dataset versions (`Resources/`).
3. **Explore** each risk factor against diabetes status (`Visualizations/`).
4. **Model and compare:** Logistic Regression, Random Forest, XGBoost and a neural network, scored on accuracy, precision, recall and F1.
5. **Tune** the best model (Random Forest).
6. **Deploy** the final model as an interactive Gradio app that returns a Low or High risk level.

## Key findings

| Metric | Result |
|---|---:|
| Best model | Random Forest |
| Accuracy | 91% |
| No diabetes: precision / recall | 0.93 / 0.95 |
| Diabetes: precision / recall | 0.82 / 0.76 |

**Strongest predictors of risk:** BMI, age category, general health status, income level and high blood pressure.

The model catches about 3 in 4 people with diabetes (recall 0.76). For a screening tool, that recall is the number to improve first, since a missed case costs more than a false alarm.

## Visuals

| | |
|---|---|
| ![BMI vs diabetes](Visualizations/bmi%20vs%20diabetes.png) | ![Age vs diabetes](Visualizations/age%20vs%20diabetes.png) |
| ![General health vs diabetes](Visualizations/general%20health%20vs%20diabetes.png) | ![Blood pressure vs diabetes](Visualizations/blood%20pressure%20vs%20diabetes.png) |

<details>
<summary>More risk factors: income, cholesterol, physical activity, smoking, gender</summary>

![Income vs diabetes](Visualizations/income%20vs%20diabetes.png)
![Cholesterol vs diabetes](Visualizations/cholesterol%20vs%20diabetes.png)
![Physical activity vs diabetes](Visualizations/physical%20activity%20vs%20diabetes.png)
![Smoking vs diabetes](Visualizations/smoking%20vs%20diabetes.png)
![Gender vs diabetes](Visualizations/gender%20vs%20diabetes.png)

</details>

## How to run

```bash
git clone https://github.com/juliocezarcarneiro/diabetes-risk-prediction-model.git
cd diabetes-risk-prediction-model
pip install -r requirements.txt
jupyter notebook
```

Run `Resources/` notebooks first (cleaning and merging), then the models in `Machine_Learning_Models/`, then `diabetes_risk_predictor.ipynb` for the final model and Gradio app.

## Folder structure

```text
diabetes-risk-prediction-model/
├── Resources/                    # raw BRFSS data, cleaning and merging notebooks
├── Machine_Learning_Models/      # logistic regression, random forest, XGBoost, neural network, comparison
├── Visualizations/               # risk factor charts
├── diabetes_risk_predictor.ipynb # final model + Gradio app
└── Early Diabetes Risk Prediction Presentation.pdf
```

## Team

Anqa Javed, Humaira Enayetullah, Julio Carneiro, Shahab Eshghifard
University of Toronto Data Analytics Bootcamp

**Data:** [Diabetes Health Indicators Dataset (Kaggle)](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset), from the CDC BRFSS 2015 survey.

## Contact

**Julio Carneiro** · Data Analyst · Toronto, ON
[LinkedIn](https://www.linkedin.com/in/juliocezarcarneiro/) · [Portfolio](https://github.com/juliocezarcarneiro) · [Email](mailto:juliocezarcarneiro@outlook.com)
