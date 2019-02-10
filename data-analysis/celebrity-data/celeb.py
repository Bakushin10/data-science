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
    loc_details = defaultdict() #store the list of 
    for index, row in df.iterrows():
        l = row["Location"]
        if not pd.isnull(l):
            location[l] += 1
            # store the detail
            if l in loc_details:
                loc_details[l].append(row)
            else:
                loc_details[l] = [row]

    location = sorted(location.items(), key=operator.itemgetter(1))
    label = []
    place_count = []
    
    for value in location:
        print("\n" + str(value[0]) + " " + str(value[1]))
        ClassifyByseason(loc_details[value[0]])
        label.append(value[0].decode('utf-8'))
        place_count.append(value[1])
    

    y_pos = np.arange(len(label))
    plt.bar(y_pos,place_count, align='center', alpha=0.5)
    plt.xticks(y_pos, label, rotation='vertical')
    plt.ylabel('House Price')
    plt.title('where celebs have been to in Tokyo')
    plt.show()

def ClassifyByseason(loc_details):
    season = defaultdict(int)
    for j in loc_details:
        month = j["Month"]
        if not pd.isnull(month):
            season[month] += 1
        else:
            season["N/A"] += 1
    for s in season:
        print("     " + str(s) + " " + str(season[s]))

def findMostVisitedMonth(df):
    location = defaultdict(int)
    loc_details = defaultdict() #store the list of 
    for index, row in df.iterrows():
        l = row["Month"]
        if not pd.isnull(l):
            location[l] += 1
            # store the detail
            if l in loc_details:
                loc_details[l].append(row)
            else:
                loc_details[l] = [row]

    location = sorted(location.items(), key=operator.itemgetter(1))
    label = []
    place_count = []
    
    for value in location:
        print("\n" + str(value[0]) + " " + str(value[1]))
        ClassifyByseason(loc_details[value[0]])
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
findMostVisitedMonth(df)

