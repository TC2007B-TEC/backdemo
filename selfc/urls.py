from django.urls import path
from selfc import views


urlpatterns=[
    path("usuario/",views.usuariosApi),
    path("activity/",views.activitiesApi),
    path("admin/",views.adminsApi),
    path("tests/",views.testsApi),
    path("school/",views.schoolApi),
    path("usuario/<slug:email>/",views.usuariosApi),
    path("login/",views.login),

]