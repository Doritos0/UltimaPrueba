from django.shortcuts import redirect, render

from pruebaApp.compra import Compra
from .models import Producto
from .serializers import ProductoSerializer

# CREACION DE API
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

#ELEMENTOS DE LA AUTENTICACION
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        query = Producto.objects.all()
        serializer = ProductoSerializer(query, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            nom_prod = request.POST.get('nom_prod', None)
            if nom_prod in Producto.objects.values_list('nom_prod', flat=True):
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto (request,id):
    try:
        productos = Producto.objects.get(nom_prod=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serilizer = ProductoSerializer(productos)
        return Response(serilizer.data)
    if request.method == 'PUT':
        serializer = ProductoSerializer(productos,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        else:
            return Response(serilizer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method =='DELETE':
        productos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username'] 
    password = data['password']

    try:
        user = User.objects.get(username= username)
    except User.DoesNotExist:
        return Response("Usuario Invalido")

    validar =check_password(password, user.password)

    if not validar:
        return("Password Incorrecta") 

    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)       


def inicio(request):
    return render(request,'core/inicio.html')

def locales(request):
    return render(request,'core/locales.html')

def local_1 (request):
    return render(request,'core/local_1.html')

def local_2 (request):
    return render(request,'core/local_2.html')

def productos (request):
    prod = Producto.objects.all()
    return render(request, "core/productos.html",{"productos":prod})

def producto1 (request):
    return render(request,'core/producto1.html')

def producto2 (request):
    return render(request,'core/producto2.html')

def carrito (request):
    return render(request,'core/carrito.html')

def registro (request):
    return render(request,'core/registro.html')


#FUNCIONES PARA EL FUNCIONAMIENTO DE LA COMPRA
def agregar_producto (request, nom_produc):
    compra = Compra(request)
    producto = Producto.objects.get(nom_prod=nom_produc)
    compra.agregar(producto)
    return redirect("productos")

def eliminar_producto(request, nom_produc):
    compra= Compra(request)
    producto = Producto.objects.get(nom_prod=nom_produc)
    compra.eliminar(producto)
    return redirect("productos")

def restar_producto(request, nom_produc):
    compra= Compra(request)
    producto = Producto.objects.get(nom_prod=nom_produc)
    compra.restar(producto)
    return redirect("productos")

def limpiar_compra (request):
    compra = Compra(request)
    compra.limpiar()
    return redirect("productos")

def agregar_tradicional (request):
    compra = Compra(request)
    compra.agregar_tradicional()
    return redirect("productos")

def restar_tradicional (request):
    compra = Compra(request)
    compra.restar_tradicional()
    return redirect("productos")

def eliminar_tradicional(request):
    compra= Compra(request)
    compra.eliminar_tradicional()
    return redirect("productos")


def agregar_vegana (request):
    compra = Compra(request)
    compra.agregar_vegana()
    return redirect("productos")

def restar_vegana (request):
    compra = Compra(request)
    compra.restar_vegana()
    return redirect("productos")

def eliminar_vegana(request):
    compra= Compra(request)
    compra.eliminar_vegana()
    return redirect("productos")