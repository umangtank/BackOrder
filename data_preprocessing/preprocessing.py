
class Preprocessor:
    def __init__(self):
        pass

    def remove_columns(self,data,columns):
        self.data=data
        self.columns=columns

        try:
            self.useful_data=self.data.drop(columns = self.columns)
            # drop the labels specified in the columns
            return self.useful_data

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    def encode_categorical_columns(self,data):
        self.data = data
        try:
            self.categorical_column = [column for column in self.data.columns if self.data[column].dtype == 'object']

            for x in self.categorical_column:
                if x != 'sku':
                    self.data[x].replace({'Yes': 1, 'No': 0}, inplace=True)

            return self.data

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
