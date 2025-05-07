# importing necessary libraries
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import plotly.express as px
from urllib.parse import quote_plus




#coonecting to the database
database = 'customer_segmentation'
username = 'root'
password = quote_plus('Chodrykhan@880')
host = 'localhost'
port = 3306
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Verifying the connectivity to the database
try:
    connection = engine.connect()
    print("Connection to the database was successful.")
except Exception as e:
    print("Error connecting to the database:", e)


# load data from the database
query = "SELECT * FROM customer_orders limit 10;"
df = pd.read_sql(query, engine)
#print(df)

# converting the order_date column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# set today's date as the snapshot date
snapshot_date = df['order_date'].max() + pd.DateOffset(days=1)
# print("Snapshot date:", snapshot_date)


# grouping the data by customer_id and calculating RFM metrics
rfm = df.groupby('customer_id').agg({'order_date': lambda x: snapshot_date - x.max(), 'order_id': 'count', 'total_amount':'sum'}).reset_index()

# renaming the columns
rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']
# print(rfm.head())  


# creating RFM segments
rfm['R'] = pd.qcut(rfm['recency'], 4, labels=[4, 3, 2, 1])
rfm['F'] = pd.qcut(rfm['frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm['M'] = pd.qcut(rfm['monetary'], 4, labels=[1, 2, 3, 4])

# combine to singal score
rfm['RFM_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)
print(rfm.head())


plt.figure(figsize=(10, 6))
sns.countplot(data=rfm, x='RFM_Score', order=rfm['RFM_Score'].value_counts().index)
plt.title('Customer segments by RFM score')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:/Users/hp/Desktop/customer-segmentation-rfm-analysis/graphs/customer_segments.png')
plt.show()
plt.close()

