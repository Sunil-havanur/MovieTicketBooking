from django.urls import path
from .views import Theatre_Showtime_view

urlpatterns = [
    path('showtime/<slug>/<date_str>/', Theatre_Showtime_view, name='theatre_showtime'),
]