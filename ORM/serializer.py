from pyexpat import model
from rest_framework import serializers
from .models import Salesforce,Company

class GetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesforce
        fields = '__all__'

class GetCompanyDataSerializer(serializers.ModelSerializer):
    Salesforce = GetDataSerializer()
    class Meta:
        model =Company
        fields = '__all__'
