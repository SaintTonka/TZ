from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def greetings(name: str = "Recruto", msg: str = "Давай дружить!") -> PlainTextResponse:
    return PlainTextResponse(
        content=f"Hello {name}! {msg}",
        media_type="text/plain; charset=utf-8"
    )