# Generated by Django 3.2.4 on 2022-08-15 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='assigned_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='phone_customer', to='customer.customer'),
        ),
    ]
