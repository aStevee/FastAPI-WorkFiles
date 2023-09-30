
from fastapi import FastAPI, File, UploadFile, Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from External_APis import testing1
from calculations_ import *
from typing import Optional
import os,asyncio, aiofiles
import uvicorn


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

@app.get("/")
def main():
    return {"result":"server is actually working! You can use the diferents methods!"}

@app.get("/proof1")
async def proof1():
    return {"result":"This is an API"}


"""End this method"""
@app.post("/send_email/{user_email}")
async def send_email(user_email: str, ): # Write a schema here
    pass




if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port = 8432,
        reload=True
    )
