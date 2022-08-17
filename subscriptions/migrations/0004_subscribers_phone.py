# Generated by Django 3.2.4 on 2022-08-17 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_phone_assigned_customer'),
        ('subscriptions', '0003_auto_20220818_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscribed_phone', to='company.phone'),
        ),
    ]
