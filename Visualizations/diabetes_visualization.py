#!/usr/bin/env python
# coding: utf-8

# # Diabetes Visualization

# In[219]:


#Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

sns.set(style="whitegrid")


# In[221]:


# Load dataset
df = pd.read_csv("Resources/full_cleaned_merged.csv")
df.head()


# In[223]:


# Diabetes class balance
df['Diabetes_binary'].value_counts(normalize=True)


# In[243]:


# Create Copy of dataframe and change values to categories

df2 = df.copy()

# Age
age_map = {
    1: '18 to 24', 2: '25 to 29', 3: '30 to 34', 4: '35 to 39',
    5: '40 to 44', 6: '45 to 49', 7: '50 to 54', 8: '55 to 59',
    9: '60 to 64', 10: '65 to 69', 11: '70 to 74',
    12: '75 to 79', 13: '80 or older'
}
df2['Age'] = data2['Age'].replace(age_map)

# Binary categories
binary_map = {0: 'No', 1: 'Yes'}
binary_columns = [
    'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity',
    'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare',
    'NoDocbcCost', 'DiffWalk'
]
for col in binary_columns:
    df2[col] = df2[col].replace(binary_map)

# Sex
df2['Sex'] = df2['Sex'].replace({0: 'Female', 1: 'Male'})

# Diabetes
df2['Diabetes_binary'] = df2['Diabetes_binary'].replace({0: 'No Diabetes', 1: 'Diabetes'})

# HighBP and HighChol
df2['HighBP'] = df2['HighBP'].replace({0: 'Not High', 1: 'High BP'})
df2['HighChol'] = df2['HighChol'].replace({0: 'Not High', 1: 'High Cholesterol'})

# Cholesterol Check
df2['CholCheck'] = df2['CholCheck'].replace({
    0: 'No Cholesterol Check in 5 Years',
    1: 'Cholesterol Check in 5 Years'
})

# General Health
genhlth_map = {
    5: 'Excellent', 4: 'Very Good', 3: 'Good', 2: 'Fair', 1: 'Poor'
}
df2['GenHlth'] = df2['GenHlth'].replace(genhlth_map)

# Education
education_map = {
    1: 'Never Attended School', 2: 'Elementary', 3: 'Junior High School',
    4: 'Senior High School', 5: 'Undergraduate Degree', 6: 'Masters'
}
df2['Education'] = df2['Education'].replace(education_map)

# Income
income_map = {
    1: 'Less Than $10,000', 2: 'Less Than $10,000', 3: 'Less Than $10,000',
    4: 'Less Than $10,000', 5: 'Less Than $35,000', 6: 'Less Than $35,000',
    7: 'Less Than $35,000', 8: '$75,000 or More'
}
df2['Income'] = df2['Income'].replace(income_map)

#Drop any null values
df2.dropna(inplace=True)

#Preview Data 
df2.head()


# In[245]:


#BMI vs Diabetes status
# Categorize BMI
def bmi_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'

df2['BMI_Category'] = df2['BMI'].apply(bmi_category)

# Stacked bar plot
pd.crosstab(df2['BMI_Category'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='Accent')

plt.title('BMI Category vs Diabetes Status')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[247]:


# Smoking vs Diabetes
pd.crosstab(df2['Smoker'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='Set1')

plt.title('Smoking vs Diabetes Status')
plt.xlabel('Smoker')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[249]:


# Physical Activity vs Diabetes
pd.crosstab(df2['PhysActivity'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='Set2')

plt.title('Physical Activity vs Diabetes Status')
plt.xlabel('Physically Active')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[251]:


#General healh vs Diabetes
pd.crosstab(df2['GenHlth'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='viridis')

plt.title('General Health vs Diabetes Status')
plt.xlabel('General Health')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[253]:


#Blood Pressure vs Diabetes
pd.crosstab(df2['HighBP'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='magma')

plt.title('High Blood Pressure vs Diabetes Status')
plt.xlabel('High Blood Pressure')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[255]:


#Cholestrol vs Diabetes
pd.crosstab(df2['HighChol'], df2['Diabetes_binary']).plot(
    kind='bar', stacked=True, colormap='tab20')

plt.title('High Cholestrol vs Diabetes Status')
plt.xlabel('High Cholestrol')
plt.ylabel('Count')
plt.legend(title='Diabetes Status')
plt.show()


# In[239]:


# Sex vs Diabetes

fig = px.histogram(
    df2,
    x="Sex",
    color="Diabetes_binary",
    barmode="group",
    title="Sex vs Diabetes Status",
    color_discrete_sequence=px.colors.qualitative.Dark2 
)

fig.update_layout(
    xaxis_title="Sex",
    yaxis_title="Count",
    legend_title="Diabetes Status"
)

fig.show()


# In[241]:


#Age vs Diabetes
age_map = {
    1: '18 to 24', 2: '25 to 29', 3: '30 to 34', 4: '35 to 39',
    5: '40 to 44', 6: '45 to 49', 7: '50 to 54', 8: '55 to 59',
    9: '60 to 64', 10: '65 to 69', 11: '70 to 74',
    12: '75 to 79', 13: '80 or older'
}

df['Age'] = df['Age'].map(age_map)

# Define the correct order of age categories
age_order = [
    '18 to 24', '25 to 29', '30 to 34', '35 to 39',
    '40 to 44', '45 to 49', '50 to 54', '55 to 59',
    '60 to 64', '65 to 69', '70 to 74', '75 to 79', '80 or older'
]

# Convert Age to a categorical type with proper order
df['Age'] = pd.Categorical(df['Age'], categories=age_order, ordered=True)

# Remove any rows with missing Age or Diabetes info
df_clean = df[df['Age'].notna() & df['Diabetes_binary'].notna()]

# Plot histogram
fig = px.histogram(
    df_clean,
    x="Age",
    color="Diabetes_binary",
    barmode="group",  # or use 'stack' for stacked bars
    title="Age Category vs Diabetes Status",
    color_discrete_sequence=px.colors.qualitative.Set2,
    category_orders={"Age": age_order}  # Ensures correct sorting
)

fig.update_layout(
    xaxis_title="Age Category",
    yaxis_title="Count",
    legend_title="Diabetes Status"
)

fig.show()


# In[215]:


# Income vs Diabetes

fig = px.histogram(
    df2,
    x='Income',
    color='Diabetes_binary',
    barmode='group',
    title='Income vs Diabetes Status',
    color_discrete_sequence=px.colors.qualitative.Set3
)

fig.update_layout(
    xaxis_title='Income Level',
    yaxis_title='Count',
    legend_title='Diabetes Status'
)

fig.show()


# In[145]:


# Compute correlation matrix on numeric columns
corr = df.corr()

plt.figure(figsize=(12,10))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='Spectral', square=True, cbar=True)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()


# In[ ]:




