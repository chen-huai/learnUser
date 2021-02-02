from django.contrib import admin
from user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','nickname','age','gender','phone','email')
    search_fields = ('username',)
    list_per_page = 20
    ordering = ('username',)
    # list_editable = ["address",'phone','email','remark','is_delete']
admin.site.register(User, UserAdmin)
