#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 150, verbose_name = 'Tytuł')
    content = models.TextField(verbose_name = 'Zawartość')
    published = models.DateTimeField(verbose_name = 'Data publikacji')
    # image = models.FileField(upload_to='images', verbose_name='Picture')
    
    def __unicode__(self):
        return self.title 
