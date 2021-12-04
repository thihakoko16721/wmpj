from django.contrib import admin
from .models import Clinic
# Register your models here.
class ClinicAdmin(admin.ModelAdmin):
    list_dsplay = ['paitent_name', 'paitent_phone', 'paitent_address', 'paitent_case', 'drug', 'fees', 'doctor', 'datetime']
    list_filter = ['paitent_address', 'paitent_case', 'doctor', 'drug', 'fees', 'datetime']
    search_fields = ['paitent_name']

admin.site.register(Clinic, ClinicAdmin)