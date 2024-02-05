"""App Entrypoint"""
from fastapi import FastAPI
import uvicorn
from app_logic import inflect_words

app = FastAPI()


@app.get("/")
async def root():
    """Health Check"""
    return "OK"


@app.get("/pluralize/{text}")
async def pluralize(text: str):
    """Gets a dict of plural words from text.
    Some are not valid"""
    return inflect_words.get_plurals(text)


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
