# Generated by Django 5.0.1 on 2024-02-18 06:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('raspi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='manmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_gas', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_carbon', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('bunho', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='raspi.imagewithtext')),
                ('managercode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.businesscode')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
