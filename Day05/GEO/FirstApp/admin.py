from django.contrib import admin
from .models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ('Bookname', "Author")

admin.site.register(Books, BooksAdmin)