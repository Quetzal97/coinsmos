from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

STATUS = (
    (0, "Borrador"),
    (1, "Publicacion")
)

postd = (
    (0, "Estandar"),
    (1, "Destacado"),
)
# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')

choices = Categoria.objects.all().values_list('name','name')

choice_list = []
for item in choices:
    choice_list.append(item)


class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    categoria = models.CharField(max_length = 20, choices = choice_list, default = 'Noticias')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    updated_on = models.DateTimeField(auto_now = True)
    thumbnail = models.CharField(max_length = 10000, default = 'https://coinsmos.s3.us-east-2.amazonaws.com/coinastrologo.png', editable = True)
    content =RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(choices = STATUS, default = 0)
    destacado = models.IntegerField(choices = postd, default = 0 )
    banner = models.CharField(max_length = 10000, default = "https://i.ibb.co/5FqNvJP/banner3.png", editable = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
