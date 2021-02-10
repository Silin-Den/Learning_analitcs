import pandas as pd

s = pd.read_csv('titanic.csv', sep=',')
print(s.head(15))
