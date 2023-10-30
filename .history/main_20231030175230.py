from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/products")
def get_root():
    return  {"message": "this is not working"}