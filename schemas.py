from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FilamentBase(BaseModel):
    brand: str
    material: str
    color: str
    diameter: float = 1.75
    weight: Optional[float] = None
    storage_location: Optional[str] = None
    nozzle_temp_min: Optional[int] = None
    nozzle_temp_max: Optional[int] = None
    nozzle_temp_recommended: Optional[int] = None
    bed_temp: Optional[int] = None
    print_speed_recommended: Optional[int] = None
    notes: Optional[str] = None
    purchase_date: Optional[datetime] = None
    purchase_price: Optional[float] = None

class FilamentCreate(FilamentBase):
    pass

class FilamentUpdate(BaseModel):
    brand: Optional[str] = None
    material: Optional[str] = None
    color: Optional[str] = None
    diameter: Optional[float] = None
    weight: Optional[float] = None
    storage_location: Optional[str] = None
    nozzle_temp_min: Optional[int] = None
    nozzle_temp_max: Optional[int] = None
    nozzle_temp_recommended: Optional[int] = None
    bed_temp: Optional[int] = None
    print_speed_recommended: Optional[int] = None
    notes: Optional[str] = None
    purchase_date: Optional[datetime] = None
    purchase_price: Optional[float] = None

class FilamentResponse(FilamentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True