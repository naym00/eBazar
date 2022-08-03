from django.contrib import admin
from .models import Mobile_Description, Mobile_Colors, Mobile_Images, Mobile_Ram_Rom

# Register your models here.

admin.site.register([Mobile_Description, Mobile_Colors, Mobile_Images, Mobile_Ram_Rom])
