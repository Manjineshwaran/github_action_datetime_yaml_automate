import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)
from datetime import datetime

# Get current time
if __name__=="__main__":
    current_time = datetime.now().strftime("%H:%M:%S")
    logger.info(f"Current time is: {current_time}")
    print("Current time is:", current_time)