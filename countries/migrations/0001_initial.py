# Generated by Django 4.1.5 on 2023-11-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_code', models.CharField(max_length=5)),
                ('color', models.CharField(max_length=15)),
                ('flag', models.ImageField(upload_to='')),
            ],
        ),
    ]
