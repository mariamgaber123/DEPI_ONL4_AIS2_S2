import pandas as pd
def chk_type(df):
   dtypes=df.dtypes
   n_unique=df.nunique()
   return pd.DataFrame({"Dtype":dtypes,"num_unigue":n_unique}).T

