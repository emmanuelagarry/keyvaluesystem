from django.contrib import admin

# from .models import Store

from .models import Store, Entry

admin.site.register([Store, Entry])
