from marketplace.models import Pessoa
from rest_framework import viewsets
from marketplace.serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """
    endpoint da API que permite usuário visualizar ou editar.
    """
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    print(serializer_class)