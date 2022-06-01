# Generated by Django 4.0.4 on 2022-05-25 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id_doc', models.AutoField(primary_key=True, serialize=False)),
                ('tdocumento', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipo_documento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPersonas',
            fields=[
                ('id_tpersonas', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tipo_personas',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TipoDeDocumento',
        ),
        migrations.DeleteModel(
            name='TipoPersona',
        ),
    ]
