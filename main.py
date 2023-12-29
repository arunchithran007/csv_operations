import pandas as pd 

df = pd.read_csv("input.csv")

df = df.drop_duplicates()

