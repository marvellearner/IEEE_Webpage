from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Register(models.Model):
    Name = models.CharField(max_length=100 , blank=False)
    Email = models.EmailField(max_length=120 , blank=False)
    Mobile_number = models.IntegerField(unique=True , blank=False)
    Address = models.CharField(max_length=10000 ,blank=False)
    College = models.CharField(max_length=500)
    IEEE_mem_no = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{1,10}$')])
    def __str__(self):
        return self.Name


