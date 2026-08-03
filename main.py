from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    print("hello")
    return {"message" : "hello world"}

