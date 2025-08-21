from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Mapping
from .serializers import MappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mapping.objects.all()

class MappingRetrieveView(generics.ListAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        return Mapping.objects.filter(patient_id=patient_id)

class MappingDeleteView(generics.DestroyAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mapping.objects.all()
