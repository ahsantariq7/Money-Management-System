from django.contrib import admin
from .models import models_name

# Register your models here.
for model in models_name:
    admin.site.register(model)
