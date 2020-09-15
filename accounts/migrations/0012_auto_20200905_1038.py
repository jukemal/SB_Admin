# Generated by Django 3.0.8 on 2020-09-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200904_1210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='name',
        ),
        migrations.AddField(
            model_name='meal',
            name='meal_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
