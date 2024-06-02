from django.shortcuts import render, redirect, get_object_or_404
from .models import Musician
from .forms import MusicianForm

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians/musician_list.html', {'musicians': musicians})

def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musicians/edit_musician.html', {'form': form})

def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    if request.method == 'POST':
        musician.delete()
        return redirect('musician_list')
    return render(request, 'musicians/delete_musician.html', {'musician': musician})
