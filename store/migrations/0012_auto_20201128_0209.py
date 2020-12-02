# Generated by Django 3.1.3 on 2020-11-28 01:09

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20201128_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, validators=[store.models.email_validation_function]),
        ),
    ]
