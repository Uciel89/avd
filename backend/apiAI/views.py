from django.shortcuts import render

from .models import Querys
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ConsultaSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .inteligencia_art import gpt3



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Querys.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request):
        
        respuesta_a = gpt3(request.data.get('consulta'))
        
        serializer = self.get_serializer(data=request.data)
        response = {}
        response['succes'] = True
        response['message'] = "Registro guardado exitosamente"
        response['status'] = status.HTTP_201_CREATED
        response['response'] = respuesta_a
        
        Querys.objects.create(consulta=request.data.get('consulta'), respuesta=respuesta_a)
        
        return Response(response)
