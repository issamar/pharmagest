# Generated by Django 3.2.12 on 2022-04-14 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makecmd', '0002_mycmd_indisponible'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycmd',
            name='client',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
