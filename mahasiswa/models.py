from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Data_mahasiswa(models.Model):
    npm = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=50, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.nama
    