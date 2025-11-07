from loguru import logger
import sys
import os
from django.conf import settings

# Make sure logs directory exists
LOG_DIR = os.path.join(settings.BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, "app.log")

# Remove default logger
logger.remove()

# Add console logging (stdout)
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>")

# Add file logging (rotating)
logger.add(
    LOG_FILE_PATH,
    rotation="10 MB",          # rotate after 10MB
    retention="7 days",        # keep logs for 7 days
    compression="zip",         # compress old logs
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    enqueue=True               # thread/process safe
)
