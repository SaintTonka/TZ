from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def greetings(name: str = "Recruto", msg: str = "Давай дружить!") -> dict:
    try:
        return JSONResponse(content={"message": f"Hello {name}! {msg}"}, media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")