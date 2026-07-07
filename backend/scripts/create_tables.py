import sys
import os

# Add the backend directory to Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, backend_dir)

from app.database.database import Base, engine

# Import all models
from app.models import User, ChatSession, Message

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully.")