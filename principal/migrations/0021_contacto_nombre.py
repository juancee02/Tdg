# Generated by Django 4.0.4 on 2022-06-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_contacto'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
