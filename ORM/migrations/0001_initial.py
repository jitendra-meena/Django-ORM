# Generated by Django 3.2.12 on 2022-03-16 17:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salesforce',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('Salesforce', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('role', models.CharField(max_length=40)),
                ('is_developer', models.BooleanField(default=False)),
                ('Salesforce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORM.salesforce')),
            ],
        ),
    ]