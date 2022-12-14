from django.db import models
from ucover_backend_api.users.models.users import User
class Event_Address(models.Model):
    Address = models.CharField(max_length=200)
    Details = models.CharField(max_length=300, null=True, blank=True)

class Event_Images(models.Model):
    image_url = models.models.ImageField(upload_to='events/images/', null=True, blank=True)

class Genre(models.Model):
    Name = models.CharField(max_length=200)
    def __str__(self):
        return self.Name
class Event(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField(max_length=500)
    Host = models.ForeignKey(User, on_delete=models.CASCADE,
    null=False, blank=False, related_name='Events')
    Genre = models.ManyToManyField(Genre, related_name='Genres')
    Quantity = models.PositiveIntegerField()
    Address = models.ForeignKey(Event_Address, on_delete=models.CASCADE,
    )
    Image= models.ForeignKey(Event_Images, on_delete=models.CASCADE,
    null=True, blank=True, related_name='Images')
    def __str__(self):
        return self.Name
class Ticket(models.Model):
    Price = models.FloatField()
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)+'.' + ' ' + self.Event.Name
class Event_address(models.Model):
    Address = models.CharField(max_length=200)
    Details = models.CharField(max_length=300, null=True, blank=True)
    Host = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='Event_address')
    def __str__(self):
        return 'Direccion: '+ self.Host.Name