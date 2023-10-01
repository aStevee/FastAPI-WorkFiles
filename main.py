
from fastapi import FastAPI, File, UploadFile, Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from External_APis.Gmail_API import API_Conection, Send_Email
from calculations_ import *
from DataStrucure import schemas
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
@app.post("/send_email", description="Send an email to paumat17@gmail.com")
async def send_email(body: schemas.EmailStrucure):
    # INFO: In theory, this sends an email, i have to imporve this method anyway
    # WARNING: Remember to make the exceptions in case that the user introduce an incorrect email 

    try:
        recipient = body.to
        subject = body.subject
        message_text = body.message_text

        # Call Gmail API to send the email
        mime_message = Send_Email.PauEmail.create_message(to=recipient, subject=subject, message_text=message_text)
        result = Send_Email.PauEmail.send_message(API_Conection.service, 'me', mime_message)

        return {"Result": result}

    finally:
        pass



if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port = 8432,
        reload=True
    )
