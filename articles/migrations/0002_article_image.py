# Generated by Django 3.1.6 on 2021-02-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.FileField(default='test', upload_to='images', verbose_name='Picture'),
        ),
    ]