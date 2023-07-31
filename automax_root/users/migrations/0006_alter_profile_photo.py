# Generated by Django 3.2.5 on 2023-05-04 19:11

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]
