import pandas as pd

df = pd.read_csv("dataset/UNSW_NB15.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.shape)