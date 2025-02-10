from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def greetings(name:str = "Recruto", msg:str = "Давай дружить!") -> str:
    try:
        return f"Hello {name}! {msg}"
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")