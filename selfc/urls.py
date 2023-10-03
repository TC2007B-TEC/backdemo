from django.urls import path
from selfc import views


urlpatterns=[
    path("usuario/",views.usuariosApi),
    path("admin/",views.adminsApi),
    path("tests/",views.testsApi),
    path("usuario/<slug:email>/",views.usuariosApi),
    path("login/",views.login)

]