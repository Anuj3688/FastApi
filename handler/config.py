# config/log_config.py

import logging
import logging.config
import os

LOG_FORMAT = "%(asctime)s — %(name)s — %(levelname)s — %(message)s"

# Get absolute path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, "logs", "app.log")

# Ensure logs directory exists
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": LOG_FORMAT,
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": LOG_FILE_PATH,
            "formatter": "default",
            "level": "INFO",
        },
    },

    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

logging.config.dictConfig(logging_config)
logger = logging.getLogger(__name__)
