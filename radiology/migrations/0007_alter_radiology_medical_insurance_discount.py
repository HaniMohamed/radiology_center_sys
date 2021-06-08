# Generated by Django 3.2.4 on 2021-06-08 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiology', '0006_alter_radiology_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radiology',
            name='medical_insurance_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
