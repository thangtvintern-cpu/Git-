from fastapi import FastAPI

app = FastAPI()

@app.get("/api/health")
def health_check():
    return {"status":"ok","message":"Server is running"}

@app.get("/")
def root():
    return {"message":"Welcome to the API"}