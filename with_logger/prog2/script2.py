import logging
import sys

sys.path.append('../')
from archives import start_logger, task
from prog1 import script1

MY_NAME = "SCRIPT2.PY"
my_name = sys.argv[0]

logger = logging.getLogger(__name__)


def one_task_prog():
    logger.info(f"I am a task of {MY_NAME}")


if __name__ == "__main__":
    # This is equivalent!
    # logging.basicConfig(filename=my_name.replace("py","log"), level=logging.INFO)
    # logging.getLogger().addHandler(logging.StreamHandler())
    
    start_logger.start_log_system(my_name.replace("py","log"))
    
    logger.warning(f"I am {my_name}")
    logger.error(f"I am {my_name}")
    
    task.my_task()
    
    one_task_prog()
    script1.one_task_prog()
