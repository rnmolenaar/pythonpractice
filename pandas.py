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


