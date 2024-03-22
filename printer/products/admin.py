from django.contrib import admin

from products.models import PrinterCategory, Printer

# Register your models here.
admin.site.register(PrinterCategory)
admin.site.register(Printer)