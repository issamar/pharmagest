# Generated by Django 3.2.13 on 2022-10-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_remove_labo_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='patient_age',
            field=models.IntegerField(verbose_name='age'),
        ),
    ]