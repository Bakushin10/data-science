import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import operator

sns.set(style="ticks", color_codes=True)

def findMostVisitedLoc(df):
    location = defaultdict(int)
    for index, row in df.iterrows():
        l = row["Location"]
        if not pd.isnull(l): location[l]+= 1
    
    location = sorted(location.items(), key=operator.itemgetter(1))
    label = []
    place_count = []
    for value in location:
        print(str(value[0]) + " " + str(value[1]))
        label.append(value[0].decode('utf-8'))
        place_count.append(value[1])

    y_pos = np.arange(len(label))
    plt.bar(y_pos,place_count, align='center', alpha=0.5)
    plt.xticks(y_pos, label, rotation='vertical')
    plt.ylabel('House Price')
    plt.title('where celebs have been to in Tokyo')
    plt.show()

df = pd.read_csv("celeb.csv")
print(df.head())
print(len(df))
findMostVisitedLoc(df)

