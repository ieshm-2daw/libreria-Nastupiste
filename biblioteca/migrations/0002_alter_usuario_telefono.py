# Generated by Django 4.2.7 on 2023-11-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
