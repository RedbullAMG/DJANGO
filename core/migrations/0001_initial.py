# Generated by Django 4.1.5 on 2023-06-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idcategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='idcategoria')),
                ('nombrecategoria', models.CharField(max_length=50, verbose_name='nombre categoria')),
            ],
        ),
    ]