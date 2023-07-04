from joblib import load
import pandas as pd
import matplotlib.pyplot as plt
import os
import logging
from sklearn.preprocessing import StandardScaler

class Drawer:
    def __init__(self,file):
        self.model = load("model.joblib")
        self.file = file
        self.df = pd.read_csv(file)
        self.scaler = StandardScaler()
        self.scaled_prep_df = self.prep()
        self.predict()
        self.plot_sensor_anomolies()
    
    def remove_col(self,data,collumns:list):
        """
        function:
                remove columns from dataframe
        input:
            data = origineel dataframe
            collumns = list of columns to be removed

        return:
                cleaned data  
        """
        for column in collumns:
            data.drop(column,inplace = True,axis =1)
        return data


    def prep(self):
        """
        function:
                -prep the data based on all the empty columns.
                -scale data

        input:
            data = origineel dataframe
            collumns = list of columns to be removed

        return:
                scaled_cleaned_df
        """
        to_remove = []
        self.df['timestamp'] = pd.to_datetime(self.df["timestamp"])
        for column in self.df.columns:
            na_per_col = self.df[column].isna().sum() / len(self.df[column]) * 100
            if na_per_col == 100:
                to_remove.append(column)
        self.df = self.remove_col(self.df,to_remove)
        self.df = self.df.drop(columns=["Unnamed: 0"])
        self.df = self.df.set_index('timestamp')
        self.df = self.df.fillna(self.df.mean())
        scaled_cleaned_df = self.scaler.fit_transform(self.df)
        print("Transforming data")
        return scaled_cleaned_df


    def predict(self):
        y_pred = self.model.predict(self.scaled_prep_df)
        self.df["prediction"] = y_pred
        print("Predicting")
    
    def plot_sensor_anomolies(self):
        for sensor in self.df:
            if sensor != "prediction":
                anomoly_rows = self.df[self.df["prediction"] == -1]
                plt.figure(figsize=(25,3))
                plt.plot(self.df[sensor], color='grey')
                plt.plot(anomoly_rows[sensor], linestyle='none', marker='X', color='blue', markersize=4, label='anomoly predicted', alpha = 0.1)
                plt.title(sensor)
                plt.legend()
                plt.savefig(f"img/{sensor}.png")
                print(f"{sensor} to /img")
                self.create_log_file(sensor)
            else:
                print("Finishing process")
                break

        

    def create_log_file(self,name):
        log_file_name = f"{name}.log"
        log_file_path = os.path.join("C:/Users/marsh/Desktop/programming2/week 2.7/log", log_file_name)

        # Create a new logger
        logger = logging.getLogger(name)

        # Set the log level
        logger.setLevel(logging.INFO)

        # Create a file handler and set the log file path
        file_handler = logging.FileHandler(log_file_path)

        # Set the log format
        formatter = logging.Formatter("%(asctime)s  %(message)s", "%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Log the creation of the log file
        logger.info(f"Log file created for '{name}'")

        return logger

        


# if __name__ == '__main__':
#     draw = Drawer("august.csv")
