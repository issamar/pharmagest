# Generated by Django 3.2.12 on 2022-04-27 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_userpayementstat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpayementstat',
            name='user',
        ),
        migrations.AddField(
            model_name='userpayementstat',
            name='user_name',
            field=models.CharField(max_length=50, null=True, verbose_name='user_name'),
        ),
    ]
