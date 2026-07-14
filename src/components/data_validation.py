from src.logger.logger import logger


class DataValidation:
    """
    Responsible for validating the raw dataset before
    it enters the preprocessing pipeline.
    """

    def __init__(self, config):
        self.config = config
        logger.info("DataValidation component initialized.")