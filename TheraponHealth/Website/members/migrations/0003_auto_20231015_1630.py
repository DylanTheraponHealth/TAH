# Generated by Django 3.2.22 on 2023-10-15 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20231015_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
