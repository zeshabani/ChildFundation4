# Generated by Django 2.0 on 2018-02-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0004_auto_20180204_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamyar',
            name='report_method',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'email')]),
        ),
    ]
