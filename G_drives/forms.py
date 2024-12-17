from django import forms
from .models import Folder,File

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']  

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'folder']  