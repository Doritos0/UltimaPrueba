from django.urls import path
from .views import agregar_producto, agregar_tradicional, agregar_vegana, eliminar_producto, eliminar_tradicional, eliminar_vegana, inicio, limpiar_compra, locales, local_1, local_2, productos, producto1, producto2, registro, carrito, restar_producto, restar_tradicional, restar_vegana
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import lista_productos, detalle_producto, login

urlpatterns=[
    path('',inicio, name="inicio"),
    path('locales/', locales, name="locales"),
    path('local_1/', local_1, name="local_1"),
    path('local_2/', local_2, name="local_2"),
    path('productos/', productos, name="productos"),
    path('producto1/', producto1, name="producto1"),
    path('producto2/', producto2, name="producto2"),
    path('registro/', registro, name="registro"),
    path('carrito/', carrito, name="carrito"),
    path('lista_productos/', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),
    path('login/', login, name="login"),
    path ('agregar/<nom_produc>', agregar_producto, name="agregar"),
    path ('eliminar/<nom_produc>', eliminar_producto, name="eliminar"),
    path ('restar/<nom_produc>', restar_producto, name="restar"),
    path ('limpiar/', limpiar_compra, name="limpiar"),
    path ('tradicional/', agregar_tradicional, name="agregar_tradicional"),
    path ('restar_tradicional/', restar_tradicional, name="restar_tradicional"),
    path ('eliminar_tradicional/', eliminar_tradicional, name="eliminar_tradicional"),
    path ('vegana/', agregar_vegana , name="agregar_vegana"),
    path ('restar_vegana/', restar_vegana, name="restar_vegana"),
    path ('eliminar_vegana/', eliminar_vegana, name="eliminar_vegana"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)