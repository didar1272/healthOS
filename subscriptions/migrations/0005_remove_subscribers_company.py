# Generated by Django 3.2.4 on 2022-08-17 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_subscribers_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='company',
        ),
    ]
