# Generated by Django 4.1.7 on 2023-04-12 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_contact_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contact_num',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]