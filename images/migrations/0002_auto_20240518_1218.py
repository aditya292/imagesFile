# Generated by Django 3.2.1 on 2024-05-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='image_base64',
            field=models.TextField(blank=True, null=True),
        ),
    ]