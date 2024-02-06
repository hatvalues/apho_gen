"""App Entrypoint"""
from fastapi import FastAPI, APIRouter
import uvicorn
from routes import inflect_end_point
from routes import apho_end_point

app = FastAPI()
api_router = APIRouter()
api_router.include_router(apho_end_point.router)
api_router.include_router(inflect_end_point.router)
app.include_router(api_router)

@app.get("/")
async def root():
    """Health Check"""
    return "OK"

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
