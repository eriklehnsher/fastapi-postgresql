from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/product")
async def posts():
    return await {"msg": "this is not working"}