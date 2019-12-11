from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    cpf = models.IntegerField()
    dataN = models.DateField()
    mae = models.CharField(max_length=140)
    opcoes_plano = [
        ('Mensal', 'Basic'),
        ('trimestral', 'Padrao'),
        ('Anual', 'Premium'),
    ]
    login = models.CharField(max_length=15, default= "1111")
    senha = models.CharField(max_length=15, default= "1111")

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField()
    assunto = models.CharField(max_length=30)
    messagem = models.CharField(max_length=400)

    def __str__(self):
        return self.nome