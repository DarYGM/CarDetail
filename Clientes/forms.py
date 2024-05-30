
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    estados_choice=[
        ('En espera','En espera'),
        ('En lavando','En lavando'),
        ('Terminado','Terminado')
        ]
    def validate_matricula_length(value):
        if len(value) > 7:
            raise forms.ValidationError('La matrícula debe tener 7 o menos caracteres.')
        
    nombre=forms.CharField(label="Nombre",widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Nombre del cliente.',
            'nombre':'necesidad_proyecto',
            'type':'text',
            'required':'required',
            'autocomplete':'on'
        }
    ))
    marca_modelo_auto=forms.CharField(label='Marca y modelo',widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Marca y modelo del auto.',
            'name':'Requerimiento',
            'type':'text',
            'required':'required',
            'autocomplete':'on'
            
        }
    ))
    matricula=forms.CharField(label='Matrícula',validators=[validate_matricula_length],widget=forms.TextInput(
        attrs={
            'class':'form-control text-uppercase form-control-solid mb-3 mb-lg-0',
            'placeholder':'Matrícula del auto.',
            'name':'Requerimiento',
            'type':'text',
            'required':'required',
            'autocomplete':'on'
            
        }
    ))
    detalles=forms.CharField(label='Detalles',widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Detalles extras.',
            'name':'Requerimiento',
            'type':'text',
            'autocomplete':'on'
            
        }
    ))
    numero_telef=forms.CharField(label='Teléfono',widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Número de teléfono del cliente.',
            'name':'Requerimiento',
            'type':'tel',
            'required':'required',
            'autocomplete':'on'
            
        }
    ))
    
    costo=forms.CharField(label='Costo',widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Costo del servicio.',
            'name':'Requerimiento',
            'type':'number',
            'required':'required',
            'autocomplete':'off',
            'step': '0.5',  # Permite dos decimales para precios
            'min': '0'  # Valor mínimo permitido
            
        }
    ))
    estado=forms.CharField(label='Estado',widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-solid mb-3 mb-lg-0',
            'placeholder':'Estado del servicio',
            'name':'Requerimiento',
            'type':'text',
            'required':'required',
            'autocomplete':'off',
            
        }
    ))
    class Meta:
        
        model = Cliente
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        fields=('nombre','marca_modelo_auto','matricula','detalles','numero_telef','costo','estado',)

    