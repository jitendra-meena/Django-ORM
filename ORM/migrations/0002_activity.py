# Generated by Django 3.2.12 on 2022-03-21 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_act', models.IntegerField(null=True)),
                ('activity_type', models.CharField(max_length=20)),
                ('current_date', models.DateTimeField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ORM.company')),
            ],
        ),
    ]
