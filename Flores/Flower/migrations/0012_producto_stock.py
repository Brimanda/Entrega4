# Generated by Django 4.0.5 on 2022-06-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flower', '0011_alter_flor_descflor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]