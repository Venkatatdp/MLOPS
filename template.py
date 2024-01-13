import os
from pathlib import Path
import logging
from ipdb import set_trace as st

list_of_files=[

    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"

]

class Logger:
    """ This class is used for creating log file and code tracking"""
    def __init__(self,logfile):
        # Create a logger object
        self.logger = logging.getLogger(__name__)
        # Set the logging level
        self.logger.setLevel(logging.INFO)
        # Adding Handlers
        streamhandler = logging.StreamHandler()
        filehandler = logging.FileHandler(logfile)
        # Setting the format
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        #Setting the format to handlers
        streamhandler.setFormatter(formatter)
        filehandler.setFormatter(formatter)
        #Adding the handlers to logger
        self.logger.addHandler(streamhandler)
        self.logger.addHandler(filehandler)
    
    def log(self,msg,level='info') -> None:
        '''This method is used for saving various levels of logging'''
        if level == 'info':
            self.logger.info(msg)
        elif level == 'error':
            self.logger.error(msg,exc_info=True)
        elif level == 'warning':
            self.logger.warning(msg)


class ProjectStructure:

    def __init__(self,logger):
        self.logger = logger
    
    def create_files(self,files) -> None:
        for file in files:
            # using Path from pathlib sinces it handles files based on the sytem configration linur or windows
            filepath = Path(file)
            filedir,filename = os.path.split(filepath)
            if filedir != '':
                os.makedirs(filedir,exist_ok=True)
                self.logger.log(f"creating file directory : {filedir} for filename : {filename}","info")
            if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
                with open(filepath,'w'):
                    pass
                    self.logger.log(f"creating filename: {filename}","info")
            else:
                self.logger.log(f"filepath {filepath} already exists","warning")


      
if __name__ == "__main__":
    logger = Logger(os.path.join(os.getcwd(),'logger.log'))
    folder = ProjectStructure(logger)
    folder.create_files(list_of_files)