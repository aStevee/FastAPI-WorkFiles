import asyncio, os
import numpy as np
import pandas as pd
from pathlib import Path

path = os.getcwd()

async def verify_files_and_read():
    file = None
    extension = None
    if not os.path.isdir("files_input"): # Create a new file in case doesn't exist
        print("There isn't any file in your directory, and by this way i've created. Put your file\nin the 'files_input' folder and execute this again!")
        os.mkdir("files_input")
    if len(os.listdir("files_input")) > 1:
        # Verify if there's less than two files in files_input folder
        raise FileNotFoundError("You must introduce a single folder in /files_input")

    if os.listdir("files_input")[0].endswith(".json"):        
        extension = "json"
    elif os.listdir("files_input")[0].endswith(".csv"):
        extension = "csv"
    elif os.listdir("files_input")[0].endswith(".xlsx"):
        extension = "xlsx"
    else:
        raise BaseException("You can only use .json and csv extensions")

    file = os.listdir("files_input")[0]
    return file, extension


async def read_with_pandas():
    file, extension = await verify_files_and_read()

    if extension == "csv":
        Data_Frame = pd.read_csv(Path("files_input" / file))
    elif extension == "json":
        Data_Frame = pd.read_json(Path("files_input" / file))
    elif extension == "xlsx":
        Data_Frame = pd.read_excel(Path("files_input" / file))
        
    return Data_Frame

async def extract_some_info(data_frame):
    pass


async def main_function():
    print("Hello world, this is the main function where I'll execute the main scripts")