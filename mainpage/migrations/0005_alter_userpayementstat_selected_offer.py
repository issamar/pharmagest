# Generated by Django 3.2.12 on 2022-04-27 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_rename_prove_of_payement_userpayementstat_proof_of_payement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayementstat',
            name='selected_offer',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Avancé', 'Avancé'), ('Professionnel', 'Professionnel')], max_length=30, verbose_name='offer'),
        ),
    ]
