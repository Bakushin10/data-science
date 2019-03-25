
"""
Learning session from Data Science battle ground
https://tokyotechies.com/courses/data-science-battleground/
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#matplotlib inline

def plot_relationships_numerical(
    df,
    target,
    features,
    plot_width=8,
    plot_height=7,
):
    """Plot relationships with multiple numerical columns.
    
    Args:
        df: The dataframe from which we get the data to plot.
        target: Name of the target column.
        features: A list of column names. A plot is drawn for each column
            in the list, showing its relationship with the target column.
        plot_width: Width of each subplot.
        plot_height: Height of each subplot.
    Returns:
        None
    """
    n_features = len(features)
    n_cols = min(2, n_features)
    n_rows = (n_features + n_cols - 1) // n_cols
    figsize = (plot_width*n_cols, plot_height*n_rows)
    fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols,figsize=figsize)

    if n_rows == 1:
        ax = [ax]
    if n_cols == 1:
        ax = [[x] for x in ax]
    
    i = 0                                                                                                                                                                                                                                                                                                                                                                               
    for row in range(n_rows):
        for col in range(n_cols):
            if i >= n_features:
                break
            sns.scatterplot(x=df[features[i]],
                            y=df[target],
                            ax=ax[row][col])
            i += 1
    plt.show()

def show_missing(df):
    """Show missing data in a DataFrame."""
    total = df.isnull().sum().sort_values(ascending=False)
    missing_data = pd.DataFrame({'Total': total})
    missing_data['Percent'] = missing_data['Total'] / len(df)
    # Show only columns with missing data
    return missing_data[missing_data['Percent'] > 0]

def drop_outliers(df, columns_to_check, thresholds):
    """Drop outliers from a dataframe.

    Args:
      columns_to_check: A list of column names to check for outliers.
      thresholds: A list of threshold values to identify outliers. The length
          of this list must be the same as columns_to_check.
    Returns:
      A dataframe with outliers removed.
    """
    if (isinstance(columns_to_check, str) or not isinstance(columns_to_check, Iterable)):
        columns_to_check = [columns_to_check]
    if not isinstance(thresholds, Iterable):
        thresholds = [thresholds]
    assert len(columns_to_check) == len(thresholds)

    returned_df = df.copy()
    print(zip(columns_to_check, thresholds))
    for col_name, thres in zip(columns_to_check, thresholds):
        returned_df.drop(returned_df[returned_df[col_name] >= thres].index,inplace=True)
    return returned_df

numerical_features = [
    'GrLivArea',
    'LotArea',
    'LotFrontage',
    'TotalBsmtSF',
    'EnclosedPorch',
    '3SsnPorch'
]

if __name__ == '__main__':
    DATA_TRAIN = 'train.csv'
    DATA_TEST = 'test.csv'

    train_data = pd.read_csv(DATA_TRAIN, index_col='Id')
    test_data = pd.read_csv(DATA_TEST, index_col='Id')

    print(train_data.head())
    print(test_data.head())
    #plot_relationships_numerical(train_data, 'SalePrice', list(train_data.columns.values))
    #plot_relationships_numerical(train_data, 'SalePrice', numerical_features)
 
    # print('Missing values in training data')
    # print(show_missing(train_data))
    #train_data = drop_outliers(train_data, 'SalePrice', 500000)
    corrmat = train_data.corr()
    fig, ax = plt.subplots(figsize=(15, 15))
    sns.heatmap(corrmat, square=True)
