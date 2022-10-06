from django.db import models

# Create your models here.
class Dosen(models.Model):
    NIP = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Foto = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Fakultas = models.CharField(max_length=200)
    Prodi = models.CharField(max_length=200)
    Alamat = models.TextField(max_length=200)

class Tendik(models.Model):
    NIP = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Foto = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Unit = models.CharField(max_length=200)
    Alamat = models.TextField(max_length=200)

class Mahasiswa(models.Model):
    NIM = models.CharField(max_length=200)
    Nama = models.CharField(max_length=200)
    TanggalLahir = models.CharField(max_length=50)
    Foto = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Fakultas = models.CharField(max_length=200)
    Prodi = models.CharField(max_length=200)


def _str_(self):
    return self.NIP
    return self.NIP
    return self.NIM
