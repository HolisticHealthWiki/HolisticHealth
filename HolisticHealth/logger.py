import logging
import sys
from types import FrameType
from typing import Optional, Union

from loguru import logger

from HolisticHealth.config import settings

LOG_LEVEL = logging.getLevelName(settings.log_level.upper())


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        # Get corresponding Loguru level if it exists.
        try:
            level: Union[str, int] = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame: Optional[FrameType] = sys._getframe(6)
        depth = 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


def setup_logging() -> None:
    logging.captureWarnings(True)
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(0)

    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger.configure(handlers=[{"sink": sys.stdout, "level": LOG_LEVEL}])


setup_logging()
