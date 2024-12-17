from django.shortcuts import render, redirect
from .models import Folder
from django.contrib.auth.decorators import login_required

@login_required
def create_folder(request):
    if request.method == 'POST':
        name = request.POST['name']
        parent_id = request.POST.get('parent_id')
        parent = Folder.objects.get(id=parent_id) if parent_id else None
        Folder.objects.create(name=name, parent=parent, owner=request.user)
        return redirect('folder_list')
    return render(request, 'create_folder.html')
