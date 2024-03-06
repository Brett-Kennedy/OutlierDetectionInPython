class Radius_OutlierDetector:
    def __init__(self):
        pass

    def fit_predict(self, df, radius):
        tree = BallTree(df)
        counts = tree.query_radius(df, radius, count_only=True)
        min_score = min(counts)
        max_score = max(counts)
        scores = [(max_score - x)/(max_score - min_score) for x in counts]
        return scores
