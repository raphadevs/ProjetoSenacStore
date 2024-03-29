from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from Store.models import Departamento, Categoria, Produto
from django.core.mail import send_mail


# Create your views here.
def index (request):
    meu_nome = 'Raphael Carvalho'
    sexo = 'M'
    context = {
        'nome': meu_nome,
        'artigo': 'o' if sexo == 'M' else 'a'}
    return render(request, 'index.html', context)

def teste(request):
 # depto = ['Casa', 'Informática', 'Telefonia', 'Game']
    depto = Departamento.objects.all ()
    context = {'departamentos': depto}
    return render(request, 'teste.html', context)

def Departamentos(request):
    depto = Departamento.objects.all ()
    context = {'departamentos': depto}
    return render(request, 'departamentos.html', context)

def categorias(request, id):
    lista_categorias = Categoria.objects.filter(departamento_id = id)
    depto = Departamento.objects.get(id = id)
    context = {
                'categorias': lista_categorias,
                'departamento': depto
    }
    return render(request, 'categorias.html', context)

def produtos(request, id):
    tabela_produtos = Produto.objects.filter (categoria_id = id)
    context = {'produtos': tabela_produtos}
    return render(request, 'produtos.html', context)

def produtos_detalhe(request, id):
    produtos = Produto.objects.get(id =id)
    context = {
                'produto': produtos
    }
    return render (request, 'produto_detalhe.html',context)

def institucional (request):
    return render(request, 'institucional.html')

def contato(request):
    return render (request, 'contato.html')

def enviar_email(request):
    nome = request.POST['nome']
    telefone = request.POST['telefone']
    assunto = request.POST['assunto']
    mensagem = request.POST['mensagem']
    remetente = request.POST['email']
    destinatario = ['raphaelcarvalho.law@gmail.com']
    corpo = f"Nome: {nome} \nTelefone: {telefone}  \nMensagem : {mensagem}"
    
    try:
        send_mail(assunto, corpo, remetente, destinatario)
        context = {'msg': 'E-mail enviado com sucesso!'}
        
    except:
        context = {'msg': 'Erro ao enviar e-mail!'}
    return render(request, 'contato.html', context)





