from fastapi import FastAPI

app = FastAPI()


@app.get("/home")

def home():
    return "hello world"


@app.get("/about")
def about():
    return "this is about page"