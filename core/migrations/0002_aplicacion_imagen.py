# Generated by Django 5.0 on 2023-12-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aplicacion',
            name='imagen',
            field=models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen'),
        ),
    ]
