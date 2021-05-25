from django.urls import path, include
from .views import home, listar_ordenes, registro, agregar_insumos, listar_insumos, modificar_insumos, eliminar_insumos, listar_pedidos, InsumosViewset, error_facebook, save_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register('insumos', InsumosViewset)


urlpatterns = [

    path('', home, name ="home"),
    path('registro/', registro, name="registro"),
    path('agregar-insumos/', agregar_insumos, name="agregar_insumos"),
    path('listar-insumos/', listar_insumos, name="listar_insumos"),
    path('modificar-insumos/<id>/', modificar_insumos, name="modificar_insumos"),
    path('eliminar-insumos/<id>/', eliminar_insumos, name="eliminar_insumos"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
    path('save-token/', save_token, name="save_token"),
    path('listar-pedidos/', listar_pedidos, name="listar_pedidos"),
    path('listar-ordenes/', listar_ordenes, name="listar_ordenes"),


]