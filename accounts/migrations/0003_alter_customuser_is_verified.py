# Generated by Django 4.1.7 on 2023-03-25 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
