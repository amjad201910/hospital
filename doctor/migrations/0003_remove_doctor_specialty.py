# Generated by Django 4.1.7 on 2023-03-15 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_from_doctor_to_alter_doctor_license_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='specialty',
        ),
    ]