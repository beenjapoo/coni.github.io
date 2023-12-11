from django.db import models


class Aplicacion(models.Model):
    idAplicacion = models.IntegerField(primary_key=True, verbose_name="Id de aplicacion")
    nombreAplicacion = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la aplicacion")
    descripcionAplicacion = models.TextField(max_length=200, blank=False, default='', verbose_name="Descripcion de la aplicacion")
    versionAplicacion = models.CharField(max_length=80, blank=False, null=False, verbose_name="Version de la aplicacion")
    imagen = models.ImageField(upload_to="images/", default="sinfoto.jpg", null=False, blank=False, verbose_name="Imagen")
    archivo_apk = models.FileField(upload_to='archivos_apk/')

    def __str__(self):
        return f'{self.nombreAplicacion}'

