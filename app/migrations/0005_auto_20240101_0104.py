# Generated by Django 2.2.4 on 2023-12-31 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20231231_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='package_name',
        ),
        migrations.AddField(
            model_name='package',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='package',
            name='package_destination',
            field=models.CharField(default='nablus', max_length=45),
        ),
    ]
