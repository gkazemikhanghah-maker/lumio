# Lumio — Frontend

<div align="center">

**Your Career, Illuminated.**

A Job Market Intelligence SaaS that helps job seekers understand what the market actually wants — before writing their resume.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-00e5a0?style=for-the-badge)](https://relaxed-kelpie-504b6d.netlify.app)
[![Backend Repo](https://img.shields.io/badge/Backend-lumio--backend-7b61ff?style=for-the-badge)](https://github.com/gkazemikhanghah-maker/lumio-backend)

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

### 📊 Market Intelligence
Search any job title and instantly see:
- Top in-demand skills with % frequency and trend direction (↑↓→)
- Salary ranges (min, median, max) in USD
- Top hiring companies with industry tags
- Skill trends — what's rising and what's fading

### 🎯 Skill Gap Analysis
- Tick the skills you already have
- Get a **Market Fit Score** out of 100
- See your missing skills ranked by market importance
- Understand exactly what to learn next

### 🏢 Company Intel
- Search any company
- See which roles they hire for most
- View skills they specifically look for
- Compare their salary ranges to market average

### 📄 AI Resume Builder
- Conversational flow — not a boring form
- AI builds your resume section by section, with your approval
- ATS-optimized output
- Choose from professional templates

### 🔐 Auth & Onboarding
- Sign up / Sign in
- 3-step onboarding to personalize your experience
- Dashboard pre-loaded with your target role

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 18 + TypeScript |
| Styling | Tailwind CSS + shadcn/ui |
| Animations | Framer Motion |
| Routing | React Router v6 |
| Build Tool | Vite |
| Deployment | Netlify |

---

## 📁 Project Structure

```
src/
├── components/
│   ├── ui/                    # shadcn/ui base components
│   ├── Navbar.tsx             # Top navigation bar
│   ├── SearchBar.tsx          # Job title search input
│   └── Logo.tsx               # Lumio logo component
│
├── pages/
│   ├── Landing.tsx            # Homepage with hero, features, pricing
│   ├── Dashboard.tsx          # Market Intelligence results page
│   ├── SkillGap.tsx           # Skill Gap Analysis (2-step flow)
│   ├── ResumeBuilder.tsx      # Conversational AI resume builder
│   ├── Templates.tsx          # Resume template gallery
│   ├── CompanyIntel.tsx       # Company Intelligence page
│   ├── SignUp.tsx             # Registration page
│   ├── SignIn.tsx             # Login page
│   └── Onboarding.tsx         # 3-step onboarding flow
│
├── lib/
│   ├── api.ts                 # Backend API calls + TypeScript interfaces
│   └── mockData.ts            # Fallback mock data
│
└── hooks/                     # Custom React hooks
```

---

## 🚀 Getting Started

### Prerequisites

- Node.js v18+
- npm v9+

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/gkazemikhanghah-maker/lumio-frontend.git
cd lumio-frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Build for Production

```bash
npm run build
```

Output is in the `dist/` folder.

---

## 🔌 Backend Connection

This frontend connects to the [Lumio Backend](https://github.com/gkazemikhanghah-maker/lumio-backend).

The API base URL is set in `src/lib/api.ts`:

```ts
// Production (default)
const API_BASE = "https://lumio-backend-production.up.railway.app";

// Local development
const API_BASE = "http://localhost:8000";
```

---

## 🌐 Deployment

Deployed on **Netlify** with continuous deployment from this GitHub repo.

Every push to `main` automatically triggers a new deployment.

- Build command: `npm run build`
- Publish directory: `dist`
- Redirects: `public/_redirects` handles React Router routes

---

## 🗺️ Roadmap

- [ ] Live job scraping from Indeed & Glassdoor
- [ ] Real-time salary data from Glassdoor & Levels.fyi
- [ ] Resume PDF export
- [ ] LinkedIn profile import
- [ ] Stripe payments (Free / Pro $15/month)
- [ ] Supabase auth & persistent user profiles

---

## 🎨 Design System

| Token | Value |
|-------|-------|
| Background | `#0a0a0f` |
| Primary Accent | `#00e5a0` |
| Secondary | `#7b61ff` |
| Heading Font | Syne |
| Body Font | DM Sans |

---

## 📄 License

MIT

---

## 👤 Author

**Ghazal Kazemi** · [GitHub](https://github.com/gkazemikhanghah-maker) · [LinkedIn](https://linkedin.com/in/ghazal-kazemi)
