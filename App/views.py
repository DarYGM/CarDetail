import csv
import os
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from Clientes.models import Cliente
from Clientes.forms import ClienteForm
from django.contrib.auth import authenticate, login,logout
import openpyxl
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from Clientes.models import Profile


# Create your views here.
def StartLogin(request):
    pk='error'
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('List_User')
    else :
        return render(request,'registration/login.html',{"sms":pk})
    
def Login(request):
    return render(request,"registration/login.html")

def Logout(request):
    logout(request) 
    return render(request,'registration/login.html')

def List_User(request):
    costos=0
    form=ClienteForm()
    prof=Profile.objects.get(user=request.user)
    clientes=Cliente.objects.filter(owner=request.user)
    
    mensaje=''
    if request.method == 'POST':
        formclient = ClienteForm(request.POST)

        if formclient.is_valid():
            new_cliente=formclient.save(commit=False)
            new_cliente.owner=request.user
            new_cliente.save()
            form=ClienteForm()
            return redirect('List_User') 
        else:
            print('Darianaaaaaa')
            print(formclient.errors)  # Imprime los errores del formulario en la consola
            print(formclient.non_field_errors())  # Imprime errores no asociados a un campo específico

    #costos=sum(c.costo for c in clientes)
    return render(request,'list.html',{'clientes':clientes,'form':form,'profile':prof})
    

def Delete_client(request,pk):
    
    cliente=Cliente.objects.get(id=pk)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente.')
    clientes=Cliente.objects.filter(owner=request.user)
    form=ClienteForm()
    #costos=sum(c.costo for c in clientes)
    #return  render(request,'list.html',{'clientes':clientes,'form':form,})  
    return redirect('List_User') 

def Search_client(request):
    client=[]
    form=ClienteForm()
    costos=0
    if request.method =='POST':
        
        nomb = request.POST.get('clientsearch')
        #print(nomb)
        if nomb:
            client= Cliente.objects.filter(owner=request.user, nombre__icontains=nomb)
            
            #costos = sum(c.costo for c in client)
    return redirect('List_User') 
    #return  render(request,'list.html',{'clientes':client,'form':form})

def Filtrar(request):
    clientes=Cliente.objects.filter(owner=request.user, estado=request.POST.get('estado_filtro'),marca_modelo_auto__icontains=request.POST.get('marca_auto'))
    
    form=ClienteForm()
    #return render(request,'list.html',{'clientes':clientes,'form':form})
    return redirect('List_User') 

def Finalizar(request,pk):
    cliente=Cliente.objects.get(id=pk)
    cliente.estado='Terminado'
    cliente.save()
    # parte dedicada a enviar mensaje o whatsapp
    clientes=Cliente.objects.all()
    form=ClienteForm()
    #costos=sum(c.costo for c in clientes)
    return redirect('List_User')
    #return  render(request,'list.html',{'clientes':clientes,'form':form})

def Editar_cliente(request,tk):
    #para cargar vista inicial con todo
    clientes=Cliente.objects.filter(owner=request.user)
    formm=ClienteForm()
    #costos= sum(c.costo for c in clientes)
    #para actualizar en caso de confirmarce actualizaci'on
    cliente=Cliente.objects.get(id=tk)
    form=ClienteForm(instance=cliente)
    if request.method=='POST':
        form=ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('List_User') 
            #return  render(request,'list.html',{'clientes':clientes,'form':formm,})   

    return  render(request,'edit_client.html',{'form':form,'id':cliente.id})        



def Exportar_datos_clientes(request):
    formato = request.GET.get('format')
    if formato == 'excel':
        file_path = exportar_a_excel()
        return redirect('List_User')
    elif formato == 'pdf':
        file_path = exportar_a_pdf()
        return redirect('List_User')
    elif formato == 'cvs':
        file_path = exportar_a_cvs()
        return redirect('List_User')
    #elif formato == 'zip':
    #    exportar_a_zip()
    elif formato =='':
        sms='noformat'
        clientes=Cliente.objects.all()
        formm=ClienteForm()
        return  render(request,'list.html',{'clientes':clientes,'form':formm,'sms':sms}) 


        
    #return redirect('List_User')

def exportar_a_excel():
# Crear el libro de trabajo y la hoja
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Clientes'
    # Encabezados de la hoja
    headers = ['Nombre', 'Marca y Modelo del Auto', 'Matrícula', 'Detalles', 'Número de Teléfono', 'Costo', 'Estado']
    ws.append(headers)
    # Obtener todos los clientes
    clientes = Cliente.objects.all() 
    # Agregar los datos de los clientes   
    for cliente in clientes:
        ws.append([
            cliente.nombre,
            cliente.marca_modelo_auto,
            cliente.matricula,
            cliente.detalles,
            str(cliente.numero_telef),
            cliente.costo,
            cliente.estado
        ])
    # Generar una cadena con la fecha y hora actuales
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # Definir la ruta del archivo
    file_path = os.path.join('Media/EXCEL', f'clientes_{now}.xlsx')

    # Guardar el libro de trabajo en la ruta definida
    wb.save(file_path)

    return file_path

def exportar_a_cvs():
    # Generar una cadena con la fecha y hora actuales
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    
    # Definir la ruta del archivo con la fecha y hora
    file_path = os.path.join('media/CVS', f'clientes_{now}.csv')

    # Obtener todos los clientes
    clientes = Cliente.objects.all()

    # Crear el archivo CSV y escribir los datos
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Escribir los encabezados
        headers = ['Nombre', 'Marca y Modelo del Auto', 'Matrícula', 'Detalles', 'Número de Teléfono', 'Costo', 'Estado']
        csvwriter.writerow(headers)
        # Escribir los datos de los clientes
        for cliente in clientes:
            csvwriter.writerow([
                cliente.nombre,
                cliente.marca_modelo_auto,
                cliente.matricula,
                cliente.detalles,
                cliente.numero_telef,
                cliente.costo,
                cliente.estado
            ])

    return file_path

def exportar_a_pdf():
# Generar una cadena con la fecha y hora actuales
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Definir la ruta del archivo con la fecha y hora
    file_path = os.path.join('Media/PDFs', f'clientes_{now}.pdf')

    # Crear el PDF
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Título del documento
    c.setFont("Helvetica-Bold", 20)
    c.drawString(30, height - 40, "Listado de Clientes")

    # Encabezados de la tabla
    c.setFont("Helvetica-Bold", 14)
    headers = ['Nombre', 'Marca y Modelo', 'Matrícula', 'Teléfono', 'Costo']
    x_offset = 30
    y_offset = height - 80
    for header in headers:
        c.drawString(x_offset, y_offset, header)
        x_offset += 120

    # Datos de los clientes
    clientes = Cliente.objects.all()
    y_offset -= 20
    c.setFont("Helvetica", 10)
    row_height = 25  # Altura de cada fila
    for cliente in clientes:
        x_offset = 30
        data = [
            cliente.nombre,
            cliente.marca_modelo_auto,
            cliente.matricula,
            cliente.numero_telef,
            cliente.costo
        ]
        for item in data:
            c.drawString(x_offset, y_offset, str(item))
            x_offset += 120
        y_offset -= row_height
        if y_offset < 40:
            c.showPage()
            c.setFont("Helvetica", 10)
            y_offset = height - 40

    c.save()
    
    return file_path