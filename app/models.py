from django.db import models


class MyModel(models.Model):
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
