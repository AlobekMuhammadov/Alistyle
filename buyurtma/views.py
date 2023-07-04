from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from asosiy.models import Mahsulot
from userapp.models import Account


class TanlanganOchirView(View):
    def get(self,request,son):
        Tanlangan.objects.filter(id=son).delete()
        return redirect('tanlangan')

class ShoppingView(View):
    def get(self,request):
        a = Savat.objects.get(account__user=request.user)
        itemlar = SavatItem.objects.filter(savat=a)
        narx_sum = 0
        chegirma = 0
        for item in itemlar:
            chegirma += item.mahsulot.chegirma * item.miqdor
            narx_sum += item.mahsulot.narx * item.miqdor
        a.umumiy_summa = narx_sum-chegirma
        a.save()
        content = {
            'savat':a,
            'savat_items':itemlar,
            'total':narx_sum,
            'total_ch':chegirma,
            'price':narx_sum-chegirma

        }
        return render(request,'page-shopping-cart.html',content)

class MiqdorKamaytir(View):
    def get(self,request,son):
        item = SavatItem.objects.get(id=son)
        if item.miqdor > 1:
            item.miqdor -= 1
            item.summa -= item.mahsulot.narx
            item.save()
        return redirect('/buyurtma/')

class MiqdorQosh(View):
    def get(self , request, son):
        item = SavatItem.objects.get(id=son)
        item.miqdor += 1
        item.summa += item.mahsulot.narx
        item.save()
        return redirect("/buyurtma/")

class SavatItemQosh(View):
    def get(self,request,pk):
        savati = Savat.objects.get(account_user=request.user)
        m = Mahsulot.objects.get(id=pk)
        savat_item = SavatItem.objects.filter(mahsulot=m, savat=savati)
        if len(savat_item) == 0:
            return redirect(f"/mahsulot/{pk}/")
        SavatItem.objects.create(
            miqdor = 1,
            mahsulot = m,
            savat = savati,
            summa = m.narx
        )
        return redirect(f"/mahsulot/{pk}/")


class OchirishView(View):
    def get(self,request,son):
        SavatItem.objects.filter(id=son,savat__account__user=request.user).delete()
        return redirect('shopping')


class BuyurtmaView(View):
    def get(self,request):
        content = {
            'buyurtmalar':Buyurtma.objects.get(account__user=request.user)
        }
        return render(request,'page-profile-orders.html',content)

class BuyurtmaQosh(View):
    def get(self,request,pk):
        Buyurtma.objects.create(
            savat = Savat.objects.get(id=pk),
            account = Account.objects.get(user=request.user),
            holat = "Jarayonda",
            manzil = Manzil.objects.get(account__user=request.user,asosiy=True)
        )
        return redirect("/buyurtma/orders/")

class TanlanganView(View):
    def get(self,request):
        content = {
            'tanlanganlar':Tanlangan.objects.all()
        }
        return render(request,'page-profile-wishlist.html',content)




