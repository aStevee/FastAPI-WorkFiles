
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    description = """ 
        This is an application using FAST API that allows users to perform basic statistical calculations on numerical datasets. 
        The application will accept data in the form of lists of numbers and provide statistical results such as mean, median, 
        standard deviation, and sum of the entered numbers using the NumPy library.""",
    version="beta 0.0.1",
    docs_url="/documentation"
    )


@app.get("/")
def read_root():
    return {"result":"the server is actually working!"}



# uvicorn main:app --reload