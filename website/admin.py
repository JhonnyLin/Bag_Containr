from django.contrib import admin
from website.models import Cadastro, Contato
from .models import Post

# Register your models here.
admin.site.register(Cadastro)
admin.site.register(Contato)
admin.site.register(Post)