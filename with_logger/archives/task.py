import logging

logger = logging.getLogger(__name__)


def my_task():
    logger.info("I am my_task with INFO")
    logger.warning("I am my_task with WARNING")
    logger.error("I am my_task with ERROR")
    logger.debug("I am my_task with DEBUG")
