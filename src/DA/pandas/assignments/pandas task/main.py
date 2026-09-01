import pandas as pd
from preprocessing import Read_data_file, Drop_unnecessary_features, Check_data_type
from config import cols_to_drop 

file_path = "/home/sandosa/Desktop/Depi-Ai/CA-R5-S2S2-AI-/src/DA/pandas/assignments/pandas task/Titanic.csv"
df = Read_data_file(file_path)

df = Drop_unnecessary_features(df, cols_to_drop)

df = Check_data_type(df)

print(df)
