# Generated by Django 2.2.7 on 2019-12-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20191210_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicepercentage',
            name='percentage',
            field=models.IntegerField(verbose_name='Percentage'),
        ),
    ]