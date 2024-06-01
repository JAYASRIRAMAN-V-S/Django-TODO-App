# Generated by Django 5.0.3 on 2024-06-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='untitled', max_length=255),
            preserve_default=False,
        ),
    ]
