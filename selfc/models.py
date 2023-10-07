from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)

class Usuarios(models.Model):
    email = models.EmailField(max_length=500,primary_key=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    discipline = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class File(models.Model):
    file=models.FileField(upload_to='files/', null=True, blank=True,default=None)

class Activity(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='activities')
    file = models.OneToOneField(File, on_delete=models.CASCADE, related_name='activity',default=None)



class Admins(models.Model):
    email = models.EmailField(max_length=200,primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    role = models.CharField(max_length=50,default="admin")

class Test(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50)

class Pregunta(models.Model):
    # ...
    # Definimos la relación con el modelo Test
    namepregunta=models.CharField(max_length=500)
    idpregunta = models.IntegerField()
    usuario= models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    test_type = models.ForeignKey(Test, on_delete=models.CASCADE)

class Respuesta(models.Model):
    # ...
    respuesta = models.IntegerField()
    # Definimos la relación con el modelo Pregunta
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Resultado(models.Model):
    # Definimos la relación con el modelo Test
    test_type = models.ForeignKey(Test, on_delete=models.CASCADE)

    # Definimos la relación con el modelo Usuario
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    # Definimos el campo de resultados
    resultados = models.IntegerField(default=0)
