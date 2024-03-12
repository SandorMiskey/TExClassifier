# region: packages

from dotenv import load_dotenv
from loguru import logger
import os
import sys

# endregion
# region: const

LOG_SEVERITY_KEY = "LOG_SEVERITY"
LOG_SEVERITY_VALUE = "TRACE"
LOG_FORMAT_KEY = "LOG_FORMAT"
LOG_FORMAT_VALUE = "<green>{time}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

# endregion
# region: fn

def get_env(env_path=".env"):
    if os.path.isfile(env_path):
        load_dotenv(env_path)
    env_vars = dict(os.environ)
    return env_vars

def get_logger():
    env.setdefault(LOG_SEVERITY_KEY, LOG_SEVERITY_VALUE)
    env.setdefault(LOG_FORMAT_KEY, LOG_FORMAT_VALUE)

    logger.remove(0)
    logger.add(sys.stdout,
               colorize=True,
               format=env.get(LOG_FORMAT_KEY),
               level=env.get(LOG_SEVERITY_KEY)
              )
    logger.debug("logger has been initialized")

    return logger

# endregion
# region: init

env = get_env()
logger = get_logger()

# endregion