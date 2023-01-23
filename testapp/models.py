from pyexpat import model
from django.db import models

# Create your models here.
COLOR_CHOICES = (
    ('l&a','L&A'),
    ('claims', 'CLAIMS'),
    ('nonclaims','NONCLAIMS'),
    ('ba','BA'),
    ('tester','TESTER'),
)
class Mymodel(models.Model):
    name=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    project=models.CharField(max_length=30,choices=COLOR_CHOICES,default='L&A')
    email=models.EmailField(default='manager@gmail.com')
    location=models.CharField(max_length=30,default='mumbai')

