from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    TANLOV = (
        ('Erkak','Erkak'),
        ('Ayol','Ayol'),
    )
    DAVLATLAR = (
        ('Uzbekistan', 'Uzbekistan'),
        ('Russia', 'Russia'),
        ('Armenia', 'Armenia'),
        ('Tajikistan', 'Tajikistan'),
        ('Kazakhstan', 'Kazakhstan'),
        ('Kyrgzstan', 'Kyrgzstan'),
        ('Azerbayjan', 'Azerbayjan'),
        ('Moldova', 'Moldova'),
        ('Latviya', 'Latviya'),
        ('Turkmenistan', 'Turkmenistan'),
    )
    jins = models.CharField(max_length=30,choices=TANLOV)
    shahar = models.CharField(max_length=60)
    davlat = models.CharField(max_length=30,choices=DAVLATLAR)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


