import pandas as pd
import numpy as np

def clear_gender(df_table, column = 'Gender'):
    """
      params:
          df_table: DataDrame
          column : str
    """
    df_table.loc[df_table[column] == '1', column] = 'Female'
    df_table.loc[df_table[column] == '0', column] = 'Male'

    df_table.loc[df_table[column] == 'F', column] = 'Female'
    df_table.loc[df_table[column] == 'M', column] = 'Male'

    return df_table


def clear_name(df_table, column = None):
    df_table.loc[:, column] = df_table[column].astype(str).str.replace('"', '',  regex = True)
    df_table.loc[:, column] = df_table[column].astype(str).str.replace("'", '',  regex = True)
    df_table.loc[:, column] = df_table[column].astype(str).str.replace("\\", '',  regex = True)

    df_table.loc[:, column] = df_table[column].str.lower()
    df_table.loc[:, column] = df_table[column].str.title()

    return df_table


def clear_city(df_table, column = 'City'):
    """
      params:
          df_table: DataDrame
          column : str
    """
    df_table.loc[:, column] = df_table[column].astype(str).str.replace('-', ' ',  regex = True)
    df_table.loc[:, column] = df_table[column].astype(str).str.replace('_', ' ',  regex = True)

    df_table.loc[:, column] = df_table[column].str.lower()
    df_table.loc[:, column] = df_table[column].str.title()

    return df_table


def drop_dunder(df_table, drop_words = [], table = 'Gender'):
    for drop in drop_words:
        df_table.loc[:, table] = df_table[table].astype(str).str.replace(drop, '')
    return df_table


def clear_table1(table1):
    """
      params:
          table1 : DataFrame
    """
    table1 = clear_gender(table1)

    table1 = clear_name(table1, column = 'FirstName')
    table1 = clear_name(table1, column = 'LastName')
    table1 = clear_city(table1, column = 'City')

    table1.loc[:, 'Email'] = table1['Email'].astype(str).str.lower()
    table1['Country'] = 'USA'

    return table1


def clear_table2(table2):
    table2.loc[:, 'Age'] = table2['Age'].astype(str).str.replace(r'[a-z]+', '', regex=True)
    
    table2 = clear_city(table2, column = 'City')
    table2 = clear_gender(table2, column = 'Gender')

    table2.loc[:, 'Email'] = table2['Email'].astype(str).str.lower()

    split = table2['fs_names'].str.split(expand = True)
    table2 = table2.drop('fs_names', axis = 1)
    table2['FirstName'] = split[0]
    table2['LastName'] = split[1]

    table2 = clear_name(table2, column = 'FirstName')
    table2 = clear_name(table2, column = 'LastName')

    table2['Country'] = 'USA'
    table2['UserName'] = np.nan

    return table2[['Gender', 'FirstName', 'LastName', 'UserName', 'Email', 'Age', 'City', 'Country']]


def clear_table3(table3):
    table3['Country'] = 'USA'

    table3 = drop_dunder(table3, table = 'Gender', drop_words = ['string_', 'boolean_', 'character_'])
    table3 = clear_gender(table3, column = 'Gender')

    table3 = drop_dunder(table3, table = 'fs_names', drop_words = ['string_', 'boolean_', 'character_'])
    split = table3['fs_names'].astype(str).str.split(expand = True)
    table3 = table3.drop('fs_names', axis = 1)
    table3['FirstName'] = split[0]
    table3['LastName'] = split[1]

    table3 = clear_name(table3, column = 'FirstName')
    table3 = clear_name(table3, column = 'LastName')

    table3 = drop_dunder(table3, table = 'City', drop_words = ['string_', 'boolean_', 'character_'])
    table3 = clear_city(table3, column = 'City')

    table3 = drop_dunder(table3, table = 'Email', drop_words = ['string_', 'boolean_', 'character_'])
    table3.loc[:, 'Email'] = table3['Email'].astype(str).str.lower()

    table3 = drop_dunder(table3, table = 'Age', drop_words = ['integer_'])
    table3.loc['Age'] = table3['Age'].str.replace(r'[a-z]+', '', regex=True)

    table3['UserName'] = np.nan

    return table3[['Gender', 'FirstName', 'LastName', 'UserName', 'Email', 'Age', 'City', 'Country']]


