from rest_framework import serializers
from selfc.models import Usuarios,Admins,Activity,Tests

class UsuariosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Usuarios
        fields = '__all__'

class AdminsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Admins
        fields = '__all__'

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields = '__all__'

class TestSerializers(serializers.ModelSerializer):
    class Meta:
        model=Tests
        fields = '__all__'