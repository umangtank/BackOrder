import pickle
import os
import shutil


class Model_Operation:
    
    def __init__(self):
        self.model_directory='Model/'

    def save_model(self,model,filename):
        try:
            path = os.path.join(self.model_directory,filename)
            #create separate directory for each cluster
            if os.path.isdir(path):
                #remove previously existing models for each clusters
                shutil.rmtree(self.model_directory)
                os.makedirs(path)
            else:
                os.makedirs(path)
            
            with open(path +'/' + filename+'.sav','wb') as f:
                pickle.dump(model, f) # save the model to file
            
            return 'success'

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    
    def load_model(self,filename):
        
        try:
            with open(self.model_directory + filename + '/' + filename + '.sav','rb') as f:
                return pickle.load(f)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    def find_correct_model_file(self):
        
        try:
            # self.cluster_number= cluster_number
            self.folder_name = self.model_directory
            self.list_of_files = []
            self.list_of_files = os.listdir(self.folder_name)
            for self.file in self.list_of_files:
                try:
                    self.model_name = self.file
                except:
                    continue
            self.model_name = self.model_name.split('.')[0]
            
            return self.model_name
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'