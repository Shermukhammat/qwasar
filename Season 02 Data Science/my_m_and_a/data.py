import os
import pandas as pd

def load_data():
    table1 = pd.read_csv("https://storage.googleapis.com/qwasar-public/only_wood_customer_us_1.csv")
    table1.to_csv("only_wood_customer_us_1.csv", index = False)

    table2 = pd.read_csv("https://storage.googleapis.com/qwasar-public/only_wood_customer_us_2.csv", sep = ';')
    table2.to_csv("only_wood_customer_us_2.csv", index = False)

    table3 = pd.read_csv("https://storage.googleapis.com/qwasar-public/only_wood_customer_us_3.csv", sep = '\t', skiprows = 1)
    table3.to_csv("only_wood_customer_us_3.csv", index = False)


def delet_data():
    os.remove('only_wood_customer_us_1.csv')
    os.remove('only_wood_customer_us_2.csv')
    os.remove('only_wood_customer_us_3.csv')
    os.remove('open.csv')
