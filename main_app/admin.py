from django.contrib import admin
# import your models here
from .models import Watch, Brand, Band

# Register your models here
admin.site.register(Watch)
admin.site.register(Brand)
admin.site.register(Band)

