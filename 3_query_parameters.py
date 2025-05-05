from fastapi import FastAPI

app = FastAPI()

item_list = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return item_list[skip : skip + limit]

