# Generated by Django 5.0.4 on 2024-05-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_myuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]