# Generated by Django 4.0.4 on 2022-06-04 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0019_alter_producto_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact1', to='principal.personas')),
            ],
        ),
    ]
