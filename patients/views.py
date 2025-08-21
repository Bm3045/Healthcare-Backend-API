from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Patient
from .serializers import PatientSerializer

# List all patients created by authenticated user
class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    # Automatically set created_by to logged-in user
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# Retrieve, Update, Delete a patient
class PatientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Patient.objects.all()
