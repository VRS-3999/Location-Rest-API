# Generated by Django 2.2.6 on 2020-01-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20200126_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gsm',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
        migrations.AlterField(
            model_name='gsm',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=12),
        ),
    ]
