from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.TextField(unique=True)
    icon = models.ImageField(upload_to='icons/')


class Level(models.Model):
    name = models.TextField(unique=True)
    code = models.CharField(max_length=2, unique=True)


class Theme(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    level = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    name = models.TextField(unique=True)
    photo = models.ImageField(upload_to='photos/')


class Word(models.Model):
    name = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    example = models.TextField()
    sound = models.FileField(upload_to='sounds/')
    theme = models.ForeignKey(to=Theme, on_delete=models.CASCADE, related_name='words')




