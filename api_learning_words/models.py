from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.TextField()
    icon = models.ImageField(upload_to='icons/')


class Level(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=2)


class Word(models.Model):
    name = models.TextField()
    translation = models.TextField()
    transcription = models.TextField()
    example = models.TextField()
    sound = models.FileField(upload_to='sounds/')


class Theme(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    level = models.ForeignKey(to=Level, on_delete=models.CASCADE)
    name = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    words = models.ManyToManyField(Word)

