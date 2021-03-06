from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Activity, Salesforce,Company

class GetDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesforce
        fields = '__all__'

class GetCompanyDataSerializer(serializers.ModelSerializer):
    Salesforce = GetDataSerializer()
    class Meta:
        model =Company
        fields = '__all__'

class ActivityRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = "__all__"      

