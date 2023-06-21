from django.contrib import admin
from .models import Professor
# Register your models here.

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display=('nome','email','discipina')