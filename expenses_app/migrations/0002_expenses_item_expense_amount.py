# Generated by Django 3.2.5 on 2021-07-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses_item',
            name='expense_amount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
