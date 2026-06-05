from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .forms import DestinationForm
# Create your views here.pyrhon

def index(request):
    
    destinations = Destination.objects.all()    

    return render(request, 'index.html', {'destinations': destinations})

def agregar(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinationForm()
    return render(request, 'agregar.html', {'form': form})

def modificar(request, pk):
    dest = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=dest)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinationForm(instance=dest)
    return render(request, 'modificar.html', {'form': form, 'dest': dest})

def eliminar(request, pk):
    dest = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        dest.delete()
        return redirect('index')
    return render(request, 'eliminar.html', {'dest': dest})