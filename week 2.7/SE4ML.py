import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
scaler = StandardScaler()
from joblib import load


class Predictor:
    def __init__(self,data):
        self.data = data
        self.data = pd.read_csv(self.data)
        self.to_remove = self.get_null_col()
        self.prosses_data = self.remove_col()
        self.model = load("model.joblib")
        self.final_data = self.predict()
        self.save_data()
 
    def get_null_col(self):
        to_remove = []
        self.data['timestamp'] = pd.to_datetime(self.data["timestamp"])
        for column in self.data.columns:
            na_per_col = self.data[column].isna().sum() / len(self.data[column]) * 100
            if na_per_col > 30:
                to_remove.append(column) 
        return to_remove
    
    def remove_col(self):
        for column in self.to_remove:
            self.data.drop(column,inplace = True,axis =1)
        return self.data
    
    def predict(self):
        final_data = self.prosses_data
        X = scaler.fit_transform(self.prosses_data)
        y_pred = self.model.predict(X)
        final_data["prediction"] = y_pred
        return final_data
    
    def save_data(self):
        self.final_data.to_csv('results.csv', index=False)




pred = Predictor("other_months_data.csv")