from django.shortcuts import render,redirect
from Theatres.models import Theatre,Showtime
from Movies.models import Movie
from django.contrib import messages
import datetime
# Create your views here.
#dates = [datetime.date.today(),datetime.date.today() + datetime.timedelta(days=1),datetime.date.today() + datetime.timedelta(days=2),datetime.date.today() + datetime.timedelta(days=3),datetime.date.today() + datetime.timedelta(days=4)]
dates = [datetime.date.today()+datetime.timedelta(days=i) for i in range(6)]

def Theatre_Showtime_view(request,slug,date_str=datetime.date.today()):
    if not Movie.objects.filter(slug=slug).exists():
        messages.error(request,'Movie not found')
        return redirect('movie_list')
    movie = Movie.objects.get(slug=slug)
    selected_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    if selected_date == datetime.now().date():
        Theatre_showtimes = [showtime.objects.filter(movie=movie,showtime__date=selected_date,showtime__time__gt=datetime.now().time(),
                                                 theatre=theatre).order_by('showtime') 
                                                 for theatre in Theatre.objects.all()
                                                 if Showtime.objects.filter(movie=movie,showtime__date=selected_date,showtime__time__gt=datetime.now().time(),theatre=theatre).exists()]
    else:
        Theatre_showtimes = [showtime.objects.filter(movie=movie,showtime__date=selected_date,
                                                 theatre=theatre).order_by('showtime') for theatre in Theatre.objects.all()
                                                 if Showtime.objects.filter(movie=movie,showtime__date=selected_date,theatre=theatre).exists()]
    context = {
        'movie':movie,
        'theatre_showtimes':theatre_showtimes,
        'dates':dates,
        'slug':slug,
        'week':week,
        'current_date' : selected_date,
        
    }
    return render(request,'Theatre/showtime.html',context)