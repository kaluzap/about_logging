import logging
import sys

sys.path.append('../')
from archives import task
from prog2 import script2

MY_NAME = "SCRIPT1.PY"
my_name = sys.argv[0]


def one_task_prog():
    logging.info(f"I am a task of {MY_NAME}")


if __name__ == "__main__":
    logging.basicConfig(filename=my_name.replace("py","log"), level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    
    logging.warning(f"I am {my_name}")
    logging.error(f"I am {my_name}")
    
    task.my_task()
    
    one_task_prog()
    script2.one_task_prog()
