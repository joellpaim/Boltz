# Generated by Django 4.1.3 on 2022-11-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('data_rev', models.DateField(auto_now=True)),
            ],
        ),
    ]