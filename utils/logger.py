import logging
from colorlog import ColoredFormatter

def setup_logger():
    logger = logging.getLogger("discord_bot")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = ColoredFormatter(
        "[%(asctime)s] %(log_color)s%(levelname)s%(reset)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "blue",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red"
        },
        reset=True
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger