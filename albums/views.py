from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {'form': form})

def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/edit_album.html', {'form': form})

def delete_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('album_list')
    return render(request, 'albums/delete_album.html', {'album': album})
