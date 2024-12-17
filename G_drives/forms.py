from django import forms
from .models import Folder,File

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']  # Parent folder is optional

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'folder']  # Ensure folder is passed to associate the file with a folder