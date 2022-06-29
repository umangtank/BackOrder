from Save_Model import save_methods
import pandas as pd
from data_preprocessing import preprocessing

import warnings

warnings.filterwarnings("ignore")

class prediction :
    def __init__(self):
        pass

    def convert_input_into_data(self,user_input):
        self.input = user_input
        try:
            preprocessor = preprocessing.Preprocessor()
            df = pd.DataFrame(self.input, index=["forecast_3_month","forecast_6_month","forecast_9_month","sales_1_month","sales_3_month","sales_6_month","sales_9_month","perf_6_month_avg","perf_9_month_avg"])
            data = df.transpose()

            ##Convert categorical values to numeric values
            data = preprocessor.encode_categorical_columns(data)
            return data

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

 

    def get_prediction(self , data):
        self.data = data
        try:
            model_loader = save_methods.Model_Operation()
            model_name = model_loader.find_correct_model_file()
            print(model_name)
            model = model_loader.load_model(model_name)
            result = list(model.predict(self.data))
            print(result)
            # result = pd.DataFrame(result, columns=['Prediction'])
            # result["Prediction"] = result["Prediction"].map({0: "Yes", 1: "No"})
            # path = "Prediction_Output_File/Predictions.csv"
            # result.to_csv("Prediction_Output_File/Predictions.csv", header=True,mode='a+')
            
        except Exception as error:
            print('The Exception message is: ', error)
            return 'something is wrong'

