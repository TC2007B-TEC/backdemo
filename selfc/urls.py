from django.urls import path
from selfc import views


urlpatterns=[
    path("usuario/",views.usuariosApi), 
    path("usuario/<slug:email>/",views.usuariosApi),
    path("login/",views.login)

]