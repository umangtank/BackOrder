import logging

class Logger:
    def __init__(self):
        pass
    
    def log(self,path,msg,level):
        try:
            logging.basicConfig(filename=path,level = logging.INFO, format="[%(asctime)s: %(levelname)s] %(message)s")
            
            if level == 'info': 
                logging.info(msg) 
            if level == 'warning': 
                logging.warning(msg)
            if level == 'error': 
                logging.error(msg)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

