from django.contrib import admin
from .models import Sheet, Content, SheetPermission
# Register your models here.
admin.site.register(Sheet)
admin.site.register(Content)
admin.site.register(SheetPermission)
