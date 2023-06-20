from datetime import datetime

from django.db.models import *
from django.shortcuts import render, redirect
from django.views import View
from .models import Bolim, Mahsulot, Izoh
from userapp.models import Account


class Home(View):
    def get(self,request):
        content = {
            'bolimlar':Bolim.objects.all()[:7]
        }
        return render(request,'page-index.html',content)

class HomeLoginsiz(View):
    def get(self,request):
        return render(request,'page-index-2.html')

class BolimView(View):
    def get(self,request,pk):
        izohlar = Izoh.objects.filter(mahsulot__bolim__id=pk)
        content = {
            'mahsulotlar':Mahsulot.objects.filter(bolim__id=pk),
            'izohlar_soni':len(izohlar),
        }
        return render(request,'page-listing-grid.html',content)


class HammaBolimView(View):
    def get(self,request):
        content = {
            'bolimlar':Bolim.objects.all()

        }
        return render(request,'page-category.html',content)

class BittaMahsulotView(View):
    def get(self,request,pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        ortachasi = izohlar.aggregate(Avg('baho')).get('baho__avg')
        content = {
            'mahsulot':Mahsulot.objects.get(id=pk),
            'izohlar':Izoh.objects.filter(mahsulot__id=pk),
            'izoh_soni':len(izohlar),
            'ortachasi':ortachasi*20,
        }
        return render(request,'page-detail-product.html', content)


    def post(self, request, pk):
        Izoh.objects.create(
            matn=request.POST.get('comment'),
            mahsulot=Mahsulot.objects.get(id=pk),
            baho=request.POST.get('rating'),
            account=Account.objects.get(user=request.user)
        )
        return redirect(f"/asosiy/mahsulot/{pk}/")




