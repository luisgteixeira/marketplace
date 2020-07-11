from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from marketplace.models import Pessoa
from marketplace.serializers import PessoaSerializer


@csrf_exempt
def pessoas(request):
    """
    Busca todas as pessoas cadastradas, ou cria uma nova pessoa
    """
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        serializer = PessoaSerializer(pessoas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PessoaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pessoa_id(request, id_pessoa):
    """
    Busca ou deleta pessoa através do id_pessoa
    """
    try:
        pessoa = Pessoa.objects.filter(id_pessoa=id_pessoa)
    except Pessoa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        pessoa.delete()
        return HttpResponse(status=204)


@csrf_exempt
def pessoa_email(request, email):
    """
    Busca ou deleta pessoa através do email
    """
    try:
        pessoa = Pessoa.objects.filter(email=email)
    except Pessoa.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PessoaSerializer(pessoa, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        pessoa.delete()
        return HttpResponse(status=204)