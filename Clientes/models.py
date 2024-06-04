from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.
class Cliente(models.Model):
    estados_choice=[
        ('Pendiente','Pendiente'),
        ('Terminado','Terminado')
    ]
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
