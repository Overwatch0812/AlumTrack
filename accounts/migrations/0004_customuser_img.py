# Generated by Django 4.1.7 on 2023-03-31 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='none', upload_to='users_img'),
        ),
    ]