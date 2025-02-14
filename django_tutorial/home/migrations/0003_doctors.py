# Generated by Django 5.0.6 on 2024-05-26 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_departments_dep_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('doc_spec', models.CharField(max_length=255)),
                ('doc_imgage', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]
