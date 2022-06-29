import data_loder
from data_preprocessing import preprocessing
from sklearn.model_selection import train_test_split

class training:
    def __init__(self):
        pass

    def trainingModel(self):
        try:
            data_getter = data_loder.dataGatter()
            data = data_getter.get_data()

            preprocessor = preprocessing.Preprocessor()
            # remove the unnamed column as it doesn't contribute to prediction.
            data = preprocessor.remove_columns(data, ["sku", "national_inv", "lead_time", "in_transit_qty", "min_bank", "potential_issue",
                                               "pieces_past_due", "local_bo_qty", "deck_risk", "oe_constraint", "ppap_risk", "stop_auto_buy", "rev_stop"])

            # Convert categorical values to numeric values
            data = preprocessor.encode_categorical_columns(data)

            # check if missing values are present in the dataset
            is_null_present, cols_with_missing_values = preprocessor.is_null_present(
                data)

            # if missing values are there, replace them appropriately.
            if (is_null_present):
                data = preprocessor.impute_missing_values(
                    data, cols_with_missing_values)

            # create separate features and labels
            X, Y = preprocessor.separate_label_feature(
                data, label_column_name='went_on_backorder')

            # scaling the X values
            X = preprocessor.scale_numerical_columns(X)

            # Imbalanced dataset to make it a balanced one
            X, Y = preprocessor.handle_imbalanced_dataset(X, Y)

            # parsing all the clusters and looking for the best ML algorithm to fit on individual cluster
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=1 / 3, random_state=355)
            

            print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    