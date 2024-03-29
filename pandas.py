#### pandas
# basically set up like folders within folders
# most common alias is pd. make sure to execute it

import pandas as pd

# Series is ordered. Works like dictionary but value doesn't need to be unique

queens_regnant = ["Mary I", "Elizabeth I", "Mary II"]
pd.Series(queens_regnant)
# When executed, numbers will be assigned to each value. It starts with 0
0         Mary I
1    Elizabeth I
2        Mary II

## series attributes

# is_unique to check if there is only 1. Answer is a Boolean

# parameters and arguments


# head and tails methods: pull out the first few or last few rows of a series. The default is 5

# Python functions and pandas

len(series_name)

sorted(series_name)

dict(series_name)

# in looks in the index of a series, not the values

in series.index
in series.values

# inloc and loc. Loc is for labels. iloc for the index. These are accessors

planets.loc["Venus"]


# value_counts methods to check how often a value exists in a series


# sort_values() method is sorting by values instead of index

# accesssor: you used [] to extract from series

# some methods only for series and others for data frames
