# Generated by Django 4.1 on 2022-08-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aeropuerto_app', '0004_usuario_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
