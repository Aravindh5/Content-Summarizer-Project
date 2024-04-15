import os

os.chdir('../')

# This file is the research phase of the Data Ingestion phase.

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
class DataIngestionConfig:

    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


# STEP - 4
# Based on the README.md file, this is the fourth step. (Step 4: Updating configuration manager in src configuration.py)
# As we are in the research phase, instead of using the configuration manager, we are going to do the thing here
# Once the research phase is done, we have to put this code in the src/config/configuration.py file.

# Sub step -> We have to update the constants/__init__.py file.
# Because, you have to read the config.yaml and params.yaml files.
# And, in textSummarizer/utils/common.py, we have a functions to read the yaml and create the directories.
from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories


class ConfigurationManager:

    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config


# STEP 5
# Based on the README.md file, this is the fifth step. (Step 5: Update the components)
import os
import urllib.request as request
import zipfile
from pathlib import Path
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


try:
    config = ConfigurationManager()

    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)

    data_ingestion.download_file()
    data_ingestion.extract_zip_file()

except Exception as e:
    raise e


# STEP 6 - Update the pipeline
# STEP 7 - Update the main.py
# STEP 8 - Update the app.py
# After executing the code above, we have to update the pipeline. It means to update the above steps in respective place
