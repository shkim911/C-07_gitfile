import pandas as pd
import  openpyxl
df = pd.read_excel("d:/04_python/ju_data.xlsx")
print(df)
df.to_excel("d:/04_python/ju_data2.xlsx", sheet_name = "data1")