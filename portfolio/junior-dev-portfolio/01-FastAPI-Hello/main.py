#main.py

from fastapi import FastAPI

app = FastAPI(
    title="Marlou's Portfolio API",
    description="Junior Python Web Developer - FastAPI Track",
    version="0.1.0"

)

@app.get("/")
def home():
    return{
        "message":"Hello from Marlou!",
        "role":"Junior Web developer",
        "status":"Try some API",
        "github":"https://github.com/Chabilis/python-automation"
    }

@app.get("/health")
def health_check():
    return{"status":"Healty"}