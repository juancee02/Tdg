# Generated by Django 4.0.4 on 2022-06-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0038_categorias_producto_categorias'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.BooleanField(default=True),
        ),
    ]
