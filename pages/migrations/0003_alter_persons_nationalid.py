# Generated by Django 4.2.11 on 2024-05-07 06:04

from django.db import migrations, models
import pages.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_persons_nationalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='nationalId',
            field=models.BigIntegerField(null=True, unique=True, validators=[pages.models.validate_national_id_length]),
        ),
    ]
