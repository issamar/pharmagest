# Generated by Django 3.2.13 on 2022-10-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now_add=True)),
                ('p_name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('params', models.TextField(max_length=500)),
                ('lab_price', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('pay', models.IntegerField(default=0)),
                ('rest', models.IntegerField(default=0)),
                ('info', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Parametre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Param_name', models.CharField(max_length=500, verbose_name='parameter')),
                ('lab_price', models.IntegerField(default=0)),
                ('ph_price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=250, verbose_name='name')),
                ('paitent_age', models.IntegerField(default=0, verbose_name='age')),
                ('patient_dob', models.DateField(blank=True, null=True, verbose_name='dob')),
            ],
        ),
    ]
