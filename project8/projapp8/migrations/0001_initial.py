# Generated by Django 3.2.16 on 2022-11-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places8',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('place', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
