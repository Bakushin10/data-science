import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import operator

sns.set(style="ticks", color_codes=True)
MONTH = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 
         9:"September", 10:"October", 11:"November", 12:"December"}
         
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
                print(row)
                loc_details[l] = [row]

    location = sorted(location.items(), key=operator.itemgetter(1))
    label = []
    place_count = []
    month_data = []
    for value in location:
        print("\n" + str(value[0]) + " " + str(value[1]))
        month_data.append(ClassifyByseason(loc_details[value[0]]))
        label.append(value[0].decode('utf-8'))
        place_count.append(value[1])
    
    print(month_data)
    #demo(month_data, label)
    """
        plot here
    """
    y_pos = np.arange(len(label))
    plt.bar(y_pos,place_count, align='center', alpha=0.5)
    plt.xticks(y_pos, label, rotation='vertical')
    plt.ylabel('Count')
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
    
    sorted_month = []
    """ sort Jan to Dec """
    for i in range(len(MONTH)):
        if season[MONTH[i+1]] != None:
            sorted_month.append(season[MONTH[i+1]])
        else:
            sorted_month.append(0)
    print(sorted_month)
    return sorted_month

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
    label = [] # holds the location
    place_count = []
    
    for value in location:
        print("\n" + str(value[0]) + " " + str(value[1]))
        ClassifyByseason(loc_details[value[0]])
        label.append(value[0].decode('utf-8'))
        place_count.append(value[1])
    
    y_pos = np.arange(len(label))
    plt.bar(y_pos,place_count, align='center', alpha=0.5)
    plt.xticks(y_pos, label, rotation='vertical')
    plt.ylabel('Count')
    plt.title('Month')
    plt.show()

def demo(data, col):
    # data = [[ 66386, 174296,  75131, 577908,  32015],
    #     [ 58230, 381139,  78045,  99308, 160454],
    #     [ 89135,  80552, 152558, 497981, 603535],
    #     [ 78415,  81858, 150656, 193263,  69638],
    #     [139361, 331509, 343164, 781380,  52269]]

    columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
    columns = col
    rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

    values = np.arange(0, 2500, 500)
    value_increment = 1000

    # Get some pastel shades for the colors
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    n_rows = len(data)

    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(columns))

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        print(row)
        plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
        y_offset = y_offset + data[row]
        #print(y_offset)
        cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
        print(cell_text)
    # Reverse colors and text labels to display the last value at the top.
    colors = colors[::-1]
    cell_text.reverse()

    # Add a table at the bottom of the axes
    the_table = plt.table(cellText=cell_text,
                        rowLabels=rows,
                        rowColours=colors,
                        colLabels=columns,
                        loc='bottom')

    # Adjust layout to make room for the table:
    plt.subplots_adjust(left=0.2, bottom=0.2)

    plt.ylabel("Loss in ${0}'s".format(value_increment))
    plt.yticks(values * value_increment, ['%d' % val for val in values])
    plt.xticks([])
    plt.title('Loss by Disaster')

    plt.show()


df = pd.read_csv("celeb.csv")
print(df.head())
print(len(df))
#demo()
findMostVisitedLoc(df)
#findMostVisitedMonth(df)

