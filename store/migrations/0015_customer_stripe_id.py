# Generated by Django 3.1.3 on 2020-11-29 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20201129_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
