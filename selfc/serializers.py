from rest_framework import serializers
from selfc.models import Usuarios,Admins,Activity,School,File,Test,Pregunta, Respuesta, Resultado
from django.contrib.auth.hashers import make_password

class UsuariosSerializers(serializers.ModelSerializer):
    def create(self, validated_data):
        # Set the password hash
        validated_data['password'] = make_password(validated_data['password'])
        user = super().create(validated_data)
        return user
    school= serializers.SlugRelatedField(queryset=School.objects.all(), slug_field="name")
    class Meta:
        model=Usuarios
        fields = '__all__'

class AdminsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Admins
        fields = '__all__'

def validate_name(value):
    if value not in ActivitySerializers.NAME_CHOICES:
        raise serializers.ValidationError("Invalid choice.")
    return value


class ActivitySerializers(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(queryset=Usuarios.objects.all(), slug_field="email")
    class Meta:
        model=Activity
        fields = '__all__'



class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'

class FileSerializers(serializers.ModelSerializer):
    class Meta:
        model=File
        fields= '__all__'

class TestSerializers(serializers.ModelSerializer):
    usuario = serializers.SlugRelatedField(queryset=Usuarios.objects.all(), slug_field="email")
    class Meta:
        model=Test
        fields= '__all__'

class PreguntaSerializers(serializers.ModelSerializer):
    test_type = serializers.SlugRelatedField(queryset=Test.objects.all(), slug_field="test_type")
    usuario = serializers.SlugRelatedField(queryset=Usuarios.objects.all(), slug_field="email")

    class Meta:
        model=Pregunta
        fields= '__all__'

class RespuestaSerializers(serializers.ModelSerializer):
    pregunta = serializers.SlugRelatedField(queryset=Pregunta.objects.all(), slug_field="id")
    class Meta:
        model=Respuesta
        fields= '__all__'

class ResultadoSerializers(serializers.ModelSerializer):
    test = serializers.SlugRelatedField(queryset=Test.objects.all(), slug_field="test_type")
    usuario = serializers.SlugRelatedField(queryset=Usuarios.objects.all(), slug_field="email")
    class Meta:
        model=Resultado
        fields= '__all__'