from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
calf_houses = fetch_california_housing()
#print(calf_houses.feature_names)
df  = pd.DataFrame(calf_houses.data,columns=calf_houses.feature_names)
df["price"] = calf_houses.target
df.to_csv("california.csv")
#print(df.describe())


#q1
q1_price = df["price"].quantile(0.25)
#q2
# print(df["price"].median())
#q3
q3_price = df["price"].quantile(0.75)
iqr_price= q3_price-q1_price

#q1
q1_house = df["HouseAge"].quantile(0.25)
#q2
# print(df["price"].median())
#q3
q3_house= df["HouseAge"].quantile(0.75)

iqr_house= q3_house-q1_house
print(iqr_house)
print(iqr_price)
