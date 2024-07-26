from fastapi import FastAPI, Path
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}

# @app.get("/hello/{name}/{age}")
# async def hello(name:str,age:int):
#    return {"name": name, "age":age} 

@app.get("/hello")
async def hello(name:str,age:int):
   return {"name": name, "age":age}

@app.get("/hello/{name}")
async def hello(name:str=Path(...,min_length=3,
max_length=10)):
   return {"name": name}

class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []
   
@app.post("/students/")
async def student_data(s1: Student):
   return s1