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
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

%pip install pdfplumber
%pip install openai

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# https://medium.com/@azhar.sayyad6/a-step-by-step-guide-to-parsing-pdfs-using-the-pdfplumber-library-in-python-c12d94ae9f07

# CELL ********************

import pdfplumber

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Open the PDF
with pdfplumber.open("path/to/pdf") as pdf:
    # Extract the text
    text = pdf.extract_text()
    print(text)

    # Extract the data
    tables = pdf.extract_table()
    for table in tables:
        print(table)

    # Extract the images
    images = pdf.get_images()
    for image in images:
        print(image["page_number"])
        with open(f"image_{image['page_number']}.jpg", "wb") as f:
            f.write(image["data"])

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
