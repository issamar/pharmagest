# Generated by Django 3.2.12 on 2022-05-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addmed', '0007_addart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmed',
            name='cond',
            field=models.CharField(max_length=100, verbose_name='cond'),
        ),
    ]