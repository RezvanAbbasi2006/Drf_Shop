# Generated by Django 4.2.7 on 2023-12-24 08:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=uuid.UUID('bcab2cf5-72dc-4971-be5c-dfef4540a7fd'), max_length=300, verbose_name='uid'),
        ),
    ]
