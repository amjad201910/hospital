# Generated by Django 4.1.7 on 2023-03-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='amjad', max_length=30, verbose_name='name'),
            preserve_default=False,
        ),
    ]
