
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from calculations_ import *
from  API_integrations import graphic_deign
from calculations_ import *
import os,asyncio, aiofiles


def get_file(file):
    with open(os.getcwd() + f"/{file}","r") as f:
        return f.read() 


app = FastAPI(
    description = get_file("README.md"),
    version="beta 0.0.1",
    docs_url="/documentation",
)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You might want to specify exact origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def verify_files_and_read(uploaded_file: UploadFile):
    accepted_files = ('.json','.csv','.xlsx')
    
    # Extract filename and file extension
    file_name = uploaded_file.filename
    extension = Path(file_name).suffix  # using pathlib to get the file extension

    if extension not in accepted_files:
        raise ValueError(f"You can only use .json, Excel, and csv extensions. Got {extension}")

    # Read file contents if needed
    file_contents = await uploaded_file.read()

    return file_contents, extension


"""Application start here"""


@app.get("/", description="Simple message where we can see that the server is actually working")
async def root():
    return {"result":"the server is actually working!"}

@app.post("/send_file")
async def post_file(uploadedFile: UploadFile = File(...)):
    file, name = await verify_files_and_read(uploadedFile) # Verify file
    instance = await FileManager.__new__(FileManager)
    await instance.__ainit__(file, name)



    return {"result": uploadedFile.filename}


@app.get("/send_something/{thing}")
def do_something(thing: str):
    return {"Result": f"All correct {thing}!"}



# uvicorn main:app --reload