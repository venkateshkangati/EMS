# Generated by Django 5.0.2 on 2025-03-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
