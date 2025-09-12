import pandas as pd

class DataInvestigator:

    #initializes
    def __init__(self, df):
        self.df = df

    #computes baseline for a column given its index
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
        
    #computes correlation between two columns given their indexes
    def corr(self, col1, col2):
        try:
            col1_name = self.df.columns[col1]
            col2_name = self.df.columns[col2]
            return self.df[col1_name].corr(self.df[col2_name])
        except Exception:
            return None
    
    #computes ZeroR for a column given its index
    def zeroR(self, col):
        try:
            col_name = self.df.columns[col]
            #allows uses mode for both numeric and categorical
            return self.df[col_name].mode()[0]
        except Exception:
            return None
        

# Sample data
data = {
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Female"],
    "Height": [73.8, 68.7, 74.1, 65.3, 62.8, 70.2],
    "Weight": [241.8, 162.3, 212.7, 150.0, 120.5, 180.6]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create investigator
investigator = DataInvestigator(df)

# Test baseline
print("Baseline (Height):", investigator.baseline(1))   # mean of Height
print("Baseline (Gender):", investigator.baseline(0))   # mode of Gender

# Test correlation
print("Correlation (Height vs Weight):", investigator.corr(1, 2))

# Test ZeroR
print("ZeroR (Gender):", investigator.zeroR(0))
print("ZeroR (Height):", investigator.zeroR(1))
