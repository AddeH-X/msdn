from django.contrib import admin

# Register your models here.
from distribution.models import Hospital,M_material

admin.site.register(Hospital)
admin.site.register(M_material)