import numpy as np
import pandas as pd
import sys, os, asyncio

# 1 define datasets



async def verify_files_and_read():
    exception = None
    if not os.path.isdir("files_input"):
        # Create a new file is case doesn't exist
        os.mkdir("files_input")
    if len(os.listdir("files_input")) > 1:
        # Verify if there's less than two files in files_input folder
        raise FileNotFoundError("You must introduce a single folder in /files_input")

    if os.listdir("files_input")[0].endswith(".json"):
        exception = "json"
    elif os.listdir("files_input")[0].endswith(".csv"):
        exception = "csv"
    elif os.listdir("files_input")[0].endswith(".txt"):
        exception = "txt"

    else:
        raise BaseException("You can only use .json and csv extensions")

    return exception

verify_files_and_read()
Data = pd.read_json("files_input/deviation.json")
print(Data)

