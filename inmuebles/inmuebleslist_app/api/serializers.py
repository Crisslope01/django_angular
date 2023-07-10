from rest_framework import serializers
from inmuebleslist_app.models import Inmueble



class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        #fields = '__all__'
        fields = ('id', 'direccion', 'pais', 'imagen')
        
    def validate(self, data):
        if data["direccion"] == data["pais"]:
            raise serializers.ValidationError("El pais no puede ser igual a la direccion")
        else:
            return data
    def validate_imagen(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("El valor de la url es demasiado corto ")
        else:
            return data

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es demasiado corto ")
    

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud],max_length=150)
#     pais = serializers.CharField(validators=[column_longitud],max_length=150)
#     descripcion = serializers.CharField(max_length=500)
#     imagen = serializers.CharField()
#     active = serializers.BooleanField(default=True)
    
#     def create(self, validated_data):
#         return Inmueble.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.direccion = validated_data.get('direccion', instance.direccion)
#         instance.pais = validated_data.get('pais', instance.pais)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.imagen = validated_data.get('imagen', instance.imagen)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data["direccion"] == data["pais"]:
#             raise serializers.ValidationError("El pais no puede ser igual a la direccion")
#         else:
#             return data
#     def validate_imagen(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("El valor de la url es demasiado corto ")
#         else:
#             return data