from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(
    title="FastAPI Application",
    description="This is a simple FastAPI application",
    version="1.0.0",
)

@app.get("/home", response_class=HTMLResponse)
async def home_app():
    return """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>

        <body>
            <H1>THIS IS MY FIRST APPLICATION IN FAST API</H1>
        </body>

        </html>
    """
