🍽️ QR-Based Restaurant Food Ordering System

A fully responsive, mobile-friendly digital food ordering platform built using Python, Django, HTML, Tailwind CSS & JavaScript.
Customers can scan a QR code placed on the table, browse the menu, add items, place orders, and restaurant staff can manage orders in real time using a dashboard.

🚀 Features
Customer Side (QR Menu)

Scan QR and instantly open menu page

Filter food items by category (Biriyani, Starter, Drinks, etc.)

Add or remove quantity using + / – buttons

“Check Order” preview before placing order

Submit order with table number

Instant Thank You confirmation without refreshing the page

Fully responsive for all mobile screens

Admin / Staff Dashboard

View all active orders from different tables

Displays:

Table number

Ordered items

Time of order

Mark orders as completed

Delete orders

Clean, card-based layout

🛠️ Tech Stack
Frontend

HTML

CSS / Tailwind CSS

JavaScript

Backend

Python

Django Framework

SQLite Database

Django Admin Panel

📁 Project Structure
qr_food_ordering/
│── menu/
│   ├── templates/
│   │   ├── menu.html
│   │   ├── qr.html
│   │   ├── Dashboard.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│── qr_code/
│   ├── settings.py
│   ├── urls.py
│── static/
│── media/
│── db.sqlite3
│── manage.py

🎯 How It Works

Restaurant staff generates a unique QR code for each table.

Customer scans the QR → opens menu/ page on mobile.

Customer selects items, checks order, and places it.

Order is saved with:

Table number

Food list

Timestamp

Dashboard updates in real-time with new orders.

📸 Screenshots (Add Images Later)
![Menu Page](screenshots/menu.png)
![Order Summary](screenshots/summary.png)
![Dashboard](screenshots/dashboard.png)

⚙️ Setup Instructions
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/qr-food-ordering-system.git
cd qr-food-ordering-system

2. Create Virtual Environment
python -m venv env
env\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Migrations
python manage.py migrate

5. Start Server (with your IP)
python manage.py runserver 192.168.xx.xx:8000

🧪 Generate QR Code

Your project automatically generates QR using your IP so customers can scan and view menu on mobile.

👨‍💻 Author

Mayil Vaganan
Python Full Stack Developer