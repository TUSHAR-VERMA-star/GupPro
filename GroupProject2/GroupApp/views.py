from pyexpat.errors import messages
from secrets import randbelow
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Sheet, Content, SheetPermission
import random
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def homePage(request):
    pendingRequest = SheetPermission.objects.all()
    try:
        if(request.user.email):
            pendingRequest = SheetPermission.objects.filter(
                ownerEmail=request.user.email, sheetPermission=False, giveAccess=True)
    except AttributeError:
        pass
    return render(request, "GroupApp/homepage.html", {
        "pendingRequest": pendingRequest,
        "length": len(pendingRequest)
    })


def createSheet(request):
    if(request.method == "GET"):
        return render(request, 'GroupApp/getName.html')
    randomNumber = random.randint(1000, 1000000)
    name = request.POST.get('value', 0)
    val = Sheet(creater=request.user.get_full_name(), createrEmail=request.user.email,
                randomNum=randomNumber, nameOfSheet=name, type=request.POST.get('0', 0))
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
                x = Content(userName=request.user.get_full_name(),
                            name=name, description=dis, sheet=val)
                x.save()
    else:
        val = Sheet.objects.get(randomNum=pk)
    messages = Content.objects.filter(sheet=val)
    if(val.type == "Public" or val.creater == request.user.get_full_name()):
        return render(request, "GroupApp/SheetForCreater.html", {
            'Data': val,
            'messages': messages
        })
    else:
        try:
            check = SheetPermission.objects.get(
                sheetId=val.randomNum, userEmail=request.user.email)
            if(check.sheetPermission == True):
                return render(request, "GroupApp/SheetForCreater.html", {
                    'Data': val,
                    'messages': messages
                })
            else:
                return render(request, "GroupApp/NoPermission.html")
        except ObjectDoesNotExist:
            per = SheetPermission(
                ownerEmail=val.createrEmail, userEmail=request.user.email, sheetId=val.randomNum, sheetName=val.nameOfSheet)
            per.save()
            # return HttpResponse("2")
            return render(request, "GroupApp/NoPermission.html")


def joinSheet(request):
    # return HttpResponse("okay ji")
    return render(request, "GroupApp/joinSheet.html")


def OurSheet(request):
    sheets = Sheet.objects.filter(creater=request.user.get_full_name())
    size = len(sheets)
    return render(request, "GroupApp/Oursheet.html", {
        "sheets": sheets,
        "size": size
    })


def pending(request):
    pendingRequest = SheetPermission.objects.filter(
        ownerEmail=request.user.email, sheetPermission=False, giveAccess=True)
    return render(request, "pendingRequest.html", {
        "pendingRequest": pendingRequest
    })


def giveaccess(request, id):
    val = SheetPermission.objects.get(pk=id)
    val.sheetPermission = True
    val.save()
    return render(request, "AccessGranted.html")


def noaccess(request, id):
    val = SheetPermission.objects.get(pk=id)
    val.giveAccess = False
    val.save()
    return render(request, "NoAccessGranted.html")


def addpeople(request, id):
    useremail = request.POST.get('useremail', 0)
    sheetname = Sheet.objects.get(randomNum=id).nameOfSheet
    try:
        chk = SheetPermission.objects.get(
            ownerEmail=request.user.email, userEmail=useremail, sheetId=id)
        chk.sheetPermission = True
        chk.giveAccess = True
        chk.save()
        return render(request, "AddPeople.html", {
            "randomNum": id
        })
    except ObjectDoesNotExist:
        giveaccess = SheetPermission(
            ownerEmail=request.user.email, userEmail=useremail, sheetId=id, sheetName=sheetname, sheetPermission=True)
        giveaccess.giveAccess = True
        giveaccess.save()
        return render(request, "AddPeople.html", {
            "randomNum": id
        })
