from sqlalchemy import create_engine
from app.config import settings

# Create the engine with the database URL
engine = create_engine(settings.DATABASE_URL)

# Try to connect to the database
try:
    connection = engine.connect()
    print("Connection Successful!")
    connection.close()  # Close the connection after testing
except Exception as e:
    print(f"Error: {e}")
