"""DjangoORM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import GetData,GetCompanyData,ActivityRecord
from django.urls import path

urlpatterns = [
    path('get_data',GetData.as_view(),name='get_data'),
    path('get_company_data',GetCompanyData.as_view(),name='get_company_data'),
    path('activity/',ActivityRecord.as_view(),name='activity')
]   

