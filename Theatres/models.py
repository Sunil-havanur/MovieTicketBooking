from django.db import models
from Movies.models import Movie
# Create your models here.
class Theatre(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name
    
seat_type =[
    ('silver','silver'),
    ('gold','gold'),
    ('platinum','platinum')
]    
class Seat(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    row_label = models.CharField(max_length=1)
    seat_number = models.IntegerField()
    seat_type = models.CharField(max_length=100,choices=seat_type)
    #is_available = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.row_label}{self.seat_number}"

class Showtime(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    silver_price = models.DecimalField(max_digits=6, decimal_places=2)
    gold_price = models.DecimalField(max_digits=6, decimal_places=2)   
    recliner_price = models.DecimalField(max_digits=6, decimal_places=2)

   