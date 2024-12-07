from django.urls import path
from .views import pricing_algorithm_view

urlpatterns = [
    path('pricing/', pricing_algorithm_view, name='pricing'),
]

