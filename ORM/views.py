from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Salesforce, Company
from .serializer import GetDataSerializer,GetCompanyDataSerializer
from django.db.models import Q
from django.db.models import Subquery
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
        sales_object = Salesforce.objects.all()
        saless = Salesforce.objects.filter(name__startwith ="J")| Salesforce.objects.filter(name__endwith='e')
        queryset = Salesforce.objects.filter(Q(name__startwith='J')Q(name__endwith='e'))
        # NOT operation ORM.
        query = Company.objects.filter(~Q(role="Software Developer"))
        query_by_id = Company.objects.filter(~Q(id__lt=5))
        query_by_exclude =  Company.objects.filter(name__startwith="P").exclude(is_developer=False)

        # select some fields only in a queryset
        query_by_only = Company.object.filter(is_developer=True).values('name')
        query_by_only = Company.object.filter(is_developer=True).only('name')

        # SubQuery in ORM
        query_by_sub= Company.objects.filter(Salesforce__id__in =Subquery(sales_object('id')))
        
        #join operations ORM
        
        serializer = GetCompanyDataSerializer(list_obj)
        return Response(serializer.data,status=status.HTTP_200_OK)




