import pandas as pd
import numpy as np
from my_ds_babel import csv_to_sql
from data import load_data, delet_data
from cleaner import clear_table1, clear_table2, clear_table3



def my_m_and_a(content_database_1, content_database_2, content_database_3):
    table1 = pd.read_csv(content_database_1)
    table2 = pd.read_csv(content_database_2, names = ['Age', 'City', 'Gender', 'fs_names', 'Email'])
    table3 = pd.read_csv(content_database_3, names = ['Gender', 'fs_names', 'Email', 'Age', 'City', 'Country'])

    table1 = clear_table1(table1)
    table2 = clear_table2(table2)
    table3 = clear_table3(table3)    

    table = pd.concat([table1, table2, table3])
    table.replace(np.nan, 'N/A', inplace=True)

    table.to_csv('open.csv', index = False)
    return table

load_data()
merged_csv = my_m_and_a("only_wood_customer_us_1.csv", "only_wood_customer_us_2.csv", "only_wood_customer_us_3.csv")

csv_content = open('open.csv')
csv_to_sql(csv_content, 'plastic_free_boutique.sql', 'customers')

delet_data()