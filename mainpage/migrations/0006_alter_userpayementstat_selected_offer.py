# Generated by Django 3.2.13 on 2022-06-16 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_alter_userpayementstat_selected_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpayementstat',
            name='selected_offer',
            field=models.CharField(choices=[('Basic', 'Basic')], max_length=30, verbose_name='offer'),
        ),
    ]