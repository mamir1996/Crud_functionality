from django.contrib import admin

# Register your models here.
from CRUD.models import Registration

class RegistraionModel(admin.ModelAdmin):
    list_display=('id','name','email','roll_num','subject')
admin.site.register(Registration,RegistraionModel)