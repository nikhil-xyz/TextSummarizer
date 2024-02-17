from textSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummerizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
from textSummerizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummerizer.logging import logger

STAGE_NAME = 'data_ingestion_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'data_validation_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_validation_training_pipeline = DataValidationTrainingPipeline()
    data_validation_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'data_transformation_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    data_transformation_training_pipeline = DataTransformationTrainingPipeline()
    data_transformation_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'model_training_training'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e


STAGE_NAME = 'model_evaluation'
try:
    logger.info(f'>>>>> stage {STAGE_NAME} has started <<<<<')
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.main()
    logger.info(f'>>>>> stage {STAGE_NAME} has completed <<<<<')
except Exception as e:
    logger.error(f'>>>>> stage {STAGE_NAME} has failed <<<<<')
    raise e
