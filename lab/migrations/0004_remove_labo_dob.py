# Generated by Django 3.2.13 on 2022-10-15 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_rename_paitent_age_patients_patient_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labo',
            name='dob',
        ),
    ]
