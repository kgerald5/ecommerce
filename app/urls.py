from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),  # Correction du nom de la vue
    # Autres vues et chemins URL peuvent être ajoutés ici
   # path('category/ ', views.CategoryView.as_view(), name='category')
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
]