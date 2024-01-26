from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig

import sys

if __name__=="__main__":
    logging.info('The execution has started!')
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # data_transformation_config = DataTransformationConfig()
        data_transformation = DataTransformation()
        data_transformation.init_data_transformation(train_data_path, test_data_path)
        
    except Exception as e:
        raise CustomException(e,sys)