# AI Company Research Assistant 🤖

An AI-powered company intelligence tool that researches companies automatically, collects website information, analyzes the data using AI, and generates a downloadable PDF research report.

## 🚀 Live Deployment

### Frontend
https://YOUR_VERCEL_URL

### Backend API
https://YOUR_RENDER_BACKEND_URL

---

# Features

- 🔍 Company research automation
- 🌐 Website crawling
- 🤖 AI-powered company analysis
- 📄 Automatic PDF report generation
- ⚡ FastAPI backend API
- 🎨 Modern web interface
- ☁️ Cloud deployment with Vercel + Render

---

# Project Structure

```
AI-Company-Research-Assistant/

├── frontend/
│   ├── app/
│   ├── components/
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   │   └── main.py
│   │
│   ├── api/
│   │   └── research.py
│   │
│   ├── services/
│   │   └── research_service.py
│   │
│   ├── crawler/
│   ├── search/
│   ├── ai/
│   ├── pdf/
│   ├── requirements.txt
│   └── ...
│
└── README.md
```

---

# Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/DroopLoser/AI-Company-Research-Assistant.git

cd AI-Company-Research-Assistant/backend
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Environment Variables

Create a `.env` file inside the backend folder:

```
OPENAI_API_KEY=your_openai_api_key

SERPER_API_KEY=your_serper_api_key
```

### Required Variables

| Variable | Purpose |
|---|---|
| OPENAI_API_KEY | Used for AI company analysis |
| SERPER_API_KEY | Used for Google search API |

---

## 5. Run Backend Locally

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Go to frontend:

```bash
cd frontend
```

Install packages:

```bash
npm install
```

---

## Environment Variables

Create:

```
.env.local
```

Add:

```
NEXT_PUBLIC_API_URL=https://YOUR_RENDER_BACKEND_URL
```

Example:

```
NEXT_PUBLIC_API_URL=https://ai-company-research-assistant-qrhh.onrender.com
```

---

## Run Frontend Locally

```bash
npm run dev
```

Frontend will run on:

```
http://localhost:3000
```

---

# API Endpoints

## Health Check

```
GET /
```

Response:

```json
{
  "message": "AI Research Backend Running"
}
```

---

## Research Company

```
POST /research/research
```

Request:

```json
{
  "company": "Tesla"
}
```

Response:

```json
{
  "report": {},
  "pdf": "https://backend-url/reports/Tesla_report.pdf"
}
```

---

# Deployment

## Backend Deployment

Backend is deployed using:

- Render
- FastAPI
- Uvicorn

Start command:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## Frontend Deployment

Frontend is deployed using:

- Vercel
- Next.js

Required environment variable:

```
NEXT_PUBLIC_API_URL
```

---

# CORS Configuration

The backend allows requests from the deployed frontend URL.

Example:

```python
allow_origins=[
    "https://your-vercel-domain.vercel.app"
]
```

---

# PDF Reports

Generated reports are stored in:

```
backend/reports/
```

They are served through:

```
/reports/{filename}.pdf
```

Example:

```
https://backend-url.onrender.com/reports/tesla_report.pdf
```

---

# Technologies Used

## Backend

- FastAPI
- Python
- OpenAI API
- BeautifulSoup
- Playwright
- ReportLab

## Frontend

- Next.js
- React
- Tailwind CSS

## Deployment

- Vercel
- Render
- GitHub

---

# Author

Created by DroopLoser

GitHub:
https://github.com/DroopLoser

---

# License

This project is for educational and demonstration purposes.
