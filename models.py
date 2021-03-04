from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date,Time
from sqlalchemy.orm import relationship

from .database import Base


class Hall(Base):
    __tablename__ = "halls"

    id = Column(Integer)
    hall_name = Column(String, primary_key=True)

    hall_rel = relationship("BookEvent")

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, index=True)
    name = Column(String)
    phone_no = Column(Integer, primary_key=True, unique=True)
    email = Column(String, unique=True)
    address = Column(String)

    customer_rel = relationship("BookEvent")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, index=True)
    event_name = Column(String, primary_key=True, unique=True)
    event_price = Column(Integer)

    event_rel = relationship("BookEvent")

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, index=True)
    package_name = Column(String,primary_key=True, unique=True)
    extra_charges = Column(Integer)

    package_rel = relationship("BookEvent")

class BookEvent(Base):
    __tablename__ = "book_event"

    id = Column(Integer, primary_key=True, index=True)
    hall_name = Column(String, ForeignKey('halls.hall_name'))
    name = Column(String)
    phone_no = Column(Integer, ForeignKey('customers.phone_no'))
    event = Column(String, ForeignKey("events.event_name"))
    package = Column(String, ForeignKey("packages.package_name"))
    start_date = Column(Date)
    #start_time = Column(Time)
    end_date = Column(Date)
    #end_time = Column(Time)
    total_price = Column(Integer)
