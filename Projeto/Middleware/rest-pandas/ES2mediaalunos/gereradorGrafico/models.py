from django.db import models

# Create your models here.
class gereradorGrafico(models.Model):
    Ano = models.CharField(max_length=4)
    UnidadeGeografica = models.CharField(max_length=8)
    localizacao = models.CharField(max_length=6)
    DependenciaAdministrativa = models.CharField(max_length=7)
    Creche = models.FloatField()
    PreEscola = models.FloatField()
    AnosIniciais = models.FloatField()
    AnosFinais = models.FloatField()
    _1Ano = models.FloatField()
    _2Ano = models.FloatField()
    _3Ano = models.FloatField()
    _4Ano = models.FloatField()
    _5Ano = models.FloatField()
    _6Ano = models.FloatField()
    _7Ano = models.FloatField()
    _8Ano = models.FloatField()
    _9Ano = models.FloatField()
    TurmasMultietapa = models.FloatField()
    _1Serie = models.FloatField()
    _2Serie = models.FloatField()
    _3Serie = models.FloatField()
    _4Serie = models.FloatField()
    NaoSeriado = models.FloatField()