# Contact Manager Web Application

## Overview

This project is a client–server web application written in Python that allows users to manage a list of contacts. Users can:

- Add new contacts  
- View all contacts  
- Edit contacts inline  
- Delete contacts  

Each contact contains:

- Name  
- Phone number  
- Address  

The system uses a layered object-oriented architecture and an SQLite database for persistent storage.

---

## Architecture

The application follows a multi-layer design:

Client (HTML + JavaScript)  
→ Controller Layer  
→ Service Layer  
→ Repository Layer  
→ SQLite Database  

### Layers

**Model**
- `Contact`
- Represents a single contact entity.

**Repository**
- `ContactRepository`
- Handles direct interaction with SQLite.

**Service**
- `ContactService`
- Contains business logic.
- Acts as an intermediary between controller and repository.

**Controller**
- `ContactController`
- Translates HTTP requests into service calls.
- Formats responses as JSON.

**Server**
- `ContactHandler`
- Subclass of `SimpleHTTPRequestHandler`.
- Routes HTTP requests to the controller.

---

## Project Structure

```
contacts-app/
│
├── server.py
├── controller.py
├── service.py
├── database.py
├── models.py
├── contacts.db
│
└── static/
    ├── index.html
    └── app.js
```

---

## Technologies Used

- Python
- Built-in `http.server`
- SQLite (via `sqlite3`)
- HTML
- CSS
- JavaScript (Fetch API)

---

## How to Run

Step 1: Clone the repository

```
git clone [<your-repository-url>](https://github.com/LunaticSage218/contacts-app)
cd contacts-app
```

Step 2: Run the server

```
python server.py
```

Step 3: Open in browser

```
http://localhost:8000
```

The database file (`contacts.db`) will be created automatically if it does not exist.

---

## API Endpoints

GET `/api/contacts`  
Returns all contacts as JSON.

POST `/api/contacts`  
Creates a new contact.  
Body must contain JSON with:
- name
- phone
- address

PUT `/api/contacts/{id}`  
Updates an existing contact.

DELETE `/api/contacts/{id}`  
Deletes a contact by ID.

---

## Author

Larry Griffith, Jack Morris, Yahir Espinoza  
CS 440 Software Architecture
Spring 2026
