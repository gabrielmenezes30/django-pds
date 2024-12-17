from django.urls import path, include
from .views import home, categoria, cadastrar_categoria, cadastrarCategoria, editarProduto, updateProduto, cadastrarProduto, cadastrar_produto, editarCategoria, updateCategoria, delete, custom_login, test_view, custom_logout


urlpatterns = [
    path('', home, name="home"),
    path('categoria/<int:id>', categoria, name="categoria"),
    path('cadastrar_categoria/', cadastrar_categoria, name="cadastrar_categoria"),
    path('cadastrarCategoria', cadastrarCategoria, name="cadastrarCategoria"),

    path('editarProduto/<int:id>', editarProduto, name="editarProduto"),
    path('updateProduto/<int:id>', updateProduto, name="updateProduto"),
    
    path('cadastrarProduto', cadastrarProduto, name="cadastrarProduto"),
    path('cadastrar_produto', cadastrar_produto, name="cadastrar_produto"),

    path('editarCategoria/<int:id>', editarCategoria, name="editarCategoria"),
    path('updateCategoria/<int:id>', updateCategoria, name="updateCategoria"),

    path('delete/<int:id>', delete, name="delete"),

    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),

    path('test/', test_view, name='test'),
]
