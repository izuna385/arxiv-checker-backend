import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/papers/")
def read_nlp_papers(num: int = 10):
    return {"num": num}


if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000,
                log_level="trace", debug=True)
