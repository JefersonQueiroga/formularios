from django.shortcuts import render
from .forms import AlunoForm
from .models import Aluno

def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            nome =  form.cleaned_data['nome']
            email = form.cleaned_data['email']
            data_nascimento = form.cleaned_data['data_nascimento']
            Aluno.objects.create(nome=nome, email=email, data_nascimento=data_nascimento)

            form = AlunoForm()
    else:
        print("->>>> entrou primeiro aqui")
        form = AlunoForm()
    
    context ={
        'form' : form,
        'nome' : "Jeferson Queiroga"
    }
    return render(request, 'escola/form_aluno.html', context)