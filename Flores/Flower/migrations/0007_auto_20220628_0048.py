# Generated by Django 2.1.15 on 2022-06-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flower', '0006_auto_20220628_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
