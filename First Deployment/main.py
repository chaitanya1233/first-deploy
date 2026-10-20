from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="First Deploy")

class Text(BaseModel):
    text : str


@app.get("/health")
def health():
    return {"status":"ok"}


@app.post("/predict")
def predict(data : Text):
    return {"length":len(data.txt), "words":len(data.txt.split())}

