import pandas as pd

df = pd.read_csv("insurance.csv")

print(df.head())

print(df.describe())
print(df.columns)

df_female = df[df['sex'] == "female"]
df_male = df[df['sex'] == 'male']

print(df_female.head())
print(df_male.head())

print(f'There are {len(df_male)} male data points and {len(df_female)} female datapoints')