import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info("Named logger info message")
logger.warning("Named logger warning message")
