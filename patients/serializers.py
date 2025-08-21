from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "name", "age", "disease", "created_by")
        read_only_fields = ("created_by",)  # created_by automatic set hoga backend se

    # Extra validation: age positive number ho
    def validate_age(self, value):
        if value <= 0:
            raise serializers.ValidationError("Age must be positive!")
        return value
