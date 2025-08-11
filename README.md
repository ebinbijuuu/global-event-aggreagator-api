# global-event-aggregator-api
Aggregates concerts, tech meetups, sports, and local events from multiple APIs and scrapers into a unified, searchable JSON API. Built with FastAPI, PostgreSQL, and SQLAlchemy, featuring API key auth, rate limiting, and automated daily updates.

# 🌍 Global Event Aggregator API

A **FastAPI-based public API** that aggregates events from multiple sources (concerts, tech meetups, sports, etc.), normalizes the data, and allows users to search & filter events with ease.

## 🚀 Features
- Aggregates data from Eventbrite, Meetup, Ticketmaster, and local city event sites
- Scrapes sites without APIs
- Normalizes event data into a **standard JSON schema**
- Search & filter by location, category, date, and price
- API key authentication & rate limiting
- Live interactive Swagger documentation
- Automated daily event updates

## 🛠 Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL + SQLAlchemy
- **Scraping:** Requests + BeautifulSoup4
- **Auth & Rate Limiting:** API keys + Redis
- **Deployment:** Render / Railway
- **Testing:** Pytest
- **Env Config:** python-dotenv

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/global-event-aggregator-api.git
cd global-event-aggregator-api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
