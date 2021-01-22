from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from .models import Post, Comentario
from .forms import CommentForm
from django.urls import reverse_lazy, path
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class PostDest(generic.ListView):
    model = Post
    queryset = Post.objects.filter(destacado = 1).order_by('created_on')
    template_name = 'index.html'

def contacto(request):
    return render(request, 'contacto.html')

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddCommentView(CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = 'comentar.html'
    #fields = '__all__'
    success_url = reverse_lazy('post_detail')

def CategoryView(request, ctgs):
    ctgs = ctgs.lower()
    post_ctgs = Post.objects.filter(categoria = ctgs)
    paginator = Paginator(post_ctgs, 6)
    page = request.GET.get('page')
    try:
        post_ctgs = paginator.page(page)
    except PageNotAnInteger:
        post_ctgs = paginator.page(1)
    except EmptyPage:
        post_ctgs = paginator.page(paginator.num_pages)
    return render(request, 'categorias.html', {'ctgs' : ctgs.title(), 'page':page ,'post_ctgs':post_ctgs})

def post_list(request):
    query = request.GET.get('q', '')
    queryset_list = Post.objects.filter(status = 1).order_by('-created_on')
    if query:
        queryset_list = queryset_list.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        'object_list' : queryset,
        'title' : 'List',
        'page' : page,
    }
    return render(request, 'busqueda.html', context)
