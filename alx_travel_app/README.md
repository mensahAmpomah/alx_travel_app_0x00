# alx_travel_app_0x00 – Django Listings App

A Django REST API for managing travel **Listings**, **Bookings**, and **Reviews**, including database modeling, serializers, and a management command for seeding sample data.

This project was created as part of the **ALX Backend Specialization – Django Tasks**.

---

## Features

- Manage travel listings  
- Create and manage bookings  
- Post reviews for listings  
- Seed database with sample data  
- REST API-ready with serializers  
- Clean database relationships and constraints  

---

## Tech Stack

- Python 3.x  
- Django  
- Django REST Framework  
- SQLite / PostgreSQL  
- Management Commands 


## Models Overview

### **Listing**
- Title  
- Description  
- Price per Night  
- Location  
- Availability  
- Created At  

### **Booking**
- User (FK)  
- Listing (FK)  
- Check-in / Check-out  
- Date constraint ensuring check-out > check-in  

### **Review**
- User (FK)  
- Listing (FK)  
- Rating (1–5)  
- Comment  
- Created At 

- `ListingSerializer`
- `BookingSerializer`

These convert Django model instances into JSON for API responses.

---

##  Database Seeding (Sample Data)

A custom command is provided to populate the database with sample listings.
