import pandas as pd

class DataInvestigator:

    def __init__(self, df):
        self.df = df

    def baseline(self, col):
        try:
            col_name = self.df.columns[col]
            #check if the column is numeric or categorical
            if pd.api.types.is_numeric_dtype(self.df[col_name]):
                return self.df[col_name].mean()
            else:
                return self.df[col_name].mode()[0]
        except Exception:
            return None

    def corr(self, col1, col2):
        try:
            col1_name = self.df.columns[col1]
            col2_name = self.df.columns[col2]
            return self.df[col1_name].corr(self.df[col2_name])
        except Exception:
            return None
    
    def zeroR(self, col):
        try:
            col_name = self.df.columns[col]
            #allows uses mode for both numeric and categorical
            return self.df[col_name].mode()[0]
        except Exception:
            return None