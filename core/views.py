from django.shortcuts import render
from .models import Crop
from django.contrib.auth.decorators import login_required
import requests


def home(request):
    crops = Crop.objects.all()
    return render(request, 'core/home.html', {'crops': crops})


def contact(request):
    return render(request, 'core/contact.html')


def help_page(request):
    return render(request, 'core/help.html')


@login_required
def dashboard(request):
    # For now show all crops; later associate Farmer with auth.User and filter per-user
    crops = Crop.objects.all()

    # Weather API (safe request)
    city = "Patna"
    api_key = "76202208983353818c42baee1567b4c1"
    temp = None
    desc = None
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            temp = data.get('main', {}).get('temp')
            weather = data.get('weather')
            if weather and len(weather) > 0:
                desc = weather[0].get('description')
    except Exception:
        # Don't propagate external API errors to user
        temp = None
        desc = None

    return render(request, 'core/dashboard.html', {
        'crops': crops,
        'temp': temp,
        'desc': desc,
    })


def weather(request):
    """Return only the current weather card (uses same API as dashboard)."""
    city = "Patna"
    api_key = "76202208983353818c42baee1567b4c1"
    temp = None
    desc = None
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            temp = data.get('main', {}).get('temp')
            weather = data.get('weather')
            if weather and len(weather) > 0:
                desc = weather[0].get('description')
    except Exception:
        temp = None
        desc = None

    return render(request, 'core/weather.html', {
        'temp': temp,
        'desc': desc,
    })
