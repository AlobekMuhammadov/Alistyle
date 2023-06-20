from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Account


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Savat(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    umumiy_summa = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)
    status = models.BooleanField()

    # def save(self,*args,**kwargs):
    #     savat_items = SavatItem.objects.filter(savat__id=self.id)
    #     summa = 0
    #     for item in savat_items:
    #         ch = item.mahsulot.chegirma
    #         narxi = item.mahsulot.narx - ch
    #         narxi = narxi * item.miqdor
    #         summa += narxi
    #     self.umumiy_summa =  summa
    #     super(Savat, self).save(*args, **kwargs)

class SavatItem(models.Model):
    savat = models.ForeignKey(Savat,on_delete=models.CASCADE, related_name='itemlari')
    mahsulot = models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField()
    summa = models.PositiveSmallIntegerField()


    # def save(self, *args, **kwargs):
    #     ch = self.mahsulot.chegirma
    #     narxi = self.mahsulot.narx - ch
    #     self.summa = narxi * self.miqdor
    #     savat = Savat.objects.update(umumiy_summa=0)
    #     savat.save()
    #     super(SavatItem, self).save(*args, **kwargs)

class Manzil(models.Model):
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
    davlat =models.CharField(choices=DAVLATLAR, max_length=50)
    shahar = models.CharField(max_length=70)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    manzil = models.CharField(max_length=70)
    zipcode = models.CharField(max_length=6)
    asosiy = models.BooleanField(default=True)
    def __str__(self):
        return self.manzil

class Buyurtma(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    holat = models.CharField(max_length=50)
    manzil = models.ForeignKey(Manzil,on_delete=models.CASCADE)
    def __str__(self):
        return self.account.user.username





