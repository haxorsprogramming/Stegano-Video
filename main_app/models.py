from django.db import models

# Create your models here.
class Encode_Pesan(models.Model):
    kd_uji = models.CharField(max_length=150)
    nama_video = models.CharField(max_length=150)
    nama_pengujian = models.CharField(max_length=150)
    rsa = models.CharField(max_length=150)
    rsa_crt = models.CharField(max_length=150)
    a_value = models.IntegerField()
    c_value = models.IntegerField()
    m_value = models.IntegerField()
    chiper_text = models.CharField(max_length=150)
    crt_value = models.FloatField()
    waktu_pengujian = models.DateTimeField()
    message_encode = models.CharField(max_length=200)

class Decode_Pesan(models.Model):
    kd_uji = models.CharField(max_length=150)
    nama_video = models.CharField(max_length=150)
    nama_pengujian = models.CharField(max_length=150)
    rsa_public = models.CharField(max_length=150)
    rsa_crt = models.CharField(max_length=150)
    a_value = models.IntegerField()
    c_value = models.IntegerField()
    m_value = models.IntegerField()
    chiper_text = models.CharField(max_length=150)
    crt_value = models.FloatField()
    waktu_pengujian = models.DateTimeField()
    message_decode = models.CharField(max_length=200)

class Video_Proses(models.Model):
    kd_uji = models.CharField(max_length=150)
    frame = models.CharField(max_length=10)
    hash_data = models.CharField(max_length=200)

class Kunci_RSA(models.Model):
    nama = models.CharField(max_length=150)
    p = models.CharField(max_length=150)
    q = models.CharField(max_length=150)
    dp = models.CharField(max_length=150)
    dq = models.CharField(max_length=150)
    q_inv = models.CharField(max_length=150)
    public_key = models.CharField(max_length=150)
    private_key =  models.CharField(max_length=150)
    active = models.CharField(max_length=150)