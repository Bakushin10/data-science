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

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()



"""
diff in 'loc' and 'iloc'

“iloc” in pandas is used to select rows and columns by number, 

"loc" method directly selects based on index values of any rows.
For example, setting the index of our test data frame to the persons “last_name”:
"""
# Rows:
data.iloc[0] # first row of data frame (Aleshia Tomkiewicz) - Note a Series data type output.
data.iloc[1] # second row of data frame (Evan Zigomalas)
data.iloc[-1] # last row of data frame (Mi Richan)
# Columns:
data.iloc[:,0] # first column of data frame (first_name)
data.iloc[:,1] # second column of data frame (last_name)
data.iloc[:,-1] # last column of data frame (id)
data.iloc[0:5] # first five rows of dataframe
data.iloc[:, 0:2] # first two columns of data frame with all rows

#loc
data.loc[['Andrade', 'Veness'], 'city':'email']
# Select same rows, with just 'first_name', 'address' and 'city' columns
data.loc['Andrade':'Veness', ['first_name', 'address', 'city']]
