# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_restaurant_details, get_weather_data,get_busy_times

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Pricing Algorithm API!")

def pricing_html_view(request):
    # Example data to pass to the template
    menu_items = [
        {"name": "Chicken Curry", "price": 15.99},
        {"name": "Paneer Tikka", "price": 12.99},
        {"name": "Naan Bread", "price": 2.99},
    ]
    return render(request, "pricing.html", {"menu_items": menu_items})

def pricing_algorithm_view(request):
    # Step 1: Fetch Village restaurant details
    village_details = get_restaurant_details("https://www.yelp.com/biz/village-the-soul-of-india-hicksville")

    # Step 2: Fetch nearby restaurant details
    # Add logic to find competitors (using Yelp/Google Maps API)

    # Step 3: Fetch busy times and weather
    busy_times = get_busy_times("https://maps.app.goo.gl/AbLBny2kZBek65Xm7")
    temperature, rain = get_weather_data("YOUR_API_KEY", 20, 10)

    # Step 4: ML Pricing Model
    # Placeholder: Use a simple ML model or a rules-based system
    # Example: Use scikit-learn to predict prices
    
    return JsonResponse({
        "village_details": village_details,
        "busy_times": busy_times,
        "temperature": temperature,
        "rain": rain,
        # Add pricing predictions
    })
