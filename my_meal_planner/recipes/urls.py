from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import (
    HomeView, 
    RecipeCreateView,
    RecipeDetailView,
    RecipeUpdateView,
    RecipeDeleteView,
    TagListView,
    SearchView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='mmp-home'),
    path('recipe/new/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipe/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),
    path('tag/', TagListView.as_view(), name='tag-list'),
    path('search/', SearchView.as_view(), name='search-list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)