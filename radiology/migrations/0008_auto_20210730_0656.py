# Generated by Django 3.0.5 on 2021-07-30 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radiology', '0007_auto_20210730_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examination',
            old_name='shift_id',
            new_name='shift',
        ),
    ]
