import pandas as pd
def isNull(df):
   null =df.isnull().sum()
   return pd.DataFrame(null).T