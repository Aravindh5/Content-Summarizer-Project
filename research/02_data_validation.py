import os

os.chdir('../')

# STEP - 1
# Based on the README.md file, Step 1 is to Update config/config.yaml file
# There, we have added a Data Ingestion section and its components.

# STEP - 2
# Based on the README.md file, Step 2 is to Update params/params.yaml file
# In this, Data Ingestion phase we are not required to update the params.yaml file.

# STEP - 3
# Based on the README.md file, this is the third step. (Step 3: Updating the entity)
# The following code is the entity, which is the return type of the function.
# Whenever we call this DataIngestionConfig class, it will say (return), "These are the types of the variables."
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataValidationConfig:

    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


# STEP - 4
# Updating Configuration manager

from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories


class ConfigurationManger:

    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_validation_config(self) -> DataValidationConfig:

        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config


# STEP 5:
# Updating the components
import os
from textSummarizer.logging import logger


class DataValidation:

    def __init__(self, config: DataValidationConfig):

        self.config = config

    def validate_all_files_exist(self) -> bool:

        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:

                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {validation_status}")

                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Statu: {validation_status}")

            return validation_status

        except Exception as e:
            raise e


# STEP 6:
# Update the pipeline
try:
    config = ConfigurationManger()
    data_validation_config = config.get_data_validation_config()
    data_validation = DataValidation(config=data_validation_config)
    data_validation.validate_all_files_exist()
except Exception as e:
    raise e
