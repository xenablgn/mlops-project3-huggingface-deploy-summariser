import os 
from box.exceptions import  BoxValueError
import yaml
from src.textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            content = ConfigBox(content)
            return content
    except BoxValueError as e:
        logger.error(f"Error while converting yaml file to ConfigBox: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error while reading yaml file: {e}")
        raise e