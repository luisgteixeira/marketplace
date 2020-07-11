from marketplace.models import Pessoa
from rest_framework import serializers


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id_pessoa', 'nome', 'email', 'cep', 'telefone']
        #fields = ['nome', 'email', 'cep', 'telefone']