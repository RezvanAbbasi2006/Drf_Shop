# Generated by Django 4.2.7 on 2023-11-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
