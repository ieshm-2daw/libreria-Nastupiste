# Generated by Django 4.2.7 on 2023-11-28 09:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='rating',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
