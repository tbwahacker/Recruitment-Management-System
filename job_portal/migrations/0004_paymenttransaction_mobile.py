# Generated by Django 5.0.6 on 2024-05-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0003_paymenttransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='mobile',
            field=models.BigIntegerField(blank=True, max_length=12, null=True),
        ),
    ]
