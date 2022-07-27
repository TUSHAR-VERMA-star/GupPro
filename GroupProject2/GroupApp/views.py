from pyexpat.errors import messages
from secrets import randbelow
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Sheet, Content
import random
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def homePage(request):
    return render(request, "GroupApp/homepage.html")


def createSheet(request):
    if(request.method == "GET"):
        return render(request, 'GroupApp/getName.html')
    randomNumber = random.randint(1000, 1000000)
    name = request.POST.get('value', 0)
    val = Sheet(creater=request.user.get_full_name(),
                randomNum=randomNumber, nameOfSheet=name)
    val.save()
    return render(request, "GroupApp/SuccessfullPage.html", {
        'Data': val
    })


def ShowSheet(request, pk):
    if(request.method == "POST"):
        randomNumber = request.POST.get('value', 0)
        if(randomNumber != 0):
            print(randomNumber)
            try:
                val = Sheet.objects.get(randomNum=randomNumber)
            except ObjectDoesNotExist:
                return render(request, "GroupApp/notFindPage.html")
        else:
            name = request.POST.get('name', 0)
            dis = request.POST.get('description', 0)
            val = Sheet.objects.get(id=pk)
            if(name != "" and dis != ""):
                print(name, dis)
                x = Content(userName=request.user.get_full_name(), name=name, description=dis, sheet=val)
                x.save()
    else:
        val = Sheet.objects.get(randomNum=pk)
    messages = Content.objects.filter(sheet=val)
    return render(request, "GroupApp/SheetForCreater.html", {
        'Data': val,
        'messages': messages
    })


def joinSheet(request):
    # return HttpResponse("okay ji")
    return render(request, "GroupApp/joinSheet.html")

def OurSheet(request):
    sheets = Sheet.objects.filter(creater=request.user.get_full_name())
    size = len(sheets)
    return render(request,"GroupApp/Oursheet.html",{
        "sheets":sheets,
        "size":size
    })