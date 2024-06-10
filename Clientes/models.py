from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Cliente(models.Model):
    estados_choice=[
        ('Pendiente','Pendiente'),
        ('Terminado','Terminado')
    ]
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    nombre= models.CharField(max_length=60,blank=False, null=False)
    marca_modelo_auto= models.CharField(max_length=100,blank=False, null=False,help_text="Describa la marca y modelo del auto.")
    matricula=models.CharField(max_length=7,blank=False, null=False)
    detalles=models.CharField(max_length=200,blank=True, null=True)
    numero_telef=PhoneNumberField()
    hora_entrada=models.DateTimeField(auto_now_add=True)
    costo=models.FloatField()
    estado=models.CharField(max_length=50,choices=estados_choice, default="En espera")


    def __str__(self):
        return self.nombre 

    def __unicode__(self):
        return self.nombre
