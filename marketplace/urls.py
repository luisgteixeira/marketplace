from django.urls import include, path
from rest_framework import routers
from marketplace import views

router = routers.DefaultRouter()
router.register(r'pessoas', views.PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)), # conjunto de urls da aplicação
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # autenticação
]