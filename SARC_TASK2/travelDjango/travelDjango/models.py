from django.db import models


class Travel(models.Model):
    destination = models.CharField(max_length=200)
    about = models.CharField(max_length=500)


# class Employ(models.Model):
#     name = models.CharField(max_length=200)
#     department = models.CharField(max_length=200)
#     phone = models.CharField(max_length=10)
#     iserId = models.IntegerField(max_length=20)
#     address = models.CharField(max_length=200)