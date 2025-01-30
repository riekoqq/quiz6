from rest_framework import serializers
from base.models import Drug

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'