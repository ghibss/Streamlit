import csv
import os
from datetime import datetime, timedelta

import pandas as pd

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

current_date = start_date
df_tables =pd.read_csv("tables.csv",";")

df_tables = df_tables.dropna(axis=1)
df_tables.index = df_tables['Table Id']
df_tables = df_tables.drop('Table Id',axis=1)
df_tables['State'] = "Free"
df_tables['N_persone'] = 0
folder_name = "data"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

while current_date <= end_date:
    filename = current_date.strftime("%Y-%m-%d") + ".csv"
    file_path = os.path.join(folder_name, filename)
    with open(file_path, "w", newline="") as f:
        df_tables.to_csv(f,index=True)
    current_date += timedelta(days=1)

print("All CSV files have been created in the folder 'data'.")
#%%
