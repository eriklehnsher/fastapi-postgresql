from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/product")
async def posts():
    return{"msg": "this is not working"}