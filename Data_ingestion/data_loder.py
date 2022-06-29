import pandas as pd


class dataGatter:
    def __init__(self):
        self.training_file = 'Dataset\Kaggle_Training_Dataset_v2.csv'
        self.testing_file = "Dataset\Kaggle_Test_Dataset_v2.csv"
        self.prediction_data = 'Prediction_Output_File\Predictions.csv'

    def get_data(self):
        try:
            self.train_data = pd.read_csv(self.training_file)
            self.test_data = pd.read_csv(self.testing_file)
            self.data = self.train_data[:-1].append(self.test_data[:-1],ignore_index = True)
            return self.data
        
        except Exception as e:
            # # # # print('The Exception message is: ', e)
            return 'something is wrong'

    def prediction(self):
        try:
            self.Pdata = pd.read_csv(self.prediction_data)  # reading the data file
            return self.Pdata

        except Exception as e:
            # # # # print('The Exception message is: ', e)
            return 'something is wrong'