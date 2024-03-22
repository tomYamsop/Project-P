from django.db import models


# Create your models here.
# models == tables

class PrinterCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Printer Catigories'
    
    def __str__(self):
        return self.name
    
class Printer(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='printer_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quntity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(PrinterCategory, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.name} | {self.category}'