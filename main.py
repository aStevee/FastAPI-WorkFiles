
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




"""Application start here"""


@app.get("/proof1")
async def proof1():
    return {"result":"This is an API"}































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

