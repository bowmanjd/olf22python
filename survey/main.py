from fastapi import FastAPI

app = FastAPI()


@app.get("/tools/{tool}")
async def root(tool: str):
    return {"message": f"Hello {tool}"}
