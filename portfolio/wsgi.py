import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings.dev')
application = Cling(get_wsgi_application())
