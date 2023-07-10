from rest_framework import serializers

class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    direccion = serializers.CharField(max_length=150)
    pais = serializers.CharField(max_length=150)
    descripcion = serializers.CharField(max_length=500)
    imagen = serializers.ImageField()
    active = serializers.BooleanField(default=True)