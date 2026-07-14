from pathlib import Path
import yaml


class Config:
    """
    Loads project configuration from YAML files.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parents[2]

        config_path = project_root / "configs" / "config.yaml"
        schema_path = project_root / "configs" / "schema.yaml"

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        with open(schema_path, "r") as file:
            self.schema = yaml.safe_load(file)

    def get_config(self):
        return self.config

    def get_schema(self):
        return self.schema


config = Config()