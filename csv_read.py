print('Start csv uitlezen applicatie')

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r,rij in df.iterrows():
    print (r)
    print (rij["Attack"])


