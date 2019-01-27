import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
sns.set(style="ticks", color_codes=True)

def priceAgainstBedrooms(df):
    print(len(df))
    bedroom_price = defaultdict(int)
    bedroom_count = defaultdict(int)
    room_size = []
    room_price = []

    for index, row in df.iterrows():
        bedroom = row["bedrooms"]
        price = row["price"]

        totalPrice = bedroom_price[bedroom] + price
        bedroom_price[bedroom] = totalPrice
        bedroom_count[bedroom] = bedroom_count[bedroom] + 1
    
    for key, value in bedroom_count.iteritems():
        if key < 10:
            totalprice = bedroom_price[value]
            totalCount = value
            averagePrice = int(totalPrice/totalCount)
            print(averagePrice)
            room_size.append(key)
            room_price.append(averagePrice)
            print(str(key) + " : " + str(averagePrice))
        
    plt.bar(room_size, room_price, align='center', alpha=0.5)
    plt.xticks(room_size, room_size)
    plt.ylabel('House Price')
    plt.title('Number of bedrooms against the house price')
    plt.show()


df = pd.read_csv("kc_house_data.csv")

print(df.columns)
print(df.head())
print(df.describe())

#Visualizing the data
# print(sns.pairplot(df, 
#              x_vars=["sqft_above", "sqft_living", "sqft_lot", "sqft_basement"], 
#              y_vars=["price"],
#              hue = "bedrooms"
#              )
# )
priceAgainstBedrooms(df)
