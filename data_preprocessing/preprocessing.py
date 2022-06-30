import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from imblearn.under_sampling import NearMiss
import warnings,pickle
warnings.filterwarnings("ignore")


class Preprocessor:
    def __init__(self):
        pass

    def remove_columns(self, data, columns):
        self.data = data
        self.columns = columns

        try:
            self.useful_data = self.data.drop(columns=self.columns)
            # drop the labels specified in the columns
            return self.useful_data

        except Exception as e:
            # print('The Exception message is: ', e)
            return 'something is wrong'

    def encode_categorical_columns(self, data):
        self.data = data
        print(self.data.columns)
        try:
            self.categorical_column = [
                column for column in self.data.columns if self.data[column].dtype == 'object']

            for x in self.categorical_column:
                if x != 'sku':
                    self.data[x].replace({'Yes': 1, 'No': 0}, inplace=True)

            return self.data

        except Exception as e:
            # print('The Exception message is: ', e)
            return 'something is wrong'

    def is_null_present(self, data):
        self.null_present = False
        self.cols_with_missing_values = []
        self.data = data
        self.cols = self.data.columns

        try:
            # check for the count of null values per column
            self.null_counts = self.data.isnull().sum()
            for i in range(len(self.null_counts)):
                if self.null_counts[i] > 0:
                    self.null_present = True
                    self.cols_with_missing_values.append(self.cols[i])

            if(self.null_present):  # write the logs to see which columns have null values
                self.dataframe_with_null = pd.DataFrame()
                self.dataframe_with_null['columns'] = self.cols
                self.dataframe_with_null['missing values count'] = np.asarray(
                    self.data.isnull().sum())
                self.dataframe_with_null.to_csv(
                    'Data_Information/null_values.csv')
                # storing the null column information to file

            return self.null_present, self.cols_with_missing_values

        except Exception as e:
            # print('The Exception message is: ', e)
            return 'something is wrong'

    def separate_label_feature(self, data, label_column_name):
        self.data = data
        self.column = label_column_name

        try:
            # drop the columns specified and separate the feature columns
            self.X = self.data.drop(columns=[self.column])
            self.Y = self.data[self.column]  # Filter the Label columns
            return self.X, self.Y

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    def scale_numerical_columns(self, data):

        self.data = data

        try:
            path = "scalingModel.pkl"
            self.num_df = self.data
            self.scaler = RobustScaler()  # initializing robust scaler
            self.scaled_data = self.scaler.fit_transform(self.num_df)
            self.scaled_num_df = pd.DataFrame(
                data=self.scaled_data, columns=self.num_df.columns)
            print(self.scaled_num_df.columns)

            with open("scale/scalingModel.pkl",'wb') as f:
                pickle.dump(self.scaler, f)
            # with open('robustScaler.pkl','wb') as f:
                # pickle.dump(self.scaler, f)
            print('Scaling done')
            return self.scaled_num_df

        except Exception as e:
            # print('The Exception message is: ', e)
            return 'something is wrong'

    def handle_imbalanced_dataset(self, x, y):
        try:
            self.nmsample = NearMiss()
            self.x_sampled, self.y_sampled = self.nmsample.fit_resample(
                x, y)  # upsampling the data
            print(self.x_sampled)
            return self.x_sampled, self.y_sampled

        except Exception as e:
            # print('The Exception message is: ', e)
            return 'something is wrong'
