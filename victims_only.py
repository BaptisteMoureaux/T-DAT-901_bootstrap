import pandas as p

titanic = p.read_csv("titanic.csv")

print("total: ",titanic["survived"].value_counts()[0])
print("age: ",titanic.groupby("survived")["age"].mean()[0])
print("fare: ",titanic.groupby("survived")["fare"].mean()[0])