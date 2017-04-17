from django.contrib import admin
from .models import Place,CarOwner,Security,LandOwner

from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Place)
admin.site.register(CarOwner)
admin.site.register(LandOwner)
admin.site.register(Security)