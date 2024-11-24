from CNN_Classifier.config.configuration import ConfigurationManager
from CNN_Classifier.components.model_evaluation_mlflow import Evaluation
from CNN_Classifier import logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evlauation = Evaluation(eval_config)
        evlauation.evalutation()
        evlauation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"***********************")
        logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e