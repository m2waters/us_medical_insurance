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

correlation_matrix_male = df_male.corr()
correlation_matrix_female = df_female.corr()


figure, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

sns.heatmap(correlation_matrix_male, annot=True, cmap='coolwarm', ax=ax1)
ax1.set_title('Correlation Matrix for Male US healthcare charges')

sns.heatmap(correlation_matrix_female, annot=True, cmap='coolwarm', ax=ax2)
ax2.set_title('Correlation Matrix for Female US healthcare charges')

plt.show()



print(correlation_matrix_male)