from .models import Querys
from rest_framework import serializers


class ConsultaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Querys
        fields = ['consulta', 'respuesta', 'date']

