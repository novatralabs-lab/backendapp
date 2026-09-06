from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS settings
origins = [
    "https://test1-fawn-zeta.vercel.app",  # Sab origins allow — production mein isko specific domains tak limit karein
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # allowed origins ki list
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, PUT, DELETE, etc. sab allow
    allow_headers=["*"],         # sab headers allow
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Railway!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
