# Generated by Django 4.1.7 on 2023-03-16 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_reservation_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='Body',
            field=models.TextField(blank=True, null=True),
        ),
    ]