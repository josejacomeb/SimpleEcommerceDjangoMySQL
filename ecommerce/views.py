from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader # Carga la plantilla de HTML 
from .models import Televisores, TelefonoCelular, Laptop # Aqui importo mis modelos creados
from .forms import TVForma, TVDeleteForm

# Create your views here.
def index(request):
    todos_televisores = Televisores.objects.all()
    todos_celulares = TelefonoCelular.objects.all()
    todos_laptops = Laptop.objects.all()
    template = loader.get_template("ecommerce/index.html")
    context = {
        "televisores": todos_televisores,
        "celulares": todos_celulares,
        "laptops": todos_laptops,
    }
    print(context)
    return HttpResponse(template.render(context, request))

def anadir_tv(request):
    if request.method == 'POST':
        forma = TVForma(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("index")
    else:
        # Cuando hay un Get por ejemplo, devolver una forma vacia
        forma = TVForma()
    print(forma)
    print(forma)
    print(forma)
    
    return render(request, 'ecommerce/anadir_tv.html', {'forma': forma})

def editar_tv(request, tv_id):
    instancia_tv = get_object_or_404(Televisores, id=tv_id)
    if request.method == 'POST':
        forma = TVForma(request.POST, instance=instancia_tv)
        if forma.is_valid():
            forma.save()
            return redirect('index')  # Redirect to the TV list view after successful edit
    else:
        forma = TVForma(instance=instancia_tv)

    return render(request, 'ecommerce/editar_tv.html', {'form': forma, 'instancia_tv': instancia_tv, 'tv_id': tv_id})

def eliminar(request, tv_id):
    instancia_tv = get_object_or_404(Televisores, id=tv_id)

    if request.method == 'POST':
        forma = TVDeleteForm(request.POST)
        instancia_tv.delete()
        return redirect('index')  # Redirect to the TV list view after successful deletion
    else:
        forma = TVDeleteForm()
    print(forma)

    return render(request, 'ecommerce/eliminar.html', {'forma': forma, 'instancia_tv': instancia_tv, 'tv_id': tv_id})