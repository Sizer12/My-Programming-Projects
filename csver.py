
import pandas as pd

read_file = pd.read_excel (r'C:/Users/inci1/Desktop/liste.xlsx')
read_file.to_csv (r'C:/Users/inci1/Desktop/liste.csv', index = None, header=True,)