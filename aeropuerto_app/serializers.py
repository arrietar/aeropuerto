from rest_framework import serializers
from aeropuerto_app.models import *

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

