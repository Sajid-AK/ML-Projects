import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging

import os
import sys
import dill

import dill # Save a Python object to a file. working as pikling 
import os  # Import the os module to work with file paths and directories

# Function to save an object to a specified file path
def save_object(file_path, obj):
    try:
        # Extract the directory path from the provided file path (removes file name)
        dir_path = os.path.dirname(file_path)

        # Create the directory if it doesn't exist; exist_ok=True prevents error if it already exists
        os.makedirs(dir_path, exist_ok=True)

        # Open the specified file path in write-binary mode ('wb')
        with open(file_path, 'wb') as file_obj:
            # Serialize and save the Python object to the file using dill
            dill.dump(obj, file_obj)  # 'dill.dump()' saves the object in the file

    except Exception as e:
        # If an error occurs, raise a custom exception with the error details
        raise CustomException(e, sys)  # Ensure CustomException is defined elsewhere in your code
