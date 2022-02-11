from django.db import models


class hayvan_tanitimi(models.Model):
    hayvan_tur = models.CharField(max_length=100)
    hayvan_cins = models.CharField(max_length=100)
    hayvan_isim = models.CharField(max_length=100)
    hayvan_yas = models.IntegerField(null=False)
    hayvan_aciklama = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.hayvan_isim}, {self.hayvan_cins}, {self.hayvan_tur}'


class musteriler(models.Model):
    musteri_adisoyadi = models.CharField(max_length=100)
    musteri_eposta = models.EmailField(null=True)
    musteri_telefon = models.IntegerField(null=False)
    musteri_adres = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.musteri_adisoyadi}       {self.musteri_telefon}'


class musteri_hayvaniliskisi(models.Model):
    musteri_adisoyadi = models.ForeignKey(musteriler, on_delete=models.CASCADE)
    hayvan_adivecinsi = models.ForeignKey(hayvan_tanitimi, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.musteri_adisoyadi}     {self.hayvan_adivecinsi}'
