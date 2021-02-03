from django.contrib import admin
from user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','nickname','age','gender','phone','email')
    fieldsets = [
        ("基础信息", {"fields": ["username", "nickname", "gender",'age', 'phone','password']}),
        ("权限", {"fields": ['groups','user_permissions']}),
    ]
    search_fields = ('username',)
    list_per_page = 20
    ordering = ('username',)
    # list_editable = ["address",'phone','email','remark','is_delete']
admin.site.register(User, UserAdmin)
