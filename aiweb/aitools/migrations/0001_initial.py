# Generated by Django 5.1.1 on 2024-10-06 13:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_uuid', models.CharField(max_length=36, unique=True)),
                ('file_path', models.CharField(max_length=1024)),
                ('file_mime_type', models.CharField(max_length=50)),
                ('file_ext', models.CharField(max_length=50)),
                ('file_size', models.FloatField()),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aitools.user')),
            ],
        ),
    ]
