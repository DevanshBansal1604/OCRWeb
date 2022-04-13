# django file to keep records of all forms/models created

from msilib.schema import File
from django import forms
from uploader.models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', )
