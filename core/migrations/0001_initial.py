# Generated by Django 5.0 on 2023-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacion',
            fields=[
                ('idAplicacion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de aplicacion')),
                ('nombreAplicacion', models.CharField(max_length=80, verbose_name='Nombre de la aplicacion')),
                ('descripcionAplicacion', models.TextField(default='', max_length=200, verbose_name='Descripcion de la aplicacion')),
                ('versionAplicacion', models.CharField(max_length=80, verbose_name='Version de la aplicacion')),
                ('archivo_apk', models.FileField(upload_to='archivos_apk/')),
            ],
        ),
    ]
