import pandas as pd

df = pd.read_csv(r"C:\Users\dines\OneDrive\Documents\python\\dataset\\Sample_ Superstore.csv")
print(df.duplicated().sum())