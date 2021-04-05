from django.contrib import admin
from .models import Technology, Business, Science, Art
# Register your models here.
admin.site.register(Technology)
admin.site.register(Business)
admin.site.register(Science)
admin.site.register(Art)