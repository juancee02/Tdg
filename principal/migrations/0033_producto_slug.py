# Generated by Django 4.0.4 on 2022-06-18 13:49

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0032_remove_producto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='nombre'),
            preserve_default=False,
        ),
    ]
