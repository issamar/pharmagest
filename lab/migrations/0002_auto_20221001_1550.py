# Generated by Django 3.2.13 on 2022-10-01 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parametre',
            new_name='Parameters',
        ),
        migrations.RenameModel(
            old_name='Patient',
            new_name='Patients',
        ),
    ]
