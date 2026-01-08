from django.shortcuts import render
from .models import SearchHistory
import requests , json
from django.conf import settings

api_key = settings.OPENWEATHER_API_KEY
def index(request):
    weather = None
    error = None
    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]  # last 5 searches

    if request.method == "POST":
        city = request.POST.get('city', '').strip()
        if city:

            if api_key == "ADD YOUR API KEY":
                error = "This project requires an OpenWeather API key .Please add your key to settings.py (OPENWEATHER_API_KEY)."
                return render(request, "main/index.html", {
                    'weather': None,
                    'error': error,
                    'recent_searches': recent_searches
                })

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                resp = requests.get(url, timeout=5)

                data = resp.json()

                if resp.status_code == 200:
                    weather = {
                        'city': f"{data['name']}, {data['sys']['country']}",
                        'temperature': data['main']['temp'],
                        'humidity': data['main']['humidity'],
                        'description': data['weather'][0]['description'].title(),
                        'icon': data['weather'][0]['icon'],
                    }
                    
                    SearchHistory.objects.create(
                        city_name=data['name'],
                        temperature=data['main']['temp'],
                        humidity=data['main']['humidity'],
                        description=data['weather'][0]['description'].title()
                    )
                    
                    recent_searches = SearchHistory.objects.order_by('-searched_at')[:5]
                else:
                    error = data.get("message", "Could not fetch weather data.")
            except requests.RequestException:
                error = "Network error. Please try again."
        else:
            error = "Please enter a city name."

    return render(request, "main/index.html", {
        'weather': weather,
        'error': error,
        'recent_searches': recent_searches
    })