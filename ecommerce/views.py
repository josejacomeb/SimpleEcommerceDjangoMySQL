from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader # Carga la plantilla de HTML 
from .models import Televisores, TelefonoCelular, Laptop # Aqui importo mis modelos creados
from .forms import TVForma, LaptopForma, CelularForma

# Diccionario que contiene todos los modelos
MODELOS_FORMAS_ECOMMERCE = {
    "tv": {
        "modelo": Televisores,
        "forma": TVForma
    },
    "celular": {
        "modelo": TelefonoCelular,
        "forma": CelularForma
    },
    "laptop": {
        "modelo": Laptop,
        "forma": LaptopForma
    }
}

# Create your views here.
def index(request):
    # Revisar todos los electrodomésticos
    datos_electrodomesticos = []
    for nombre in MODELOS_FORMAS_ECOMMERCE.keys():
        datos = MODELOS_FORMAS_ECOMMERCE[nombre]["modelo"].objects.all()
        atributos = MODELOS_FORMAS_ECOMMERCE[nombre]["forma"].Meta.fields
        datos_compilados = {"datos": datos, "atributos": atributos, "nombre": nombre}
        print(datos_compilados)
        datos_electrodomesticos.append(datos_compilados)
        
    template = loader.get_template("ecommerce/index.html")
    context = {
        "datos_electrodomesticos": datos_electrodomesticos,
    }
    return HttpResponse(template.render(context, request))

def anadir(request, nombre):
    # Chequear haya ese nombre en los modelos incluidos
    if nombre in MODELOS_FORMAS_ECOMMERCE:
        electrodomestico = MODELOS_FORMAS_ECOMMERCE[nombre]
    else:
        pass # Devolver algo nullo
    if request.method == 'POST':
        forma = electrodomestico["forma"](request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("index")
    else:
        # Cuando hay un Get por ejemplo, devolver una forma vacia
        forma = electrodomestico["forma"]()
    
    return render(request, 'ecommerce/anadir.html', {'forma': forma, 'nombre': nombre})

def editar(request, nombre, id):
    if nombre in MODELOS_FORMAS_ECOMMERCE:
        electrodomestico = MODELOS_FORMAS_ECOMMERCE[nombre]
    else:
        pass # Devolver algo nullo
    instancia_elec = get_object_or_404(electrodomestico["modelo"], id=id)
    if request.method == 'POST':
        forma = electrodomestico["forma"](request.POST, instance=instancia_elec)
        if forma.is_valid():
            forma.save()
            return redirect('index')  # Redirect to the TV list view after successful edit
    else:
        forma = electrodomestico["forma"](instance=instancia_elec)

    return render(request, 'ecommerce/editar.html', {'form': forma, 'instancia_elec': instancia_elec, "nombre": nombre, 'id': id})

def eliminar(request, nombre, id):
    if nombre in MODELOS_FORMAS_ECOMMERCE:
        electrodomestico = MODELOS_FORMAS_ECOMMERCE[nombre]
    else:
        pass # Devolver algo nullo
    instancia_elec = get_object_or_404(electrodomestico["modelo"], id=id)

    if request.method == 'POST':
        instancia_elec.delete()
        return redirect('index')  # Redirect to the TV list view after successful deletion

    return render(request, 'ecommerce/eliminar.html', {'nombre': nombre, 'instancia_elec': instancia_elec, 'id': id})