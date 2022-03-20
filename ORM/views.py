from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Salesforce, Company
from .serializer import GetDataSerializer,GetCompanyDataSerializer

# Get Data From SalesForces Model
class GetData(APIView):
    def get(self,request):
        sales_obj = Salesforce.objects.all()
        serializer = GetDataSerializer(sales_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


# ORM Filter 
class GetCompanyData(APIView):
    def get(self,request):
        sales_obj = Company.objects.all()
        sale_obj = Company.objects.filter(name__contains= 'Ji')
        get_sales = Company.objects.get(id =2)
        # sales = Company.objects.values('id')
        list_obj = Company.objects.values('id')
        print(list_obj)
        serializer = GetCompanyDataSerializer(list_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)




