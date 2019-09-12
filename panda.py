import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('https://gist.githubusercontent.com/jwalsh/ce1dc0436aba5b7a5c9666f47fa5a380/raw/5ce3854392b43ff97907112d344fc008229b0445/titanic.csv')

#print(df.info())
#print(df.columns)
#print(df[['Survived', 'Age', 'SibSp', 'Fare']].describe())
# df['Died'] = df['Survived'] - 1
# df['AgeMultiplied'] = df['Age'].apply(lambda x: x*2)
# print(df[df['Survived'] > 0][['Survived', 'Age', 'SibSp', 'Fare', 'AgeMultiplied']].describe())

# df['Age'].plot('hist')
# plt.show()
#df.to_json('test.json')

# print(df.dropna(how='all').count()) #dropna возвращает почищенный от пустых значений список
# print(df.fillna(method='ffill')) #заполняет пустые значения
#print(df.dropna().count())
df = df.groupby('Sex')
print(df['Survived'].describe())



