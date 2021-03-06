from django.contrib import admin
from .models import *

# Register your models here.

class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle']
    # list_filter = ['id']
    # search_fields = ['btitle']
    # list_per_page = 10
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)


