from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Tytuł')
    content = models.TextField(verbose_name= 'Zawartość')
    published = models.DateTimeField(verbose_name= 'Data publikacji')
    image = models.FileField(upload_to='images', verbose_name='Obrazek')
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150, verbose_name = 'Użytkownik')
    content = models.TextField(verbose_name= 'Komentarz')
    published = models.DateTimeField(verbose_name= 'Data publikacji')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
