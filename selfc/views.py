from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from selfc.models import Usuarios,Admins,Activity,Tests,School
from selfc.serializers import UsuariosSerializers,AdminsSerializers,ActivitySerializers, TestSerializers, SchoolSerializers
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.permissions import AllowAny 
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.

@csrf_exempt
def usuariosApi(request, id=0):
    if request.method=='GET':
        usuarios = Usuarios.objects.all()
        usuarios_ser = UsuariosSerializers(usuarios,many=True)
        return JsonResponse(usuarios_ser.data,safe=False)
    elif request.method=='POST':
        usuariosdata =JSONParser().parse(request)
        usuarios_ser=UsuariosSerializers(data=usuariosdata)
        if usuarios_ser.is_valid():
            usuarios_ser.save()
            return JsonResponse("Usuario anadido exitosamente", safe=False, status=status.HTTP_201_CREATED) 
        return JsonResponse("No se pudo agregar", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='PUT':
        usuariodata =JSONParser().parse(request)
        usuario = Usuarios.objects.get(usuarioemail=usuariodata['email'])
        usuarios_ser=UsuariosSerializers(usuario,data=usuariodata)
        if usuarios_ser.is_valid():
            usuarios_ser.save()
            return JsonResponse("Usuario actualizado exitosamente", safe=False, status=status.HTTP_200_OK) 
        return JsonResponse("No se actualizo", safe=False, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method=='DELETE':
        usuario=Usuarios.objects.get(email=id)
        usuario.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False, status=status.HTTP_204_NO_CONTENT) 
    
@ensure_csrf_cookie
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

# Create a login view that uses the APIView and the JWT tokens

@csrf_exempt
def login(request):
    userdata =JSONParser().parse(request)
    email = userdata.data.get('email') # get the email from the request data
    password = request.data.get('password') # get the password from the request data

    user = authenticate(email=email, password=password) # authenticate the user

    if user is not None: # if user is valid
        refresh = RefreshToken.for_user(user) # create a refresh token for the user
        res = { 
            'refresh': str(refresh), # send the refresh token as a string
            'access': str(refresh.access_token), # send the access token as a string
        }
        return Response(res, status=status.HTTP_200_OK) # return a success response with the tokens
    else: # if user is invalid
        res = {
            'error': 'Invalid credentials' # send an error message
        }
        return Response(res, status=status.HTTP_401_UNAUTHORIZED) # return an unauthorized response
   
@csrf_exempt
def activitiesApi(request, id=0):
    if request.method=='GET':
        activities = Activity.objects.all()
        activities_ser = ActivitySerializers(activities,many=True)
        return JsonResponse(activities_ser.data,safe=False)
    elif request.method=='POST':
        activitiesdata =JSONParser().parse(request)
        activities_ser=ActivitySerializers(data=activitiesdata)
        if activities_ser.is_valid():
            activities_ser.save()
            return JsonResponse("activity anadido exitosamente", safe=False)
        return JsonResponse("No se pudo agregar", safe=False)
    elif request.method=='PUT':
        activitydata =JSONParser().parse(request)
        activity = Activity.objects.get(activityemail=activitydata['email'])
        activities_ser=ActivitySerializers(activity,data=activitydata)
        if activities_ser.is_valid():
            activities_ser.save()
            return JsonResponse("activity actualizado exitosamente", safe=False)
        return JsonResponse("No se actualizo")
    elif request.method=='DELETE':
        activity=Activity.objects.get(email=id)
        activity.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False)

@csrf_exempt
def testsApi(request, id=0):
    if request.method=='GET':
        tests = Tests.objects.all()
        tests_ser = TestSerializers(tests,many=True)
        return JsonResponse(tests_ser.data,safe=False)
    elif request.method=='POST':
        testsdata =JSONParser().parse(request)
        tests_ser=TestSerializers(data=testsdata)
        if tests_ser.is_valid():
            tests_ser.save()
            return JsonResponse("test anadido exitosamente", safe=False)
        return JsonResponse("No se pudo agregar", safe=False)
    elif request.method=='PUT':
        testdata =JSONParser().parse(request)
        test = test.objects.get(testemail=testdata['email'])
        tests_ser=TestSerializers(test,data=testdata)
        if tests_ser.is_valid():
            tests_ser.save()
            return JsonResponse("test actualizado exitosamente", safe=False)
        return JsonResponse("No se actualizo")
    elif request.method=='DELETE':
        test=test.objects.get(email=id)
        test.delete()
        return JsonResponse("Eliminado de forma correcta",safe=False)

@ensure_csrf_cookie
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

