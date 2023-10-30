from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/products")
def get():
    return  {"message": "this is not working"}