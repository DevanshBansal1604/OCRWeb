# urls route of app's templates

from django.urls import path
from uploader.views import home

urlpatterns = [
    path('', home, name='home'),
]
