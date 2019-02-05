import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from uszipcode import SearchEngine
sns.set(style="ticks", color_codes=True)

def findState(df):
    search = SearchEngine()
    for index, row in df.iterrows():
        view = row['view']
        zipcode = row['zipcode']
        zipcode = search.by_zipcode(zipcode)
        print(str(zipcode))
        print("")


df = pd.read_csv("kc_house_data.csv")

print(df.columns)
print(df.head())
print(df.describe())

findState(df)