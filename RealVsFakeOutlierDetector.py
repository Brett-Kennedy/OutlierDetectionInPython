import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class RealVsFakeOutlierDetector():
    def __init__(self, max_depth=4, max_leaf_nodes=6):
        self.clf = None
        self.max_depth = max_depth
        self.max_leaf_nodes = max_leaf_nodes

    def fit(self, df):
        real_df = df.copy()        
        real_df['Real'] = True
        
        synth_df = pd.DataFrame() 
        for col_name in data_df.columns:
            mean = real_df[col_name].mean()
            stddev = real_df[col_name].std()
            synth_df[col_name] = np.random.normal(
               loc=mean, scale=stddev, size=len(data_df))
        synth_df['Real'] = False  
        
        full_df = pd.concat([real_df, synth_df])
        
        self.clf = DecisionTreeClassifier(max_depth=self.max_depth, 
                                          max_leaf_nodes=self.max_leaf_nodes,
                                          random_state=0) 
        self.clf.fit(full_df.drop(columns=['Real']), full_df['Real'])
    
    def predict(self, df):
        return self.clf.predict_proba(df)
