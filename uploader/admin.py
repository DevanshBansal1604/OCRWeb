# admin file of django app (uploader) used to display the models

from django.contrib import admin
from uploader.models import File

admin.site.register(File)
