from django.db import models

from userapp.models import Account


class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolimlar')
    def __str__(self):
        return self.nom


class Mahsulot(models.Model):
    DAVLATLAR = (
        ('Uzbekistan','Uzbekistan'),
        ('Russia','Russia'),
        ('Armenia','Armenia'),
        ('Tajikistan','Tajikistan'),
        ('Kazakhstan','Kazakhstan'),
        ('Kyrgzstan','Kyrgzstan'),
        ('Azerbayjan','Azerbayjan'),
        ('Moldova','Moldova'),
        ('Latviya','Latviya'),
        ('Turkmenistan','Turkmenistan'),
    )
    nom = models.CharField(max_length=100)
    narx = models.PositiveSmallIntegerField()
    min_miqdor = models.IntegerField()
    bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    davlat = models.CharField(max_length=50,choices=DAVLATLAR)
    brend = models.CharField(max_length=70)
    matn = models.CharField(max_length=200)
    yetkazish = models.IntegerField(default=0)
    mavjud = models.BooleanField(default=False)
    kafolat = models.CharField(default="Kafolat yo'q", max_length=20)
    chegirma = models.PositiveSmallIntegerField(default=0)
    # rasm = models.FileField()


class Media(models.Model):
    rasm = models.FileField(upload_to='mahsulotlar')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)


class Izoh(models.Model):
    matn = models.CharField(max_length=200,null=True,blank=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    baho = models.PositiveSmallIntegerField(default=5)



