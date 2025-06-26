from django.contrib import admin
from . models import Theatre,Seat,Showtime

# Register your models here.
@admin.register(Theatre)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'city','address')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('theatre','row_label','seat_number','seat_type')

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('theatre', 'movie', 'show_time', 'silver_price', 'gold_price', 'recliner_price')
