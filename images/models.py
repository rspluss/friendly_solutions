from django.db import models


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Album nr. {self.album_id}"


class Image(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, models.DO_NOTHING, blank=True, null=True)
    width = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='content', null=True, blank=True)