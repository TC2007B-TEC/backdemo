from django.urls import path
from selfc import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="SEL4C API",
      default_version='v1',
      description="API's para la conexión de los emprendedores sociales, para la conexión con ios y front",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("usuario/",views.usuariosApi),
    path("school/",views.schoolApi),
    path("usuariolog/",views.loginusu),
    path("adminlog/",views.loginadmin),
    path("fileup/",views.postfile),
    path("filedown/",views.download_file),
    path("newtest/",views.crear_test),
    path("newpregunta/",views.crear_pregunta),
    path("profe/",views.profesApi),
    path("activity/",views.ActivityApi),
    path("unusuario/",views.unUsuario),
    path("verifact/",views.verifact),
    path("getpreguntas/",views.getTest),
    path("filedownapp/",views.download_fileapp),
    path("getname/",views.getName),
    path("getact/",views.getActividades)


]