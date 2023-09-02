
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from io import BytesIO
from PIL import Image

import shutil
import asyncio

class MyData_(BaseModel):
    name: str
    description:str | None = None
    price:float
    tags: list | None = [None]


x = "a"


"""App configuration"""
app = FastAPI(
    description = "This will be my application where i will do some tests about scraping data",
    docs_url="/documentation", redoc_url=None
    )

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""App requests"""

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send_something")
async def send_something(data: MyData_):

    return {
        "Name": str.upper(data.name),
        "desctiption": data.description,
        "len_description": len(data.description),
        "price": data.price,
        "Tags": data.tags
    }


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    with open(Path("image_results") / file.filename, "wb") as buffer:
        result = buffer.rotate(45)
        shutil.copyfileobj(file.file, result)

    return {"filename": file.filename}

@app.get("/download/")
async def download_image(filename: str):
    return FileResponse(Path("image_results") / filename)

@app.get("/loadImage")
@app.get("/loadImage/{filename}")
async def show_image(filename: str):
    """Load image from the database"""
    try:  
        return await FileResponse(Path("image_results") / filename)
       

    except Exception as e:
        return {"An error ocurred": {"Response": f"File {filename} doesen't exists!","Type":"ValueError"}}