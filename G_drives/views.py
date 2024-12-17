from django.shortcuts import render, redirect
from .models import Folder
from django.contrib.auth import login  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import FolderForm  , FileUploadForm
from django.db import connection

def get_folders(user):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_folder WHERE owner_id = %s;", [user.id])
        rows = cursor.fetchall()
        return rows

@login_required  
def home(request):
    folders = get_folders(user = request)

    return render(request, 'home.html', {'folders': folders})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home') 
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

@login_required
def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            
            folder = form.save(commit=False)
            folder.owner = request.user 
            folder.save()
            return redirect('folder_list') 
    else:
        form = FolderForm()

    return render(request, 'folder/create_folder.html', {'form': form})


def folder_list(request):
    folders = Folder.objects.filter(owner=request.user)  
    return render(request, 'folder/folder_list.html', {'folders': folders})

from django.shortcuts import get_object_or_404

def update_folder(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    if request.method == 'POST':
        form = FolderForm(request.POST, instance=folder)
        if form.is_valid():
            form.save()
            return redirect('folder_list')
    else:
        form = FolderForm(instance=folder)

    return render(request, 'folder/update_folder.html', {'form': form, 'folder': folder})

from django.shortcuts import get_object_or_404

def delete_folder(request, pk):
    folder = get_object_or_404(Folder, pk=pk)
    folder.delete()
    return redirect('folder_list')  

@login_required
def upload_file(request, folder_id):
    folder = Folder.objects.get(id=folder_id)

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.folder = folder 
            file.save()
            return redirect('folder_details', folder_id=folder.id) 
    else:
        form = FileUploadForm()

    return render(request, 'folder/upload_file.html', {'form': form, 'folder': folder})


@login_required
def folder_details(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id, owner=request.user)

    return render(request, 'folder/folder_details.html', {'folder': folder})