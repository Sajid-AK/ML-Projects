''' The main aim of this data_ingestion.py file is that we can
read the data from database or some other resources like API's 
'''

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass #It automatically adds methods like __init__, __repr__, and __eq__.
#By dataclass create variable directly  

## Import From Data_Transformation 
from src.components.data_transformation import DataTransfromation
from src.components.data_transformation import DataTransformationConfig

##Import from Model_Trainer.py
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
      train_data_path: str=os.path.join('artifacts', 'train.csv')
      test_data_path: str=os.path.join('artifacts', 'test.csv')
      raw_data_path: str=os.path.join('artifacts', 'data.csv')

class DataIngestion:
      def __init__(self):
         self.ingestion_config = DataIngestionConfig() #All the path save in that varibale
       

      def initiate_data_ingestion(self):# Read the data set
          logging.info('Entered the data Ingestion method or component')
          try:
              df = pd.read_csv(r'Notebook\data\stud.csv')#Dataset can be read from any where like api,some databases like mongoDB
              logging.info('Read the dataset as dataframe')
              os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
              #os.path.dirname()` gets the directory from the full path, and `os.makedirs()` creates it.

              df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)

              logging.info('Train test split initiated')
              train_set,test_set=train_test_split(df, test_size=0.2, random_state=42)
              

              train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
              test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)
              logging.info('Ingestion of the data is completed')


              return (self.ingestion_config.train_data_path,
       
                     self.ingestion_config.test_data_path

                    )
    
          except Exception as e:
                 raise CustomException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransfromation()
    train_arr,test_arr,_=data_transformation.initiate_data_transfromation(train_data,test_data)

    modeltrainer= ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))