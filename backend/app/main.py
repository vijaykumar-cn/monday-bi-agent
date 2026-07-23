from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.dashboard import router as dashboard_router
from app.routers.monday import router as monday_router
from app.routers.chat import router as chat_router

app = FastAPI(
    title="Monday BI Agent",
    version="1.0.0",
    description="Business Intelligence Dashboard with AI Chat Assistant",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins temporarily
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(monday_router)
app.include_router(chat_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": "🚀 Monday BI Agent API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }