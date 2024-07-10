from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def train(self, normal_data):
        self.model.fit(normal_data)

    def detect(self, data):
        predictions = self.model.predict(data)
        return np.where(predictions == -1)[0]