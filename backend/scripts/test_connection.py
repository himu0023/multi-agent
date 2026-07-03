from app.database.database import engine, SessionLocal
from sqlalchemy import text

try:
    # Test connection
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        print(f"✅ Query result: {result.scalar()}")
    print("✅ Engine created successfully")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    print(f"Error type: {type(e).__name__}")