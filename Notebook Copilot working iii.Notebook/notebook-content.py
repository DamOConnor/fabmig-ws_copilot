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
# META       "default_lakehouse_workspace_id": "6caa4d3a-14be-48a8-9c5a-a18eac75aea3",
# META       "known_lakehouses": [
# META         {
# META           "id": "551ae946-0eea-42a6-83b2-30d4890b2e25"
# META         },
# META         {
# META           "id": "f7c0414a-6cfc-41fe-bb26-6d0ff45e10e2"
# META         }
# META       ]
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

# MAGIC %%code
# MAGIC show the data distribution from all features the df dataframe

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
