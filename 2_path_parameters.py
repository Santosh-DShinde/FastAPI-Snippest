from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
async def home_app():
    return {"message": "Hello World"}

@app.get("/item/{id}")
async def get_items(id: int):
    try:
        if not id:
            return {"error": "ID is required"}
        if id == 1:
            return {"item": "item 1"}
        elif id == 2:
            return {"item": "item 2"}
        elif id == 3:                                       
            return {"item": "item 3"}
        else:
            return {"item": "item is not found"}
    except Exception as e:
        return {"error": str(e)}
    