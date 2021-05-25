from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumos
from .forms import InsumosForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import InsumosSerializer, TokenSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice
# Create your views here.

@api_view(["POST"])
def save_token(request):
    #ssssssssssssssssssssssssssssssss
    serializador = TokenSerializer(data=request.data)
    if serializador.is_valid():
        token = serializador.data["token"]

        dispositivo = FCMDevice.objects.filter(registration_id=token, active=True).first()

        if not dispositivo:
            dispositivo = FCMDevice(registration_id=token, active=True)

        if request.user.is_authenticated:
            dispositivo.user = request.user
        
        dispositivo.save()

        return JsonResponse({"mensaje": "ok"}, status=200)
    return JsonResponse({"mensaje": "no viene el token"}, status=400)

def error_facebook(request):
    return render(request, 'registration/error_facebook.html')

class InsumosViewset(viewsets.ModelViewSet):
    queryset = Insumos.objects.all()
    serializer_class = InsumosSerializer

    def get_queryset(self):
        insumos = Insumos.objects.all()

        nombre = self.request.GET.get('nombre')
        cantidad = self.request.GET.get('cantidad')

        if nombre:
            insumos = insumos.filter(nombre__contains=nombre)
            
        if cantidad:
            insumos = insumos.filter(cantidad=cantidad)
        
        return insumos
   

def home(request):
    insumos = Insumos.objects.all()
    data = {
        'insumos': insumos
    }

    return render(request, 'app/home.html', data)


@permission_required('app.add_insumos')
def agregar_insumos(request):

    data ={
        'form': InsumosForm()
    }
    if request.method == 'POST':
        formulario = InsumosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()

            nombre_insumo = formulario.cleaned_data["nombre"]

            dispositivo = FCMDevice.objects.all()
            
            dispositivo.send_message(
                tile="Nuevo insumo ingresado",
                body=f"han ingresado el insumo {nombre_insumo}",
                icon="/static/app/img/logo.png"
            )

            messages.success(request, "Insumo agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/insumos/agregar.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)

@permission_required('app.view_insumos')
def listar_insumos(request):

    insumos = Insumos.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(insumos, 10)
        insumos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': insumos,
        'paginator':paginator
    }

    return render(request, 'app/insumos/listar.html', data)

@permission_required('app.change_insumos')
def modificar_insumos(request, id):

    insumos = get_object_or_404(Insumos, id=id )

    data = {
        'form': InsumosForm(instance=insumos)
    }

    if request.method == 'POST':
        formulario = InsumosForm(data=request.POST, instance=insumos, files=request.FILES)
        if formulario.is_valid():
            messages.success(request, "Modificado correctamente")
            formulario.save()
            return redirect(to="listar_insumos")
            data["Form"] = formulario


    return render(request, 'app/insumos/modificar.html/', data)

@permission_required('app.delete_insumos')
def eliminar_insumos(request, id):
    insumos = get_object_or_404(Insumos, id=id )
    insumos.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_insumos")

def listar_pedidos(request):

    return render(request,'app/vendedor/listar_pedidos.html')

def listar_ordenes(request):

    return render(request,'app/bodeguero/listar_ordenes.html')
