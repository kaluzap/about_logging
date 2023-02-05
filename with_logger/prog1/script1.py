import logging
import sys

sys.path.append('../')
from archives import start_logger, task
from prog2 import script2

MY_NAME = "SCRIPT1.PY"
my_name = sys.argv[0]

logger = logging.getLogger(__name__)


def one_task_prog():
    logger.info(f"I am a task of {MY_NAME}")

    
if __name__ == "__main__":
    
    start_logger.start_log_system(my_name.replace("py","log"))
    
    logger.warning(f"I am {my_name}")
    logger.error(f"I am {my_name}")
    
    task.my_task()
    
    one_task_prog()
    script2.one_task_prog()
