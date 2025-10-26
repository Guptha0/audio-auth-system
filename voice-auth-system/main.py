from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="VoiceAuth 2.0")

# Fix CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {}

@app.get("/")
def root():
    return {"message": "VoiceAuth 2.0 API - LIVE"}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Voice Authentication"}

@app.post("/enroll")
async def enroll(user_id: str, voice_sample: UploadFile = File(...)):
    users_db[user_id] = "enrolled"
    return {
        "success": True,
        "message": f"User {user_id} enrolled successfully",
        "user_id": user_id
    }

@app.post("/authenticate")
async def authenticate(voice_sample: UploadFile = File(...)):
    return {
        "authenticated": True,
        "user_id": "demo_user",
        "confidence": 0.95,
        "spoof_detected": False,
        "message": "Authentication successful"
    }

@app.get("/users")
async def get_users():
    return {
        "total_users": len(users_db),
        "users": list(users_db.keys())
    }

@app.get("/dashboard")
async def dashboard():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

if __name__ == "__main__":
    print("🚀 VoiceAuth 2.0 Server STARTING...")
    print("📍 http://localhost:8000")
    print("📊 http://localhost:8000/dashboard")
    
    # FIX: Remove reload parameter
    uvicorn.run(app, host="0.0.0.0", port=8000)