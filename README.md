# Fatura Fullstack

A fullstack invoice creation tool with a FastAPI backend and a React frontend.  
🔗 Live Demo: [fatura-fullstack.vercel.app](https://fatura-fullstack.vercel.app)

> **Note:** Backend is hosted on a free tier platform, so the initial request may take 30-50 seconds to spin up if it has been idle.

## Features
* Create an invoice with recipient, seller, product, and tax details
* Automatic total and tax (VAT) calculation
* List and view all saved invoices from the database
* Interactive API documentation via Swagger UI

## Tech Stack

### Backend
* Python
* FastAPI
* SQLAlchemy (ORM)
* Pydantic
* Uvicorn
* SQLite

### Frontend
* React 19
* Vite
* ESLint

## Project Structure
fatura_fullstack/
│
├── backend/     # FastAPI REST API
├── frontend/    # React + Vite UI
└── README.md

## Running the Project

### Backend
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
uvicorn main:app --reload

API docs will be available at: http://127.0.0.1:8000/docs

### Frontend
cd frontend
npm install
npm run dev
Open the local URL printed in the terminal (Vite default: http://localhost:5173).

## API Endpoints

* `GET /` - Check API status
* `POST /invoices` - Create a new invoice
* `GET /invoices` - Retrieve all invoices

## Screenshots
*(Buraya uygulamanın arayüzüne ait bir ekran görüntüsü ekleyebilirsin)*

## Future Improvements
* Authentication & Authorization (JWT)
* PostgreSQL support for production
* Docker setup & containerization
* PDF export and download options for invoices

## Purpose
Built as a portfolio project to practice fullstack development: REST API design with FastAPI and a modern React frontend.
