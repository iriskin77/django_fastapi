# Generated by Django 5.0.2 on 2024-02-20 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_fp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_info_id',
            new_name='client_info',
        ),
    ]
