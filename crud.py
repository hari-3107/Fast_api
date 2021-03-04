from sqlalchemy.orm import Session
from sqlalchemy import select,text,cast
from fastapi.encoders import jsonable_encoder
from . import models, schemas
from fastapi import FastAPI, HTTPException
from .database import engine
from sqlalchemy import Integer 
#Halls
def get_halls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hall).offset(skip).limit(limit).all()

def get_hall_by_id(db: Session, id: int):
    return db.query(models.Hall).filter(models.Hall.id == id).first()

def create_halls(db: Session, hall: schemas.Hall):
    db_hall = models.Hall(id=hall.id, hall_name=hall.hall_name)
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)
    return db_hall

def update_hall(db: Session, id: int, hall: schemas.Hall):

    hall_query = db.query(models.Hall).filter(models.Hall.id == id).first()
    for key, value in jsonable_encoder(hall).items():
        setattr(hall_query, key, value)
    db.commit()
    return hall_query   

def delete_hall(db: Session, id: int):
   hall_del = db.query(models.Hall).filter(models.Hall.id == id).first()
   db.delete(hall_del)
   db.commit()
   return hall_del

#Customers
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()

def get_customer_by_id(db: Session, id: int):
    return db.query(models.Customer).filter(models.Customer.id == id).first()

def create_Customer(db: Session, customer: schemas.Customer):
    db_customer = models.Customer(name=customer.name, phone_no=customer.phone_no, email=customer.email, address=customer.address)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def update_customer(db: Session, id: int, customer: schemas.Customer):

    customer_query = db.query(models.Customer).filter(models.Customer.id == id).first()
    for key, value in jsonable_encoder(customer).items():
        setattr(customer_query, key, value)
    db.commit()
    return customer_query

def delete_customer(db: Session, id: int):
   customer_del = db.query(models.Customer).filter(models.Customer.id == id).first()
   db.delete(customer_del)
   db.commit()
   return customer_del

#Events
def get_events(db: Session, skip: int =0, limit: int = 100):
    return db.query(models.Event).offset(skip).limit(limit).all()
 
def get_event_by_id(db: Session, id: int):
    return db.query(models.Event).filter(models.Event.id == id).first()
 
def create_Event(db:Session, event: schemas.Event):
    db_event=models.Event(id=event.id, event_name=event.event_name, event_price=event.event_price)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
 
def update_event(db: Session, id: int, event: schemas.Event):

    event_query = db.query(models.Event).filter(models.Event.id == id).first()
    for key, value in jsonable_encoder(event).items():
        setattr(event_query, key, value)
    db.commit()
    return event_query

def delete_event(db: Session, id: int):
   event_del = db.query(models.Event).filter(models.Event.id == id).first()
   db.delete(event_del)
   db.commit()
   return event_del

#Packages
def get_packages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Package).offset(skip).limit(limit).all()

def get_package_by_id(db: Session, id: int):
    return db.query(models.Package).filter(models.Package.id == id).first()

def create_package(db: Session, package: schemas.Package):
    db_package = models.Package(id=package.id, package_name=package.package_name, extra_charges=package.extra_charges)
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package

def update_package(db: Session, id: int, package: schemas.Package):

    package_query = db.query(models.Package).filter(models.Package.id == id).first()
    for key, value in jsonable_encoder(package).items():
        setattr(package_query, key, value)
    db.commit()
    return package_query

def delete_package(db: Session, id: int):
   package_del = db.query(models.Package).filter(models.Package.id == id).first()
   db.delete(package_del)
   db.commit()
   return package_del    

#BookEvent
def get_bookevent(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BookEvent).offset(skip).limit(limit).all()

def get_bookevent_by_id(db: Session, id: int):
    return db.query(models.BookEvent).filter(models.BookEvent.id == id).first()

def create_bookevent(db: Session, bookevent: schemas.BookEvent):
    db_bookevent = models.BookEvent(id=bookevent.id, hall_name=bookevent.hall_name, 
    name=bookevent.name, phone_no=bookevent.phone_no, event=bookevent.event, 
    package=bookevent.package, start_date=bookevent.start_date, end_date=bookevent.end_date, 
    total_price=bookevent.total_price)
    sql_query_hall= text("select hall_name from halls")
    sql_query_name= text("select name from customers")
    sql_query_mobile= text("select phone_no from customers")
    sql_query_event_name= text("select event_name from events")
    sql_query_package_name= text("select package_name from packages")
    hall_names = []
    customer_names = []
    customer_mobile = []
    event_names = []
    package_names = []
    result = db.execute(sql_query_hall)
    for row in result:
        hall_names.append(row.hall_name)
    if bookevent.hall_name not in hall_names :
        raise HTTPException(status_code=404, detail="Invalid hall name")
    result = db.execute(sql_query_name)
    for row in result:
        customer_names.append(row.name)
    if bookevent.name not in customer_names :
        raise HTTPException(status_code=404, detail="Invalid customer name")
    result = db.execute(sql_query_mobile)
    for row in result:
        customer_mobile.append(row.phone_no)
    if bookevent.phone_no not in customer_mobile :
        raise HTTPException(status_code=404, detail="Invalid phone number")
    result = db.execute(sql_query_event_name)
    for row in result:
        event_names.append(row.event_name)
    if bookevent.event not in event_names :
        raise HTTPException(status_code=404, detail="Invalid event name")
    result = db.execute(sql_query_package_name)
    for row in result:
        package_names.append(row.package_name)
    if bookevent.package not in package_names :
        raise HTTPException(status_code=404, detail="Invalid package name")
    else :
        #sql_query_marriage= text("SELECT count(id) from book_event where event='marriage'")
        sql_query_marriage = text("SELECT count(id) from book_event where (event='marriage' and start_date= +\"bookevent.start_date\"+ and end_date= +\"bookevent.start_date+\"+)")
        result = db.execute(sql_query_marriage)
        #print(type(result))
        #print(result.first()[0])
        number_of_marriages = result.first()[0]
        print(number_of_marriages)
        db.add(db_bookevent)
        db.commit()
        db.refresh(db_bookevent)
        return db_bookevent

def update_bookevent(db: Session, id: int, bookevent: schemas.BookEvent):

    bookevent_query = db.query(models.BookEvent).filter(models.BookEvent.id == id).first()
    for key, value in jsonable_encoder(bookevent).items():
        setattr(bookevent_query, key, value)
    db.commit()
    return bookevent_query

def delete_bookevent(db: Session, id: int):
   bookevent_del = db.query(models.BookEvent).filter(models.BookEvent.id == id).first()
   db.delete(bookevent_del)
   db.commit()
   return bookevent_del        