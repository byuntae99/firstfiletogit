# Generated by Django 3.0.7 on 2023-06-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_001', '0005_courseregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregister',
            name='cdd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseregister',
            name='ssdd',
            field=models.CharField(max_length=100),
        ),
    ]
