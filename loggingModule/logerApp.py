import logging

class Logger:
    def __init__(self):
        pass
    
    def log(self,path,msg,level):
        logging.basicConfig(filename=path,format="[%(asctime)s: %(levelname)s: %(module)s] %(message)s")
        
        if level == 'info': 
            logging.info(msg) 
        if level == 'warning': 
            logging.warning(msg)
        if level == 'error': 
            logging.error(msg)
