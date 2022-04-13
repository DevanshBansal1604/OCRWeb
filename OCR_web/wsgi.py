# wsgi file, used for deployement purpose only. 

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OCR_web.settings')
application = get_wsgi_application()
