from django.db import models
import os

# Create your models here.


class Photos(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    photo = models.ImageField(
        upload_to="photos/%y/%m/%d/", verbose_name='Foto')

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super(Photos, self).delete(*args, **kwargs)

class Songs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    song = models.FileField(
        upload_to="songs/%y/%m/%d/", verbose_name='Cancion')

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.song:
            if os.path.isfile(self.song.path):
                os.remove(self.song.path)
        super(Songs, self).delete(*args, **kwargs)
