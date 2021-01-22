from . import views
from .views import CategoryView, AddCommentView, PostDest, contacto, post_list
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('', views.PostDest.as_view(), name = 'destacado'),
    path('categorias/<str:ctgs>/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('categorias/<str:ctgs>/', CategoryView, name = 'categoria'),
    path('contacto', views.contacto),
    path('busqueda.html', post_list, name = 'busqueda')
    #path('categorias/<str:ctgs>/<slug:slug>/comentar', AddCommentView.as_view(), name='comentar'),
]
