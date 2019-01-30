import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sns.set(style="ticks", color_codes=True)
df = pd.read_csv("kc_house_data.csv")

print(df.columns)
print(df.head())
print(df.describe())

# Visualizing the data
print(sns.pairplot(df, 
             x_vars=["sqft_above", "sqft_living", "sqft_lot", "sqft_basement"], 
             y_vars=["price"],
             hue = "bedrooms"
             )
)


X = df[['sqft_living']]
y = df[['price']]



# Splitting the dataset into train and validation sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)


print(str(len(X_train)) + " " + str(len(y_train)))
print(str(len(X_test)) + " " + str(len(y_test)))

#Training a Linear Regression Model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# Fitting the training data to our model
regressor.fit(X_train, y_train)

# Predicting price for the Validation set
y_pred = regressor.predict(X_test)

# Scoring the model
from sklearn.metrics import r2_score, mean_squared_error

# R2 score closer to 1 is a good model
print("R2 score:")
print(r2_score(y_test, y_pred))

# MSE score closer to zero is a good model
#print(f"MSE score: {mean_squared_error(y_test, y_pred)}")