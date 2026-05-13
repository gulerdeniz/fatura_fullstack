# Invoice Creator — Fullstack

A fullstack web application for creating and managing invoices, built with FastAPI and React.

## Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite
- **Frontend:** React, Vite

## Features

- Create invoices with recipient, seller, product, quantity, price, and VAT
- Automatically calculates total amount including VAT
- Lists all invoices in a table
- REST API with auto-generated documentation

## Project Structure

```
fatura_fullstack/
├── backend/
│   ├── main.py        # API endpoints
│   ├── database.py    # Database connection
│   ├── models.py      # Database models
│   └── schemas.py     # Request/response schemas
└── frontend/
    └── src/
        └── App.jsx    # React UI
```

## Getting Started

### Backend

```bash
cd backend
pip install fastapi uvicorn sqlalchemy
python -m uvicorn main:app --reload
```

API runs at `http://127.0.0.1:8000`
API docs at `http://127.0.0.1:8000/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App runs at `http://localhost:5173`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /invoices | List all invoices |
| POST | /invoices | Create a new invoice |
