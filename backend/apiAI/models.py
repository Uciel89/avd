from django.db import models

# Create your models here.
class Querys(models.Model):
    consulta = models.CharField(max_length=200)
    respuesta = models.CharField(max_length=400, blank=True, default='some_value', editable=False)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.date