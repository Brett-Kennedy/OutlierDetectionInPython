# Requires mlxtend be installed.

from mlxtend.frequent_patterns import apriori
import pandas as pd

class FPOFOutlierDetector():
    def __init__(self, min_support=0.3):
        self.frequent_itemsets = None
        self.min_support = min_support
    
    def fit(self, df):
        self.frequent_itemsets = apriori(df, min_support=self.min_support, use_colnames=True) 
    
    def predict(self, df_in):
        df = df_in.copy()
        df['FPOF_Score'] = 0
        for fis_idx in self.frequent_itemsets.index: 
            fis = self.frequent_itemsets.loc[fis_idx, 'itemsets']
            support = self.frequent_itemsets.loc[fis_idx, 'support'] 
            col_list = (list(fis))
            cond = True
            for col_name in col_list:
                cond = cond & (data_df[col_name])

            df.loc[data_df[cond].index, 'FPOF_Score'] += support 
        min_score = df['FPOF_Score'].min() 
        max_score = df['FPOF_Score'].max()
        df['FPOF_Score'] = [(max_score - x) / (max_score - min_score) 
                         for x in df['FPOF_Score']]
        return df['FPOF_Score']
