# Generated by Django 5.0.7 on 2024-07-22 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doct_name', models.CharField(max_length=50)),
                ('doct_specialization', models.CharField(max_length=100)),
                ('doct_image', models.ImageField(blank=True, null=True, upload_to='doctors_pic')),
                ('doct_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('patient_phone', models.IntegerField()),
                ('patient_email', models.EmailField(max_length=254)),
                ('booking_date', models.DateField(blank=True, null=True)),
                ('booked_on', models.DateField(auto_now=True)),
                ('doct_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
                ('doct_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors')),
            ],
        ),
    ]
