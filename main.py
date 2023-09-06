
from fastapi import FastAPI, File, UploadFile, Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from calculations_ import *
from  API_integrations import graphic_deign
from calculations_ import *
from typing import Optional
import os,asyncio, aiofiles



app = FastAPI(
    description = get_file("README.md"),
    version="beta 0.0.1",
    docs_url="/documentation"
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

    X = await instance.read_file()

    return {"result": X}


@app.get("/send_something/{thing}")
def do_something(thing: str):
    return {"Result": f"All correct {thing}!"}































'''
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="This is a parameter where you have to introduce an ID of your item")): # With Path() allow us some more detail or more enforcement on our parameter
    return {"Item":item_id}
'''
inventory = [
        {
        "name":"Pau",
        "id": 1
        },
        {
        "name":"Raul",
        "id": 2
        },
        {
        "name":"Facundo",
        "id":3
        }
    ]



@app.get("/get-by-name")
def get_by_name(*, name: Optional[str] = None, test: float):
    if name:
        for id in inventory:
            if id["name"] == name:
                return {"Result": f"{id['id']} | {test} |{id['name']} "}
        return {"Message": f"{name} not found"}
    return {"Message":"Input error ( GET /get-by-name?name=VALUE )"}

