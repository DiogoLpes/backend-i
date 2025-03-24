from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Fake "database" (list) for testing
reservations = []

class Reservation(BaseModel):
    name: str
    date_time: str  # Format: "2023-10-15 19:00"
    guests: int
    phone: str

@app.post("/make_reservation/")
def make_reservation(reservation: Reservation):
    # Check if slot is already booked
    for r in reservations:
        if r["date_time"] == reservation.date_time:
            raise HTTPException(status_code=400, detail="Time slot already booked!")
    
    reservations.append(reservation.model_dump())
    return {"message": "Reservation successful!"}

@app.get("/view_reservations/")
def view_reservations():
    return reservations

@app.delete("/cancel_reservation/{phone}")
def cancel_reservation(phone: str):
    global reservations
    reservations = [r for r in reservations if r["phone"] != phone]
    return {"message": "Reservation canceled!"}