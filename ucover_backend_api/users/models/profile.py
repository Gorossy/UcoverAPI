from django.db import models
from .users import User


class Profile(models.model):


    users = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        "Profile picture",
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    """ Stats """
    services_taken = models.PositiveIntegerField(default=0)
    services_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(default=0.0)
    def __str__(self):
        return self.users.username