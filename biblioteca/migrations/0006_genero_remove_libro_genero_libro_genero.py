# Generated by Django 4.2.7 on 2023-12-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_libro_bestseller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='libro',
            name='genero',
        ),
        migrations.AddField(
            model_name='libro',
            name='genero',
            field=models.ManyToManyField(to='biblioteca.genero'),
        ),
    ]