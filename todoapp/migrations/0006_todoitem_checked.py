# Generated by Django 3.1.5 on 2021-01-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0005_todoitem_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
