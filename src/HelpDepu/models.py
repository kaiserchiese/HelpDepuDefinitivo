from django.db import models
from django.urls import reverse 

# Create your models here.
class Association(models.Model):
    
    EntNome = models.TextField()
    EntDireccion = models.TextField()
    EntConcello = models.TextField()
    EntCp = models.TextField()
    EntProvincia = models.TextField()
    EntTelefono = models.TextField()
    EntEmail = models.TextField()
    EntCategoria = models.TextField()
    Descr = models.TextField()

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.EntNome
