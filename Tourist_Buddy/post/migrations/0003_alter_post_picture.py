# Generated by Django 3.2.12 on 2024-12-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(upload_to='photos/place', verbose_name='Picture'),
        ),
    ]
