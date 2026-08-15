# This function will take in a data frame and out put some basic analysis
import numpy as np
def number_of_columns(df):
    col_num = df.shape[1]
    return col_num

# Mean
def df_mean(df):
    col_num = number_of_columns(df)
    mean_col = []
    for col in col_num:
        mean_col.append(np.mean(df[col]))

    return mean_col

# Sum
def df_sum(df):
    return np.sum(df)

# Max
def df_max(df):
    return np.max(df)

# Min
def df_min(df):
    return np.min(df)
