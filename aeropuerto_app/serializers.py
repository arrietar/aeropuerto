from rest_framework import serializers
from aeropuerto_app.models import *

class Usuario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class Base_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = '__all__'

class Piloto_Serializer(serializers.ModelSerializer):
    base = Base_Serializer(read_only=True)
    base_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Base.objects.all(), source='base')
    class Meta:
        model = Piloto
        fields = '__all__'

class Avion_Serializer(serializers.ModelSerializer):
    base = Base_Serializer(read_only=True)
    base_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Base.objects.all(), source='base')
    class Meta:
        model = Avion
        fields = '__all__'

class Miembro_Serializer(serializers.ModelSerializer):
    base = Base_Serializer(read_only=True)
    base_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Base.objects.all(), source='base')
    class Meta:
        model = Miembro
        fields = '__all__'

class Tripulacion_Serializer(serializers.ModelSerializer):
    miembro = Miembro_Serializer(read_only=True)
    miembro_id =  serializers.PrimaryKeyRelatedField(write_only=True, queryset=Miembro.objects.all(), source='miembro')
    class Meta:
        model = Tripulacion
        fields = '__all__'

class Vuelo_Serializer(serializers.ModelSerializer):
    piloto = Piloto_Serializer(read_only=True)
    piloto_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Piloto.objects.all(), source='piloto')
    avion = Avion_Serializer(read_only=True)
    avion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Avion.objects.all(), source='avion')
    tripulacion = Tripulacion_Serializer(read_only=True)
    tripulacion_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Tripulacion.objects.all(), source='tripulacion')
    class Meta:
        model = Vuelo
        fields = '__all__'

