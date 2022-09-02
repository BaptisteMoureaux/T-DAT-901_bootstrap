import pandas as p

titanic = p.read_csv("titanic.csv")

# print(titanic.head(10)) # ! first 10 rows
print(titanic["age"].mean()) # ! average of age in the file
print(titanic["age"].isnull().sum()) # ! nb of people with no age specified