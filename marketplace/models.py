from django.db import models

class Pessoa(models.Model):
    id_pessoa = models.AutoField(auto_created=True,primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11, null=True)

    class Meta:
        verbose_name_plural = 'pessoas'

    def __unicode__(self):
        return u"%s's Pessoa " % self.nome