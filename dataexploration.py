import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("insurance.csv")

print(df.head())
print(df.describe())
print(df.columns)

df.loc[df['smoker'] == 'no', 'smoker'] = 0
df.loc[df['smoker'] == 'yes', 'smoker'] = 1

df['region'].replace({'northeast' : 1, 'northwest': 2, 'southeast': 3, 'southwest': 4}, inplace=True)
## Northeast = 1; Northwest=2; Southeast=3; Southwest=4

print(df['region'].unique())

df_female = df[df['sex'] == "female"].reset_index(drop=True)
df_male = df[df['sex'] == 'male'].reset_index(drop=True)

df_male.drop("sex", axis=1, inplace=True)
df_female.drop("sex", axis=1, inplace=True)

print(df_female.head())
print(df_male.head())


print(f'There are {len(df_male)} male data points and {len(df_female)} female datapoints')

correlation_matrix = df_male.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix for US healthcare charges')
plt.show()

print(correlation_matrix)