import pandas as pd
import loggingModule.logerApp as logerApp
import os

class dataGatter:
    def __init__(self):
        self.training_file = 'Dataset\Kaggle_Training_Dataset_v2.csv'
        self.testing_file = "Dataset\Kaggle_Test_Dataset_v2.csv"
        self.prediction_data = 'Prediction_Output_File\Predictions.csv'

        self.data_log = logerApp.Logger()
        self.filepath = 'Training_Logs/GeneralLog.log'

    def get_data(self):
        print("Enter In Get_data")
        self.data_log.log(self.filepath, "Enter In Get_data", 'info')
        try:
            self.train_data = pd.read_csv(self.training_file)
            self.test_data = pd.read_csv(self.testing_file)
            self.data = self.train_data[:-1].append(self.test_data[:-1],ignore_index = True)
            self.data_log.log(self.filepath, "Exit In Get_data", 'info')
            return self.data
        
        except Exception as e:
            self.data_log.log(self.filepath, f"The Exception message is: {e}", 'error')
            return 'something is wrong'

    def prediction(self):
        try:
            self.Pdata = pd.read_csv(self.prediction_data)  # reading the data file
            self.data_log.log(self.filepath, "Enter In Prediction", 'info')
            return self.Pdata

        except Exception as e:
            self.data_log.log(self.filepath, f"The Exception message is: {e}", 'error')
            return 'something is wrong'
