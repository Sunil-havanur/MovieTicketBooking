from django.db import models

genres=[('Action','Action'),('Comedy','Comedy'),('Drama','Drama'),('Horror','Horror'),('Romance','Romance'),('Fiction','Fiction'),('Thriller','Thriller')]

languages=[('English','English'),('Hindi','Hindi'),('Tamil','Tamil'),('Telugu','Telugu'),('Kannada','Kannada'),('Malayalam','Malayalam')]

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=genres,null=True, blank=True)
    language = models.CharField(max_length=20, choices=languages,null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Upcoming', 'Upcoming'), ('Released', 'Released')], default='Upcoming',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    movie_image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.title
        
class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='casts')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='casts/',null=True,blank=True)
