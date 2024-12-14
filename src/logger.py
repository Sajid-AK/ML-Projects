'''

We use logging to track and record events, errors, and other information during program execution.
It helps with debugging, monitoring,
and maintaining the code by providing a history of what happens during runtime.


'''

import logging
import os
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
logs_path =os.path.join(os.getcwd(),'logs', LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
        filename=LOG_FILE_PATH,
        format='[%(asctime)s] %(lineno)d %(name)s -%(levelname)s-%(message)s',
        level=logging.INFO,
)

