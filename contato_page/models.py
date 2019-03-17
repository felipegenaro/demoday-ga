from django.db import models

# Create your models here.

class Contato(models.Model):
        SUGESTAO = 'SG'
        CRITICAS = 'CT'
        DIVERSOS = 'DV'

        ASSUNTO = [
                (SUGESTAO, 'Sugestões'),
                (CRITICAS, 'Críticas'),
                (DIVERSOS, 'Diverso'),
        ]


        nome = models.CharField(max_length=40)
        email =  models.EmailField()
        assunto = models.CharField(max_length=2, choices=ASSUNTO, default=SUGESTAO)
        descricao = models.TextField(max_length=240, blank=True, null=True)

        def __str__(self):
                return self.email