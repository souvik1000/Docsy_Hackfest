from django.contrib import admin
from .models import patient
from .models import allergies
# Register your models here.
admin.site.register(patient)
admin.site.register(allergies)