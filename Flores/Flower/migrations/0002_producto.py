# Generated by Django 2.1.15 on 2022-06-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('nombre', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
