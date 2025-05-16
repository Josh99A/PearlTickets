# 🚍 Pearl Tickets

**Pearl Tickets** is a web-based bus ticketing system designed to make intercity travel in Uganda faster, smarter, and more convenient. Built with Django and Django Template Language (DTL), the platform allows users to search, book, and pay for bus trips, while giving bus companies tools to manage schedules, view reports, and optimize operations.

---

## 🌟 Features

- 🚌 Search and browse available bus trips
- 🎫 Book tickets and select seats
- 💳 Handle payments with mobile money or card
- 🧾 View e-tickets and booking history
- 🧑‍💼 Admin panel for bus operators to manage trips
- 📊 Daily sales and trip reports
- 🌍 Integrated with mapping services for route information
- 🏞 Tourist attraction listings and featured banners

---

## 🛠️ Tech Stack

- **Backend**: Django (Function-Based Views)
- **Frontend**: Django Templates + bootstrap5 CSS
- **Database**: PostgreSQL / SQLite (for dev)
- **Image Handling**: Django Media
- **Styling**: Custom Figma-based design system with CSS variables

---

## 🚀 Getting Started

### 🔽 Clone the Repository

```bash
git clone https://github.com/Josh99A/PearlTickets
cd PearlTickets
```

---

## Create and Activate a virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 🔽 Install dependencies
pip install -r requirements.txt


## Apply Migrations
python manage.py makemigrations
python manage.py migrate

## Create a Superuser
python manage.py createsuperuser

## Run development server
python manage.py runserver



