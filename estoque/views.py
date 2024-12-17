from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Produto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial ou outra página desejada
        else:
            messages.error(request, 'Usuário ou senha incorretos')  # Adiciona mensagem de erro
            return render(request, 'login.html')  # Retorna para a página de login com a mensagem
    else:
        return render(request, 'login.html') 

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def test_view(request):
    return HttpResponse("Você está autenticado!")

@login_required
def home(request):
    categorias = Categoria.objects.all()
    return render(request, "index.html", {"categorias": categorias})


@login_required
def categoria(request, id):
    # categoria = Categoria.objects.get(id=id)
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria.objects.prefetch_related('produtos'), id=id)
    return render(request, "categoria.html", {"categoria": categoria, "categorias": categorias})


@login_required
def cadastrar_categoria(request):
    return render(request, "cadastrar_categoria.html")


@login_required
def cadastrarCategoria(request):
    nome = request.POST.get("nome")
    Categoria.objects.create(nome=nome)
    categorias = Categoria.objects.all()
    return render(request, "index.html", {"categorias": categorias})


@login_required
def editarProduto(request, id):
    produto = get_object_or_404(Produto, id=id) 
    categorias = Categoria.objects.all() 
    return render(request, "produto.html", {"produto": produto, "categorias": categorias})

@login_required
def updateProduto(request, id):
    produto = get_object_or_404(Produto, id=id)
    categorias = Categoria.objects.all() 

    if request.method == "POST":
        produto.nome = request.POST.get("nome")
        produto.categoria_id = request.POST.get("categoria")
        produto.quantidade = request.POST.get("quantidade")
        produto.preco = request.POST.get("preco")
        produto.descricao = request.POST.get("descricao")
        produto.save()
        return redirect('categoria', id=produto.categoria.id)  

    return render(request, "editar_produto.html", {"produto": produto, "categorias": categorias})


@login_required
def cadastrarProduto(request):
    categorias = Categoria.objects.all() 
    return render(request, "cadastrarProduto.html", {"categorias": categorias})


@login_required
def cadastrar_produto(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        categoria_id = request.POST.get("categoria")
        quantidade = request.POST.get("quantidade")
        preco = request.POST.get("preco")
        descricao = request.POST.get("descricao")

      
        categoria = Categoria.objects.get(id=categoria_id)  
        Produto.objects.create(
            nome=nome,
            categoria=categoria,
            quantidade=quantidade,
            preco=preco,
            descricao=descricao
        )
        return redirect('categoria', id=categoria.id)

    # Caso contrário, exibir a página de cadastro de produtos
    categorias = Categoria.objects.all()
    return render(request, "cadastrarProduto.html", {"categorias": categorias})


@login_required
def editarCategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, "editarCategoria.html", {"categoria": categoria})


@login_required
def updateCategoria(request, id):
 
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
   
        nome = request.POST.get("nome")
        if nome: 
            categoria.nome = nome
            categoria.save()  
            return redirect('home')  

    return render(request, "editar_categoria.html", {"categoria": categoria})


@login_required
def delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('categoria', id=produto.categoria.id)  
    
