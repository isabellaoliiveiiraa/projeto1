# recipes/urls.py
from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='recipes_home'),
]

# recipes/urls.py
from django.urls import path # Importa a função 'path' que define URLs.
from . import views # Importa o arquivo views.py do próprio app.

urlpatterns = [
path('', views.recipe_list, name='recipe_list'), # nova view para listar
]

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'), # view para listar receitas
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'), # view para detalhes
]