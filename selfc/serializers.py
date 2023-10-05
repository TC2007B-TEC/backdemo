from rest_framework import serializers
from selfc.models import Usuarios,Admins,Activity,Tests, School

class UsuariosSerializers(serializers.ModelSerializer):
    school= serializers.SlugRelatedField(queryset=School.objects.all(), slug_field="name")
    class Meta:
        model=Usuarios
        fields = '__all__'

class AdminsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Admins
        fields = '__all__'

class ActivitySerializers(serializers.ModelSerializer):
    NAME_CHOICES = (
        ("A1", "Activity 1"),
        ("A2", "Activity 2"),
        ("A3", "Activity 3"),
        ("A4", "Activity 4"),
        ("FA", "Final Activity"),
    )
    name = serializers.ChoiceField(choices=NAME_CHOICES)
    author = serializers.SlugRelatedField(queryset=Usuarios.objects.all(), slug_field="email")
    class Meta:
        model=Activity
        fields = '__all__'


class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tests
        fields = '__all__'

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model=School
        fields = '__all__'