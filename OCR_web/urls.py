# file that stores all the views/links to web pages deployed

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # default page of django administration
    path('admin/', admin.site.urls),
    # default page of our project, accessible via 'localhost/'
    path('', include("uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
