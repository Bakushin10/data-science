import pandas as pd
f500 = pd.read_csv("f500.csv", index_col=0)

#find the median 
median = f500[["revenues", "profits"]].median(axis = 0)
print(median)
"""
revenues    40236.0
profits      1761.6
"""

print(f500["sector"].value_counts().head())
"""
Financials                118
Energy                     80
Technology                 44
Motor Vehicles & Parts     34
Wholesalers                28
"""

