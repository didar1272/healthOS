# Generated by Django 3.2.4 on 2022-08-15 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=64)),
                ('primary_number', models.CharField(max_length=16, null=True)),
                ('customer_email', models.EmailField(max_length=50, unique=True)),
                ('customer_password', models.CharField(max_length=128)),
                ('balance', models.IntegerField(default=1000)),
                ('current_plan', models.CharField(blank=True, choices=[('GLOBALNET BRONZE', 'Globalnet Bronze'), ('GLOBALNET SILVER', 'Globalnet Silver'), ('GLOBALNET GOLD', 'Globalnet Gold')], max_length=64)),
                ('registrasion_datetime', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
