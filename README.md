# ASO Tracker

**ASO Tracker** is a lightweight tool to help developers and marketers track **App Store Optimization (ASO) keywords** and app rankings. It currently supports tracking apps on **iOS** (Apple App Store) and is designed for future support for **Google Play**.  

This project is built with **FastAPI** and **PostgreSQL**, making it easy to extend into a SaaS in the future.  

---

## Features

- Add and manage apps to track
- Add keywords to monitor for each app
- Store and track keyword rankings over time
- Simple backend API ready for frontend integration

**Future plans:**
- Graphs and analytics for keyword performance
- Competitor keyword tracking
- Machine learning models to predict high-impact keywords

---

## Tech Stack

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Environment management:** `uv` (Astral.sh) or virtualenv  
- **HTTP requests:** `httpx` (for API fetching)  
- **Environment variables:** `python-dotenv`  

---
