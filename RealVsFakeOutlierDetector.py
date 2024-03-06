import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

class RealVsFakeOutlierDetector():
    def __init__(self, max_depth=5):
        self.clf = None
        self.max_depth = max_depth

    def fit(self, df, label_col):
        self.clf = DecisionTreeClassifier(max_depth=self.max_depth, random_state=0) 
        self.clf.fit(df.drop(columns=['Real']), train_df['Real'])
    
    def predict(self, df):
        return self.clf.predict(df)
