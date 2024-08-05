# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "551ae946-0eea-42a6-83b2-30d4890b2e25",
# META       "default_lakehouse_name": "lh_copilot",
# META       "default_lakehouse_workspace_id": "6caa4d3a-14be-48a8-9c5a-a18eac75aea3"
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Fabric Copilot demo
# 
# Source:
# https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FIP%20Release%2FData%20and%20AI%2FFabric%2F1%20%2D%20Upskilling%2F6%20%2D%20Data%20science&viewid=971b6985%2D5ac6%2D47e5%2Da6dc%2D5c0664b149a9&OR=Teams%2DHL&CT=1721299160479&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDA2MTMxODQwOSIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D

# MARKDOWN ********************

# 
# #### Run the cell below to install the required packages for Copilot


# CELL ********************


#Run this cell to install the required packages for Copilot
%pip install https://aka.ms/chat_magics-0.0.0-py3-none-any.whl
%load_ext chat_magics


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC Load bankcustomer_churn.csv from the Files folder into a pandas dataframe. and then print first 5 record

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
df = pd.read_csv('/lakehouse/default/Files/bankcustomerchurn_churn.csv')
print(df.head())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/bankcustomerchurn_churn.csv")
# df now is a Spark DataFrame containing CSV data from "Files/bankcustomerchurn_churn.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
df = pd.read_csv('/lakehouse/lh_copilot/Files/bankcustomer_churn.csv')
print(df.head())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pandas as pd
df = pd.read_csv('/lakehouse/default/Files/bankcustomerchurn_churn.csv')
print(df.head())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# Try this in the Copilot Prompt:
# 
# Load bankcustomer_churn.csv from the Files folder into a pandas dataframe. and then print first 5 record

# CELL ********************

# MAGIC %%code
# MAGIC Delete null values and duplicate values from the df dataframe
# MAGIC Drop columns 'RowNumber', 'CustomerId', 'Surname' from the df dataframe

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC show the data distribution from all features the df dataframe

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.describe()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import matplotlib.pyplot as plt
import seaborn as sns

# Plot distribution of all features in df
for col in df.columns:
    plt.figure(figsize=(8,6))
    sns.histplot(data=df, x=col, kde=True)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC create correlation chart with 'CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Tenure', 'NumofProducts', 'HasCrCard', 'IsActiveMember', 'Existed' features from the df dataframe

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import seaborn as sns
import matplotlib.pyplot as plt

features = ['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Tenure', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'Exited']
corr = df[features].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Chart')
plt.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 7. Feature Engineering

# CELL ********************

# MAGIC %%code
# MAGIC One hot encode Geography and Gender features from df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_encoded = pd.get_dummies(df, columns=['Geography', 'Gender'])

display(df_encoded)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### 8. Model Training and testing

# CELL ********************

# MAGIC %%code
# MAGIC create a Random Forest classification model for customer churn using the 'Exited' feature for predction from the df_encoded dataframe

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = df_encoded.drop('Exited', axis=1)
y = df_encoded['Exited']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
