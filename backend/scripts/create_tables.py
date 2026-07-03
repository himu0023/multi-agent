import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.database import Base, engine

# Import all models
from app.models import User
from app.models.chat_session import ChatSession  # Add this if you have it

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")