# Generated by Django 4.2.7 on 2023-12-08 06:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=uuid.UUID('92bcb8c1-eab8-4b63-9679-5d91ca7d7d04'), max_length=300, verbose_name='uid'),
        ),
    ]
