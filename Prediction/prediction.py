from Save_Model import save_methods
import pandas as pd
from data_preprocessing import preprocessing
import os
import warnings
import loggingModule.logerApp as logerApp

warnings.filterwarnings("ignore")


class prediction:
    def __init__(self):
        self.log_writer = logerApp.Logger()
        self.filepath = "Prediction_Logs/PredictionLog.log"
        os.makedirs("Prediction_Logs", exist_ok=True)

    def convert_input_into_data(self, user_input):
        self.log_writer.log(
            self.filepath, "Enter In Convert_input_into_data", 'info')
        self.input = user_input

        try:
            preprocessor = preprocessing.Preprocessor()
            df = pd.DataFrame(self.input, index=["forecast_3_month", "forecast_6_month", "forecast_9_month", "sales_1_month",
                              "sales_3_month", "sales_6_month", "sales_9_month", "perf_6_month_avg", "perf_9_month_avg"])
            data = df.transpose()
            self.log_writer.log(
                self.filepath, "Convert categorical values to numeric values", 'warning')
            data = preprocessor.encode_categorical_columns(data)
            self.log_writer.log(
                self.filepath, "Exit In Convert_input_into_data", 'info')

            return data

        except Exception as error:
            self.log_writer.log(
                self.filepath, f"The Exception message is: {error}", 'error')
            return 'something is wrong'

    def get_prediction(self, data):
        self.log_writer.log(self.filepath, "Enter In Get_prediction", 'info')
        self.data = data

        try:
            model_loader = save_methods.Model_Operation()
            model_name = model_loader.find_correct_model_file()
            self.log_writer.log(self.filepath, f"Model Name:  {model_name}")
            model = model_loader.load_model(model_name)
            result = list(model.predict(self.data))
            self.log_writer.log(
                self.filepath, f"Prediction:  {result}", 'error')
            result = pd.DataFrame(result, columns=['Prediction'])
            result["Prediction"] = result["Prediction"].map(
                {0: "Yes", 1: "No"})
            path = "Prediction_Output_File"
            os.makedirs(path, exist_ok=True)
            result.to_csv("Prediction_Output_File/Predictions.csv",
                          header=True, mode='a+')
            self.log_writer.log(self.filepath, "Exit In Get_prediction")

        except Exception as error:
            self.log_writer.log(
                self.filepath, f"The Exception message is: {error}", 'error')
            return 'something is wrong'
