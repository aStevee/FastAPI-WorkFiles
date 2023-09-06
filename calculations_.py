import asyncio, os
import numpy as np
import pandas as pd
from pathlib import Path
from async_class import AsyncClass, AsyncObject, task, link
import aiofiles 

path = os.getcwd()
np.set_printoptions(precision=4, suppress=True)

path = os.getcwd()
np.set_printoptions(precision=4, suppress=True)

async def verify_files_and_read(file):
    accepted_files = ('.json','.csv','.xlsx')
    extension = None

    if not file.endswith(accepted_files):        
        raise ValueError("You can only use .json, Excel, and csv extensions")
    
    for acepF in accepted_files:
        if file.endswith(acepF):
            extension = acepF
            break

    return file, extension

def get_file(file):
    with open(os.getcwd() + f"/{file}","r") as f:
        return f.read() 

class FileManager(AsyncObject):
    async def __ainit__(self, file=None, extension=None):
        self._AsyncObject__closed = False 
        self.file = file or ValueError("You haven't provided any file")
        self.extension = extension or ValueError("You haven't provided any extension")

    async def read_file(self, file = None):
        """Read a file and return its values"""
        async with aiofiles.open(self.file or file, "r") as f:
            return await f.read()

    async def extract_some_data_and_check(self, data_frame):
        """Data_frame is our document in str format"""
        columns = data_frame.shape[1]
        rows = data_frame.shape[0]
        return columns, rows

    async def main_function(self):
        print("Hello world, this is the main function where I'll execute the main scripts")

    async def sort_column(self, GivenArray):
        pass

if __name__ == "__main__":
    async def main():
        # Provide a sample file name for testing purposes.
        # You should replace 'sample_file.json' with the actual file path you want to use.
        file_name, extension = await verify_files_and_read('sample_file.json')
        instance = await FileManager.__new__(FileManager)
        await instance.__ainit__(file_name, extension)
        await instance.est

    asyncio.run(main())