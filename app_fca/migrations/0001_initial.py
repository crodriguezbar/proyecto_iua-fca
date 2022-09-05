# Generated by Django 4.1 on 2022-08-31 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.IntegerField()),
                ('titulo_grado', models.CharField(max_length=40)),
                ('titulo_posgrado', models.CharField(max_length=40)),
                ('hs_asignar', models.IntegerField()),
                ('metodo_alta', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField()),
            ],
        ),
    ]
