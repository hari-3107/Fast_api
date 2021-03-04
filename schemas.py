from typing import List, Optional
from datetime import date,datetime,time
from pydantic import BaseModel


class Hall(BaseModel):

    id: int
    hall_name: str 

    class Config:
        orm_mode = True

class Customer(BaseModel):

    id: int
    name: str
    phone_no: int
    email: str
    address: str

    class Config:
        orm_mode = True
 
class Event(BaseModel):

    id: int
    event_name: str
    event_price: int

    class Config:
        orm_mode = True

class Package(BaseModel):

    id: int
    package_name: str
    extra_charges: int

    class Config:
        orm_mode = True

class BookEvent(BaseModel):

    id: int
    hall_name: str
    name: str
    phone_no: int
    event: str
    package: str
    start_date: date
    end_date: date
    total_price: int

    class Config:
        orm_mode = True
