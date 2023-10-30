from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/products")
def posts():
    return  {"msg": "this is not working"}