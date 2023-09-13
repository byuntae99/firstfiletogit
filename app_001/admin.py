from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
"""class UserModel(UserAdmin):
    pass
"""
class res(admin.ModelAdmin):
    list_display=('id',)

admin.site.register(AdminHOD,res)
class resw(admin.ModelAdmin):
    list_display=('id',)
admin.site.register(Status,resw)
class re(admin.ModelAdmin):
    list_display=('id',)
admin.site.register(Students,re)
class req(admin.ModelAdmin):
    list_display=('id',)
admin.site.register(LeaveReportStudent,req)
class rwe(admin.ModelAdmin):
    list_display=('id',)
admin.site.register(Courseregister,rwe)
class rqwe(admin.ModelAdmin):
    list_display=('id',)
admin.site.register(CustomUser,rqwe)
