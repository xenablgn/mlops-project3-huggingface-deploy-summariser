import os
import sys
import logging

LOG_DIR="logs"
logging_str= "[%(asctime)s - %(levelname)s - %(module)s - %(message)s]"
log_filepath=os.path.join(LOG_DIR,"continuous_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)


logging.basicConfig(
level=logging.INFO,
format=logging_str,
handlers=[logging.FileHandler(log_filepath),
logging.StreamHandler(sys.stdout)]
)

logger=logging.getLogger("summary_logger")