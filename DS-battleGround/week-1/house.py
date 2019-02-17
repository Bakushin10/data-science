from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#matplotlib inline

DATA_TRAIN = 'train.csv'
DATA_TEST = 'test.csv'

train_data = pd.read_csv(DATA_TRAIN, index_col='Id')
test_data = pd.read_csv(DATA_TEST, index_col='Id')

print(train_data.head())
print(test_data.head())


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
    fig, ax = plt.subplots(nrows=n_rows, ncols=n_cols,
                           figsize=figsize)
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

numerical_features = [
    'GrLivArea',
    'LotArea',
#    'LotFrontage',
#    'TotalBsmtSF',
]

#plot_relationships_numerical(train_data, 'SalePrice', list(train_data.columns.values))
plot_relationships_numerical(train_data, 'SalePrice', numerical_features)