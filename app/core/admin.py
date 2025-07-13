from django.contrib import admin

from core.models import Book, Branch, Inventory

admin.site.register(Book)
admin.site.register(Branch)
admin.site.register(Inventory)