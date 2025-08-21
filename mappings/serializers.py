from rest_framework import serializers
from .models import Mapping
from patients.models import Patient
from doctors.models import Doctor

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = ("id", "patient", "doctor")

    # Validation: prevent duplicate mapping
    def validate(self, attrs):
        patient = attrs.get('patient')
        doctor = attrs.get('doctor')
        if Mapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return attrs
