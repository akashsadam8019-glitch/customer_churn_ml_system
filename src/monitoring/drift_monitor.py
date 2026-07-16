import os
import sys
import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset, DataSummaryPreset

from src.exception.exception import CustomException
from src.logger.logger import logger


class DriftMonitor:

    def __init__(self):

        logger.info("DriftMonitor initialized.")

        self.reference_path = "artifacts/reference_data.csv"

        self.report_dir = "reports"

        self.report_path = os.path.join(
            self.report_dir,
            "evidently_report.html",
        )

    def generate_report(self, current_data_path):

        try:

            logger.info("Loading reference dataset...")

            reference_data = pd.read_csv(
                self.reference_path
            )

            logger.info("Loading current dataset...")

            current_data = pd.read_csv(
                current_data_path
            )

            logger.info("Creating Evidently report...")

            report = Report(
                metrics=[
                    DataDriftPreset(),
                    DataSummaryPreset(),
                ]
            )

            report.run(
                reference_data=reference_data,
                current_data=current_data,
            )

            os.makedirs(
                self.report_dir,
                exist_ok=True,
            )

            report.save_html(
                self.report_path
            )

            logger.info(
                f"Report saved at {self.report_path}"
            )

            return self.report_path

        except Exception as e:

            logger.error(e)

            raise CustomException(e, sys)