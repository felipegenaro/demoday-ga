from django.shortcuts import render
from contato_page.forms import ContatoCriarForm

# Create your views here.

def adicionar_contato(request):
        formulario = ContatoCriarForm(request.POST or None)

        if formulario.is_valid():
                formulario.save()
                formulario = ContatoCriarForm()

        context = {
                'form': formulario
        }
        
        return render(request, 'contato.html', context)