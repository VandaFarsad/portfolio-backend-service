import os

from .settings import *


def get_env_data_as_dict(path: str) -> dict:
    """
    For loading the .env -file (for docker) into the virtual environment
    """
    with open(path, "r") as f:
        return dict(
            tuple(line.replace("\n", "").split("=", maxsplit=1)) for line in f.readlines() if not line.startswith("#")
        )


ENV_FILE_NAME = os.getenv("ENV_FILE_NAME", ".env.dev")

vars_dict = get_env_data_as_dict(ENV_FILE_NAME)
os.environ.update(vars_dict)

os.environ["ENVIRONMENT"] = "testing"
