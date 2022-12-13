# Create your views here.
from django.shortcuts import render, redirect
#from Devolu.forms import FormRegistro
from Devolu.models import Cliente, Devolucion, Producto
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
import requests


def is_admin (user):
    return user.groups.filter(name = 'admin').exists()

def registrarse(request):
    cli_username = request.POST['txt_username']
    cli_email = request.POST['txt_email']
    cli_password = request.POST['txt_contrasena']

    user = User.objects.create_user(cli_username, cli_email, cli_password)
    user.save()
    grupo, created = Group.objects.get_or_create(name ='admin')
    user.groups.add(grupo)

    return redirect('/inicio/login')
    
def registrar(request):
    if request.user.is_authenticated:
        redirect('/menu/')
    return render(request,'registrarse.html')

@login_required
@user_passes_test(is_admin)
def crearVend(request):
    v_username = request.POST['txt_nombrev']
    v_email = request.POST['txt_emailv']
    v_password = request.POST['txt_passwordv']

    use = User.objects.create_user(v_username,v_email,v_password)
    use.save()
    grupo, created =Group.objects.get_or_create(name = 'vendedor')
    use.groups.add(grupo)
    
    
@login_required
@user_passes_test(is_admin)
def listadev(request):
    devolucion = Devolucion.objects.all()
    data = {'devolucion':devolucion}
    return render(request,'listarDevolucion.html', data)

@login_required
def registrard(request):
    cliente = Cliente.objects.all()
    producto = Producto.objects.all()
    context = {
        'clientes': cliente,
        'producto': producto
    }

    return render(request,'FormularioDev.html', context)    

@login_required
def registrardevo(request):
    dev_producto = request.POST['sel_producto']
    dev_cliente = request.POST['sel_cliente']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_nombre_vendedor = request.POST['txt_nombrevendedor']
    dev_comentario = request.POST['txt_comentario']
    dev_fecha = request.POST['txt_fecha']
    dev_costo = float(request.POST['txt_costo'])


    cliente = Cliente.objects.get(id=dev_cliente)
    producto = Producto.objects.get(id=dev_producto)

    costopesos= dev_costo
    print(type(costopesos))
    

    response = generarRequest('https://mindicador.cl/api/dolar/13-12-2022')
    r_dolar = response.get('serie')[0]
    v_dolar = r_dolar.get('valor')
    
    print(type(v_dolar))


    valor_costo_dolares = costopesos / v_dolar


    devolucion = Devolucion(Producto = producto, Cliente=cliente, Distribuidor=dev_distribuidor, nombre_vendedor=dev_nombre_vendedor, comentario = dev_comentario, fecha = dev_fecha, costo = dev_costo, costodolar = valor_costo_dolares)
    
    devolucion.save()
    

    return redirect('/menu/')

@login_required
def eliminardev(request, id):
    elemidev = Devolucion.objects.get(id=id)
    elemidev.delete()

    return redirect(listadev)

@login_required
def devoluActualizar(request,id):
    devolucion = Devolucion.objects.get(id=id)
    return render(request,'Actualizardev.html',{"devolucion":devolucion})    

@login_required
def editarDev(request):
    dev_producto = request.POST['sel_producto']
    dev_cliente = request.POST['sel_cliente']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_nombre_vendedor = request.POST['txt_nombrevendedor']
    dev_comentario = request.POST['txt_comentario']
    dev_fecha = request.POST['txt_fecha']
 
    cliente = Cliente.objects.get(id=dev_cliente)
    producto = Producto.objects.get(id=dev_producto)

    devolu = Devolucion.objects.get(Cliente = cliente)
    
    devolu.Producto = producto
    devolu.nombre_vendedor = dev_nombre_vendedor
    devolu.Distribuidor = dev_distribuidor
    devolu.fecha = dev_fecha
    devolu.comentario = dev_comentario

    devolu.save()
    return redirect(listadev)


@login_required
def menu(request):
    return render(request,'menu.html')  

@login_required

def listaclient(request):
    cliente = Cliente.objects.all()
    data = {'cliente':cliente}
    return render(request,'listarClient.html', data)

@login_required
def registrarc(request):
    return render(request,'FormularioClient.html')

@login_required
@user_passes_test(is_admin)
def registrarclient(request):
    client_rut = request.POST['txt_rut']
    client_nombre = request.POST['txt_nombre']
  
    cliente = Cliente(rut = client_rut, nombre = client_nombre)
    cliente.save()
    return redirect(listaclient)
    

@login_required
@user_passes_test(is_admin)
def eliminarClient(request, id):
    elemiclient = Cliente.objects.get(id=id)
    elemiclient.delete()

    return redirect(listaclient)

@login_required
@user_passes_test(is_admin)
def clientActualizar(request,id):
    client = Cliente.objects.get(id=id)
    return render(request,'ActualizarClient.html',{"client":client})    

@login_required
@user_passes_test(is_admin)
def editarClient(request):
    client_rut = request.POST['txt_rut']
    client_nombre = request.POST['txt_nombre']

    client = Cliente.objects.get(rut = client_rut)
    client.nombre = client_nombre


    client.save()
    return redirect(listaclient)




@login_required
@user_passes_test(is_admin)
def listaproduct(request):
    producto = Producto.objects.all()
    data = {'producto':producto}
    return render(request,'listarProduct.html', data)

@login_required
@user_passes_test(is_admin)
def registrarp(request):
    return render(request,'FormularioProduct.html')

@login_required
@user_passes_test(is_admin)
def registrarproduct(request):
    product_nombre = request.POST['txt_producto']
    product_cantidad = request.POST['txt_cantidad']
    producto = Producto(nomproduct = product_nombre, cantidad = product_cantidad)
    producto.save()
    return redirect(listaproduct)

@login_required
@user_passes_test(is_admin)
def eliminarProduct(request, id):
    elemiproduct = Producto.objects.get(id=id)
    elemiproduct.delete()
    return redirect(listaproduct)

@login_required
@user_passes_test(is_admin)
def productActualizar(request,id):
    product = Producto.objects.get(id=id)
    return render(request,'ActualizarProduct.html',{"product":product})    

@login_required
@user_passes_test(is_admin)
def editarProduct(request):
    product_nombre = request.POST['txt_producto']
    product_cantidad = request.POST['txt_cantidad']

    product = Producto.objects.get(nomproduct = product_nombre)
    product.nomproduct =product_nombre
    product.cantidad = product_cantidad

    product.save()
    return redirect(listaproduct)

def generarRequest(url):
    response  = requests.get(url)
    if response.status_code == 200:
        return response.json()
