🌐 FutureReady Hub

A Platform Connecting Youth & Teenage Mothers to Internships, Training Programs, and Free Certifications

📌 Overview

FutureReady Hub is a web platform designed to empower youth and teenage mothers in Rwanda, especially those in rural areas, by providing easy access to:

🎓 Free & low-cost online courses

💼 Internship opportunities

🧰 Resume-building resources

💬 Interview guidance

The platform aims to reduce youth unemployment, promote digital inclusion, and help vulnerable groups gain the skills needed to thrive in the modern digital world.

👉 Live Deployment:
🔗 https://futureready-hub.onrender.com/

📽️ Demo Video

👉 (Insert your Google Drive or YouTube link here)


📄 Documents
Document	Link
SRS Document: https://docs.google.com/document/d/1woWBtP3nX0ZEqEIPqQlUfuZV_FHYtjQpM7_ASFHNVro/edit?tab=t.0

🧩 System Features

✔ User Features

Search for internships

Search for training programs

Simple filters (location, field, description)

Login & Signup

Logout

View resources:

Resume-building templates

Interview tips


✔ Admin Features

Manage training content

Manage internship content

View dashboard


✔ Technical Features

Real-time API-based internship fetching 

Strong error handling

Secure auth system


🛠️ Tech Stack
Frontend

UI libraries:
	1.Bootstrap 
	2.javascript


Backend

Python

Flask Frameworks


Database

SQLite (development)


Deployment

Render Web Service

📦 Folder Structure

FutureReady_Hub/
│
├── backend/
│   ├── __init__.py
│   ├── routes/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   └── app.py (if exists)
│
├── README.md
├── requirements.txt
└── migrations/

🚀 How to Run the Project (Local Setup)


Follow these steps exactly to run the project on your computer.

✔ 1. Clone the Repository
git clone https://github.com/Clarisse-12/FutureReady_Hub.git

cd FutureReady_Hub

✔ 2. Create a Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

✔ 3. Install Dependencies
pip install -r requirements.txt

✔ 4. Set Up Environment Variables

Create a file named:

.env


Inside add:

FLASK_APP=backend
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db

✔ 5. Initialize the Database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

✔ 6. Run the Flask Application
flask run


Your app will run at:

http://127.0.0.1:5000/


🌐 Deployment (Render)


This project is deployed on Render using:

A web service

Gunicorn as the production server

To deploy on Render:

Push your latest code to GitHub

Create new Web Service on Render

Connect to your GitHub repository

Set the Start Command:

gunicorn backend:app


Add environment variables under Render → Environment

Deploy

🔐 Authentication

The platform supports:

User registration

User login

Session authentication

Secure logout

All sensitive data is encrypted during transmission.

📊 SRS Summary


The SRS includes:

Purpose

Problem statement

Actors

Use case diagram

Class diagrams

Activity diagrams

Component diagrams

Functional Requirements (FR)

Non-Functional Requirements (NFR)

You can find the full document here:
👉 (https://docs.google.com/document/d/1woWBtP3nX0ZEqEIPqQlUfuZV_FHYtjQpM7_ASFHNVro/edit?tab=t.0)

🧨 Known Issues & Limitations

Some APIs (Coursera, EDX, Indeed) may require paid API keys

Rural areas may struggle with limited internet access

Render free tier may sleep after inactivity

Future versions will include:

Mobile app

Advanced filters

User profiles

AI career recommendations

🤝 Contributors

Clarisse Mukayiranga
African Leadership University
2025

📬 Contact

If you have questions or want support:

📧 Email: c.mukayiran@alustudent.com
🌍 Website: https://futureready-hub.onrender.com/

🎯 License

This project is for academic use. You may extend or modify it for personal learning.