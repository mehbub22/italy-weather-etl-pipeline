import logging
import os

def setup_logger():
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "pipeline.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(__name__)