from django.contrib import admin
from core.models import *

# Register Roles model.
admin.site.register(Roles)

# Register Gender model
admin.site.register(Gender)

# Register Doctor model.
admin.site.register(Doctor)

# Register Patient model.
admin.site.register(Patient)
