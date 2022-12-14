from django.db import models


class Payment_method(models.Model):
    Type = models.IntegerField()