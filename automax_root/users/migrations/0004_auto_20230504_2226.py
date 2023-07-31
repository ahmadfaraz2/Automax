# Generated by Django 3.2.5 on 2023-05-04 17:26

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_location_address_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]
