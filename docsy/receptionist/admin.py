from django.contrib import admin
from .models import doctor
from .models import prescription
from .models import problem
from .models import medicines
from .models import diagnostic
from .models import labreport
from .models import imagingexam
# Register your models here.
admin.site.register(doctor)
admin.site.register(prescription)
admin.site.register(problem)
admin.site.register(medicines)
admin.site.register(diagnostic)
admin.site.register(labreport)
admin.site.register(imagingexam)