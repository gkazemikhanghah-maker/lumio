# Lumio — Job Market Intelligence SaaS

<div align="center">

**Your Career, Illuminated.**

Lumio helps job seekers understand what the market actually wants — before writing their resume.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-00e5a0?style=for-the-badge)](https://relaxed-kelpie-504b6d.netlify.app)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## 🎯 What is Lumio?

Most job seekers waste hours scrolling job boards trying to figure out what skills employers want. **Lumio automates that.**

Unlike competitors (Jobscan, Teal, ResuMax) that start from your resume, **Lumio starts from real market data.**

```
Search Job Title → Market Intelligence → Skill Gap Analysis → AI Resume Builder
```

---

## ✨ Features

- **📊 Market Intelligence** — Top skills, salary ranges, hiring companies & trends for any job title
- **🎯 Skill Gap Analysis** — Tick what you know → get a Market Fit Score out of 100
- **🏢 Company Intel** — Deep-dive into any company's hiring patterns
- **📄 AI Resume Builder** — Conversational resume builder based on real market data
- **📋 Resume Templates** — ATS-optimized templates

---

## 🗂️ Project Structure

```
lumio/
├── frontend/          # React + TypeScript + Tailwind CSS
│   ├── src/
│   │   ├── pages/     # Dashboard, SkillGap, ResumeBuilder, etc.
│   │   ├── components/
│   │   └── lib/       # API calls
│   └── README.md      # Frontend documentation
│
├── backend/           # Python + FastAPI + Claude AI
│   ├── main.py        # API routes + Claude integration
│   ├── requirements.txt
│   └── README.md      # Backend documentation
│
└── README.md          # This file
```

---

## 🚀 Quick Start

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

### Backend

```bash
cd backend
pip install -r requirements.txt
# Create .env file with your ANTHROPIC_API_KEY
uvicorn main:app --reload
```

Open [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18 · TypeScript · Tailwind CSS · Framer Motion |
| Backend | Python · FastAPI |
| AI | Anthropic Claude API |
| Frontend Deploy | Netlify |
| Backend Deploy | Railway |

---

## 🌐 Live Deployment

| Service | URL |
|---------|-----|
| Live App | [relaxed-kelpie-504b6d.netlify.app](https://relaxed-kelpie-504b6d.netlify.app) |
| API | [lumio-backend-production.up.railway.app](https://lumio-backend-production.up.railway.app) |
| API Docs | [lumio-backend-production.up.railway.app/docs](https://lumio-backend-production.up.railway.app/docs) |

---

## 🗺️ Roadmap

- [ ] Live job scraping from Indeed & Glassdoor
- [ ] Real-time salary data from Glassdoor & Levels.fyi
- [ ] Resume PDF export
- [ ] LinkedIn profile import
- [ ] Stripe payments (Free / Pro $15/month)
- [ ] Supabase auth & persistent user profiles

---

## 📄 License

MIT

---

## 👤 Author

**Ghazal Kazemi**

[![GitHub](https://img.shields.io/badge/GitHub-gkazemikhanghah--maker-181717?style=flat&logo=github)](https://github.com/gkazemikhanghah-maker)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/ghazal-kazemi)
