from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/product")
def posts():
    return  {"msg": "this is not working"}