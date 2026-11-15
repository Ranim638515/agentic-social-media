from fastapi import FastAPI

app = FastAPI(title="Agentic AI Social Media")


@app.get("/health")
def health():
    return {"status": "ok"}
