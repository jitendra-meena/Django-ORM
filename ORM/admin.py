from django.contrib import admin
from .models import Activity, Salesforce,Company

admin.site.register(Salesforce)
admin.site.register(Company)

admin.site.register(Activity)



