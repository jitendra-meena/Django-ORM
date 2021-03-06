from itertools import count
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Activity, Salesforce, Company
from .serializer import GetDataSerializer,GetCompanyDataSerializer,ActivityRecordSerializer
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
        # queryset = Salesforce.objects.filter(Q(name__startwith='J')Q(name__endwith='e'))
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

        #second largest record ORM 
        query_by_record =  Company.objects.order_by('-role')[1]

        # Duplicate Records
        duplicate_record = Company.objects.values('name').annotate(name_count=count('name').filter(name__gt=1))
        
        
        serializer = GetCompanyDataSerializer(query_by_record)
        return Response(serializer.data,status=status.HTTP_200_OK)

   
class ActivityRecord(APIView):
    
    def get(self,request,id=None):
        activity_obj = Activity.objects.all()
        serializer = ActivityRecordSerializer(activity_obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,id):
        data = request.data
        company = Company.objects.get(id =id)
        print(company)
        serializer = ActivityRecordSerializer(company,data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def put(self,request,id):
        company = Company.objects.get(id =id)
        serializer = ActivityRecordSerializer(company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)    

