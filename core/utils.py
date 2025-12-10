import sys
from loguru import logger
from constants import Constants as const

def init_logger_and_wandb(config):
    # SOLO logger, niente wandb
    logger_config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | {module}.{function} | <level>{message}</level>",
            },
            {
                "sink": "logging/" + "logger_{time}.log",
                "format": "<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | {module}.{function} | <level>{message}</level>",
            },
        ],
        "extra": {"user": "usr"},
    }

    logger.configure(**logger_config)
    logger.info(f"Logger initialized. Training with config: {config.__dict__}")
