# Generated by Django 5.0.2 on 2024-02-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='menu_type',
            field=models.IntegerField(),
        ),
    ]
