from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
def greetings(name: str = "Recruto", msg: str = "Давай дружить!") -> PlainTextResponse:
    try:
        return PlainTextResponse(
            content=f"Hello {name}! {msg}", 
            media_type="text/plain; charset=utf-8"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")