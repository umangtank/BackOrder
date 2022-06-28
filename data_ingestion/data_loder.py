import pandas as pd
class dataGatter:
    def __init__(self):
        self.training_file='Kaggle_Training_Dataset_v2.csv'
        self.testing_file = 'Kaggle_Test_Dataset_v2.csv'

    def get_data(self):
        try:
            self.train_data = pd.read_csv(self.training_file)
            self.test_data = pd.read_csv(self.testing_file)
            
            self.data = self.train_data[:-1].append(self.test_data[:-1],ignore_index = True)
            return self.data
        
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'