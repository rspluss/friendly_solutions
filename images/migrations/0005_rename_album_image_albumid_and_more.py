# Generated by Django 4.1.2 on 2022-10-27 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='album',
            new_name='albumId',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_url',
            new_name='url',
        ),
    ]
