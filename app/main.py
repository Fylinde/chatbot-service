import threading
import logging
from fastapi import FastAPI
from app.database import get_db
from app.consumers.user_created_consumer import start_user_consuming
from app.consumers.vendor_created_consumer import start_vendor_consuming

# Initialize FastAPI with metadata for Swagger
app = FastAPI(
    title="Chatbot Service API",
    description="API documentation for the Chatbot Service, which handles user interactions and integrates with various consumers.",
    version="1.0.0",
    openapi_tags=[
        {"name": "chatbot", "description": "Operations related to chatbot interactions"},
    ],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Chatbot service is running"}

def start_all_consumers():
    logger.info("Starting all consumers...")
    user_thread = threading.Thread(target=start_user_consuming)
    vendor_thread = threading.Thread(target=start_vendor_consuming)
    user_thread.start()
    vendor_thread.start()
    logger.info("All consumers started")

@app.on_event("startup")
def on_startup():
    logger.info("Starting up the service")
    start_all_consumers()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
