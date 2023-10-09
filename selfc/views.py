from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from selfc.models import Usuarios,Admins,Activity,Test,School,File,Pregunta, Resultado, Profesor
from selfc.serializers import UsuariosSerializers,AdminsSerializers,ActivitySerializers, TestSerializers, SchoolSerializers, FileSerializers,PreguntaSerializers,ResultadoSerializers,ProfesoresSerializers
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
def profesApi(request, email=None):
    if request.method=='GET':
        queryset = Profesor.objects.all()
        email = request.GET.get('email')
        if email is not None:
            queryset = queryset.filter(email=email)
        profesores_ser = ProfesoresSerializers(queryset,many=True)
        return JsonResponse(profesores_ser.data,safe=False)
    elif request.method=='POST':
        profesordata =JSONParser().parse(request)
        profesores_ser=ProfesoresSerializers(data=profesordata)
        if profesores_ser.is_valid():
            profesores_ser.save()
            return JsonResponse({"message": "Admin anadido exitosamente"}, safe=False, status=status.HTTP_201_CREATED)
        print(profesores_ser.errors)
        return JsonResponse("No se pudo agregar", safe=False, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def adminsApi(request, email=None):
    if request.method=='GET':
        queryset = Admins.objects.all()
        email = request.GET.get('email')
        if email is not None:
            queryset = queryset.filter(email=email)
        admins_ser = AdminsSerializers(queryset,many=True)
        return JsonResponse(admins_ser.data,safe=False)
    elif request.method=='POST':
        admindata =JSONParser().parse(request)
        admins_ser=AdminsSerializers(data=admindata)
        if admins_ser.is_valid():
            admins_ser.save()
            return JsonResponse({"message": "Admin anadido exitosamente"}, safe=False, status=status.HTTP_201_CREATED)
        print(admins_ser.errors)
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

@api_view(['POST'])
def loginusu(request):
    email = request.data['email']
    password = request.data['password']

    user = Usuarios.objects.filter(email=email).first()
    if user is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    data = {
        'email': user.email,
        'name': user.name,
        'lname': user.lname,
        'gender': user.gender,
        'age': user.age,
        'country': user.country,
        'discipline': user.discipline,
        'school': user.school.name,
    }
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['POST'])
def loginadmin(request):
    email = request.data['email']
    password = request.data['password']

    user = Admins.objects.filter(email=email).first()
    if user is None:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    data = {
        'email': user.email,
        'name': user.name,
        'lname': user.lname,
        'role': user.role,
    }
    return Response(data=data,status=status.HTTP_200_OK)


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
    data = JSONParser().parse(request)

    # Obtenemos el test del usuario con el test_type especificado
    test = Test.objects.filter(test_type=data['test_type'], usuario=data['usuario']).first()
    if test is None:
        return JsonResponse(
            "No existe un test con el nombre especificado para el usuario",
            safe=False,
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Creamos la pregunta
    pregunta = Pregunta(
        idpregunta=data['idpregunta'],
        usuario=data['usuario'],
        Test=test,
        resp=data['resp'],
        test_type=data['test_type'],
    )

    # Guardamos la pregunta en la base de datos
    pregunta.save()

    return JsonResponse({"message": "Pregunta creada exitosamente"}, safe=False, status=status.HTTP_201_CREATED)

