# Life OS 2026

> A personal life management web application designed to help you organize,
> track, and achieve your goals across all areas of life.

##  Table of Contents
- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Database Schema](#database-schema)
- [Contributing](#contributing)

---

## Project Overview

**Life OS 2026** is a full-stack web application that serves as a personal
"operating system" for life management. It consolidates goal tracking,
journaling, financial management, health tracking, learning progress,
and strategic planning into one unified dashboard.

### Problem Statement
Managing multiple aspects of life (goals, finances, health, learning,
scheduling) across disconnected tools leads to fragmented progress tracking
and lack of holistic visibility into personal development.

### Solution
A single, unified web application that provides:
- A central dashboard ("Life Command Center") for at-a-glance life overview
- Modular pages for deep-diving into specific life areas
- Progress tracking with visual indicators
- Mood and journal tracking for mental health awareness
- Financial tracking with savings goals and investment monitoring
- Quarterly strategic planning with the "Game Plan" system

### Target User
- Primary: Personal use (Malaika Nghona / "Laika")
- Secondary: Extensible for others who want a personal life OS

---

##  Tech Stack

### Frontend
| Technology       | Purpose                        |
|-----------------|--------------------------------|
| React 18+       | UI Library                     |
| React Router    | Client-side routing            |
| Tailwind CSS    | Utility-first styling          |
| Axios           | HTTP client for API calls      |
| Chart.js / Recharts | Data visualization         |
| Lucide React    | Icon library                   |
| Vite            | Build tool & dev server        |

### Backend
| Technology       | Purpose                        |
|-----------------|--------------------------------|
| Django 5.x      | Main backend framework & ORM   |
| Django REST Framework | REST API layer            |
| FastAPI          | Real-time/async endpoints (weather, chatbot) |
| PostgreSQL       | Primary database               |
| Redis            | Caching & session management   |
| Celery           | Background task processing     |

### DevOps / Tools
| Technology       | Purpose                        |
|-----------------|--------------------------------|
| Git / GitHub     | Version control                |
| Docker           | Containerization               |
| pytest / Jest    | Testing                        |
| Swagger / Redoc  | API documentation              |
| GitHub Projects  | Agile board                    |

---

### Features

### 1. Dashboard (Life Command Center)
- Word of the Year display
- Vision Board (image collage)
- Goals overview with progress bars
- Today's Focus widget
- Today's Schedule widget
- Finance Overview widget
- Learning summary widget
- Health & Activity summary widget
- Motivational quote

### 2. Calendar
- Weekly/Monthly calendar view
- Event creation, editing, deletion
- Color-coded event categories
- Integration with Today's Schedule on dashboard

### 3. Journal
- Daily journal entries with mood selection
  (Amazing, Good, Okay, Bad, Stressed)
- Rich text writing area
- Quick Mood Log (log mood without journaling)
- 2026 Mood Calendar (yearly heatmap visualization)
- Previous entries archive with "View All"

### 4. Game Plan
- 2026 Vision overview
- Quarterly breakdown (Q1-Q4) with:
  - Key Focus Areas
  - Related Goals (linked from Goals)
  - Strategy & Action Plan (free text)
  - Optimization & Improvements (free text)
  - Quarter Progress metrics

### 5. Learning & Education
- Course tracking by category (Cybersecurity, Finance, School)
- Overall Progress percentage
- Completed Modules counter
- Active Courses counter
- Individual course progress tracking

### 6. Finance
- Monthly Income / Expenses / Total Savings / Net Worth (ZAR)
- Savings Goals with progress bars
- Income vs Expenses chart
- Expense Breakdown by category
- Trading Portfolio Performance
- Trading Stats (Total Invested, Current Value, Profit/Loss)

### 7. Health
- Workout Programs (create custom routines)
- Monthly Progress tracking
- Achievements / Badges system
- Activity logging

### 8. Settings
- Profile management (Full Name, Nickname, Email)
- Notification preferences (Daily Reminders, Goal Updates, Workout Reminders)
- Appearance (Light/Dark theme, Compact View toggle)
- Privacy & Security (Change Password, 2FA, Export Data)
- Language & Region (Language, Timezone, Currency)

### 9. Chatbot (AI Assistant)
- Floating chat button
- Personal AI assistant for productivity

---

##  Architecture

### High-Level Architecture
