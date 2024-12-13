import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import uuid
from patient import patient

df = pd.read_csv("insurance.csv")

uuids = [str(uuid.uuid4()) for x in range(len(df))]
df.insert(1, "uuid", uuids, False)


print(df.head())
print(df.describe())
print(df.columns)

test_subject_one = patient(
    df["uuid"][0],
    df['age'][0],
    df['sex'][0],
    df['bmi'][0],
    df['children'][0],
    df['smoker'][0],
    df['region'][0],
    df['charges'][0],
)

df.loc[df['smoker'] == 'no', 'smoker'] = 0
df.loc[df['smoker'] == 'yes', 'smoker'] = 1

df['region'].replace({'northeast' : 1, 'northwest': 2, 'southeast': 3, 'southwest': 4}, inplace=True)
## Northeast = 1; Northwest=2; Southeast=3; Southwest=4

print(df['region'].unique())

df_female = df[df['sex'] == "female"].reset_index(drop=True)
df_male = df[df['sex'] == 'male'].reset_index(drop=True)

df_male_corr = df_male.drop(["sex", "uuid"] , axis=1)
df_female_corr = df_female.drop(["sex", "uuid"], axis=1)

print(df_female.head())
print(df_male.head())


print(f'There are {len(df_male)} male data points and {len(df_female)} female datapoints')

correlation_matrix_male = df_male_corr.corr()
correlation_matrix_female = df_female_corr.corr()


figure, (ax1, ax2) = plt.subplots(ncols=2, figsize=(15, 5))

sns.heatmap(correlation_matrix_male, annot=True, cmap='coolwarm', ax=ax1)
ax1.set_title('Correlation Matrix for Male US healthcare charges')

sns.heatmap(correlation_matrix_female, annot=True, cmap='coolwarm', ax=ax2)
ax2.set_title('Correlation Matrix for Female US healthcare charges')

plt.show()



print(correlation_matrix_male)