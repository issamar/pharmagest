# Generated by Django 3.2.12 on 2022-05-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makecmd', '0019_auto_20220514_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycmd',
            name='qtt',
            field=models.IntegerField(default=0, verbose_name='qtt'),
        ),
    ]
