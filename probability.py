import pandas as p
import numpy as np

titanic = p.read_csv("titanic.csv")
age_groups = p.cut(titanic['age'], bins=[0, 9, 19, 35, 45, 55, 65, np.inf])
print("--------- % of survivor by : ---------")
print(titanic.groupby("sex")["survived"].mean())
print("--------------------------------------")
print(titanic.groupby("pclass")["survived"].mean())
print("--------------------------------------")
# print(titanic.groupby("age")["survived"].mean()) # Age range too wide, unusable
print(titanic.groupby(age_groups)["survived"].mean()) # Age range too wide, unusable
