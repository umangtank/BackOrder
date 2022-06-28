from data_ingestion import data_loder
from data_preprocessing import preprocessing
class training:
    def __init__(self):
        pass

    def trainingModel(self):
        try:
            data_getter = data_loder.dataGatter()
            data     = data_getter.get_data()

            preprocessor=preprocessing.Preprocessor()
            # remove the unnamed column as it doesn't contribute to prediction.
            data = preprocessor.remove_columns(data,["sku","national_inv","lead_time","in_transit_qty","min_bank","potential_issue","pieces_past_due","local_bo_qty","deck_risk","oe_constraint","ppap_risk","stop_auto_buy","rev_stop"])
            
            
            print(data)
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'