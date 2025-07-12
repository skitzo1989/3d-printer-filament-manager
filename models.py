from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Filament(Base):
    __tablename__ = "filaments"
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(100), nullable=False)
    material = Column(String(50), nullable=False)  # PLA, ABS, PETG, etc.
    color = Column(String(50), nullable=False)
    diameter = Column(Float, nullable=False, default=1.75)  # Usually 1.75mm or 3mm
    weight = Column(Float, nullable=True)  # Weight in grams
    storage_location = Column(String(100), nullable=True)
    
    # Temperature settings
    nozzle_temp_min = Column(Integer, nullable=True)
    nozzle_temp_max = Column(Integer, nullable=True)
    nozzle_temp_recommended = Column(Integer, nullable=True)  # Manufacturer recommended temp
    bed_temp = Column(Integer, nullable=True)
    
    # Print settings
    print_speed_recommended = Column(Integer, nullable=True)  # mm/s
    
    # Additional info
    notes = Column(Text, nullable=True)
    purchase_date = Column(DateTime, nullable=True)
    purchase_price = Column(Float, nullable=True)
    
    # Tracking
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Database setup
DATABASE_URL = "sqlite:///./filament_inventory.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()