import pandas as p

titanic = p.read_csv("titanic.csv")

print("total: ",titanic["survived"].sum())
print("age: ",titanic.groupby("survived")["age"].mean()[1])
print("fare: ",titanic.groupby("survived")["fare"].mean()[1])