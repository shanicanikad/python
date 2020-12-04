# Generated by Django 3.1.3 on 2020-11-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='preview',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
