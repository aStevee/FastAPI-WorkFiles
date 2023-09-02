
from fastapi import FastAPI
from pydantic import BaseModel
from API_integrations import calculations
from API_integrations import graphic_deign
import os,asyncio, aiofiles


def get_file(file):
    with open(os.getcwd() + f"/{file}","r") as f:
        return f.read() 


app = FastAPI(
    description = get_file("README.md"),
    version="beta 0.0.1",
    docs_url="/documentation",
)


"""Application start here"""


@app.get("/", description="Simple message where we can see that the server is actually working")
async def root():
    return {"result":"the server is actually working!"}




# uvicorn main:app --reload