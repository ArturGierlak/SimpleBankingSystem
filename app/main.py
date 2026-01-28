from fastapi import FastAPI
import uvicorn

def create_app():
    app = FastAPI(title = "Simple Banking System")

    return app

app = create_app()

@app.get("/")
def status():
    return {"status": "Ok"}