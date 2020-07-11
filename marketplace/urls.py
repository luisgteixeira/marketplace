from django.urls import include, path
from marketplace import views

urlpatterns = [
    path('pessoas/', views.pessoas),
    path('pessoas/id_pessoa=<int:id_pessoa>/', views.pessoa_id),
    path('pessoas/email=<str:email>/', views.pessoa_email)
]