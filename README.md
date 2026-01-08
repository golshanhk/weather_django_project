# 🌤 Django Weather App

A simple and clean weather application built with Django that fetches real-time weather data using the OpenWeather API.

This project is created for learning purposes and as a portfolio project.

---

## 🚀 Features
- Search weather by city name
- Real-time temperature (°C)
- Humidity information
- Weather description and weather icon
- Save recent search history
- Error handling for invalid city names and network issues
- Secure API key handling via Django settings

---

## 🛠 Tech Stack
- Python
- Django
- OpenWeather API
- HTML / CSS
- Requests library

---

## 📂 Project Structure
weather/
├── main/
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ └── templates/
├── weather/
│ ├── settings.py
│ └── urls.py
├── manage.py
├── requirements.txt
└── README.md


## ⚙ Installation & Setup

### 1. Clone the repository

git clone https://github.com/golshanhk/django-weather-app.git
cd django-weather-app
2. Create and activate virtual environment

Copy code
python -m venv venv
Windows:


Copy code
venv\Scripts\activate
Linux / macOS:


Copy code
source venv/bin/activate
3. Install dependencies

Copy code
pip install -r requirements.txt
4. Set OpenWeather API Key
Open settings.py and add:

python
Copy code
OPENWEATHER_API_KEY = "YOUR_API_KEY"
Get your API key from:
https://openweathermap.org/


5. Run migrations


python manage.py migrate
6. Run development server

python manage.py runserver
Open your browser and go to:

http://127.0.0.1:8000/

📌 Notes
This project is built for practice and portfolio purposes

API keys should be kept secret in real-world projects

Feel free to improve UI or add new features

👤 Author
Golshan_Hooshamnd
گلشن_هوشمند