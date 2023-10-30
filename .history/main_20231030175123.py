from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/products")
def posts():
    return  {"message": "this is not working"}