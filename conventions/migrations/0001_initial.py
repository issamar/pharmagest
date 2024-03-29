# Generated by Django 3.2.13 on 2022-10-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bordereaux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_ctr', models.CharField(max_length=20)),
                ('n_brd', models.CharField(max_length=200, unique=True)),
                ('dt_clo', models.DateField()),
                ('n_ord', models.IntegerField()),
                ('m_brd', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dt_depot', models.DateField(blank=True, null=True)),
                ('dt_jrl', models.DateField(blank=True, null=True)),
                ('n_ord_jrl', models.IntegerField(blank=True, default=0, null=True)),
                ('m_jrl', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('dt_pay', models.DateField(blank=True, null=True)),
                ('defr', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('def_o', models.IntegerField(default=0)),
                ('payement', models.BooleanField(default=False)),
            ],
        ),
    ]
