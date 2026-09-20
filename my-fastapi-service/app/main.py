from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Lab1"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
