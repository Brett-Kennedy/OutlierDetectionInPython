import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class RealVsFakeOutlierDetector():
    def __init__(self, max_depth=None, max_leaf_nodes=None):
        self.clf = None
        self.max_depth = max_depth
        self.max_leaf_nodes = max_leaf_nodes

    def fit(self, df, label_col):
        self.clf = DecisionTreeClassifier(max_depth=self.max_depth, 
                                          max_leaf_nodes=self.max_leaf_nodes,
                                          random_state=0) 
        self.clf.fit(df.drop(columns=[label_col]), train_df[label_col])
    
    def predict(self, df):
        return self.clf.predict(df)
