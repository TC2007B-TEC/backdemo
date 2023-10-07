from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from selfc.models import Usuarios,Admins,Activity,Test,School,File,Pregunta,Respuesta, Resultado
from selfc.serializers import UsuariosSerializers,AdminsSerializers,ActivitySerializers, TestSerializers, SchoolSerializers, FileSerializers,PreguntaSerializers,RespuestaSerializers,ResultadoSerializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from django.http import HttpResponse, FileResponse
from rest_framework import response, schemas


# Create your views here.



@csrf_exempt
def usuariosApi(request, email=None):
    if request.method=='GET':
        queryset = Usuarios.objects.all()
        email = request.GET.get('email')
        if email is not None:
            queryset = queryset.filter(email=email)
        usuarios_ser = UsuariosSerializers(queryset,many=True)
        return JsonResponse(usuarios_ser.data,safe=False)
    elif request.method=='POST':
        usuariodata =JSONParser().parse(request)
        usuarios_ser=UsuariosSerializers(data=usuariodata)
        if usuarios_ser.is_valid():
            usuarios_ser.save()
            return JsonResponse({"message": "Usuario anadido exitosamente"}, safe=False, status=status.HTTP_201_CREATED)
        print(usuarios_ser.errors)
        return JsonResponse("No se pudo agregar", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='PUT':
        usuariodata = request.data
        usuario = Usuarios.objects.get(email=usuariodata['email'])
        usuarios_ser=UsuariosSerializers(usuario,data=usuariodata)
        if usuarios_ser.is_valid():
            usuarios_ser.save()
            return JsonResponse("Usuario actualizado exitosamente", safe=False, status=status.HTTP_200_OK) 
        return JsonResponse("No se actualizo", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='DELETE':
        usuario=Usuarios.objects.get(email=email)
        usuario.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False, status=status.HTTP_204_NO_CONTENT) 
    
@csrf_exempt  
def adminsApi(request):
    if request.method=='GET':
        admins = Admins.objects.all()
        admins_ser = AdminsSerializers(admins,many=True)
        return JsonResponse(admins_ser.data,safe=False)
    elif request.method=='POST':
        adminsdata =JSONParser().parse(request)
        admins_ser=AdminsSerializers(data=adminsdata)
        if admins_ser.is_valid():
            admins_ser.save()
            return JsonResponse("admin anadido exitosamente", safe=False, status=status.HTTP_201_CREATED) 
        return JsonResponse("No se pudo agregar", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='PUT':
        admindata =JSONParser().parse(request)
        admin = Admins.objects.get(adminemail=admindata['email'])
        admins_ser=AdminsSerializers(admin,data=admindata)
        if admins_ser.is_valid():
            admins_ser.save()
            return JsonResponse("admin actualizado exitosamente", safe=False, status=status.HTTP_200_OK) 
        return JsonResponse("No se actualizo", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='DELETE':
        admin=Admins.objects.get(email=id)
        admin.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False, status=status.HTTP_204_NO_CONTENT) 


@csrf_exempt
def schoolApi(request):
    if request.method=='GET':
        schools = School.objects.all()
        schools_ser = SchoolSerializers(schools,many=True)
        return JsonResponse(schools_ser.data,safe=False)
    elif request.method=='POST':
        schoolsdata =JSONParser().parse(request)
        schools_ser=SchoolSerializers(data=schoolsdata)
        if schools_ser.is_valid():
            schools_ser.save()
            return JsonResponse("school anadido exitosamente", safe=False, status=status.HTTP_201_CREATED) 
        return JsonResponse("No se pudo agregar", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='PUT':
        schooldata =JSONParser().parse(request)
        school = School.objects.get(schoolemail=schooldata['email'])
        schools_ser=SchoolSerializers(school,data=schooldata)
        if schools_ser.is_valid():
            schools_ser.save()
            return JsonResponse("school actualizado exitosamente", safe=False, status=status.HTTP_200_OK) 
        return JsonResponse("No se actualizo", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='DELETE':
        school=School.objects.get(email=id)
        school.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False, status=status.HTTP_204_NO_CONTENT) 

def loginusu(request):
    # Get the query params from the request
    email = request.query_params.get('email')
    password = request.query_params.get('password')

    # Authenticate the user
    user = authenticate(email=email, password=password)

    # Verify the password
    if user is not None and check_password(password, user.password):
        return user
    else:
        return None


@csrf_exempt
@api_view(['POST'])
def postfile(request):
    if request.method != 'POST':
        # Devuelve un error 405 (Method Not Allowed)
        return Response({'status': 'error', 'message': 'Only POST requests are allowed.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    file_serializer = FileSerializers(data=request.data)
    if file_serializer.is_valid():
        file_serializer.save()

        activity_data = {
            'name': request.data['name'],
            'author': request.data['author'],
            'file': file_serializer.instance.pk
        }

        activity_serializer = ActivitySerializers(data=activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()

            return JsonResponse({'status': 'success'}, status=status.HTTP_201_CREATED)
        else:
            # Devuelve un error 400 (Bad Request) con los errores del serializador
            return Response({'status': 'error', 'errors': activity_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Devuelve un error 400 (Bad Request) con los errores del serializador
        return Response({'status': 'error', 'errors': file_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




@csrf_exempt
@api_view(['GET'])
def download_file(request):
    activity_id = request.GET.get('activity_id')
    activity = Activity.objects.get(id=activity_id)

    file = activity.file

    response = FileResponse(file.file)
    response['Content-Disposition'] = f'attachment; filename={file.file.name}'

    return response





@api_view()
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Bookings API')
    return response.Response(generator.get_schema(request=request))


@csrf_exempt
@api_view(['POST'])
def crear_test(request):
    if request.method == 'POST':
        test_data = JSONParser().parse(request)
        test_serializer = TestSerializers(data=test_data)
        if test_serializer.is_valid():
            test_serializer.save()
            return JsonResponse({"message": "Test creado exitosamente"}, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse("No se pudo crear el test", safe=False, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def crear_pregunta(request):
    if request.method == 'POST':
        pregunta_data = JSONParser().parse(request)
        pregunta_serializer = PreguntaSerializers(data=pregunta_data)
        if pregunta_serializer.is_valid():
            pregunta = pregunta_serializer.save()

            # Obtenemos el test del usuario
            test = Test.objects.filter(test_type=pregunta_data['test_type']).first()
            if test is None:
                return JsonResponse("No existe un test con el nombre especificado", safe=False, status=status.HTTP_400_BAD_REQUEST)

            # Asociamos la pregunta al test
            pregunta.test = test
            pregunta.save()

            return JsonResponse({"message": "Pregunta creada exitosamente"}, safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse("No se pudo crear la pregunta", safe=False, status=status.HTTP_400_BAD_REQUEST)

