from django.shortcuts import render
from .forms import ProfessorForm

def cadastrar_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfessorForm()
    else:
        form = ProfessorForm()
    
    return render(request, 'form2/cadastro_professor.html', {'form': form})