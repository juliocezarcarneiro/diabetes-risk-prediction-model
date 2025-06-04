#!/usr/bin/env python
# coding: utf-8

# # Diabetes Visualization

# In[51]:


#Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

sns.set(style="whitegrid")


# In[3]:


# Load dataset
df = pd.read_csv("Resources/full_cleaned_merged.csv")
df.head()


# In[5]:


# Diabetes class balance
df['Diabetes_binary'].value_counts(normalize=True)


# In[9]:


# Create Copy of dataframe and change values to categories

df2 = df.copy()

# Age
age_map = {
    1: '18 to 24', 2: '25 to 29', 3: '30 to 34', 4: '35 to 39',
    5: '40 to 44', 6: '45 to 49', 7: '50 to 54', 8: '55 to 59',
    9: '60 to 64', 10: '65 to 69', 11: '70 to 74',
    12: '75 to 79', 13: '80 or older'
}
df2['Age'] = df2['Age'].replace(age_map)

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


# In[49]:


#BMI vs Diabetes

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

# Apply the function to create a new column
df2['BMI_Category'] = df2['BMI'].apply(bmi_category)

# Count values manually
bmi_diabetes_counts = df2.groupby(['BMI_Category', 'Diabetes_binary']).size().unstack(fill_value=0)

# Order the BMI categories
ordered_bmi = ['Underweight', 'Normal', 'Overweight', 'Obese']
bmi_diabetes_counts = bmi_diabetes_counts.reindex(ordered_bmi)

# Plot
bmi_diabetes_counts.plot(kind='bar', stacked=True, colormap='Accent')

plt.title('BMI Category vs Diabetes Status')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[17]:


# Smoking vs Diabetes
smoking_diabetes_counts = df2.groupby(['Smoker', 'Diabetes_binary']).size().unstack(fill_value=0)

# Plot
smoking_diabetes_counts.plot(kind='bar', stacked=True, colormap='Set1')

plt.title('Smoking vs Diabetes Status')
plt.xlabel('Smoker')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[19]:


# Physical Activity vs Diabetes
physact_diabetes_counts = df2.groupby(['PhysActivity', 'Diabetes_binary']).size().unstack(fill_value=0)

# Plot
physact_diabetes_counts.plot(kind='bar', stacked=True, colormap='Set2')

plt.title('Physical Activity vs Diabetes Status')
plt.xlabel('Physically Active')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[29]:


#General healh vs Diabetes
genhlth_diabetes_counts = df2.groupby(['GenHlth', 'Diabetes_binary']).size().unstack(fill_value=0)

# Reorder the index
ordered_health = ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor']
genhlth_diabetes_counts = genhlth_diabetes_counts.reindex(ordered_health)

# Plot
genhlth_diabetes_counts.plot(kind='bar', stacked=True, colormap='viridis')

plt.title('General Health vs Diabetes Status')
plt.xlabel('General Health')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[25]:


#Blood Pressure vs Diabetes
bp_diabetes_counts = df2.groupby(['HighBP', 'Diabetes_binary']).size().unstack(fill_value=0)

# Plot
bp_diabetes_counts.plot(kind='bar', stacked=True, colormap='tab10')

plt.title('High Blood Pressure vs Diabetes Status')
plt.xlabel('High Blood Pressure')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[27]:


#Cholestrol vs Diabetes
chol_diabetes_counts = df2.groupby(['HighChol', 'Diabetes_binary']).size().unstack(fill_value=0)

# Plot
chol_diabetes_counts.plot(kind='bar', stacked=True, colormap='tab20')

plt.title('High Cholestrol levels vs Diabetes Status')
plt.xlabel('High Cholestrol')
plt.ylabel('Count')
plt.legend(title='Diabetes Status', labels=['No Diabetes', 'Diabetes'])
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[33]:


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


# In[47]:


# Income vs Diabetes
fig = px.histogram(
    df2,
    x='Income',
    color='Diabetes_binary',
    barmode='group',
    title='Income vs Diabetes Status',
    color_discrete_sequence=px.colors.qualitative.Set1
)

fig.update_layout(
    xaxis_title='Income Level',
    yaxis_title='Count',
    legend_title='Diabetes Status'
)

fig.show()


# In[55]:


# Compute correlation matrix
corr = df.corr()

plt.figure(figsize=(12, 10))

# Generate a mask for the upper triangle (optional: hides duplicate info)
mask = np.triu(np.ones_like(corr, dtype=bool))

# Plot heatmap with mask and improved style
sns.heatmap(
    corr,
    annot=True,                 # Show correlation values
    fmt=".2f",                  # Format decimals
    cmap='Spectral',            # Color map
    square=True,                # Make cells square
    linewidths=0.5,             # Add lines between cells
    cbar_kws={"shrink": .8},   # Make color bar smaller
    annot_kws={"size": 10}      # Smaller annotation font
)

plt.title("Correlation Matrix", fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=11)
plt.yticks(rotation=0, fontsize=11)
plt.tight_layout()
plt.show()



# In[ ]:




