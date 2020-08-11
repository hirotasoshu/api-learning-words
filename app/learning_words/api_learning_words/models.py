from django.db import models
from django.utils.html import mark_safe
from .validators import validate_file_extension


# Create your models here.

class Category(models.Model):
    name = models.TextField(unique=True)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.TextField(unique=True)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    level = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    name = models.TextField(unique=True)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    example = models.TextField()
    sound = models.FileField(upload_to='sounds/', validators=[validate_file_extension])
    theme = models.ForeignKey(to=Theme, on_delete=models.CASCADE, related_name='words')

    def sound_preview(self):
        return mark_safe(
            '<audio controls>'
            f'<source src="{self.sound.url}" type="audio/mp3">'
            '</audio>')

    def __str__(self):
        return self.name



