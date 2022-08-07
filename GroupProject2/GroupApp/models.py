from os import access
from statistics import mode
from django.db import models

# Create your models here.


class Sheet(models.Model):
    creater = models.CharField(max_length=20)
    createrEmail = models.EmailField()
    randomNum = models.IntegerField(blank=True, default=0, null=True)
    nameOfSheet = models.CharField(max_length=100)
    type = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.creater + " " + self.nameOfSheet


class Content(models.Model):
    userName = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class SheetPermission(models.Model):
    ownerEmail = models.EmailField()
    userEmail = models.EmailField()
    sheetId = models.IntegerField()
    sheetName = models.CharField(max_length=100)
    sheetPermission = models.BooleanField(default=False)
    giveAccess = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.userEmail
