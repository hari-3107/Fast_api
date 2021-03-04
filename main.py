from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Halls API
@app.post("/halls/", response_model=schemas.Hall,tags=["Halls"])
def create_hall(hall: schemas.Hall, db: Session = Depends(get_db)):
    db_hall = crud.get_hall_by_id(db, id=hall.id)
    if db_hall:
        raise HTTPException(status_code=400, detail="Id already exists")
    return crud.create_halls(db=db, hall=hall)

@app.get("/halls/", response_model=List[schemas.Hall],tags=["Halls"])
def read_halls(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    halls = crud.get_halls(db, skip=skip, limit=limit)
    return halls

@app.get("/halls/{hall_id}", response_model=schemas.Hall,tags=["Halls"])
def read_hall(hall_id: int, db: Session = Depends(get_db)):
    db_hall = crud.get_hall_by_id(db, id=hall_id)
    if db_hall is None:
        raise HTTPException(status_code=404, detail="Hall not found")
    return db_hall

@app.put("/halls/{hall_id}", response_model=schemas.Hall,tags=["Halls"])
def update_hall(hall_id: str, hall: schemas.Hall, db: Session = Depends(get_db)):
    update = crud.update_hall(db, id=hall_id, hall=hall)
    if update is None:
        raise HTTPException(status_code=404, detail="Hall not found")
    return update

@app.delete("/halls/{hall_id}", response_model=schemas.Hall,tags=["Halls"])
def delete_hall(hall_id: str, db: Session = Depends(get_db)):
    delete = crud.delete_hall(db, id=hall_id)
    return delete

#Customers API
@app.post("/customers/", response_model=schemas.Customer, tags=["Customers"])
def create_customer(customer: schemas.Customer, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, id=customer.id)
    if db_customer:
        raise HTTPException(status_code=400, detail="ID already exists")
    return crud.create_Customer(db=db, customer=customer)


@app.get("/customers/", response_model=List[schemas.Customer],tags=["Customers"])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


@app.get("/customers/{customer_id}", response_model=schemas.Customer,tags=["Customers"])
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@app.put("/customers/{customer_id}", response_model=schemas.Customer,tags=["Customers"])
def update_customer(customer_id: str, customer: schemas.Customer, db: Session = Depends(get_db)):
    update = crud.update_customer(db, id=customer_id, customer=customer)
    if update is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return update

@app.delete("/customers/{customer_id}", response_model=schemas.Customer,tags=["Customers"])
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    delete = crud.delete_customer(db, id=customer_id)
    return delete

#Events API
@app.post("/events/", response_model=schemas.Event,tags=["Events"])
def create_event(event: schemas.Event, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_id(db, id=event.id)
    if db_event:
        raise HTTPException(status_code=400, detail="ID already exists")
    return crud.create_Event(db=db, event=event)
#@app.get("/events/", response_model=List[schemas.Event],tags=["Events"])  -- orignal to be replaced --
@app.get("/events/", response_model=List[schemas.Event], tags=["Events"])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit)
    return events
 
@app.get("/events/{event_id}", response_model=schemas.Event,tags=["Events"])
def read_event(event_id: int, db: Session = Depends(get_db)):
    db_event = crud.get_event_by_id(db, id=event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event
    
@app.put("/events/{event_id}", response_model=schemas.Event,tags=["Events"])
def update_event(event_id: int, event: schemas.Event, db: Session = Depends(get_db)):
    update = crud.update_event(db, id=event_id, event=event)
    if update is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return update

@app.delete("/events/{event_id}", response_model=schemas.Event,tags=["Events"])
def delete_event(event_id: str, db: Session = Depends(get_db)):
    delete = crud.delete_event(db, id=event_id)
    return delete

#Packages API
@app.post("/packages/",response_model=schemas.Package,tags=["Packages"])
def create_package(package: schemas.Package, db:Session = Depends(get_db)):
    db_package = crud.get_package_by_id(db, id=package.id)
    if db_package:
        raise HTTPException(status_code=400, detail="ID already exists")
    return crud.create_package(db=db, package=package)

@app.get("/package/",response_model=List[schemas.Package],tags=["Packages"])
def read_packages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    package = crud.get_packages(db, skip=skip, limit=limit)
    return package

@app.get("/package/{package_id}",response_model=schemas.Package,tags=["Packages"])
def read_package(package_id: int, db: Session = Depends(get_db)):
    db_package = crud.get_package_by_id(db, id=package_id)
    if db_package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return db_package

@app.put("/package/{package_id}", response_model=schemas.Package,tags=["Packages"])
def update_package(package_id: int, package: schemas.Package, db: Session = Depends(get_db)):
    update = crud.update_package(db, id=package_id, package=package)
    if update is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return update

@app.delete("/package/{package_id}", response_model=schemas.Package,tags=["Packages"])
def delete_package(package_id: str, db: Session = Depends(get_db)):
    delete = crud.delete_package(db, id=package_id)
    return delete

#Booked Event Mapper
#@app.post("/book_event/",response_model=schemas.BookEvent, tags=["BookEvent"])
@app.post("/book_event/",response_model=schemas.BookEvent, tags=["BookEvent"])
def create_bookevent(bookevent: schemas.BookEvent, db:Session = Depends(get_db)):
    db_bookevent = crud.get_bookevent_by_id(db, id=bookevent.id)
    if db_bookevent:
        raise HTTPException(status_code=400, detail="ID already exists")
    return crud.create_bookevent(db=db, bookevent=bookevent)


@app.get("/book_event/",response_model=List[schemas.BookEvent],tags=["BookEvent"])
def read_bookevents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookevent = crud.get_bookevent(db, skip=skip, limit=limit)
    return bookevent

@app.get("/book_event/{bookevent_id}",response_model=schemas.BookEvent,tags=["BookEvent"])
def read_bookevent(bookevent_id: int, db: Session = Depends(get_db)):
    db_bookevent = crud.get_bookevent_by_id(db, id=bookevent_id)
    if db_bookevent is None:
        raise HTTPException(status_code=404, detail="Booking Event not found")
    return db_bookevent

@app.put("/book_event/{bookevent_id}",response_model=schemas.BookEvent,tags=["BookEvent"])
def update_bookevent(bookevent_id: int, bookevent: schemas.BookEvent, db: Session = Depends(get_db)):
    update = crud.update_bookevent(db, id=bookevent_id, bookevent=bookevent)
    if update is None:
        raise HTTPException(status_code=404, detail="Booking Event not found")
    return update

@app.delete("/book_event/{bookevent_id}",response_model=schemas.BookEvent,tags=["BookEvent"])
def delete_bookevent(bookevent_id: str, db: Session = Depends(get_db)):
    delete = crud.delete_bookevent(db, id=bookevent_id)
    return delete    