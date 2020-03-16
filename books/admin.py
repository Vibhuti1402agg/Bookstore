from django.contrib import admin
from .models import info,data

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class UserAdmin(admin.ModelAdmin):
    list_display = ('email','password',)


admin.site.register(info,BookAdmin)
admin.site.register(data,UserAdmin)

