# Generated by Django 4.0.4 on 2022-06-18 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0034_categorias_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productoscat', to='principal.categoria'),
        ),
        migrations.DeleteModel(
            name='Categorias',
        ),
    ]