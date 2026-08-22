import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

#Inspect data
print("/...inspect data.../")
df = pd.read_csv(url)
print(df.info())
print(df.describe())


#handle missing data 
print("/...handle missing data.../")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])


#remove duplication
print("/...remove duplication.../")
df = df.drop_duplicates()

#filter data :passenger in fist class
print("/...filter data : passenger in fist class.../")
first_class = df[df["Pclass"]==1]
print("First Class: ",first_class.head())

#bar code : servival by class
print("/...#bar code : servival by class.../")
grouped = df.groupby("Pclass")["Survived"].mean()
grouped.plot(kind="bar",color="skyblue")
plt.title("first class")
plt.show()

#Histogram : Age distribution
print("/...histogram : Age distribution.../")
sns.histplot(df["Age"],kde = True,color="blue",bins =20)
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Frequence")
plt.show()

#Scatter plot :Age vs fare
print("/...Scatter plot :Age vs fare.../")
plt.scatter(df["Age"],df["Fare"],color = "red",alpha=1 ,marker="X" )
plt.title("Age vs Fare")
plt.show()