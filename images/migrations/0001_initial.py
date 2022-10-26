# Generated by Django 4.1.2 on 2022-10-25 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('width', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='content')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.album')),
            ],
        ),
    ]
