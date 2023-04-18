from django.contrib import admin
from .models import Users
# Register your models here.
admin.site.site_header = '音站后台管理'  # 设置header
admin.site.site_title = '音站后台管理'   # 设置title
admin.site.index_title = '音站后台管理'

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','password')
admin.site.register(Users)