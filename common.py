# region: packages

# from dotenv import load_dotenv
from loguru import logger
import os
import sys

# endregion
# region: const


LOG_FORMAT_KEY = "LOG_FORMAT"
LOG_FORMAT_VALUE = "<green>{time}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
LOG_SEVERITY_KEY = "LOG_SEVERITY"
LOG_SEVERITY_VALUE = "TRACE"
LOG_SINK_KEY = "LOG_SINK"
LOG_SINK_STDERR = "sys.stderr"
LOG_SINK_STDOUT = "sys.stdout"
LOG_SINK_VALUE = "stderr"

# endregion
# region: fn

def get_env(env_path=".env"):
    # if os.path.isfile(env_path):
    #     load_dotenv(env_path)
    return dict(os.environ)

def get_logger():
    env.setdefault(LOG_FORMAT_KEY, LOG_FORMAT_VALUE)
    env.setdefault(LOG_SEVERITY_KEY, LOG_SEVERITY_VALUE)
    env.setdefault(LOG_SINK_KEY, LOG_SINK_VALUE)
    
    if env.get(LOG_SINK_KEY) == LOG_SINK_STDOUT:
        sink = sys.stdout
    elif env.get(LOG_SINK_KEY) == LOG_SINK_STDERR:
        sink = sys.stderr
    else:
        sink = env.get(LOG_SINK_KEY)

    logger.remove(0)
    logger.add(sink,
               colorize=True,
               format=env.get(LOG_FORMAT_KEY),
               level=env.get(LOG_SEVERITY_KEY)
              )
    logger.debug(f"logger has been initialized, sink is {env.get(LOG_SINK_KEY)}")

    return logger

# endregion
# region: init

env = get_env()
logger = get_logger()

# endregion