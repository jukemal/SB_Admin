# Generated by Django 3.1.1 on 2020-09-15 17:27

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200914_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(
                default=datetime(year=2020, month=1, day=1)),
            preserve_default=False,
        ),
    ]
