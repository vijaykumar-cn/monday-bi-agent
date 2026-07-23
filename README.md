# 🚀 Monday Business Intelligence Agent

An AI-powered Business Intelligence Dashboard built with **FastAPI**, **React**, **Pandas**, **Monday.com GraphQL API**, and **NVIDIA Llama AI**.

The application connects to a Monday.com workspace, analyzes business data, generates interactive dashboards, and allows users to ask natural language questions about their business using an AI assistant.

---

# Preview

> Dashboard + AI Assistant

- 📊 KPI Dashboard
- 📈 Interactive Charts
- 🤖 AI Business Assistant
- 📋 Monday.com Integration

---

#  Features

## 📊 Dashboard

- Total Deals
- Pipeline Value
- Average Deal Size
- Open Deals

## Analytics

- Pipeline by Stage
- Revenue by Sector
- Deal Status Distribution
- Top Owners Analysis
- Sector Distribution
- Closure Probability

##  AI Business Assistant

Ask questions like:

- Give me a pipeline summary
- Show revenue by sector
- Which owner has the highest deal value?
- List all open deals
- What are the key insights?
- Give recommendations to improve sales.

The AI generates executive summaries and business insights using NVIDIA Llama.

---

#  Tech Stack

## Frontend

- React.js
- Vite
- Tailwind CSS
- Axios
- Recharts
- React Markdown

---

## Backend

- FastAPI
- Pandas
- Requests
- Python

---

## AI

- NVIDIA Build API
- Llama 3.2 Instruct Model

---

## Data Source

- Monday.com GraphQL API

---

# 📂 Project Structure

```
Monday-Business-Intelligence-Agent/

│
├── backend/
│
│   ├── app/
│   │
│   ├── routers/
│   │      dashboard.py
│   │      chat.py
│   │
│   ├── services/
│   │      monday_service.py
│   │      analytics.py
│   │      data_cleaner.py
│   │      llm_service.py
│   │      agent_service.py
│   │
│   ├── models/
│   │
│   ├── config.py
│   └── main.py
│
├── frontend/
│
│   ├── src/
│   │
│   ├── components/
│   │      Dashboard.jsx
│   │      DashboardCharts.jsx
│   │      ChatBox.jsx
│   │      ChatMessage.jsx
│   │      KpiCard.jsx
│   │      Loader.jsx
│   │
│   ├── pages/
│   │      Home.jsx
│   │
│   ├── services/
│   │      api.js
│   │      dashboard.js
│   │
│   └── utils/
│          format.js
│
└── README.md
```

---

# 🏗 Architecture

```
                        +----------------------+
                        |    Monday.com API    |
                        +----------+-----------+
                                   |
                                   |
                          GraphQL Queries
                                   |
                                   |
                    +--------------v-------------+
                    |      FastAPI Backend       |
                    |----------------------------|
                    | Monday Service             |
                    | Data Cleaner               |
                    | Analytics Engine           |
                    | AI Agent                   |
                    +--------------+-------------+
                                   |
             Dashboard API         |        Chat API
                                   |
                    +--------------v-------------+
                    |       React Frontend       |
                    |----------------------------|
                    | KPI Dashboard              |
                    | Recharts                   |
                    | AI Chat                    |
                    +--------------+-------------+
                                   |
                                   |
                               End User
```

---

# 📊 Analytics

The analytics engine computes:

- Total Deals
- Pipeline Value
- Average Deal Size
- Revenue by Sector
- Pipeline by Stage
- Deal Status
- Top Owners
- Open Deals
- Sector Distribution

All calculations are performed using **Pandas**.

---

# 🤖 AI Workflow

```
User Question
       │
       ▼
React Chat
       │
       ▼
FastAPI
       │
       ▼
Agent Service
       │
       ▼
Analytics Summary
       │
       ▼
NVIDIA Llama
       │
       ▼
Business Insight
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/monday-business-intelligence-agent.git

cd monday-business-intelligence-agent
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

```bash
cd frontend

npm install
```

Run

```bash
npm run dev
```

Frontend

```
http://localhost:5173
```

---

# Environment Variables

Create

```
backend/.env
```

```env
MONDAY_API_KEY=your_monday_api_key

DEALS_BOARD_ID=xxxxxxxx

WORKORDER_BOARD_ID=xxxxxxxx

NVIDIA_API_KEY=xxxxxxxx
```

---

# API Endpoints

## Dashboard

```
GET /dashboard/
```

Returns

- KPI Summary
- Charts Data
- Revenue Analysis
- Deal Status
- Owners

---

## Chat

```
POST /chat/
```

Request

```json
{
    "message":"Give me pipeline summary"
}
```

Response

```json
{
    "answer":"Executive Summary..."
}
```

---

# Screenshots

## Dashboard

- KPI Cards
- Revenue Chart
- Pipeline Chart
- Deal Status Pie Chart
- Top Owners

## AI Assistant

- Business Insights
- Executive Summary
- Recommendations

---

# Future Enhancements

- Authentication
- PDF Export
- CSV Export
- Dark Mode
- Multi-board Support
- Multi-user Support
- Real-time Dashboard Updates

---

# Learning Outcomes

This project demonstrates:

- Full Stack Development
- FastAPI
- React
- REST APIs
- GraphQL APIs
- Pandas Data Analysis
- AI Integration
- Dashboard Development
- Business Intelligence
- Prompt Engineering
- Data Visualization

---

# Author

**Vijay Kumar C N**

GitHub: https://github.com/vijaykumar-cn/monday-bi-agent



---

# License

This project is licensed under the MIT License.