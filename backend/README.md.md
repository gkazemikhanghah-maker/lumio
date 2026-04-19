# Lumio — Backend API

<div align="center">

FastAPI backend powering Lumio's Job Market Intelligence engine.

[![API Docs](https://img.shields.io/badge/API%20Docs-Swagger-00e5a0?style=for-the-badge)](https://lumio-backend-production.up.railway.app/docs)
[![Frontend Repo](https://img.shields.io/badge/Frontend-lumio--frontend-7b61ff?style=for-the-badge)](https://github.com/gkazemikhanghah-maker/lumio-frontend)
[![Deployed on Railway](https://img.shields.io/badge/Deployed-Railway-blueviolet?style=for-the-badge)](https://railway.app)

</div>

---

## 🎯 What it does

Accepts a job title + filters → uses **Claude AI (Anthropic)** to generate structured job market intelligence:

- Top in-demand skills with % frequency and trend direction
- Salary ranges (min, median, max) in USD
- Top hiring companies with industry tags
- Rising and falling skill trends
- AI-generated market summary paragraph

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | FastAPI |
| Language | Python 3.12 |
| AI | Anthropic Claude API (`claude-sonnet-4-20250514`) |
| Deployment | Railway |

---

## 📡 API Reference

**Base URL:** `https://lumio-backend-production.up.railway.app`

**Interactive Docs:** `https://lumio-backend-production.up.railway.app/docs`

---

### `GET /health`

Health check.

```json
{"status": "ok"}
```

---

### `POST /analyze`

Generate job market intelligence for a given job title.

**Request:**
```json
{
  "job_title": "Product Manager",
  "experience_level": "Senior",
  "work_type": "Remote",
  "country": "US",
  "max_jobs": 20
}
```

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `job_title` | string | ✅ | — | Target job title |
| `experience_level` | string | ❌ | `"All"` | All / Entry / Mid / Senior / Lead |
| `work_type` | string | ❌ | `"All"` | All / Remote / Hybrid / On-site |
| `country` | string | ❌ | `"US"` | Country code |
| `max_jobs` | integer | ❌ | `20` | Max postings to analyze |

**Response:**
```json
{
  "job_title": "Product Manager",
  "skills": [
    {"name": "Product Strategy", "percentage": 88, "trend": "stable"},
    {"name": "Data Analysis", "percentage": 68, "trend": "up"}
  ],
  "salary": {
    "min": 95000,
    "max": 185000,
    "median": 135000,
    "currency": "USD"
  },
  "companies": [
    {"name": "Google", "count": 12, "industry": "Technology"}
  ],
  "trends": [
    {"skill": "AI/Automation", "direction": "up", "change_pct": 35}
  ],
  "summary": "Product management roles are experiencing strong demand...",
  "total_analyzed": 247,
  "filters": {
    "experience_level": "Senior",
    "work_type": "Remote",
    "country": "US"
  }
}
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip
- Anthropic API key → [console.anthropic.com](https://console.anthropic.com)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/gkazemikhanghah-maker/lumio-backend.git
cd lumio-backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env and add your API key
```

### Environment Variables

Create a `.env` file in the root:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

> ⚠️ Never commit `.env` — it's already in `.gitignore`

### Run Locally

```bash
uvicorn main:app --reload
```

- API: [http://localhost:8000](http://localhost:8000)
- Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📁 Project Structure

```
lumio-backend/
├── main.py              # FastAPI app, routes, Claude integration
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Ignores .env, __pycache__
└── README.md
```

---

## 🌐 Deployment

Deployed on **Railway** with continuous deployment from this GitHub repo.

Every push to `main` automatically triggers a new deployment.

**Environment variables** are set in Railway dashboard (Settings → Variables):
- `ANTHROPIC_API_KEY`

---

## 🗺️ Roadmap

- [ ] Live job scraping from Indeed & Glassdoor via Apify
- [ ] Real salary data from Glassdoor & Levels.fyi
- [ ] Supabase integration for user data & search history
- [ ] Rate limiting (Free: 3/month, Pro: unlimited)
- [ ] Resume generation endpoint
- [ ] Caching layer to reduce API costs

---

## 🔗 Related

- **Frontend:** [lumio-frontend](https://github.com/gkazemikhanghah-maker/lumio-frontend)
- **Live App:** [relaxed-kelpie-504b6d.netlify.app](https://relaxed-kelpie-504b6d.netlify.app)

---

## 📄 License

MIT

---

## 👤 Author

**Ghazal Kazemi** · [GitHub](https://github.com/gkazemikhanghah-maker) · [LinkedIn](https://linkedin.com/in/ghazal-kazemi)
