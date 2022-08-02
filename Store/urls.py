
from django.urls import path
from Store import views
from Store.models import Produto

urlpatterns = [
    path('', views.index, name= 'index'),
    path('teste/', views.teste, name= 'teste'),
    path('Departamentos/', views.Departamentos,name='departamentos'),
    path('categorias/<int:id>', views.categorias, name='categorias'),
    path('produtos/<int:id>', views.produtos, name= 'produtos')
]