"""
Author: Augustus Rivers <hello@offlabel.design>
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "running", "author": "Augustus Rivers", "site": "https://offlabel.design"}
