import Data_ingestion.data_loder as data_loder
from data_preprocessing import preprocessing
from sklearn.model_selection import train_test_split
from Model_Finder import Model
from Save_Model import save_methods
import os
import loggingModule.logerApp as logerApp

class training:
    def __init__(self):
        self.train_log = logerApp.Logger()
        self.filepath = 'Training_Logs/ModelTrainingLog.log'
        os.makedirs("Training_Logs", exist_ok=True)

    def trainingModel(self):
        self.train_log.log(self.filepath, "Enter In TrainingModel", 'info')
        try:
            data_getter = data_loder.dataGatter()
            data = data_getter.get_data()

            self.train_log.log(self.filepath, "Data Loaded", 'info')
            preprocessor = preprocessing.Preprocessor()
            
            self.train_log.log(self.filepath,"remove the unnamed column as it doesn't contribute to prediction.",'info')
            data = preprocessor.remove_columns(data, ["sku", "national_inv", "lead_time", "in_transit_qty", "min_bank", "potential_issue",
                                               "pieces_past_due", "local_bo_qty", "deck_risk", "oe_constraint", "ppap_risk", "stop_auto_buy", "rev_stop"])

            self.train_log.log(self.filepath,f"Final Data: {data}",'info')    
            self.train_log.log(self.filepath, "Convert categorical values to numeric values", 'info')
            data = preprocessor.encode_categorical_columns(data)

            self.train_log.log(self.filepath, "Check if missing values are present in the dataset", 'info')
            is_null_present, cols_with_missing_values = preprocessor.is_null_present(
                data)

            self.train_log.log(self.filepath, "Check if missing values are present in the dataset", 'info')
            if (is_null_present):
                data = preprocessor.impute_missing_values(
                    data, cols_with_missing_values)

            self.train_log.log(self.filepath, "Check if missing values are present in the dataset", 'info')
            X, Y = preprocessor.separate_label_feature(
                data, label_column_name='went_on_backorder')

            
            self.train_log.log(self.filepath, "Imbalanced dataset to make it a balanced one", 'info')
            X, Y = preprocessor.handle_imbalanced_dataset(X, Y)

        
            self.train_log.log(self.filepath, "Split the data into train and test", 'info')
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=1 / 3, random_state=0)
            
            model_finder = Model.Model_Finder() 
            self.train_log.log(self.filepath, "Get the best model for each of the clusters", 'info')
            best_model_name,best_model = model_finder.get_best_model(x_train,y_train,x_test,y_test)


            self.train_log.log(self.filepath, "Saving the best model to the directory", 'info')
            model_op = save_methods.Model_Operation()

            save_model = model_op.save_model(best_model, best_model_name)   
            self.train_log.log(self.filepath, "Model Saved", 'info')

        except Exception as e:
            self.train_log.log(self.filepath, f"The Exception message is: {e}", 'error')
            return 'something is wrong'

    