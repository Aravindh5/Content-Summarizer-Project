import os
import yaml
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from textSummarizer.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    """Reads yaml file and returns

    Args:
        Path to yaml (str): path like input.

    Raises:
        ValueError: If yaml file is empty.
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):

    """Creates directories

    Args:
        path_to_directories (list): list of path of directories.
        verbose (bool, optional): Defaults to True.
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory at {path}")


@ensure_annotations
def get_size(path: Path) -> str:

    """get size in KB

    Args:
        path (Path): path of the file.

    Returns:
        str: size in KB
    """

    size_in_kb = round(os.path.getsize(path) / 1024, 2)

    return f"{size_in_kb} KB"
