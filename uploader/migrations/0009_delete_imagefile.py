# Generated by Django 4.0.3 on 2022-04-13 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0008_delete_ocrtext'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageFile',
        ),
    ]
