# Generated by Django 4.2.13 on 2024-07-21 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
