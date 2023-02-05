import logging
import sys

sys.path.append('../')
from archives import task
from prog2 import script2

MY_NAME = "SCRIPT1.PY"
my_name = sys.argv[0]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def one_task_prog():
    logger.info(f"I am a task of {MY_NAME}")

    
if __name__ == "__main__":
    
    # https://docs.python.org/3/howto/logging-cookbook.html
    
    # create file handler which logs even debug messages
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    
    logger.warning(f"I am {my_name}")
    logger.error(f"I am {my_name}")
    
    task.my_task()
    
    one_task_prog()
    script2.one_task_prog()
