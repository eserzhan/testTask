
from django.db import models
from authentication.models import User

# Create your models here.
class Order(models.Model):
    CHOICES = (
        ('Отправлен', 'Отправлен'),
        ('Отказ', 'Отказ'),
        ('Скоро свяжемся', 'Скоро свяжемся'),
        ('Принят в работу', 'Принят в работу')
    )
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="Скоро свяжемся" ,choices = CHOICES, max_length=20, null=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)