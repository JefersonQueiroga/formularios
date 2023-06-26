from django import forms
from .models import Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'

         # Definindo o CSS para o ModelForm
 

