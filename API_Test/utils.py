import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("api-test")

def retry(func, retries=3, delay=2):
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            logger.warning(f"Attempt {attempt} failed: {e}")
            if attempt == retries:
                raise
            time.sleep(delay)
