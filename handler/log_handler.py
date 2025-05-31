import functools
import logging
import os
import logging

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Create logs directory if it doesn't exist
log_dir = os.path.join(base_dir, "..", "logs")
os.makedirs(log_dir, exist_ok=True)

# Define log file path
log_file_path = os.path.join(log_dir, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()  # Optional: also log to console
    ]
)

logger = logging.getLogger(__name__)

def log_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        logging.info(f"--> Called function: {func_name} | Args: {args} | Kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"<-- Finished function: {func_name} | Returned: {result}")
            return result
        except Exception as e:
            logging.error(f"!! Error in function: {func_name} | Error: {e}", exc_info=True)
            raise e
    return wrapper
